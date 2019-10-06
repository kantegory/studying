from collections import Counter


def main(message):
    c = Counter(message)
    rev_message = ''
    print(c)
    for char in range(len(message)):
        if message[char] is not ' ':
            rev_message += chr(ord(message[char]) + (ord('E') - ord('A')))
        else:
            rev_message += ' '
    print(rev_message)


if __name__ == "__main__":
    message = input()
    main(message)
