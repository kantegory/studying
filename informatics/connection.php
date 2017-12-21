<?php

$host = 'localhost';
$user = 'root';
$password = 'password';
$database = 'k3140_ddi';

$link = mysqli_connect($host, $user, $password, $database);
if (!$link) {
    die('Ошибка соединения: ' . mysql_error());
}

$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

echo "Вы подключились!<br>";
