//jQuery dropdown for FAQ section
$(document).ready(function(){
    $('.faqQuestion').click(function(){
        $("#a" + this.id.charAt(1)).slideToggle("slow");
    });
});

//jQuery smooth scrolling
$(document).ready(function(){
    $('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event) {
        if (location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
            
            if (target.length) {
                event.preventDefault();
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top
                    }, 
                    1000,
                    function() {
                        var $target = $(target);
                        $target.focus();
                        if ($target.is(":focus")) {
                            return false;
                        } else {
                            $target.attr("tabindex", "-1");
                            $target.focus(); 
                        }
                    }
                );
            }
        }
    });
});

//highlight active nav link
$(document).ready(function() {
    $('nav ul li a').click(function() {
        $('nav ul li a').removeClass();
        $(this).addClass('active');
    });
});

//responsive dropdown menu for mobile
function mobileDrop() {
    var x = document.getElementById("navbar");
    if (x.className === "nav") {
        x.className += " responsive";
    } else {
        x.className = "nav";
    }
}