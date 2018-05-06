<?php

// delete records

include "connection.php";

$id_abiturient = $_GET['id_abiturient'];

$query = "DELETE FROM abit
	WHERE id_abiturient ='" . $id_abiturient . "'";

$result = mysqli_query($link, $query);

// redirect
header('location: ./list.php');
