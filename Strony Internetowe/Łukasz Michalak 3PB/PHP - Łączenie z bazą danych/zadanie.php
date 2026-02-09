<?php
$conn = mysqli_connect('localhost', 'root', '', 'matemax'); //podłaczenie do bazy danych
$q = 'SELECT a1, n, r FROM ciągi_arytmetyczne WHERE n<100 AND a1>5'; //warunek (kwerenda)

$result = mysqli_query($conn, $q); //pobieranie rzeczy z bazy danych
while($row = mysqli_fetch_row($result)){  //przechowywanie rzeczy z bazy danych (wyswietlanie)
    echo $row[0]." ".$row[1]."<br>";
}
mysqli_close($conn); //zamknięcie łacza z bazą danych

?>