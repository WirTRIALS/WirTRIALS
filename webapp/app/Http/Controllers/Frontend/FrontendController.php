<?php

namespace App\Http\Controllers\Frontend;
use Auth;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\favorites;

class FrontendController extends Controller
{
    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $body_class = '';

        return view('frontend.index', compact('body_class'));
    }

    public function product()
    {
        $name ="";
        if (!empty($_GET['name'])) {
            $name = (string)$_GET['name'];
        }

        $body_class = '';
        

        return view('frontend.product', compact('body_class'),['name' => $name]);
    }
    
    public function handler(){
        $method = $_REQUEST["method"];
        $name = $_REQUEST["name"];
        $facet = $_REQUEST["facet"];
        
        $str = file_get_contents(public_path("database.xml"));
        $xml = simplexml_load_string ($str);
        $ns = $xml->getNamespaces(true);
        
        switch ($method) {
            case "graph_data":
        
                $pro_num = 0;
                $res_num = 0;
                $exp_num = 0;
                $r_data = array();
                $p_data = array();
                $alldata = array();

                $re_data = array();
                $pr_data = array();

                $fac01 = "Fakultät für Human- und Sozialwissenschaften";
                $fac02 = "Fakultät für Maschinenbau";
                $fac03 = "Fakultät für Mathematik";
                $fac04 = "Fakultät für Elektrotechnik und Informationstechnik";
                $fac05  = "Fakultät für Naturwissenschaften";
                $fac06 = "Fakultät für Wirtschaftswissenschaften";
                $fac07 = "Philosophische Fakultät";
                $fac08 = "Fakultät für Informatik";
                
                $fac01_cntr_p = 0;
                $fac02_cntr_p = 0;
                $fac03_cntr_p = 0;
                $fac04_cntr_p = 0;
                $fac05_cntr_p = 0;
                $fac06_cntr_p = 0;
                $fac07_cntr_p = 0;
                $fac08_cntr_p = 0;

                $fac01_cntr_r = 0;
                $fac02_cntr_r = 0;
                $fac03_cntr_r = 0;
                $fac04_cntr_r = 0;
                $fac05_cntr_r = 0;
                $fac06_cntr_r = 0;
                $fac07_cntr_r = 0;
                $fac08_cntr_r = 0;
                

                foreach ($xml->children($ns['rdf'])->Description as $resource) {
                    if($resource->children($ns['aiiso'])->Faculty == $fac01){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac01_cntr_p = $fac01_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac01_cntr_r = $fac01_cntr_r + 1;
                        }
                    }
                    if($resource->children($ns['aiiso'])->Faculty == $fac02){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac02_cntr_p = $fac02_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac02_cntr_r = $fac02_cntr_r + 1;
                        }
                    }
                    if($resource->children($ns['aiiso'])->Faculty == $fac03){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac03_cntr_p = $fac03_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac03_cntr_r = $fac03_cntr_r + 1;
                        }
                    }
                    if($resource->children($ns['aiiso'])->Faculty == $fac04){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac04_cntr_p = $fac04_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac04_cntr_r = $fac04_cntr_r + 1;
                        }
                    }
                    if($resource->children($ns['aiiso'])->Faculty == $fac05){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac05_cntr_p = $fac05_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac05_cntr_r = $fac05_cntr_r + 1;
                        }
                    }
                    if($resource->children($ns['aiiso'])->Faculty == $fac06){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac06_cntr_p = $fac06_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac06_cntr_r = $fac06_cntr_r + 1;
                        }
                    }
                    if($resource->children($ns['aiiso'])->Faculty == $fac07){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac07_cntr_p = $fac07_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac07_cntr_r = $fac07_cntr_r + 1;
                        }
                    }
                    if($resource->children($ns['aiiso'])->Faculty == $fac08){
                        if($resource->children($ns['schema'])->jobTitle == 'Professor'){
                            $fac08_cntr_p = $fac08_cntr_p  + 1;
                        }else if($resource->children($ns['schema'])->jobTitle == 'Researcher'){
                            $fac08_cntr_r = $fac08_cntr_r + 1;
                        }
                    }

                }
                $p_data = array("label"=>$fac01,"y"=>$fac01_cntr_p);
                $r_data = array("label"=>$fac01,"y"=>$fac01_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);
                
                $p_data = array("label"=>$fac02,"y"=>$fac02_cntr_p);
                $r_data = array("label"=>$fac02,"y"=>$fac02_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);

                $p_data = array("label"=>$fac03,"y"=>$fac03_cntr_p);
                $r_data = array("label"=>$fac03,"y"=>$fac03_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);

                $p_data = array("label"=>$fac04,"y"=>$fac04_cntr_p);
                $r_data = array("label"=>$fac04,"y"=>$fac04_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);

                $p_data = array("label"=>$fac05,"y"=>$fac05_cntr_p);
                $r_data = array("label"=>$fac05,"y"=>$fac05_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);

                $p_data = array("label"=>$fac06,"y"=>$fac06_cntr_p);
                $r_data = array("label"=>$fac06,"y"=>$fac06_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);

                $p_data = array("label"=>$fac07,"y"=>$fac07_cntr_p);
                $r_data = array("label"=>$fac07,"y"=>$fac07_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);

                $p_data = array("label"=>$fac08,"y"=>$fac08_cntr_p);
                $r_data = array("label"=>$fac08,"y"=>$fac08_cntr_r);
                array_push($pr_data,$p_data);
                array_push($re_data,$r_data);
               
                $data = array("researcher"=>$re_data,"professor"=>$pr_data);
                return $data;
                break;

            case "show_num":
        
                $pro_num = 0;
                $res_num = 0;
                $exp_num = 0;
                foreach ($xml->children($ns['rdf'])->Description as $resource) {
                    
                    if (isset($resource->children($ns['rdf'])->type)&&
                        $resource->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/DefinedTerm" )
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
                            
                            $res_id = trim($researcher->attributes($ns['rdf'])->about);
                            $res_group = trim($researcher->children($ns['aiiso'])->ResearchGroup);
                            $res_institute = trim(($researcher->children($ns['aiiso'])->Institute));
                            $res_faculty = trim(($researcher->children($ns['aiiso'])->Faculty));
                            $res_title = trim(($researcher->children($ns['schema'])->jobTitle));
                            
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
                                    
                                    if(trim($nodeID) == trim($nodeID2)) {
        
                                        $exp_id = trim(($bnode2->children($ns['schema'])->identifier->attributes($ns['rdf'])->{'resource'}));
                                                                        
                                        foreach ($xml->children($ns['rdf'])->Description as $expertise) {
        
                                            if(trim(($expertise->attributes($ns['rdf'])->about)) == $exp_id) {
                                                
                                                $exp_name = trim(($expertise->children($ns['schema'])->name));
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
        
                            $exp_id = trim($expertise->attributes($ns['rdf'])->{'about'});
                            
                            $nodes = '[' . json_encode(Array('id'=>$name, 'weight'=>'15', 'group'=> 1));
                            $nodes = $nodes . ',' . json_encode(Array('id'=> $exp_id, 'weight'=>'5', 'group'=> 3));
                            
                            $links = '[' . json_encode(Array('source'=>$name, 'target'=>$exp_id, 'value'=> 3));
                            
                            foreach ($xml->children($ns['rdf'])->Description as $bnode) {
        
                                if(isset($bnode->children($ns['schema'])->identifier) && trim(($bnode->children($ns['schema'])->identifier->attributes($ns['rdf'])->{'resource'})) == $exp_id)
                                {
                                    
                                    $nodeID = trim(($bnode->attributes($ns['rdf'])->nodeID));
                                    
                                    foreach($xml->children($ns['rdf'])->Description as $researcher) {
        
                                        $flag = false;
                                        foreach( $researcher->children($ns['schema'])->knowsAbout as $bnode2) {
                                            if(trim(($bnode2->attributes($ns['rdf'])->nodeID)) == $nodeID) {
                                                $flag = true;
                                                break;
                                            }
                                        }
                                        if($flag == true) {
                                            
                                            $res_name = trim(($researcher->children($ns['schema'])->name));
                                            
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
                    $live_search_html = "";
                    foreach ($xml->children($ns['rdf'])->Description as $researcher) {
                        
                        if(isset($researcher->children($ns['rdf'])->type)&&$researcher->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/Person") {
                            
                            if( strpos(strtolower($researcher->children($ns['schema'])->name), strtolower($name)) !== false) {
                                $count += 1;
                                if( $count <= 10)
                                {
                                    $live_search_html = $live_search_html . $researcher->children($ns['schema'])->name . ',';
                                }
                            
                            }
                        }
                    }
                    return $live_search_html;
                }
                else
                {
                    $count = 0;
                    $search_expertise = "";
                    foreach ($xml->children($ns['rdf'])->Description as $expertise) {  
                        if(isset($expertise->children($ns['rdf'])->type)&&
                            $expertise->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/DefinedTerm")
                        {
                            if( strpos(strtolower($expertise->children($ns['schema'])->name), strtolower($name)) !== false) {
                                
                                $count += 1;
                                if( $count <= 10)
                                {
                                    $search_expertise = $search_expertise . $expertise->children($ns['schema'])->name . ',';
                                }
                            }
                        }
                    }
                    return $search_expertise;
                }
                break;
        }
    }

    public function publications(){
        $result = [];
        $pubs = [];
        

        $name = strtolower($_GET['name']);
        $json = json_decode(file_get_contents(public_path("publications_dict.json")), true); 
        
        foreach($json as $data){
            $len = count($data["entities"]);
            if($len > 0){
                foreach($data["entities"] as $entity){
                    
                    $aa_len = count($entity["AA"]);
                    if($aa_len > 0){
                        foreach($entity["AA"] as $n){
                            $something = [];
                            $authors = [];
                            if(strtolower($n["AuN"]) == $name){
                                $something["title"] = $entity["Ti"];
                                $something["year"] = $entity["Y"];
                                if(array_key_exists("DOI",$entity)){
                                    $something["DOI"] = $entity["DOI"];
                                }

                                foreach($entity["AA"] as $xx){
                                    array_push($authors,$xx["AuN"]);
                                }
                                $something["authors"] = $authors;
                                
                                array_push($pubs,$something);
                            }

                            
                        }
                    }
                    
                }
            }
        }
        return $pubs;
    }

    public function topexpertise(){
        if(file_exists(public_path("2nd_level_expertise_list_old.json"))){
            $resttt = json_decode(file_get_contents(public_path("top_expertise.json")), true);
            return $resttt;
        }else{
            $myfile = fopen("2nd_level_expertise_list_old.json", "w");
            $file_data = file_get_contents(public_path("2nd_level_expertise_list.json"));
            fwrite($myfile, $file_data);
            fclose($myfile);

            $str = file_get_contents(public_path("database.xml"));
            $xml = simplexml_load_string ($str);
            $ns = $xml->getNamespaces(true);
    
            $expertises = json_decode(file_get_contents(public_path("2nd_level_expertise_list.json")), true);
            $result = [];
            $pair = [];
            
            foreach($expertises as $e){
                $count = 0;
                foreach ($xml->children($ns['rdf'])->Description as $researcher) {  
                    if(isset($researcher->children($ns['rdf'])->type)&&
                    $researcher->children($ns['rdf'])->type->attributes($ns['rdf'])->{'resource'} == "http://schema.org/DefinedTerm"
                    && trim($researcher->children($ns['schema'])->name) == $e)
                    {  
                        $exp_id = trim($researcher->attributes($ns['rdf'])->{'about'});
                        
                        foreach ($xml->children($ns['rdf'])->Description as $bnode) {
                             
                            if(isset($bnode->children($ns['schema'])->identifier) && trim(($bnode->children($ns['schema'])->identifier->attributes($ns['rdf'])->{'resource'})) == $exp_id)
                            {
                                
                                $nodeID = trim(($bnode->attributes($ns['rdf'])->nodeID));
                                
                                foreach($xml->children($ns['rdf'])->Description as $researcher) {
    
                                    foreach( $researcher->children($ns['schema'])->knowsAbout as $bnode2) {
                                        if(trim(($bnode2->attributes($ns['rdf'])->nodeID)) == $nodeID) {
                                            $count = $count + 1;
                                        }
                                    }
                                }
                            }
                        }
                        
                        
                    }
                    
                    
                }
                $pair["title"] = $e;
                $pair["count"] =  $count;
                array_push($result,$pair);
               
            }
            file_put_contents("top_expertise.json",json_encode($result));
            $resttt = json_decode(file_get_contents(public_path("top_expertise.json")), true);
            return $resttt;
        }
        
    }

    public function getfavorites(Request $request){
        $name = $request->get('name');
        $id = (string)Auth::id();
        $count = Favorites::where('userid', (string)$id)->where('professor', $name)->count();
        return $count;
    }

    public function listfavorites(){
        
        $id = (string)Auth::id();
        $data = Favorites::where('userid', (string)$id)->get();
        return $data;
    }

    public function insertfav(Request $request){
        $fav = new Favorites(); 
        $fav->userid = (string)Auth::id();
        $fav->professor = $request->get('name');
        $fav->save();
        return "true";
    }


    public function delfavorites(Request $request){
        $fav = new Favorites(); 
        $id = (string)Auth::id();
        $name = $request->get('name');
        $res = Favorites::where('userid', (string)$id)->where('professor', $name)->delete();
        return $res;
    }

    /**
     * Privacy Policy Page
     *
     * @return \Illuminate\Http\Response
     */
    public function privacy()
    {
        $body_class = '';

        return view('frontend.privacy', compact('body_class'));
    }

    /**
     * Terms & Conditions Page
     *
     * @return \Illuminate\Http\Response
     */
    public function terms()
    {
        $body_class = '';

        return view('frontend.terms', compact('body_class'));
    }

    public function contact(Request $request) {

        // Form validation
        $this->validate($request, [
            'name' => 'required',
            'email' => 'required|email',
            'subject'=>'required',
            'message' => 'required'
         ]);
        //  Send mail to admin
        \Mail::send('mail', array(
            'name' => $request->get('name'),
            'email' => $request->get('email'),
            'subject' => $request->get('subject'),
            'user_query' => $request->get('message'),
        ), function($message) use ($request){
            $message->from($request->email);
            $message->to('wirtrials2020@gmail.com', 'Admin')->subject($request->get('subject'));
        });

        return back()->with('success', 'We have received your message and would like to thank you for writing to us.');
    }
}
