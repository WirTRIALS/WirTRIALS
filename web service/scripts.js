
function showNum() {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById('professor_num').innerHTML = this.responseText.split(' ')[0];
			document.getElementById('researcher_num').innerHTML = this.responseText.split(' ')[1];
			document.getElementById('expertise_num').innerHTML = this.responseText.split(' ')[2];

		}
	};
	xmlhttp.open("GET", "handler.php?method=show_num", true);
	xmlhttp.send();
}

function search() {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			//document.getElementById('result').innerHTML = this.responseText;
			var initData = JSON.parse(this.responseText);
			
			const elem = document.getElementById('3d-graph');
			const Graph = ForceGraph3D()(elem)
				.graphData(initData)
				.linkDirectionalParticles('value')
				.linkAutoColorBy('value')
				.linkWidth(0.5)
				.linkOpacity(0.3)
				.nodeAutoColorBy('group')
				.onNodeHover(node => elem.style.cursor = node ? 'pointer' : null)
				.onNodeClick(node => searchInGraph(node.id,node.group))
				.nodeThreeObject(node => {
				  const sprite = new SpriteText(node.id);
				  sprite.material.depthWrite = false; // make sprite background transparent
				  sprite.color = node.color;
				  sprite.textHeight = node.weight;
				  return sprite;
				});

			// Spread nodes a little wider
			Graph.d3Force('charge').strength(-500);
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
	if(document.getElementById('facet').value == 'expertise')
		document.getElementById('input').placeholder = 'input an expertise';
	else
		document.getElementById('input').placeholder = 'input a researcher';
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

function searchInGraph(name,group) {
	if(group == 2)
	{		
		facet = document.getElementById('facet').value;
		if(facet == 'researcher')
			searchExpertise(name);
		else
			searchResearcher(name);
	}
	else if(group == 3)
	{
		window.open(name)
	}

}