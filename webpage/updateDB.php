<?php
	$student_id = $_POST['student_id'];
	$attendance = $_POST['attendance'];
	$subject_id = $_POST['subject_id'];	

	$conn =mysqli_connect("localhost","root","rlaehgud1!","attendance");
	mysqli_query("set names utf8;");
	mysqli_set_charset($conn,"uft8");
	mysqli_query("set session character_set_connection=euckr;");
	mysqli_query("set session character_set_results=euckr;");
	mysqli_query("set session character_set_client=euckr;");
	if(mysqli_connect_errno($conn)){
		echo "connect error :" . mysqli_connect_error();
	}
	$changeAttendance;
	if($attendance == "출석"){
		$changeAttendance = "update list_students set attendance = 0 where student_id = ".$student_id." AND lecture_id = ".$subject_id.";";
	}
	else if($attendance == "불출석"){
		$changeAttendance = "update list_students set attendance = 1 where student_id = ".$student_id." AND lecture_id = ".$subject_id.";";
	}
	
	mysqli_query($conn,$changeAttendance);
	mysqli_close($conn);
	echo ($attendance);
?>