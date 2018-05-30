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

$query = "INSERT INTO kaf VALUES (903, 'DataScience', 1, 'DATA')";

$queryOk = mysqli_query($link, $query);

$query = "INSERT INTO kaf VALUES (904, 'WEB-DEV', 1, 'WEB')";

$queryOk = mysqli_query($link, $query);

// script for update

if(isset($_GET['button']))
{
	$input_1 = $_GET['input_1'];
	$input_2 = $_GET['input_2'];
	$id_abiturient = $id;

	$query = "UPDATE abit
		SET name ='" . $input_1 . "'
		WHERE id_abiturient =' " . $id_abiturient . " '; ";
			
	$result = mysqli_query($link, $query);
	
	$new_spec = mysqli_fetch_assoc(mysqli_query($link, "SELECT name_specialization FROM kaf WHERE name_kaf = '" . $input_2 . "';"))['name_specialization'];
	print_r($new_spec);
	$query = "UPDATE abit 
	SET abit.specialization ='" . $new_spec . "'
	WHERE abit.id_abiturient ='" . $id . "';";
			
	$result = mysqli_query($link, $query);

	// redirect
	header('location: ./list.php'); 
}
?>

<html>
<body>
	<div  align = center>
	<form action = 'edit.php' method = 'get'>
	<table>
	<tr><th><i>Редактировать значения:</i></th></tr>
	<tr hidden><td>ID абитуриента: <input name = 'id_abiturient' type = 'text' value='<?php echo $id; ?>'></td></tr>
	<tr><td>Имя абитуриента: <input name = 'input_1' type = 'text' value='<?=@$_GET['input_1']?>'></td></tr>
	<tr><td>Название кафедры: <select name = 'input_2'>
	<?php 
	$kaf_names = mysqli_fetch_all(mysqli_query($link, "SELECT name_kaf FROM kaf"), MYSQLI_ASSOC);
	for ($i = 0; $i < count($kaf_names); $i++) {
		$kaf[] = ($kaf_names[$i]['name_kaf']);	
		echo "<option>";
		echo $kaf[$i];
		echo "</option>";
		print_r($kaf);
		}
	?>
	</td></tr>
	</table>
	<br/>
	<input type = 'submit' name = 'button'>
	</form>
	</div> 
</body>
</html>

