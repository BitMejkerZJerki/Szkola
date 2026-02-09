<?php
$plik=fopen("plik.txt", "r");   

$zawartosc = fread($plik, 200);
echo $zawartosc;

$plik2=fopen("plik2.txt", "w");
fwrite($plik2, $zawartosc);
fclose($plik);
fclose($plik2);
?>