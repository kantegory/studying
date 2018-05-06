<?php

include "connection.php";

$query = "SELECT abit.name, kaf.name_kaf, id_abiturient FROM abit JOIN kaf 
		ON abit.specialization = kaf.name_specialization";

$result = mysqli_query($link, $query);

echo "<table border = 1 align=center>";
echo "<tr><td>Имя</td>";
echo "<td>Кафедра</td>";
echo "<td colspan = 2>Редактировать</td></tr>";


while($row = mysqli_fetch_array($result)) {
	echo "<tr><td>" . $row['name']. "</td>";
	echo "<td>" . $row['name_kaf'] . "</td>";
	echo "<td><a href = './edit.php?id_abiturient=" . $row['id_abiturient'] . "&input_1=" . $row['name'] . "&input_2=" . $row['name_kaf'] . "'>Update</a></td>";
	echo "<td><a href = './delete.php?id_abiturient=". $row['id_abiturient'] . "'>Delete</a></td></tr>";
}

echo "</table>";

mysqli_close($link);
