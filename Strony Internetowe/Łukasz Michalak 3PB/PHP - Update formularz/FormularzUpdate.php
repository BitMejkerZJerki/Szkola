<form method="post">
<?php
$conn=mysqli_connect("localhost","root","","portal");
$q="SELECT id FROM dane";
$result = mysqli_query($conn,$q);

echo "<select name='id_selected'>";
while($row = mysqli_fetch_array($result)){
    echo "<option>".$row[0]."</option>";

}
echo "</select>";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<button name="btn_sel">Pokaż</button>

</form>
</body>
</html>
<?php
if(isset($_POST["btn_sel"])){
    $id =$_POST["id_selected"];
    $q1 = "SELECT * FROM dane WHERE id=$id";
    $result1 = mysqli_query($conn,$q1);
    $dane = mysqli_fetch_row($result1);
    $i = $dane[0];
    $r = $dane[1];
    $p = $dane[2];
    $h = $dane[3];
    $z = $dane[4];
    $s = $dane[5];

    echo "<form method='post'>
        <input type='number' name='id_new' hidden value='$i'/>
    <label> Rok urodzenia </label>
    <input type='number' name='rok' value='$r'/><br>
    <label> Liczba przyjaciół </label>
    <input type='number' name='przyjaciele' value='$p'/><br>
     <label> Hobby  </label>
    <input type='text' name='hobby' value='$h'/><br>
      <label> Zdjęcie  </label>
    <input type='text' name='zdjecie' value='$s'/><br>
      <label> Stanowisko  </label>
    <input type='text' name='stanowisko' value='$z'/><br>
</form>";
}
if (isset($_POST["btn_upd"])) {
    $id_new =$_POST['id_new'];
    $r_new =$_POST['r_new'];
    $p_new =$_POST['p_new'];
    $h_new =$_POST['h_new'];
    $z_new =$_POST['z_new'];
    $s_new =$_POST['s_new'];

    $q2="UPDATE dane SET rok_urodz = $r_new, przyjaciol =$p_new, hobby='$h_new',zdjecie = '$z_new', stanowisko ='$s_new' WHERE id=$id_new";

}


?>
