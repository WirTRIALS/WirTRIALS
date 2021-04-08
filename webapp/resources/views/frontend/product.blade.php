@extends('frontend.layouts.app')

@section('title') {{app_name()}} @endsection

@section('content')

<style>
	.wrapperxx {
		height: 500px !important;
	}
</style>

 <script src="//unpkg.com/element-resize-detector/dist/element-resize-detector.min.js"></script>
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
</section>



<section  class="section section-ld" id="data_graph_id" style="display:none;">
    <div class="row justify-content-center">
			<div class="col-md-3 col-sm-12" style="padding:20px ">
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
						
					</ul>
					
			

				</div>	
			</div>

			<div class="col-md-7 col-sm-12" style="padding:20px">
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
	<div class="wrapperxx">
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
	//maintain height of publication section
	$("#pubs-tab").on('click',function(){
		$("#3d-graph").css("display","none")
		$("#pubs_tabs_subs").attr('style', 'max-height:600px !important;')
	})

	//maintain height of 3d graph section
	$("#home-tab").on('click',function(){
		$("#3d-graph").css("display","block")
		$("#pubs_tabs_subs").attr('style', 'max-height:0px !important;')
	})

	//this function toggles favorites on and off 
function changeFavorites(){
		var name = ""
        //check and set value of researcher/expertise
		if(search_name){ 
			name = search_name
		}else{
			name = $("#profGraph01").text()
		}

		facettt = $("#facet").val() //fetch facet selected by user

        //check if researcher/expertise is bookmarked
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
					$("#favIcon").css('color','#c1c1c1') //if not bookmarked change color of favorite icon
				 }
           }  
		})

        
		if(is_exist == 0 ){
			//if not bookmarked call to server and bookmark expertise/researcher 
			$.ajax({
				url:"/favorites",
				data:{name:name,facet:facettt,"_token": "{{ csrf_token() }}"},
				method: "POST",
				success:function(data){
					//change design of favorite icon 
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
            //if bookmarked call to server and remove bookmark of expertise/researcher 
			$.ajax({
				url:"/delfavorites",
				data:{name:name,"_token": "{{ csrf_token() }}"},
				method: "POST",
				success:function(data){
					//change design of favorite icon 
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

function getFavs(name){
	$.ajax({ //get bookmark status of researcher/expertise
				url:"/getfavorites?name="+name,
				method: "POST",
				async: false,
				data:{name:name,"_token": "{{ csrf_token() }}"},
				success:function(data){
					is_exist = data 
					if(is_exist == 0)
					{
						$("#favIcon").css('color','#c1c1c1') //change design of bookmark icon
					}else{
						$("#favIcon").css('color','#fea002') //change design of bookmark icon
					}
			}  
			})
}
</script>

@endsection
