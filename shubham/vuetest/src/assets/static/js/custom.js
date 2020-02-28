
/*----Tabs----*/

$(document).ready(function () {
$('#horizontalTab').easyResponsiveTabs({
type: 'default', //Types: default, vertical, accordion           
width: 'auto', //auto or any width like 600px
fit: true,   // 100% fit in a container
closed: 'accordion', // Start closed if in accordion view
activate: function(event) { // Callback function if tab is switched
var $tab = $(this);
var $info = $('#tabInfo');
var $name = $('span', $info);
$name.text($tab.text());
$info.show();
}
});
$('#verticalTab').easyResponsiveTabs({
type: 'vertical',
width: 'auto',
fit: true
});
});

/*--------Stiky Header-------*/

var affixElement = '#navbar-main';

$(affixElement).affix({
  offset: {
    // Distance of between element and top page
    top: function () {
      return (this.top = $(affixElement).offset().top)
    },
  }
});

/*---------Expend Search--------*/

	$(document).ready(function(){
	function buttonUp(){
		 var valux = $('.ExpInput').val(); 
			valux = $.trim(valux).length;
			if(valux !== 0){
				$('.Expbtn').css('z-index','99');
			} else{
				$('.ExpInput').val(''); 
				$('.Expbtn').css('z-index','-999');
			}
	}
	});
	
	$(document).ready(function(){
		var submitIcon = $('.ExpIcon');
		var submitInput = $('.ExpInput');
		var searchBox = $('.Exp-serach');
		var isOpen = false;
		
		$(document).mouseup(function(){
			if(isOpen == true){
			submitInput.val('');
			$('.Expbtn').css('z-index','-999');
			submitIcon.click();
			}
		});
		
		submitIcon.mouseup(function(){
			return false;
		});
		
		searchBox.mouseup(function(){
			return false;
		});
				
		submitIcon.click(function(){
			if(isOpen == false){
				searchBox.addClass('Exp-serach-open');
				isOpen = true;
			} else {
				searchBox.removeClass('Exp-serach-open');
				isOpen = false;
			}
	});
	
	});
			
/*--------Css3 Animation---------*/

jQuery(document).ready(function() {
	jQuery('.post1').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated slideInDown',
		offset: 100    
	   }); 
	jQuery('.post2').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated slideInLeft',
		offset: 100    
	   }); 
	jQuery('.post3').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated slideInRight',
		offset: 100    
	   }); 
	jQuery('.post4').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeIn',
		offset: 100    
	   }); 
	jQuery('.post5').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInUp',
		offset: 100    
	   }); 
	jQuery('.post6').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInDown',
		offset: 100    
	   }); 
	jQuery('.post7').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInLeft',
		offset: 100    
	   }); 
	jQuery('.post8').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInRight',
		offset: 100    
	   }); 
	jQuery('.post9').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInUpBig',
		offset: 100    
	   }); 
	jQuery('.post10').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInDownBig',
		offset: 100    
	   }); 
	jQuery('.post11').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInLeftBig',
		offset: 100    
	   }); 
	jQuery('.post12').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated fadeInRightBig',
		offset: 100    
	   }); 
	jQuery('.post13').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated rotateIn',
		offset: 100    
	   }); 
	jQuery('.post14').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated rotateInUpLeft',
		offset: 100    
	   }); 
	jQuery('.post15').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated rotateInDownLeft',
		offset: 100    
	   }); 
	jQuery('.post16').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated rotateInUpRight',
		offset: 100    
	   }); 
	jQuery('.post17').addClass("hidden").viewportChecker({
		classToAdd: 'visible animated rotateInDownRight',
		offset: 100    
	   }); 
});            
