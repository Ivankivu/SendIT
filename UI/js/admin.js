function edit_row(no)
{
 document.getElementById("edit_button"+no).style.display="none";
 document.getElementById("save_button"+no).style.display="block";
	
 var location=document.getElementById("location_row"+no);
 var status=document.getElementById("status_row"+no);
	
 var location_data=location.innerHTML;
 var status_data=status.innerHTML;
	
 location.innerHTML="<input type='text' id='location_text"+no+"' value='"+location_data+"'>";
 status.innerHTML="<input type='text' id='status_text"+no+"' value='"+status_data+"'>";
}

function save_row(no)
{
 var location_val=document.getElementById("location_text"+no).value;
 var status_val=document.getElementById("status_text"+no).value;

 document.getElementById("location_row"+no).innerHTML=location_val;
 document.getElementById("status_row"+no).innerHTML=status_val;

 document.getElementById("edit_button"+no).style.display="block";
 document.getElementById("save_button"+no).style.display="none";
}