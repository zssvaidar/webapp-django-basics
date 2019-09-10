$(document).ready(function(){

		if ( $(window).scrollBottom() >= 100 ) {
		       $("#shelf").remove(".col-md-4");
					 $("#shelf").append(".col-md-3");


		    } else {
					$("#shelf").remove(".col-md-3");
				 $("#shelf").append(".col-md-4");

		    }

});
