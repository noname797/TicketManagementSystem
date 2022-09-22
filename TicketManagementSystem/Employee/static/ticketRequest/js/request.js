
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



var data = JSON.parse("{{categories|escapejs}}")

                function func(){
                  
                  for (cat in data){
                    let newOption = new Option(String(cat),String(cat));
                      document.getElementById("categories").add(newOption);
                  }

                  document.getElementById("sub_categories").innerHTML = "";
                  currentvar = document.getElementById("categories").value;
                  document.getElementById("sub_categories").style.display = "block";
                  for (let i = 0; i < data[currentvar].length;i++){

                    let newOption = new Option(String(data[currentvar][i]),String(data[currentvar][i]));
                    document.getElementById("sub_categories").add(newOption);
                  } 
                  
                }
              

                

                  

                function select(){
                  document.getElementById("sub_categories").innerHTML = "";
                  currentvar = document.getElementById("categories").value;
                  document.getElementById("sub_categories").style.display = "block";
                  for (let i = 0; i < data[currentvar].length;i++){

                    let newOption = new Option(String(data[currentvar][i]),String(data[currentvar][i]));
                    document.getElementById("sub_categories").add(newOption);
                  } 

                }

                


                

