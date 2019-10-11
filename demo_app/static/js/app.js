
$(document).ready(function(){


	console.log("Hello");

   
	// $('#mybutton').on('click',function(){
 // 		console.log("testing");
 // 		// $('#content').load("/partials/demopar.html");
 // 	});



	$('#auth1').on('click',function(event){
 		console.log("testing",event);
 		$('#subapp').load("/auth");
 	});

});