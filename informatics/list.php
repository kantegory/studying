<?php

include 'connection.php';

$query = "SELECT abit.name, 100 - (exam_balls.max_exam_balls - exams.sum_exam_balls) AS chance
          FROM abit JOIN (exam_balls JOIN exams ON exam_balls.id_exam_balls = exams.id_exam) 
		  ON abit.id_abiturient = exams.id_exam";

$result = mysqli_query($link, $query);

echo "<table border = 1 align=center> <tr> <td> Имя </td> <td> Шанс </td></tr>";

while($row = mysqli_fetch_array($result)) {
	echo "<tr><td>" . $row['name']. "</td><td>" . $row['chance'] . "</td></tr>";
}

echo "</table>";

mysqli_close($link);
