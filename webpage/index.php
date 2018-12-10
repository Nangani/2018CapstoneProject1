<!DOCTYPE html>

<html lang="ko" xmlns="http://www.w3.org/1999/xhtml">
<head>
	<script src="script/jquery.js"></script>
	<style type="text/css">
		
		.index {
			vertical-align: middle;
		}
		.studentattendanceIndex{
			display: table;
			table-layout: fixed;
			width:100%;
			height:60px;
			object-fit: cover;
			background-image: url(image/attendance.png);
		}
		.studentNotattendanceIndex{
			display: table;
			table-layout: fixed;
			width:100%;
			height:60px;
			background-image: url(image/not_attendance.png);
		}
		.studentField{
			height:60px;
			text-align: middle;
			vertical-align: middle;
		}
	</style>
	<div>
		<img src="image/head_background.png" style="width:100% ;height:auto;">		
	</div>
</head>
<body background="image/total_background.jpg" onload="showClock()">
	<?php
		$conn =mysqli_connect("localhost","root","rlaehgud1!","attendance");
		mysqli_query("set names utf8;");
		mysqli_set_charset($conn,"uft8");
		mysqli_query("set session character_set_connection=euckr;");
		mysqli_query("set session character_set_results=euckr;");
		mysqli_query("set session character_set_client=euckr;");

		if(mysqli_connect_errno($conn)){
			echo "connect error :" . mysqli_connect_error();
		}
	?>
	
	<header>
		<table>
			<tr >
			</tr>
			<tr>
				<td style="width:40px"></td>
				<td class="index">
					<img id="characterImage" src="image/defaultimage.jpg" width =120px height=160px>
				</td>
				<td class="index" style="width: 50px"></td>
				<td class="index" style="font-size:40px; width:400px">
					<span id="subject" class="characterInformation"><?php echo $_POST['subject'];?>
		</span>
				</td>
				<td class="index" style="font-size:60px; width:250px">
					<span id="date" class="characterInformation" >DATE</span>
				</td>
				<form>
					<td class="index" style="width: 180px">
						<select id="subjectSelect" onchange="changeSubject()" style="width: 200px; height:50px ;font-size:25px">
							<option></option>
							<option value="capstone">capstone</option>
							<option value="embedded">embedded</option>
						</select>
					</td>	
				</form>
				<td style="width: 40px">
				</td>
				<td class="index" style="font-size:20px;">
					pasword : 
					<input type="password" id="password">
				</td>
			</tr>
		</table>	
	</div>
	</header>
		<p><학생 목록></p>
		
		<table id="studentTable">
			<thead>
			</thead>
			<tbody id="student_table_body">
			</tbody>

		</table>
		<script>

		function changeSubject(){
			
			var subject = document.getElementById("subjectSelect").value;
			var password = document.getElementById("password").value;
			document.getElementById("subject").innerHTML = subject;
			var form = document.createElement('form');
			var objs1;
			var objs2;
			objs1 = document.createElement('input');
			objs1.setAttribute('type','hidden');
			objs1.setAttribute('name',"subject");
			objs1.setAttribute('value',subject);
			
			objs2 = document.createElement('input');
			objs2.setAttribute('type','hidden');
			objs2.setAttribute('name',"password");
			objs2.setAttribute('value',password);
			
			form.appendChild(objs1);
			form.appendChild(objs2);
			form.setAttribute('method','post');
			form.setAttribute('action',"./index.php");
			document.body.appendChild(form);
			form.submit();
		}
		function showClock(){
	        var currentDate = new Date();
	        var divClock = document.getElementById("date");
	         
	        var msg = currentDate.getHours()+":" +currentDate.getMinutes()+":"+currentDate.getSeconds();
	        
	        divClock.innerText = msg;
	        setTimeout(showClock,1000);
	    }
		function addStudentTable(name,id,attendance,i,subject_id){
			var tagNumber = "row"+i;
			if(attendance == "0"){
				var html = '<tr class="studentNotattendanceIndex" id="'+tagNumber+'"> '
					+'<td style="width: 30px"></td><td class="index" id="student_name">'
					+name +'</td><td class="index" id="student_id">'+ id +'</td>'+
					'<td class="index" id="nowAttendance">불출석</td></tr>'
			}else{
				var html = '<tr class="studentattendanceIndex" id="'+tagNumber+'"> '
					+'<td style="width: 30px"></td><td class="index" id="student_name">'
					+name +'</td><td class="index" id="student_id">'+ id +'</td>'+
					'<td class="index" id="nowAttendance">출석</td></tr>'
			}
			$('#studentTable > tbody').append(html);
			var tagOrder = "#"+tagNumber;
			$(document).on("click",tagOrder,function(event){
				var tr = $(this);
				var td = tr.children();
				var student_id = td.eq(2).text();
				var attendance = td.eq(3).text();
				if(attendance =="출석"){
					$(this).attr('class','studentNotattendanceIndex');
					$(td.eq(3)).text('불출석');
				}else if(attendance =="불출석"){
					$(this).attr('class','studentattendanceIndex');
					$(td.eq(3)).text('출석');
				}
				var dataString = "attendance: " + attendance + ", student_id: "+student_id;
				$.ajax({
					url:"./updateDBWeb.php",
					type:"POST",
					data: {
						"attendance": attendance, "student_id" :student_id, "subject_id" : subject_id
					},
					success : function(data){
						alert("success");
						
					},
					error:function(){
						
						alert("fail");
					}
				});
			});
		}
	</script>

	<?php
		//class AttendancePython extends Thead{
		//	private $response;

		//	public function run(){
				//echo ("start attendance");
		//		exec("python face_recognize.py");	
		//	}
		//}
		$subject =  $_POST['subject'];
		$user_password = $_POST['password'];
		$seach_subject_id ="select lecture_id,password from lecture where lecture_name =  '".$subject."';";
		$result_subject_id = mysqli_query($conn,$seach_subject_id);

		$subject_row = mysqli_fetch_assoc($result_subject_id);
		if(strcmp($subject_row["password"],$user_password)){
			exit("<script>alert ('password error');</script>");
		}

		$seach_list_student = "select student_id,attendance from list_students where lecture_id = '".$subject_row["lecture_id"]."';";
		$result_list_student = mysqli_query($conn,$seach_list_student);
		$i=0;
		while($row = mysqli_fetch_assoc($result_list_student)){
			
			$seach_student = "select name from student where id ='".$row["student_id"]."';";
			$result_student = mysqli_query($conn,$seach_student);

			$student_row = mysqli_fetch_assoc($result_student);

			$script_str = "<script>addStudentTable('".$student_row["name"]."','".$row["student_id"]."','".$row["attendance"]."','".$i."','".$subject_row["lecture_id"]."')</script>";
			echo ($script_str);
			++$i; 
		}
		mysqli_close($conn);



	?>
</body>
