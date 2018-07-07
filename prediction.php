<?php
session_start();
$columns = $_SESSION['totalcolumns'];
$a = $_SESSION['a'];
$c = $_SESSION['c'];
$q1=(int)$columns[1];
$q2=(int)$columns[4];
$q3=(int)$columns[7];
$command1 = "predictor.py $q1 $q2 $q3 $a $c ";
$output1 = shell_exec($command1);
echo '<img src="fig.png">' ;
?> 



