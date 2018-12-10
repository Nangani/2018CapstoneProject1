
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<style type="text/css">
		body { margin-left: 0px; margin-top: 0px; margin-right: 0px; margin-bottom: 0px; }
		#center { position:absolute; top:45%; left:45%; width:300px; height:200px; }
	</style>

	</head>
	
	<body>
		<form method="post" id="center" action="./index.php">

			<table >
				<div id="clock"></div>
				과목을 고르세요
				<input type="hidden" name="action" value="form_submit" />
	  
				<select name="subject">
					<option value="capstone">capstone</option>
					<option value="embedded">embedded</option>
				</select>
				<br>
			 	비밀번호 : 
				<input type="password" name="password"><br>
				  <input type="submit" value="제출하기" />

			</table	>
		</form>
	

	<script language="javascript">
    function showClock(){
        var currentDate = new Date();
        var divClock = document.getElementById("clock");
         
        var msg = "현재 시간:"+currentDate.getHours()+"시"
        msg += currentDate.getMinutes()+"분";
        msg += currentDate.getSeconds()+"초";
        
        divClock.innerText = msg;
        setTimeout(showClock,1000);
    }
</script>

<body onload="showClock()">
    <div id="divClock" class="clock"></div>

</body>

</html>


