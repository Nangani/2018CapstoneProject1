<html>
id : 
<span id="id"><?php echo $_POST['student_id'];?></span><br>
name :
<span id="name"><?php echo $_POST['student_name'];?></span><br>
picture :
<span id="name"><?php echo $_POST['student_picture_path'];?></span><br>
<br><br>
<?php
	$student_id = $_POST['student_id'];
	$student_name = $_POST['student_name'];
	$face_picture = $_POST['student_picture_path'];
	$conn =mysqli_connect("localhost","root","rlaehgud1!","attendance");
	mysqli_query("set names utf8;");
	mysqli_set_charset($conn,"uft8");
	mysqli_query("set session character_set_connection=euckr;");
	mysqli_query("set session character_set_results=euckr;");
	mysqli_query("set session character_set_client=euckr;");
	if(mysqli_connect_errno($conn)){
		echo "connect error :" . mysqli_connect_error();
	}
	//$command = escapeshellcmd('python pre_execute.py kim_gyung_jin.jpg');
	//$output = shell_exec($command)
	$outputs = exec("python extract_dot_to_list.py ".$face_picture,$output);
	
	$string_output = implode("", $output);
	$string_output;
	$queryString = "insert into student values('".$student_id."','".$student_name."','".$string_output."');";
	echo $queryString;
	if (mysqli_query($conn, $queryString)) {
	    echo "<script>alert ('insert new student successfully')</script>";
	} else {
	    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
	}
	mysqli_close($conn);
	
?>
