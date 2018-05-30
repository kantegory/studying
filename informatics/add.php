<?php

// script for add record

include "connection.php";
if(isset($_GET['button']))
{
	$name = $_GET['name']; 
	$passport = $_GET['passport']; 
	$school = $_GET['school']; 
	$medal = $_GET['medal']; 
	$specialization = $_GET['specialization']; 
	$form = $_GET['form']; 
		
	$query = "INSERT INTO abit (name, passport, school, medal, specialization, form) 
	VALUES ('$name', $passport, $school, '$medal', '$specialization', '$form')";
	
	$result = mysqli_query($link, $query);
	
	// redirect
	header('location: ./list.php');
}
?>

<html>
<body>
<form action = 'add.php' method = 'get'>
	<p><i> Добавить запись </i>
	<P> Имя: <input name = 'name' type = 'text'>
	<p> Паспорт: <input name = 'passport' type = 'text'>
	<p> Оконченный класс: 
	<p> <input name = 'school' value = '9' type = 'radio'> 9 
	<p> <input name = 'school' value = '11' type = 'radio'> 11
	<p> Наличие медали: 
	<p> <input name = 'medal' value = 'yes'  type = 'radio'> Да 
	<p> <input name = 'medal' value = 'no'  type = 'radio'> Нет
	<p> Форма обучения:
	<p> <input name = 'form' value = 'budget' type = 'radio'> Бюджет 
	<p> <input name = 'form' value = 'contract' type = 'radio'> Контракт
	<p> Специальность: 
	<p> <input name = 'specialization' value = 'IT' type = 'radio'> IT 
	<p> <input name = 'specialization' value = 'DATA' type = 'radio'> DATA
	<p> <input name = 'specialization' value = 'WEB-DEV' type = 'radio'> WEB-DEV
	<p><input name = 'button' type = 'submit'>
</form>
</body>
</html>
