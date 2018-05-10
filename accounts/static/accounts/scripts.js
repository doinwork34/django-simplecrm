$(document).ready(function(){
	$("#auto_submit_form").submit();
});




/** for menu toggle, hold click */
$(document).ready(function(){
    $('body').bind('mousedown touchstart',function(e){
        e.preventDefault;
        var times = setTimeout(function(){
        $('#myNav').css('width','100%');
        }, 1000);
        var end =  $('body').bind('mouseup touchend',function(e){
            clearTimeout(times);
        });  
        
   
   

       $('#close').click(function(){
        $('#myNav').css('width','0%');
        clearTimeout(times);
       });
    });
 });


/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function leftActionBar() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}


function searchbar() {
    var $button = $("button[name='q']");

$('#search').keyup(function() {
    var re = new RegExp($(this).val(), "i"); // case-insensitive
    $button.show().filter(function() {
        return !re.test($(this).text());
    }).hide();   
});
};

$(document).ready(function(){
  $(function () {
   var bindDatePicker = function() {
        $(".date").datetimepicker({
        format:'YYYY-MM-DD HH:mm:ss',
            icons: {
                time: "fa fa-clock-o",
                date: "fa fa-calendar",
                up: "fa fa-arrow-up",
                down: "fa fa-arrow-down"
            }
        }).find('input:first').on("blur",function () {
            // check if the date is correct. We can accept dd-mm-yyyy and yyyy-mm-dd.
            // update the format if it's yyyy-mm-dd
            var date = parseDate($(this).val());

            if (! isValidDate(date)) {
                //create date based on momentjs (we have that)
                date = moment().format('YYYY-MM-DD');
            }

            $(this).val(date);
        });
    }
   
   var isValidDate = function(value, format) {
        format = format || false;
        // lets parse the date to the best of our knowledge
        if (format) {
            value = parseDate(value);
        }

        var timestamp = Date.parse(value);

        return isNaN(timestamp) == false;
   }
   
   var parseDate = function(value) {
        var m = value.match(/^(\d{1,2})(\/|-)?(\d{1,2})(\/|-)?(\d{4})$/);
        if (m)
            value = m[5] + '-' + ("00" + m[3]).slice(-2) + '-' + ("00" + m[1]).slice(-2);

        return value;
   }
   
   bindDatePicker();
 });

});



function htmlbodyHeightUpdate() {
    var height3 = $(window).height();
    var height1 = $('.nav').height() + 50;
    height2 = $('.container-main').height();
    if (height2 > height3) {
        $('html').height(Math.max(height1, height3, height2) + 10);
        $('body').height(Math.max(height1, height3, height2) + 10);
    } else
    {
        $('html').height(Math.max(height1, height3, height2));
        $('body').height(Math.max(height1, height3, height2));
    }

}
$(document).ready(function () {
    htmlbodyHeightUpdate();
    $(window).resize(function () {
        htmlbodyHeightUpdate();
    });
    $(window).scroll(function () {
        height2 = $('.container-main').height();
        htmlbodyHeightUpdate();
    });
});


$(document).ready(function(){
    $('#opentix').click(function(){
        $('#tablebody button').each(function(){
            if (!$(this).is('#danger')) {
                $(this).hide();            
            } else {
                $(this).show();
            }

        })
    });
    $('#recenttix').click(function(){
        $('#tablebody button').each(function(){
            if (!$(this).is('#success')) {
                $(this).hide();
            } else{
                $(this).show();
            }
        })
    });
    $('#show_pending').click(function(){
        $('#tablebody button').each(function(){
            if (!$(this).is('#pendingtix')) {
                $(this).hide();
            } else {
                $(this).show();
            }
        })
    });
    $('#alltix').click(function(){
        $('#tablebody button').each(function(){
           $(this).show();
        })
    });
});


