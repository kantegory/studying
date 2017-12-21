<html>
<body>
	<form action = 'search.php' method = 'get'>
	<table>
	<tr><th><i>Значение:</i></th></tr>
	<tr><td>Имя абитуриента: <input name = 'input_1' type = 'text' value='<?=@$_GET['input_1']?>'></td></tr>
	<tr><td>Название кафедры: <input name = 'input_2' type = 'text' value='<?=@$_GET['input_2']?>'></td></tr>
	</table>
	<br/>
	<input type = 'submit' name = 'button'>
	</form>
</body>
</html
<?php

include 'connection.php';

if(isset($_GET['button']))
{
	$input_1 = $_GET['input_1'];
	$input_2 = $_GET['input_2'];

	$query = "SELECT abit.name, kaf.name_kaf FROM abit JOIN kaf 
		ON abit.specialization = kaf.name_specialization
		 WHERE  abit.name LIKE '%" . $input_1 . "%' ";
	
	if (!empty($input_2)) {
			$query .= "AND kaf.name_kaf LIKE '%" . $input_2 . "%'";
	}
	
	$result = mysqli_query($link, $query);

	echo "<table border = 1 align=center><tr><td>Имя</td><td>Кафедра</td></tr>";
	
	while($row = mysqli_fetch_array($result)) {
			echo "<tr><td>" . $row['name'] . "</td><td>" . $row['name_kaf'] . "</td></tr>";
	}

	echo "</table>";

	mysqli_close($link);
}
