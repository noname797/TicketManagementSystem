
function test(){
	var tabsNewAnim = $('#navbarSupportedContent');
	var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
	var activeItemNewAnim = tabsNewAnim.find('.active');
	var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
	var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
	var itemPosNewAnimTop = activeItemNewAnim.position();
	var itemPosNewAnimLeft = activeItemNewAnim.position();
	$(".hori-selector").css({
		"top":itemPosNewAnimTop.top + "px", 
		"left":itemPosNewAnimLeft.left + "px",
		"height": activeWidthNewAnimHeight + "px",
		"width": activeWidthNewAnimWidth + "px"
	});

}
$(document).ready(function(){
	setTimeout(function(){ test(); });
});
$(window).on('resize', function(){
	setTimeout(function(){ test(); }, 500);
});
$(".navbar-toggler").click(function(){
	$(".navbar-collapse").slideToggle(300);
	setTimeout(function(){ test(); });
});



function myFunc(x){
	document.getElementById("selected-date").innerText = x.cells.item(0).innerText
	document.getElementById("ticket-status").innerText = x.cells.item(4).innerText
	document.getElementById("ticket-description").innerText = x.cells.item(3).innerText 

	if (document.getElementById("ticket-status").innerText == "raised"){
		document.getElementById("ticket-status").style.color = "grey";
	}

	else if (document.getElementById("ticket-status").innerText == "resolved"){
		document.getElementById("ticket-status").style.color = "green";
	}

	else if (document.getElementById("ticket-status").innerText == "rejected"){
		document.getElementById("ticket-status").style.color = "red";
	}

}