<?php
$method = $_REQUEST["method"];
$name = $_REQUEST["name"];
$facet = $_REQUEST["facet"];

$xml = simplexml_load_file ( "database.xml" );
$ns = $xml->getNamespaces(true);

switch ($method) {
	case "show_num":

		$researcher_num = 0;
		foreach ($xml->xpath('//schema:jobTitle') as $resource) {
			$researcher_num += 1;
		}

		$total_num = 0;
		foreach ($xml->xpath('//schema:name') as $resource2) {
			$total_num += 1;
		}
		
		$total_num -= $researcher_num;
		echo $researcher_num . ' ' . $total_num;
		break;

	case "search":
		if( $facet == 'researcher') {
			foreach ($xml->children($ns['rdf'])->Description as $researcher) {
				if($researcher->children($ns['schema'])->name == $name) {
					$res_id = $researcher->attributes($ns['rdf'])->about;
					echo '<br><span><h3>' . $name . '</h3></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
					echo '<a href="' . $res_id . '" target="_blank"><span>' . $res_id . '</span></a><br>';
					echo '<br><strong>Expertise List:</strong><br>';
					
					foreach( $researcher->children($ns['schema'])->knowsAbout as $expertise) {
						
						$exp = $expertise->attributes($ns['rdf'])->{'resource'};
						
						foreach ($xml->children($ns['rdf'])->Description as $expertise2) {

							$exp2 = $expertise2->attributes($ns['rdf'])->{'about'};
							
							if($exp.trim() == $exp2.trim()) {
								
								echo "<br><span onclick='searchExpertise(this.innerHTML)'>" . $expertise2->children($ns['schema'])->name . "</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
								echo "<a href='" . $expertise->attributes($ns['rdf'])->{'resource'} . "' target='_blank'>" . $expertise->attributes($ns['rdf'])->{'resource'} . "</a>";
							}
						}
					}
					break;
				}
			}
		}
		else
		{
			foreach ($xml->children($ns['rdf'])->Description as $expertise) {
				if($expertise->children($ns['schema'])->name == $name) {	

					$exp_id = $expertise->attributes($ns['rdf'])->{'about'};
					echo '<br><span><h3>' . $name . '</h3></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
					echo '<a href="' . $exp_id . '" target="_blank"><span>' . $exp_id . '</span></a><br>';
					echo '<br><strong>Experts in this field:</strong><br>';

					foreach ($xml->children($ns['rdf'])->Description as $researcher) {

						$flag = false;
						foreach( $researcher->children($ns['schema'])->knowsAbout as $expertise2) {
							if($expertise2->attributes($ns['rdf'])->{'resource'}.trim() == $exp_id.trim()) {
								$flag = true;
								break;
							}
						}
						if($flag == true) {
							echo "<br><span onclick='searchResearcher(this.innerHTML)'>" . $researcher->children($ns['schema'])->name . "</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
							echo "<a href='" . $researcher->attributes($ns['rdf'])->{'about'} . "' target='_blank'>" . $researcher->attributes($ns['rdf'])->{'about'} . "</a>";
						}
					
					}
					break;
				}
			}
		}
		
		break;
		
	case "live_search":
		if( $facet == 'researcher') {
			foreach ($xml->children($ns['rdf'])->Description as $researcher) {
				
				if($researcher->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/Person") {
					
					if( strpos(strtolower($researcher->children($ns['schema'])->name), strtolower($name)) !== false) {
						echo '<span onclick="autofill(this.innerHTML)">'. $researcher->children($ns['schema'])->name . '</span><br>';
					
					}
				}
			}
		}
		else
		{
			foreach ($xml->children($ns['rdf'])->Description as $expertise) {
				
				if($expertise->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/Person")
					continue;
				else {
					if( strpos(strtolower($expertise->children($ns['schema'])->name), strtolower($name)) !== false) {
						
						echo '<span onclick="autofill(this.innerHTML)">'. $expertise->children($ns['schema'])->name . '</span><br>';
					
					}
				}
			}
		}
		break;
}
?>
