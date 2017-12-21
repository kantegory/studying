<?php

include 'connection.php'; 

$query ="CREATE TABLE IF NOT EXISTS abit(
  name varchar(255) NOT NULL,
  passport int(15) NOT NULL,
  id_abiturient int(10) NOT NULL AUTO_INCREMENT,
  school varchar(255) NOT NULL,
  medal varchar(3) DEFAULT NULL,
  specialization varchar(255) NOT NULL,
  form varchar(255) NOT NULL,
  PRIMARY KEY (id_abiturient))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}
 
$sql = "INSERT INTO abit VALUES ('Ivanov_Ivan', '400', '1', '001', 'yes', 'IT', 'budget')";

if (mysqli_query($link, $sql)) {
  echo "Created successfully <br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS college(
  id_college int(10) NOT NULL,
  id_kaf int(10) NOT NULL,
  id_faculty int(10) NOT NULL,
  name_specialization varchar(255) NOT NULL,
  number int(10) NOT NULL,
  id_secretary int(10) NOT NULL,
  PRIMARY KEY (id_college))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}

$sql = "INSERT INTO college VALUES ('001', '0902', '001', 'IT', '25', '001')";

if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}


$query ="CREATE TABLE IF NOT EXISTS kaf(
  id_kaf int(10) NOT NULL,
  name_kaf varchar(255) NOT NULL,
  id_fac int(10) NOT NULL,
  name_specialization varchar(255) NOT NULL,
  PRIMARY KEY (id_kaf))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}

$sql = "INSERT INTO kaf VALUES ('0902', 'programming', '001', 'IT')";

if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}


$query ="CREATE TABLE IF NOT EXISTS exams (
  id_exam int(30) NOT NULL AUTO_INCREMENT,
  first_exam_balls int(10) NOT NULL,
  second_exam_balls int(10) NOT NULL,
  third_exam_balls int(10) NOT NULL,
  sum_exam_balls int(10) NOT NULL,
  PRIMARY KEY (id_exam))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}

$sql = "INSERT INTO exams VALUES ('1', '100', '100', '100', '300')";

if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS faculty (
  id_fac int(10) NOT NULL,
  id_kaf int(10) NOT NULL,
  name_faculty varchar(255) NOT NULL,
  name_specialization varchar(255) NOT NULL,
  number int(10) NOT NULL,
  PRIMARY KEY (id_fac))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}

$sql = "INSERT INTO faculty VALUES ('001', '0902', 'ITs', 'IT', '25')";

if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query = "CREATE TABLE IF NOT EXISTS exam_balls(
  id_exam_balls int(30) NOT NULL,
  max_exam_balls int(10) NOT NULL,
  avg int(10) NOT NULL,
  PRIMARY KEY (id_exam_balls))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}

$sql = "INSERT INTO exam_balls VALUES ('0001', '309', '247')";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS reg(
  id_application int(10) NOT NULL AUTO_INCREMENT,
  id_secretary int(10) NOT NULL,
  name varchar(255) NOT NULL,
  passport int(15) NOT NULL,
  id_abiturient int(10) NOT NULL,
  form varchar(255) NOT NULL,
  school varchar(255) NOT NULL,
  name_specialization varchar(255) NOT NULL,
  exam_balls int(10) NOT NULL,
  number int(10) NOT NULL,
  id_fac int(10) NOT NULL,
  id_college int(10) NOT NULL,
  id_exam_balls int(10) NOT NULL,
  reg_exam int(10) NOT NULL,
  PRIMARY KEY (id_application))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}

$sql = "INSERT INTO reg VALUES ('01', '0101', 'Ivanov_Ivan', '400', '001', 'budget', '275', 'IT', '300', '25', '001', '001', '0001' , '0001')";

if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS `secretarys` (
  id_secretary int(10) NOT NULL AUTO_INCREMENT,
  fio varchar(100) NOT NULL,
  id_college int(10) NOT NULL,
  PRIMARY KEY (id_secretary))";

$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 

if($result)
{
    echo "Выполнение запроса прошло успешно <br>";
}

$sql = "INSERT INTO secretarys VALUES ('0101', 'Alex', '001')";

if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

mysqli_close($link);
