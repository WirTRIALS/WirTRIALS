<?php

use PHPMailer\PHPMailer\PHPMailer;

require_once '../PHPMailer/Exception.php';
require_once '../PHPMailer/PHPMailer.php';
require_once '../PHPMailer/SMTP.php';

$mail = new PHPMailer(true);

$alert = '';

// if(isset($_POST['submit'])){

  $name = $_POST['name'];
  $email = $_POST['email'];
  $message = $_POST['message'];

  try{
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->Username = 'wirtrials2020@gmail.com'; // Gmail address which you want to use as SMTP server
    $mail->Password = 'WirTrials2020'; // Gmail address Password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = '587';

    $mail->setFrom('wirtrials2020@gmail.com'); // Gmail address which you used as SMTP server
    $mail->addAddress('wirtrials2020@gmail.com'); // Email address where you want to receive emails (you can use any of your gmail address including the gmail address which you used as SMTP server)

    $mail->isHTML(true);
    $mail->Subject = 'Message Received from clients';
    $mail->Body = "<h3>Customer Name : $name <br>Customer Email: $email <br>Customer Message : $message</h3>";

    $mail->send();
    $alert = '<div class="alert-success">
                 <span>Message Sent! Thank you for contacting us.</span>
                </div>';
  } catch (Exception $e){
    $alert = '<div class="alert-error">
                <span>'.$e->getMessage().'</span>
              </div>';
  }
  echo"Message Sent";
// }
?>
                           