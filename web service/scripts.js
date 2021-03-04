function showNum() {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById('researcher_num').innerHTML = this.responseText.split(' ')[0];
			document.getElementById('expertise_num').innerHTML = this.responseText.split(' ')[1];;
		}
	};
	xmlhttp.open("GET", "handler.php?method=show_num", true);
	xmlhttp.send();
}

function search() {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var text = this.responseText;
			if( text.length == 0)
				text = 'no result';
			document.getElementById('result').innerHTML = text;
		}
	};
	
	document.getElementById('liveResult').innerHTML = ''
	
	xmlhttp.open("GET", "handler.php?method=search&name=" + document.getElementById('input').value + "&facet=" + document.getElementById('facet').value, true);
	xmlhttp.send();
}

function liveSearch() {
	var name = document.getElementById('input').value;
	var facet = document.getElementById('facet').value;
	if(name.length >= 3)
	{
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				document.getElementById('liveResult').innerHTML = this.responseText;
			}
		};

		xmlhttp.open("GET", "handler.php?method=live_search&name=" + name + "&facet=" + facet, true);
		xmlhttp.send();
	}
	else
	{
		document.getElementById('liveResult').innerHTML = ''
	}
}

function autofill(name) {
	document.getElementById('input').value = name;
	search();
}

function changeFacet() {
	document.getElementById('input').value = '';
	document.getElementById('liveResult').innerHTML = '';
}

function searchExpertise(name) {
	document.getElementById('facet').value = 'expertise';
	autofill(name)
}

function searchResearcher(name) {
	document.getElementById('facet').value = 'researcher';
	autofill(name)
}