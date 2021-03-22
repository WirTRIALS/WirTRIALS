<?php
$method = $_REQUEST["method"];
$name = $_REQUEST["name"];
$facet = $_REQUEST["facet"];

$xml = simplexml_load_file ( "database.xml" );
$ns = $xml->getNamespaces(true);

switch ($method) {
	case "show_num":

		$pro_num = 0;
		$res_num = 0;
		$exp_num = 0;
		foreach ($xml->children($ns['rdf'])->Description as $resource) {

			if ($resource->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/DefinedTerm" )
				$exp_num += 1;
			else if ($resource->children($ns['schema'])->jobTitle == 'Professor' )
				$pro_num += 1;
			else if ($resource->children($ns['schema'])->jobTitle == 'Researcher' )
				$res_num += 1;
		}

		echo $pro_num . ' ' . $res_num . ' ' . $exp_num;
		break;

	case "search":
		if( $facet == 'researcher') {
			foreach ($xml->children($ns['rdf'])->Description as $researcher) {
				if($researcher->children($ns['schema'])->name == $name) {
					$res_id = ($researcher->attributes($ns['rdf'])->about).trim();
					$res_group = ($researcher->children($ns['aiiso'])->ResearchGroup).trim();
					$res_institute = ($researcher->children($ns['aiiso'])->Institute).trim();
					$res_faculty = ($researcher->children($ns['aiiso'])->Faculty).trim();
					$res_title = ($researcher->children($ns['schema'])->jobTitle).trim();
					
					$nodes = '[' . json_encode(Array('id'=>$name, 'weight'=>'15', 'group'=> 1));
					$nodes = $nodes . ',' . json_encode(Array('id'=> $res_id, 'weight'=>'5', 'group'=> 3));
					$nodes = $nodes . ',' . json_encode(Array('id'=> $res_group, 'weight'=>'5', 'group'=> 4));
					$nodes = $nodes . ',' . json_encode(Array('id'=> $res_institute, 'weight'=>'5', 'group'=> 5));
					$nodes = $nodes . ',' . json_encode(Array('id'=> $res_faculty, 'weight'=>'5', 'group'=> 6));
					$nodes = $nodes . ',' . json_encode(Array('id'=> $res_title, 'weight'=>'5', 'group'=> 7));
					
					$links = '[' . json_encode(Array('source'=>$name, 'target'=>$res_id, 'value'=> 3));
					$links = $links . ',' . json_encode(Array('source'=>$name, 'target'=>$res_group, 'value'=> 4));
					$links = $links . ',' . json_encode(Array('source'=>$name, 'target'=>$res_institute, 'value'=> 5));
					$links = $links . ',' . json_encode(Array('source'=>$name, 'target'=>$res_faculty, 'value'=> 6));
					$links = $links . ',' . json_encode(Array('source'=>$name, 'target'=>$res_title, 'value'=> 7));
					
					foreach( $researcher->children($ns['schema'])->knowsAbout as $bnode) {
						
						$nodeID = $bnode->attributes($ns['rdf'])->nodeID;

						foreach ($xml->children($ns['rdf'])->Description as $bnode2) {

							$nodeID2 = $bnode2->attributes($ns['rdf'])->nodeID;
							
							if($nodeID.trim() == $nodeID2.trim()) {

								$exp_id = ($bnode2->children($ns['schema'])->identifier->attributes($ns['rdf'])->{'resource'}).trim();
																
								foreach ($xml->children($ns['rdf'])->Description as $expertise) {

									if(($expertise->attributes($ns['rdf'])->about).trim() == $exp_id) {
										
										$exp_name = ($expertise->children($ns['schema'])->name).trim();
										$nodes = $nodes . ',' . json_encode(Array('id'=>$exp_name, 'weight'=>'8', 'group'=> 2));
										
										$links = $links . ',' . json_encode(Array('source'=>$name, 'target'=>$exp_name, 'value'=> 2));
										
									}
								}
							}
						}
					}
					$nodes = $nodes . ']';
					$links = $links . ']';
					echo json_encode(Array('nodes'=>json_decode($nodes),'links'=>json_decode($links)));
					break;
				}
			}
		}
		else
		{
			foreach ($xml->children($ns['rdf'])->Description as $expertise) {
				if($expertise->children($ns['schema'])->name == $name) {	

					$exp_id = $expertise->attributes($ns['rdf'])->{'about'}.trim();
					
					$nodes = '[' . json_encode(Array('id'=>$name, 'weight'=>'15', 'group'=> 1));
					$nodes = $nodes . ',' . json_encode(Array('id'=> $exp_id, 'weight'=>'5', 'group'=> 3));
					
					$links = '[' . json_encode(Array('source'=>$name, 'target'=>$exp_id, 'value'=> 3));
					
					foreach ($xml->children($ns['rdf'])->Description as $bnode) {

						if(($bnode->children($ns['schema'])->identifier->attributes($ns['rdf'])->{'resource'}).trim() == $exp_id)
						{
							
							$nodeID = ($bnode->attributes($ns['rdf'])->nodeID).trim();
							
							foreach($xml->children($ns['rdf'])->Description as $researcher) {

								$flag = false;
								foreach( $researcher->children($ns['schema'])->knowsAbout as $bnode2) {
									if(($bnode2->attributes($ns['rdf'])->nodeID).trim() == $nodeID) {
										$flag = true;
										break;
									}
								}
								if($flag == true) {
									
									$res_name = ($researcher->children($ns['schema'])->name).trim();
									
									$nodes = $nodes . ',' . json_encode(Array('id'=>$res_name, 'weight'=>'8', 'group'=> 2));
										
									$links = $links . ',' . json_encode(Array('source'=>$name, 'target'=>$res_name, 'value'=> 2));
										
								}
							}
						}
					}

					$nodes = $nodes . ']';
					$links = $links . ']';
					echo json_encode(Array('nodes'=>json_decode($nodes),'links'=>json_decode($links)));
					break;
				}
			}
		}
		
		break;
		
	case "live_search":
		if( $facet == 'researcher') {
			$count = 0;
			foreach ($xml->children($ns['rdf'])->Description as $researcher) {
				
				if($researcher->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/Person") {
					
					if( strpos(strtolower($researcher->children($ns['schema'])->name), strtolower($name)) !== false) {
						$count += 1;
						if( $count <= 5)
						{
							echo '<span onclick="autofill(this.innerHTML)">'. $researcher->children($ns['schema'])->name . '</span><br>';
						}
					
					}
				}
			}
		}
		else
		{
			$count = 0;
			foreach ($xml->children($ns['rdf'])->Description as $expertise) {
				
				if($expertise->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/DefinedTerm")
				{
					if( strpos(strtolower($expertise->children($ns['schema'])->name), strtolower($name)) !== false) {
						
						$count += 1;
						if( count <= 5)
						{
							echo '<span onclick="autofill(this.innerHTML)">'. $expertise->children($ns['schema'])->name . '</span><br>';
						}
					}
				}
			}
		}
		break;
}
?>
