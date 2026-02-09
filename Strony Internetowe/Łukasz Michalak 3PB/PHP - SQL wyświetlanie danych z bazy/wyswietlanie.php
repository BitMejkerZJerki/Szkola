<?php
    $conn = mysqli_connect("localhost","root", "", "nazwa_bazy_danych");

    $q = "SELECT * FROM nazwa_tabeli"; // "SELECT id, nazwa_kolumny FROM nazwa_tabeli
    $result = mysqli_query($conn, $q);

    while($row = mysqli_fetch_array($result)){
        echo $row[0]." "; // id
        echo $row[1]." "; //pierwsza kolumna
    }

    mysqli_close($conn);
?>