

var content = document.getElementById("content");
var button = document.getElementById("show-more");


button.onclick() = function(){

	if (content.className == "open") {
		content.className = "";
		button.innerHTML = "Show More";
	} else  {
		content.className = "open";
		button.innerHTML = "Show Less";
	}


};


function printDiv(divName) {
     var printContents = document.getElementById(divName).innerHTML;
     var originalContents = document.body.innerHTML;

     document.body.innerHTML = printContents;

     window.print();

     document.body.innerHTML = originalContents;
}
