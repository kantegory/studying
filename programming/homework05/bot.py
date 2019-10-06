import config
from datetime import datetime, time, date
import datetime
import telebot
import requests
import time
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.access_token)


def get_page(group, week):
    if week:
        week = str(week) + '/'
    if week == '0/':
        week = ''
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group
    )
    response = requests.get(url)
    web_page = response.text
    return web_page


def day_number(day):
    days = ['/monday', '/tuesday', '/wednesday', '/thursday', '/friday', '/saturday', '/sunday']
    real_day = days.index(day) + 1
    return str(real_day) + 'day'


def convert(day):
    days = ['/monday', '/tuesday', '/wednesday', '/thursday', '/friday', '/saturday', '/sunday']
    return days[day]


def week_check():
    week = config.today.isocalendar()[1]
    if week % 2 == 0:
        return 1
    else:
        return 2


def get_tomorrow(today):
    tomorrow = today
    if today.weekday() == 5:
        tomorrow += datetime.timedelta(days=2)
    else:
        tomorrow += datetime.timedelta(days=1)
    tomorrow = tomorrow.weekday()
    days = ['/monday', '/tuesday', '/wednesday', '/thursday', '/friday', '/saturday', '/sunday']
    return days[tomorrow]


def get_schedule(web_page, day):
    soup = BeautifulSoup(web_page, "html5lib")

    schedule_table = soup.find("table", attrs={"id": day_number(day)})

    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.replace('\n', '').replace('\t', '') for lesson in lessons_list]

    return times_list, locations_list, lessons_list


def check_group(web_page, day='/monday'):
    soup = BeautifulSoup(web_page, "html5lib")
    schedule_table = soup.find("table", attrs={"id": day_number(day)})
    if schedule_table:
        return True
    else:
        return False


@bot.message_handler(commands=['all'])
def get_week(message):
    if len(message.text.split()) != 3:
        bot.send_message(message.chat.id, 'Ошибка! Вы не ввели номер группы или недели!')
    else:
        day, week, group = message.text.split()
        web_page = get_page(group, week)
        if not check_group(web_page):
            bot.send_message(message.chat.id, 'Ошибка! Вы неверно ввели номер группы!')
        else:
            _, week_number, group = message.text.split()
            week_number = int(week_number) - 1
            web_page = get_page(group, week_number + 1)
            resp = ""
            for i in range(6):
                times_lst, locations_lst, lessons_lst = get_schedule(web_page, convert(i))
                for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
                    resp += '<b>{}</b>, {}, {}\n'.format(time, location, lesson)
                resp += '\n'
            bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['tomorrow'])
def send_tomorrow(message):
    if len(message.text.split()) != 2:
        bot.send_message(message.chat.id, 'Ошибка! Вы не ввели номер группы!')
    else:
        _, group = message.text.split()
        web_page = get_page(group, week_check())
        tomorrow = get_tomorrow(config.today)
        if not check_group(web_page, tomorrow):
            bot.send_message(message.chat.id, 'Ошибка! Вы неверно ввели номер группы!')
        else:
            times_lst, locations_lst, lessons_lst = get_schedule(web_page, tomorrow)
            resp = '<b>Расписание на завтра:\n\n</b>'
            for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
                resp += '<b>{}</b>, {}, {}\n'.format(time, location, lesson)

            bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
                               'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
def get_day(message):
    if len(message.text.split()) != 3:
        bot.send_message(message.chat.id, 'Ошибка! Вы не ввели номер группы или недели!')
    else:
        day, week, group = message.text.split()
        web_page = get_page(group, week)
        if not check_group(web_page, day):
            bot.send_message(message.chat.id, 'Ошибка! Вы неверно ввели номер группы или у этой группы сегодня нет пар.')
        else:
            times_lst, locations_lst, lessons_lst = get_schedule(web_page, day)

            resp = ''
            for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
                resp += '<b>{}</b>, {}, {}\n'.format(time, location, lesson)

            bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_next_lesson(message):
    if len(message.text.split()) != 2:
        bot.send_message(message.chat.id, 'Ошибка! Вы не ввели номер группы!')
    else:
        _, group = message.text.split()
        web_page = get_page(group, week_check())
        if config.today.weekday() != 6:
            today = convert(config.today.weekday())
        else:
            today = convert(0)
        if not check_group(web_page, today):
            bot.send_message(message.chat.id, 'Error: 404. Расписание занятий не найдено.')
        else:
            times_list, locations_lst, lessons_lst = get_schedule(web_page, today)
            count = -1
            state = 0
            while not state:
                if config.today.weekday() != 6:
                    today = config.today.weekday()
                else:
                    today = 0
                for i in times_list:
                    _, time = i.split('-')
                    t1, t2 = time.split(':')
                    time = int(t1 + t2)
                    cur_hour, cur_min = datetime.datetime.now().hour, datetime.datetime.now().minute
                    if cur_hour < 10:
                        cur_hour = '0' + str(cur_hour)
                    if cur_min < 10:
                        cur_min = '0' + str(cur_min)
                    cur_time = int(str(cur_hour) + str(cur_min))
                    count += 1
                    if cur_time < time:
                        resp = '<b>Ближайшая пара:</b>\n'
                        resp += '<b>{}</b>, {}, {}\n'.format(times_list[count], locations_lst[count], lessons_lst[count])
                        bot.send_message(message.chat.id, resp, parse_mode='HTML')
                        state = 1
                        break
                    else:
                        times_list, locations_lst, lessons_lst = get_schedule(web_page, convert(today + 1))
                        resp = '<b>Ближайшая пара:</b>\n'
                        resp += '<b>{}</b>, {}, {}\n'.format(times_list[0], locations_lst[0], lessons_lst[0])
                        bot.send_message(message.chat.id, resp, parse_mode='HTML')
                        state = 1
                        break


if __name__ == '__main__':
    bot.polling(none_stop=True)
