function edit_row(no)
{
 document.getElementById("edit_button"+no).style.display="none";
 document.getElementById("save_button"+no).style.display="block";
	
 var name=document.getElementById("name_row"+no);
 var type=document.getElementById("type_row"+no);
 var status=document.getElementById("status_row"+no);
	
 var name_data=name.innerHTML;
 var type_data=type.innerHTML;
 var status_data=status.innerHTML;
	
 name.innerHTML="<input type='text' id='name_text"+no+"' value='"+name_data+"'>";
 type.innerHTML="<input type='text' id='type_text"+no+"' value='"+type_data+"'>";
 status.innerHTML="<input type='text' id='status_text"+no+"' value='"+status_data+"'>";
}

function save_row(no)
{
 var name_val=document.getElementById("name_text"+no).value;
 var type_val=document.getElementById("type_text"+no).value;
 var status_val=document.getElementById("status_text"+no).value;

 document.getElementById("name_row"+no).innerHTML=name_val;
 document.getElementById("type_row"+no).innerHTML=type_val;
 document.getElementById("status_row"+no).innerHTML=status_val;

 document.getElementById("edit_button"+no).style.display="block";
 document.getElementById("save_button"+no).style.display="none";
}

function delete_row(no)
{
 document.getElementById("row"+no+"").outerHTML="";
}

function add_row()
{
 var new_name=document.getElementById("new_name").value;
 var new_type=document.getElementById("new_type").value;
 var new_status=document.getElementById("new_status").value;
	
 var table=document.getElementById("data_table");
 var table_len=(table.rows.length)-1;
 var row = table.insertRow(table_len).outerHTML=
 "<tr id='row"+table_len+"'><td id='name_row"+table_len+"'>"+new_name+
 "</td><td id='type_row"+table_len+"'>"+new_type+
 "</td><td id='status_row"+table_len+"'>"+new_status+
 "</td><td><input type='button' id='edit_button"+table_len+
 "'value='Edit' class='edit' onclick='edit_row("+table_len+")'> <input type='button' id='save_button"+table_len+
 "'value='Save' class='save' onclick='save_row("+table_len+")'></td><td> <input type='button' value='Delete' class='delete' onclick='delete_row("+table_len+")'></td></tr>";

 document.getElementById("new_name").value="";
 document.getElementById("new_type").value="";
 document.getElementById("new_status").value="";
}


//change tble-row color on mouse hover
var tbl = document.getElementById("tblorders");
if (tbl != null) {
    if (tbl.rows[0] != null) {
        tbl.rows[0].style.backgroundColor = "#365890";
        tbl.rows[0].style.color = "#FFFFFF";
    }
    for (var i = 1; i < tbl.rows.length; i++) {
        tbl.rows[i].style.cursor = "pointer";
        tbl.rows[i].onmousemove = function () { this.style.backgroundColor = "#FF2080"; this.style.color = "#FFFFFF"; };
        tbl.rows[i].onmouseout = function () { this.style.backgroundColor = ""; this.style.color = ""; };
    }
}

