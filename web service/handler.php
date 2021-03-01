<?php
$method = $_REQUEST["method"];

$xml = simplexml_load_file ( "database.xml" );
$xml->registerXPathNamespace('schema', 'http://schema.org/');
$xml->registerXPathNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#');


switch ($method) {
	case "show_num":
		$result = $xml->xpath('//schema:jobTitle');
		print($result->count());

		break;
	}

?>