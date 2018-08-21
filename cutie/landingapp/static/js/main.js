//jQuery dropdown for FAQ section
$(document).ready(function(){
    //when a element from the .faqQuestion class is clicked,
    $('.faqQuestion').click(function(){
        //the corresponding answer is revealed using slideToggle("slow")
        $("#a" + this.id.charAt(1)).slideToggle("slow");
    });
});

//jQuery navbar smooth scrolling
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

//changes active nav link on click
$(document).ready(function() {
    $('nav ul li a').click(function() {
        $('nav ul li a').removeClass();
        $(this).addClass('active');
    });
});

//changes active nav link on scroll
$(document).ready(function() {
    $(window).scroll(function(){
        var scrollTop       = $(window).scrollTop() + 10,
            whatisOffset    = $('#whatis').offset().top,
            whatisDist      = (whatisOffset - scrollTop),
            faqOffset       = $('#faq').offset().top,
            faqDist         = (faqOffset - scrollTop),
            sponsorsOffset  = $('#sponsors').offset().top,
            sponsorsDist    = (sponsorsOffset - scrollTop),
            organizersOffset   = $('#organizers').offset().top;
            organizersDist     = (organizersOffset - scrollTop);

        if (whatisDist > 0) {
            $('nav ul li a').removeClass();   
            $('#homelink').addClass('active');
        } else if (whatisDist <= 0 && faqDist > 0) {
            $('nav ul li a').removeClass();
            $('#aboutlink').addClass('active');
        } else if (faqDist <= 0 && sponsorsDist > 0) {
            console.log("WE ARE IN FAQ BABYYYY");
            $('nav ul li a').removeClass();
            $('#faqlink').addClass('active');
        } else if (sponsorsDist <= 0 && organizersDist > 0) {
            $('nav ul li a').removeClass();
            $('#sponsorslink').addClass('active');
        } else {
            $('nav ul li a').removeClass();
            $('#contactlink').addClass('active');
        }     
    });
});    

