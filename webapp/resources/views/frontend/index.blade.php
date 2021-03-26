@extends('frontend.layouts.app')

@section('title') {{app_name()}} @endsection

@section('content')

<style>

.box {
    position: relative;
    width: 100%;
    padding-right: 15px;
    padding-left: 15px
}

.our-services {
    margin-top: 75px;
    padding-bottom: 30px;
    padding: 0 60px;
    min-height: 198px;
    text-align: center;
    border-radius: 10px;
    background-color: #fff;
    transition: all .4s ease-in-out;
    box-shadow: 0 0 25px 0 rgba(20, 27, 202, .17)
}

.our-services .icon {
    margin-bottom: -21px;
    transform: translateY(-50%);
    text-align: center
}

.our-services:hover h4,
.our-services:hover a {
    color: #fff
}

.speedup:hover {
    box-shadow: 0 0 25px 0 rgba(20, 27, 201, .05);
    cursor: pointer;
    background-image: linear-gradient(-45deg, #fb0054 0%, #f55b2a 100%)
}

.settings:hover {
    box-shadow: 0 0 25px 0 rgba(20, 27, 201, .05);
    cursor: pointer;
    background-image: linear-gradient(-45deg, #34b5bf 0%, #210c59 100%)
}

.privacy:hover {
    box-shadow: 0 0 25px 0 rgba(20, 27, 201, .05);
    cursor: pointer;
    background-image: linear-gradient(-45deg, #3615e7 0%, #44a2f6 100%)
}

.backups:hover {
    box-shadow: 0 0 25px 0 rgba(20, 27, 201, .05);
    cursor: pointer;
    background-image: linear-gradient(-45deg, #fc6a0e 0%, #fdb642 100%)
}

.ssl:hover {
    box-shadow: 0 0 25px 0 rgba(20, 27, 201, .05);
    cursor: pointer;
    background-image: linear-gradient(-45deg, #8d40fb 0%, #5a57fb 100%)
}

.database:hover {
    box-shadow: 0 0 25px 0 rgba(20, 27, 201, .05);
    cursor: pointer;
    background-image: linear-gradient(-45deg, #27b88d 0%, #22dd73 100%)
}
</style>

<section class="section-header pb-6 pb-lg-10 bg-primary text-white" 
style="background:linear-gradient(0deg, rgba(6,73,178),rgba(80,155,220, 0.7)), url(img/skills.png);" >
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-md-10 text-center">
                <h1 class="display-1 mb-4">{{app_name()}}</h1>
                <p class="lead text-muted">
                    <b>Fast-Forwarding your Ideas into Reality</b>
                </p>

                @include('frontend.includes.messages')
            </div>
        </div>
    </div>
    <div class="pattern bottom"></div>
</section>

<section class="section section-ld" id="about" style="padding-bottom:2px !important;">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2 class="mb-4 mb-lg-5 text-center">ABOUT US</h2>
                <p>
                We are a company based in the industrious city of Chemnitz founded by the students of Chemnitz University
        of Technology in 2020. We strive to develop unmatched IT solutions for the most challenging problems.
        Idea too unrealistic? Here at WirTRIALS, we will make your dream turn into reality by providing the most
        cutting-edge solutions to your problems.
                </p>
                <br />  
            </div>
           
            <div class="col-6 col-sm-4 mb-5">
                <a href="#" class="page-preview scale-up-hover-2 text-center">
                    <img height="150"  class="rounded scale" src="img/mission.png"
                     >
              
                </a><br />  
                <h4 class="text-center">Mission</h4>
                <p>To achieve a connection between ideas and the real world by developing tools which are custom built, simple and user-friendly.</p>
            </div>
            <div class="col-6 col-sm-4 mb-5">
                <a href="#" class="page-preview scale-up-hover-2 text-center">
                    <img height="150"  class="rounded scale" src="img/vision.png"
                        >
                    
                </a><br />  
                <h4 class="text-center">Vision</h4>
                <p class="text-center">To become a paradise for technophile and a channel from fantasy to reality.</p>
            </div>
            <div class="col-6 col-sm-4 mb-5">
                <a href="#" class="page-preview scale-up-hover-2 text-center">
                    <img  height="150" class="rounded scale" src="img/purpose.png"
                        >
                </a><br />  

                <h4 class="text-center">Purpose</h4>
            <p class="text-center">To support our clients to excel in new technologies and thereby going hand in hand to forge the digital future.</p>
            </div>
        </div>
    </div>
</section>


<section class="section section-ld" style="background-color:#fff;">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2 class="mb-4 mb-lg-5 text-center">OUR VALUES</h2>
                <p class="text-center">
                    <img src="img/7.png">
                </p>
            </div>
        </div>
    </div>
</section>

<section class="section section-ld" style="background-color:#fff;">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2 class="mb-4 mb-lg-5 text-center">PRODUCT</h2>
                <p class="text-center" style="margin-top:-25px;">
                    Our product Researchee is here. Take a look!
                </p>
            </div>
            <div class="container h-100">
                <div class="row h-100 justify-content-center align-items-center">
                <div class="box" style="width:50% !important;">
                    <div class="our-services privacy">
                        <div class="icon"> <img src="https://i.imgur.com/AgyneKA.png"> </div>
                        <h4>Researchee</h4>
                        <a class="btn btn-secondary" href="/product">Learn more</a>
                    </div>
                </div>
            </div> 
                </div>
            </div>

            <div class="row ">
            
           
        
        </div>
        <div class="col-md-4">
        <div class="box">
                
            </div>
        </div>
            </div>
           
        </div>
    </div>
</section>

<section class="section section-ld" id="team" style="padding-top:2px !important;background-color:#fff;">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h2 class="text-center">OUR TEAM</h2>
                <p class="text-center">We are a team of people of varied cultures & nationality thereby bringing together ideas all over the globe.</p>
                <BR/>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-4 col-md-6 d-flex align-items-stretch">
            <div class="member" data-aos="zoom-in" data-aos-delay="100">
                <div class="member-img">
                <img src="img/team/hongru.jpg"  alt="" class="img-fluid">
                <div class="social">

                    <a href=""><i class="icofont-linkedin"></i></a>
                </div>
                </div>
                <div class="member-info">
                <h4 class="text-center">Hongru Ren</h4>
                </div>
            </div>
            </div>

            <div class="col-lg-4 col-md-6 d-flex align-items-stretch">
            <div class="member" data-aos="zoom-in" data-aos-delay="200">
                <div class="member-img">
                <img src="img/team/mayuri.jpg" class="img-fluid" alt="">
                <div class="social">

                    <a href="/"><i class="icofont-linkedin"></i></a>
                </div>
                </div>
                <div class="member-info">
                <h4 class="text-center">Mayuri Pandey</h4>
                </div>
            </div>

            </div>
            <div class="col-lg-4 col-md-6 d-flex align-items-stretch">
            <div class="member" data-aos="zoom-in">
                <div class="member-img">
                <img src="img/team/swagat.jpg"  alt="" class="img-fluid">
                <div class="social">

                    <a href=""><i class="icofont-linkedin"></i></a>
                </div>
                </div>
                <div class="member-info">
                <h4 class="text-center">Swagat Gyawali</h4>
                </div>
            </div>
            </div>
            </div>
    </div>
</section>

<section class="section section-ld" id="contact" style="padding-top:50px !important;background-color:#f7fafc;">
    <div class="container" style="box-shadow:5px 5px 5px 5px #888888;padding:30px;">
        <div class="row">
            <div class="col-12">
                <h2 class="text-center">CONTACT US</h2>
                <p class="text-center">Do you have any questions or feedback? Contact us and we will get in touch with you.</p>
                <BR/>
            </div>
        </div>

        <div class="row">

            <div class="col-md-9 mx-auto">
                  <!-- Success message -->
        @if(Session::has('success'))
            <div class="alert alert-success" id="contactSendAlert">
               <script>
                    $(function() { 
                        $('html, body').animate({
                            scrollTop: $('#contact').offset().top}, 1000);
                    })
                     
                </script> 
                {{Session::get('success')}}
            </div>
        @endif

                <form role="form" method="post" action="/contact" class="php-email-form">
                @csrf
                <div class="row">
                <div class="form-group col-md-6">
                    <label>Name</label>
                    <input required="required" type="text" class="form-control {{ $errors->has('name') ? 'error' : '' }}" name="name" id="name">

                    <!-- Error -->
                    @if ($errors->has('name'))
                    <div class="error">
                        {{ $errors->first('name') }}
                    </div>
                    @endif
                </div>
                    
                <div class="form-group col-md-6">
                    <label>Email</label>
                    <input required="required" type="email" class="form-control {{ $errors->has('email') ? 'error' : '' }}" name="email" id="email">

                    @if ($errors->has('email'))
                    <div class="error">
                        {{ $errors->first('email') }}
                    </div>
                    @endif
                </div>
                </div>


                <div class="form-group">
                    <label>Subject</label>
                    <input required="required" type="text" class="form-control {{ $errors->has('subject') ? 'error' : '' }}" name="subject"
                        id="subject">

                    @if ($errors->has('subject'))
                    <div class="error">
                        {{ $errors->first('subject') }}
                    </div>
                    @endif
                </div>

                <div class="form-group">
                    <label>Message</label>
                    <textarea required="required" class="form-control {{ $errors->has('message') ? 'error' : '' }}" name="message" id="message"
                        rows="6"></textarea>

                    @if ($errors->has('message'))
                    <div class="error">
                        {{ $errors->first('message') }}
                    </div>
                    @endif
                </div>
                            <div class="text-center"><button class="btn btn-secondary" type="submit" name="submit">Send Message</button></div>
                </form>
            </div>

        </div>
    </div>
</section>



@endsection
