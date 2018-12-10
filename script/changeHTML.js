
function changeSubject(){
	var subject = document.getElementById("subjectSelect").value;
	location.reload();
	documetn.getElementById("subjectSelect").innerHTML = subject;
	document.getElementById("subject").innerHTML = subject;
}

function changeDate(e){

	document.getElementById("date").innerHTML = e.target.value;
}
/*
function addStudent(name,id){
	var studentTable= document.getElementById("student_table_body");
	var row = studentTable.insertRow(studentTable.rows.length);
	var space = row.insertCell(0);
	var student_name  = row.insertCell(1);
	var student_id = row.insertCell(2);

	row.className="studentNotattendanceIndex";
	student_name.className="index";
	student_id.className="index";
	space.style.width ="30px";	
	student_name.innerHTML = name;
	student_id.innerHTML = id;
	// = rowOnclick(row,state);
}

*/
/*
$(button).click(function(){
	var row = '<tr id ="row" class="studentattendanceIndex"><td style="width: 30px"></td><td id="name" class="index">유성권</td><td id="id"class="index">20134441</td></tr>'
	$("student_table_body>tobody:last").append(row);
});
$(document).on('click','#row',function(){
	alert("click");
})
*/