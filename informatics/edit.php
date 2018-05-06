<?php

// edit records

include "connection.php";

$id = $_GET['id_abiturient'];
$name_abit = $_GET['input_1'];
$name_kaf = $_GET['input_2'];

$query = "SELECT abit.name, kaf.name_kaf FROM abit JOIN kaf 
		ON abit.specialization = kaf.name_specialization
		WHERE  abit.name LIKE '%" . $name_abit . "%' 
		AND kaf.name_kaf LIKE '%" . $name_kaf . "%'";
	
$result = mysqli_query($link, $query);

?>

<html>
<body>
	<form action = 'edit.php' method = 'get'>
	<table>
	<tr><th><i>Редактировать значения:</i></th></tr>
	<tr hidden><td>ID абитуриента: <input name = 'id_abiturient' type = 'text' value='<?=@$_GET['id_abiturient']?>'></td></tr>
	<tr><td>Имя абитуриента: <input name = 'input_1' type = 'text' value='<?=@$_GET['input_1']?>'></td></tr>
	<tr><td>Название кафедры: <input name = 'input_2' type = 'text' value='<?=@$_GET['input_2']?>'></td></tr>
	</table>
	<br/>
	<input type = 'submit' name = 'button'>
	</form>
</body>
</html>

<?php
 
// script for update

if(isset($_GET['button']))
{
	$input_1 = $_GET['input_1'];
	$input_2 = $_GET['input_2'];
	$id_abiturient = $_GET['id_abiturient'];

	$query = "UPDATE abit
		SET name ='" . $input_1 . "'
		WHERE id_abiturient =' " . $id_abiturient . " '; ";
			
	$result = mysqli_query($link, $query);
			
	$query = "UPDATE kaf
		SET name_kaf ='" . $input_2 . "';";
			
	$result = mysqli_query($link, $query);

	// redirect
	header('location: ./list.php'); 
}
