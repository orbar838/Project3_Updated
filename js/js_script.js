$(document).ready(function(){
	//Bind Ajax button click
	$( "#send_ajax_request" ).bind( "click", function() {
	  alert( "User clicked on 'send_ajax_request.'" );
	});
	
	//Clear fields when click back
	$("[name='email']").val("");
	$("[name='password']").val("");
	$("[name='html5_email']").val("");

   $("#form1_img").click(function () {
	   var bgcolor = $("#form_one_img_div").css("background-color");
	   if(bgcolor != "rgb(255, 255, 0)"){
		   $("#form_one_img_div").css("background-color", "Yellow");
	   } else{
		   $("#form_one_img_div").css("background-color", "");
	   }
	});
	
	$("#form2_img").click(function () {
		if($("#pushed_h2").length){
			$("#pushed_h2").remove();
		} else {
			$("#second_form_div").append("<h2 id='pushed_h2'>This header is pushed by JS script!!!!</h2>");
			$("#pushed_h2").click(function () {
				alert("You clicked on me!!!");
			});
		}
	});
	
	$("#ch_div_color_btn").click(function () {
	   var divbgcolor = $("#buttons_div").css("background-color");
	   // alert(divbgcolor);
	   if(divbgcolor == "rgb(255, 255, 255)"){
		   $("#buttons_div").css("background-color", "Cyan");
	   } else if(divbgcolor == "rgb(0, 255, 255)"){
		   $("#buttons_div").css("background-color", "Crimson");
	   } else if(divbgcolor == "rgb(220, 20, 60)"){
		   $("#buttons_div").css("background-color", "LightBlue");
	   } else if(divbgcolor == "rgb(173, 216, 230)"){
		   $("#buttons_div").css("background-color", "");
	   }
	});

});


