// ---------Responsive-navbar-active-animation-----------
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
	$("#navbarSupportedContent").on("click","li",function(e){
		$('#navbarSupportedContent ul li').removeClass("active");
		$(this).addClass('active');
		var activeWidthNewAnimHeight = $(this).innerHeight();
		var activeWidthNewAnimWidth = $(this).innerWidth();
		var itemPosNewAnimTop = $(this).position();
		var itemPosNewAnimLeft = $(this).position();
		$(".hori-selector").css({
			"top":itemPosNewAnimTop.top + "px", 
			"left":itemPosNewAnimLeft.left + "px",
			"height": activeWidthNewAnimHeight + "px",
			"width": activeWidthNewAnimWidth + "px"
		});
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



// --------------add active class-on another-page move----------
jQuery(document).ready(function($){
	// Get current path and find target link
	var path = window.location.pathname.split("/").pop();

	// Account for home page with empty path
	if ( path == '' ) {
		path = 'index.html';
	}

	var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');
	// Add active class to target link
	target.parent().addClass('active');
});




// Add active class on another page linked
// ==========================================
// $(window).on('load',function () {
//     var current = location.pathname;
//     console.log(current);
//     $('#navbarSupportedContent ul li a').each(function(){
//         var $this = $(this);
//         // if the current path is like this link, make it active
//         if($this.attr('href').indexOf(current) !== -1){
//             $this.parent().addClass('active');
//             $this.parents('.menu-submenu').addClass('show-dropdown');
//             $this.parents('.menu-submenu').parent().addClass('active');
//         }else{
//             $this.parent().removeClass('active');
//         }
//     })
// });



function myFunc(x){
	document.getElementById("selected-ticket").innerText = x.cells.item(0).innerText
	document.getElementById("ticket-status").innerText = x.cells.item(5).innerText
	document.getElementById("ticket-description").innerText = x.cells.item(2).innerText 
	document.getElementById("ticket-category").innerText = x.cells.item(3).innerText 
	document.getElementById("ticket-subcategory").innerText = x.cells.item(4).innerText 


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