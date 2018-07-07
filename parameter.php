<?php 
session_start();
$a1=$_POST['qq'];
$c1=$_POST['select_catalog2'];
$command = "tuning.py $a1 $c1 ";
$output = shell_exec($command);
$_SESSION['totalcolumns'] = $output;
$_SESSION['a'] = $a1;
$_SESSION['c'] = $c1;
?>



<!DOCTYPE html>
<html lang="en">
<head>
	<title>Airfare Prediction</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>

	<div class="container-contact100">
		<div class="wrap-contact100">
			<form class="contact100-form validate-form" action="prediction.php" method="post">
				<span class="contact100-form-title">
					AIRFARE PREDICTION
				</span>


				


			
					<div><br>
						<h2>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspBuild successful</h2>
						</br>
					</div>
					

					<div>
						<br><h3>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspThe best parameter is <?php echo $output?></h3>
						</div>
					
<br>
				

				<div class="container-contact100-form-btn">
					<input type="submit" class="contact100-form-btn" value="Process Model">
						
					
				</div>

				
			</form>

			<div class="contact100-more flex-col-c-m" style="background-image: url('images/bg-01.jpg');">
			</div>
		</div>
	</div>

</body>
</html>
