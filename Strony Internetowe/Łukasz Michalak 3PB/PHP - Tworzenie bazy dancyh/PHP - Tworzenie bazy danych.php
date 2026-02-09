<form method="post">
<label> Podaj nazwę bazy dancyh </label>
<input type="text" id="newdb" name="newdb">
<input type="submit" id="btn" name="btn">
</form>

<?php
if(isset($_POST["btn"])){
    $newdb = $_POST["newdb"];
    $conn = mysqli_connect("localhost","root","");
    $q="SHOW DATABASES";
    $result = mysqli_query($conn, $q);

    $nowaBaza = $newdb;
    $i = 0;


    
    while ($row = mysqli_fetch_row($result)) {
        if($row[0] == $newdb)
        {
            echo "Baza " ."<b>" .$newdb ."</b>" ." już istnieje";
            $i = 1;
        }
    } 

    if($i == 0){
        $q2="CREATE DATABASE $newdb";
        echo "Pomyślnie utworzono bazę danych!";
        mysqli_query($conn, $q2);
    
    }
}

?>