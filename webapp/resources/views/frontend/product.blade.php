@extends('frontend.layouts.app')

@section('title') {{app_name()}} @endsection

@section('content')

<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script src="https://unpkg.com/three@0.126.1/build/three.js"></script>
<script src="https://unpkg.com/three-spritetext@1.6.1/dist/three-spritetext.min.js"></script>
<script src="https://unpkg.com/3d-force-graph@1.69.1/dist/3d-force-graph.min.js"></script>
  
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js"></script>


<p id="fav_sel_name" style="display:none">{{$name}}</p>
<p id="facet_sel_name" style="display:none">{{$facet}}</p>
<?php if (Auth::check()){ ?>
	<p id="fav_sel_check" style="display:none">true</p>
<?php }else{ ?>
	<p id="fav_sel_check" style="display:none">false</p>
<?php } ?>

<div class="main-content">
<section class="header py-7 py-lg-8 pt-lg-9 bg-primary text-white" style="background:linear-gradient(0deg, rgba(6,73,178),rgba(80,155,220, 0.7)), url(img/skills.png);" >
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-md-10 text-center">
                <h2 class="display-1 mb-4">Welcome to Researchee</h2>
                <h4>We focus on Linked Data and research information.<br>
				We have <inline id='professor_num'></inline> professors, <inline id='researcher_num'></inline> researchers, and <inline id='expertise_num'></inline> expertises so far...</h4>
    <br /> <br /> 
            </div>
				<div class="col-1"></div>
				<div class="col-3">
					<select class="form-control" id='facet' onchange="changeFacet()">
						<option value='researcher' selected>Researcher</option>
						<option value='expertise'>Expertise</option>
					</select>
				</div>
				<div class="col-7">
					<input class="form-control" type="text" id="input" name="input" placeholder="input a researcher" onkeyup="liveSearch()">
				</div>
				<div class="col-1"></div>
        </div>
    </div>
    <div class="pattern bottom"></div>
</section>



<section  class="section section-ld" id="data_graph_id" style="display:none;">
    <div class="row justify-content-center">
			<div class="col-3">
				<div id='result'>
					<div style="display:none;" class="alert alert-danger text-center" id="alertFav"  style="padding-top:4px!important;padding-bottom:4px!important;width:90%;">
						<strong id="alertFavText" >Added to Favorites</strong> 
					</div>

					
					<h4>
						<span style="color:#ee514f;display:inline-block;margin-right:10px;" id="profGraph01"></span>
						<i class='fas fa-star' id="favIcon" title=" Add to Favorites"
						onclick="return changeFavorites()"></i>

					</h4>
					<a target="_blank" id="profGraph02"></a>
					<ul id="prgr03">
						<li><h6 style="color:#21344e" id="profGraph03"></h6></li>
						<li><h6 style="color:#21344e" id="profGraph04"></h6></li>
						<li><h6 style="color:#21344e" id="profGraph05"></h6></li>
					</ul>
					
			

				</div>	
			</div>

			<div class="col-7">
				<ul style="" class="nav nav-tabs" id="myTab" role="tablist">
                    <li class="nav-itemasd">
                        <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Graph</a>
                    </li>
					<li class="nav-itemasd">
                        <a class="nav-link" id="pubs-tab" data-toggle="tab" href="#pubs" role="tab" aria-controls="pubs" aria-selected="true">Publications</a>
                    </li>
                </ul>
				<div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
					<div id="3d-graph" style="border:1px solid #bfbfbf;box-shadow:5px 5px 5px 5px #bfbfbf;"></div>
				</div>
				<div class="tab-pane fade" id="pubs" role="tabpanel" aria-labelledby="pubs-tab">
					<div id="pubs_tabs_subs">
					</div>
				</div>
				
			</div>
	</div>
</section>

<section class="section section-ld" style="background-color:#f7fafc;">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2 class="mb-4 mb-lg-5 text-center">Statistics of Staffs</h2>
                <p class="text-center">
					
                </p>

            </div>
			
        </div>
    </div>
	<div class="col-12 justify-content-center">
	<canvas id="myChart" width="350" height="150"></canvas>
	</div>
</section>

<section class="section section-ld" style="background-color:#f7fafc;">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2 class="mb-4 mb-lg-5 text-center">Statistics of Expertise</h2>
                <p class="text-center">
					
                </p>

            </div>
			
        </div>
    </div>
	<div class="col-12 justify-content-center">
	<canvas id="pieChart" width="350" height="150"></canvas>
	</div>
</section>

</div>
<script>

	$("#pubs-tab").on('click',function(){
		$("#3d-graph").css("display","none")
		$("#pubs_tabs_subs").attr('style', 'max-height:600px !important;')
	})

	$("#home-tab").on('click',function(){
		$("#3d-graph").css("display","block")
		$("#pubs_tabs_subs").attr('style', 'max-height:0px !important;')
	})

	var is_logged = "false"
	$(document).ready(function(){

		is_logged = $("#fav_sel_check").text()
		
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

		$.ajax({
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

				top_color = [];
				for(var xxx = 0;xxx < 10; xxx++){
					cp = '#'+(Math.random() * 0xFFFFFF << 0).toString(16).padStart(6, '0');
					top_color.push(cp)
				}

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
					responsive: true
				}
				};

				atx = document.getElementById('pieChart').getContext('2d');
				var myPieChart = new Chart(atx, config);

				
           }  
		})

		
	})

	var pr_data=[]
	var re_data=[]
	var re_count = []
	var pr_count = []

	window.onload = showNum()
	var search_name=""
	function showNum() {
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				document.getElementById('professor_num').innerHTML = this.responseText.split(' ')[0];
				document.getElementById('researcher_num').innerHTML = this.responseText.split(' ')[1];
				document.getElementById('expertise_num').innerHTML = this.responseText.split(' ')[2];

			}
		};
		xmlhttp.open("GET", "/handler?method=show_num&name=ABV&facet=abc", true);
		xmlhttp.send();

		$.ajax({
			url: "/handler?method=graph_data&name=" + name + "&facet=" + facet,
			type:'GET',
			success: function result(data){
				$(data).each(function(i,v) {
					re_data = v["researcher"];
					pr_data = v["professor"];
					

					for(var i =0;i < re_data.length;i++){
						re_count.push(re_data[i]["y"])
					}

					for(var i =0;i < pr_data.length;i++){
						pr_count.push(pr_data[i]["y"])
					}

				});

				var ctx = document.getElementById('myChart').getContext('2d');

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
						}
					}
				});
			}
			
		})

	}

	function changeFavorites(){

		var name = ""

		if(search_name){
			name = search_name
		}else{
			name = $("#profGraph01").text()
		}

		facettt = $("#facet").val()

		
		
		
		var is_exist = 0
		$.ajax({
			url:"/getfavorites?name="+name,
			method: "POST",
			async: false,
			data:{name:name,"_token": "{{ csrf_token() }}"},
			success:function(data){
				
				 is_exist = data 
				 if(is_exist == 0)
				 {
					$("#favIcon").css('color','#c1c1c1')
				 }
           }  
		})

		if(is_exist == 0 ){
			
			$.ajax({
				url:"/favorites",
				data:{name:name,facet:facettt,"_token": "{{ csrf_token() }}"},
				method: "POST",
				success:function(data){
					
					$("#favIcon").css('color','#fea002')
					$("#alertFav").removeAttr("class")
					$("#alertFav").attr("class","alert alert-info text-center")
					$("#alertFavText").text("Added to Favorites") 
					$("#alertFav").css({"display":"block","padding-top":"4px!important","padding-bottom":"4px!important","width":"90%"})
					
					setTimeout(function() { 
							$('#alertFav').fadeOut(); 
					}, 1000);  
				}  
			})
		}else{
			$.ajax({
				url:"/delfavorites",
				data:{name:name,"_token": "{{ csrf_token() }}"},
				method: "POST",
				success:function(data){
					
					$("#favIcon").css('color','#c1c1c1') 
					$("#alertFav").removeAttr("class")
					$("#alertFav").attr("class","alert alert-danger text-center")
					$("#alertFavText").text("Removed from Favorites") 
					$("#alertFav").css({"display":"block","padding-top":"4px!important","padding-bottom":"4px!important","width":"90%"})
					setTimeout(function() { 
							$('#alertFav').fadeOut(); 
					}, 1000);  
				}  
			})
		}

	}


function search(name) {


					$("#profGraph01").text("")
					$("#profGraph02").text("")
					$("#profGraph02").removeAttr("href")
					$("#profGraph03").text("")
					$("#profGraph04").text("")
					$("#profGraph05").text("")
					$("#data_graph_id").css("display","block")

					$("#loadingDiv").css("display","block")
					

					$(function() { 
                        $('html, body').animate({
                            scrollTop: $('#data_graph_id').offset().top}, 'slow');
       			 })

	$.ajax({
			url: "/handler?method=search&name=" + name + "&facet=" + document.getElementById('facet').value,
			type:'GET',
			success: function result(data){
				$("#loadingDiv").css("display","none")
				var initData = JSON.parse(data);
			
				var search_type = document.getElementById('facet').value

				if(search_type == "researcher"){
					$("#profGraph01").text(initData.nodes[0]["id"])
					$("#profGraph02").text(initData.nodes[1]["id"])
					$("#profGraph02").attr("href",initData.nodes[1]["id"])
					$("#profGraph03").text(initData.nodes[2]["id"])
					$("#profGraph04").text(initData.nodes[3]["id"])
					$("#profGraph05").text(initData.nodes[4]["id"])

					$("#prgr03").css("display","block")
				}else{
					$("#profGraph01").text((initData.nodes[0]["id"]).toUpperCase())
					$("#profGraph02").text(initData.nodes[1]["id"])
					$("#profGraph02").attr("href",initData.nodes[1]["id"])
					$("#prgr03").css("display","none")
				}
				

				
				
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
			}
	})
		if(is_logged == "true"){
			$("#favIcon").css('display','block')
			$("#favIcon").css('display','inline-block');
			$.ajax({
				url:"/getfavorites?name="+name,
				method: "POST",
				async: false,
				data:{name:name,"_token": "{{ csrf_token() }}"},
				success:function(data){
					is_exist = data 
					if(is_exist == 0)
					{
						$("#favIcon").css('color','#c1c1c1')
					}else{
						$("#favIcon").css('color','#fea002')
					}
			}  
			})
		}else{
			$("#favIcon").css('display','none')
		}
		var pub_html = "";
		var facet_tabs = document.getElementById('facet').value

		if(facet_tabs == "researcher"){
			$("#pubs-tab").css("display","block")
			$("#pubs_tabs_subs").empty()
			$.ajax({
					url:"/publications?name="+name,
					method: "GET",
					success:function(data){
						if(data.length > 0){
							$.each(data, function( index, value ) {
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
			$("#pubs-tab").css("display","none")
		}
		
		
}

function liveSearch() {
	var name = document.getElementById('input').value;
	var facet = document.getElementById('facet').value;
	if(name.length >= 3)
	{
		//var xmlhttp = new XMLHttpRequest();
	//	xmlhttp.onreadystatechange = function() {
	//		if (this.readyState == 4 && this.status == 200) {
				//document.getElementById('liveResult').innerHTML = this.responseText;
	//			console.log(this)
	//			var availableTags = (this.responseText).split(",")
	//		}
	//		$( "#input" ).autocomplete({
	//			source: availableTags
	//		});
	//	};
		

	//	xmlhttp.open("GET", "/handler?method=live_search&name=" + name + "&facet=" + facet, true);
	//	xmlhttp.send();


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
					search(result_selected)     
				}

			});
			}
		})
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
}

function searchExpertise(name) {
	document.getElementById('facet').value = 'expertise';
	search(name)
}

function searchResearcher(name) {
	document.getElementById('facet').value = 'researcher';
	search(name)
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
</script>



@endsection
