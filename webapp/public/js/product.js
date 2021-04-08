
var is_logged = "false" // flag to check if user is logged in

$(document).ready(function(){
	is_logged = $("#fav_sel_check").text()
	
    //checks and displays favorite icon if user is logged in 
	if(is_logged == "true"){ 
		favorite_name = $("#fav_sel_name").text()
		facet_name_fav = $("#facet_sel_name").text()
		if(favorite_name){
			var faacc = $("#facet_sel_name").text()
			$("#input").val(favorite_name)
			$("#facet").val(facet_name_fav)
			
			window.history.pushState({}, document.title, "/" + "product");
			search(favorite_name)
		}
	}
    // graph to display top expertise pie chart
	$.ajax({ // ajax call to fetch top expertise 
		url:"/topexpertise",
		method: "GET",
		success:function(data){
			prop = "count"
			data.sort(function(a, b) {
				return (b[prop] > a[prop]) ? 1 : ((b[prop] < a[prop]) ? -1 : 0);
			});
			var frameArray= [];
			for(var i = 0;i< 10;i++){
				
				frameArray.push(data[i]);
			}
			var top_titles =[]
			var top_expst_cnt = []
			$(frameArray).each(function(i,v) {
				top_titles.push(v["title"])
			})
			$(frameArray).each(function(i,v) {
				top_expst_cnt.push(v["count"])
			})
			var config = {
			type: 'pie',
			data: {
				datasets: [{
					data: top_expst_cnt,
					backgroundColor: [
						'#D79A9A',
						'#FF8C69',
						'#FFF5EE',
						'#F2B263',
						'#FFC259',
						'#F6EEAC',
						'#FFFBD5',
						'#ffb1c1',
						'#9ad0f5',
						'#FFFF6F'
					],
					label: 'Dataset 1'
				}],
				labels: top_titles
			},
			options: {
				responsive: true,
				maintainAspectRatio: false
			}
			};
			atx = document.getElementById('pieChart').getContext('2d');
			var myPieChart = new Chart(atx, config);
			
       }  
	})
	
})

//variable for storing publictaion and researcher data
var pr_data=[] 
var re_data=[]
var re_count = []
var pr_count = []

window.onload = showNum() // call showNum function on window load
var search_name=""

    //fetch and display researcher,professor and expertise count 
function showNum() { 
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				document.getElementById('professor_num').innerHTML = this.responseText.split(' ')[0];
				document.getElementById('researcher_num').innerHTML = this.responseText.split(' ')[1];
				document.getElementById('expertise_num').innerHTML = this.responseText.split(' ')[2];

			}
		};
		xmlhttp.open("GET", "/handler?method=show_num&name=&facet=researcher", true);
		xmlhttp.send();

        //fetch Staff Statistics
		$.ajax({
			url: "/handler?method=graph_data&name=&facet=researcher",
			type:'GET',
			success: function result(data){
				$(data).each(function(i,v) {
					re_data = v["researcher"];
					pr_data = v["professor"];
					

					for(var i =0;i < re_data.length;i++){
						re_count.push(re_data[i]["y"]) //push researcher into array
					}

					for(var i =0;i < pr_data.length;i++){
						pr_count.push(pr_data[i]["y"]) //push publication into array
					}

				});

				var ctx = document.getElementById('myChart').getContext('2d'); //initilize graph

                //labels and datasets for faculty 
				var barChartData = {
						labels: ["Human- und Sozialwissenschaften","Maschinenbau","Mathematik",
								"Elektrotechnik und Informationstechnik","Naturwissenschaften",
								"Wirtschaftswissenschaften","Philosophische","Informatik"], 
						datasets: [{
							label: 'Researcher',
							backgroundColor: 'rgba(154,208,245)',
							data: re_count
						}, {
							label: 'Professor',
							backgroundColor: 'rgba(255,177,193)',
							data: pr_count
						}]

				};

                //build Staff Statistics graph
				var myChart = new Chart(ctx, {
					type: 'bar',
					data: barChartData,
					options: {
						scales: {
							yAxes: [{
								ticks: {
									beginAtZero: true
								}
							}]
						},
						responsive: true,
						maintainAspectRatio: false
					}
				});
			}
			
		})

}



//fetch details of researcher/expertise and build 3d graph 
function search(name) {
    //empty details of researcher/expertise 
	$("#profGraph01").text("")
	$("#profGraph02").text("")
	$("#profGraph02").removeAttr("href")
	$("#profGraph03").remove()
	$("#profGraph04").remove()
	$("#profGraph05").remove()
	$("#data_graph_id").css("display","block")

	$("#loadingDiv").css("display","block")
	

	$(function() { 
        $('html, body').animate({
            scrollTop: $('#data_graph_id').offset().top}, 'slow');
    })

    //ajax call to fetch data of researcher/expertise entered by user
	$.ajax({
			url: "/handler?method=search&name=" + name + "&facet=" + document.getElementById('facet').value,
			type:'GET',
			success: function result(data){
				$("#loadingDiv").css("display","none")
				var initData = JSON.parse(data);
				var search_type = document.getElementById('facet').value

				if(search_type == "researcher"){ //display data of researcher
				
					$("#profGraph01").text(initData.nodes[0]["id"])
					$("#profGraph02").text(initData.nodes[1]["id"])
					$("#profGraph02").attr("href",initData.nodes[1]["id"])
					if(initData.nodes[2]['id'])
						$("#prgr03").append("<li id='profGraph03'><h6 style='color:#21344e'>"+initData.nodes[2]['id']+"</h6></li>")
					
					if(initData.nodes[3]['id'])
						$("#prgr03").append("<li id='profGraph04'><h6 style='color:#21344e'>"+initData.nodes[3]['id']+"</h6></li>")
					
					if(initData.nodes[4]['id'])
						$("#prgr03").append("<li id='profGraph05'><h6 style='color:#21344e'>"+initData.nodes[4]['id']+"</h6></li>")
					

					$("#prgr03").css("display","block")
				}else{
                    //display data of expertise
					$("#profGraph01").text((initData.nodes[0]["id"]).toUpperCase())
					$("#profGraph02").text(initData.nodes[1]["id"])
					$("#profGraph02").attr("href",initData.nodes[1]["id"])
					$("#prgr03").css("display","none")
				}
				

				
				//build 3d graph
				const elem = document.getElementById('3d-graph');
				const Graph = ForceGraph3D()(elem)
					.backgroundColor("#ffffff")
					.width(800)
					.height(600)
					.graphData(initData)
					.linkDirectionalParticles('value')
					.linkAutoColorBy('value')
					.linkWidth(0.5)
					.linkOpacity(0.3)
					.nodeAutoColorBy('group')
					.zoomToFit()
					.cameraPosition({ z: 250 })
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
				
                //make 3d graph responsive
				elementResizeDetectorMaker().listenTo(
				document.getElementById('3d-graph'),
				el => Graph.width(el.offsetWidth)
				);

			}
	})
        //check if researcher/expertise if bookmarked of logged in user
		if(is_logged == "true"){
			$("#favIcon").css('display','block')
			$("#favIcon").css('display','inline-block');

			getFavs(name)
			
		}else{
            //change design of bookmark icon
			$("#favIcon").css('display','none')
		}

		var pub_html = "";
		var facet_tabs = document.getElementById('facet').value

        //fetch publication of researcher
		if(facet_tabs == "researcher"){ // if facet is researcher show publication tab
			$("#pubs-tab").css("display","block")
			$("#pubs_tabs_subs").empty()
			$.ajax({
					url:"/publications?name="+name,
					method: "GET",
					success:function(data){
						if(data.length > 0){
							$.each(data, function( index, value ) {
                                //display the fetched data of publications
								doi_link = "https://doi.org/" + value.DOI
								pub_html = "<div style='background-color:#c1c1c1 !important' class='alert alert-secondary'><p style='color:black'><b>"+value.title+"</b></p>"

								if(value.DOI){
									pub_html = pub_html + "<a style='color:#3b6ac1' target='_blank' href="+doi_link+">DOI: "+doi_link+"</a>"
								}
											
								pub_html = pub_html + "<p style='color:black'>Published Date: "+value.year+"</p><p style='color:black'>Coauthors: "
								
								$.each(value.authors, function( i, v ) {
									pub_html = pub_html + "<span>"+v+"</span>"+"," + " " 
								})
								pub_html = pub_html.substring(0, pub_html.length - 2) + "</p></div>"
								$("#pubs_tabs_subs").append(pub_html)
							});
						}else{
							$("#pubs_tabs_subs").append("<h4>No Data Found</h4>")
						}
					
				}  
			})
		}else{
			$("#pubs-tab").css("display","none") // if facet is expertise hide publication tab
		}
		
		
}

//auto-complete suggestion for researcher/expertise
function liveSearch() {
	var name = document.getElementById('input').value;
	var facet = document.getElementById('facet').value;
	if(name.length >= 1) 
	{
		$.ajax({
			url: "/handler?method=live_search&name=" + name + "&facet=" + facet,
			type:'GET',
			success: function result(data){
				var availableTags = (data).split(",")
				$( "#input" ).autocomplete({
				source: availableTags,
				select: function( event, ui ) {
					var result_selected = ui.item.value;
					search_name = result_selected
					search(result_selected) //call search function
				}

			});
			}
		})
	}
}

//add placeholder to input box as per user selected facet 
function changeFacet() {
	if(document.getElementById('facet').value == 'expertise')
		document.getElementById('input').placeholder = 'input an expertise';
		
	else
		document.getElementById('input').placeholder = 'input a researcher';
		
	document.getElementById('input').value = '';
}

//function to search expertise
function searchExpertise(name) {
	document.getElementById('facet').value = 'expertise';
	search(name)
}

//function to search researcher
function searchResearcher(name) {
	document.getElementById('facet').value = 'researcher';
	search(name)
}

//function to search nodes inside 3d graph
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