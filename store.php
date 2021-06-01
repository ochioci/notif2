<?php

$dataToPut = "none";
$dataToPut = file_get_contents('php://input');
file_put_contents("data.txt", $dataToPut);
echo ($dataToPut);




?> 