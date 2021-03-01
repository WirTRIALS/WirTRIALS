function showNum() {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
		var num_str = this.responseText;
		document.getElementById('researcher_num').innerHTML = num_str;
		document.getElementById('expertise_num').innerHTML = num_str;
		}
	};
	xmlhttp.open("GET", "handler.php?method=show_num", true);
	xmlhttp.send();
}