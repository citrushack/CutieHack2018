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
    //when a tag with a valid anchortag is clicked
    $('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event) {
        //if the location is the same as the one that is clicked
        if (location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") && location.hostname == this.hostname) {
            //store the href as 'target'
            var target = $(this.hash);

            //ion't really know what the slice does but this basically checks if the target isn't empty
            target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
            
            if (target.length) {
                //prevent default jump scroll
                event.preventDefault();

                //jQuery smooth scroll magic 
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
    //once you click a nav link
    $('nav ul li a').click(function() {
        //remove 'active' class from all nav links
        $('nav ul li a').removeClass();
        //add 'active' class to the nav link that was clicked (this)
        $(this).addClass('active');
    });
});

//changes active nav link on scroll
$(document).ready(function() {
    $(window).scroll(function(){
        var scrollTop       = $(window).scrollTop() + 10, // top of browser + 10px
            whatisOffset    = $('#whatis').offset().top,
            whatisDist      = (whatisOffset - scrollTop), // stores current distance between top of browser and "about" section
            faqOffset       = $('#faq').offset().top,
            faqDist         = (faqOffset - scrollTop), // stores current distance between top of browser and "faq" section
            sponsorsOffset  = $('#sponsors').offset().top,
            sponsorsDist    = (sponsorsOffset - scrollTop), // stores current distance between top of browser and "sponsors" section
            organizersOffset   = $('#organizers').offset().top;
            organizersDist     = (organizersOffset - scrollTop); // stores current distance between top of browser and "contact" section

        if (whatisDist > 0) { //checks if you're in home section
            $('nav ul li a').removeClass();   
            $('#homelink').addClass('active');
        } else if (whatisDist <= 0 && faqDist > 0) { //checks if you're in about section
            $('nav ul li a').removeClass();
            $('#aboutlink').addClass('active');
        } else if (faqDist <= 0 && sponsorsDist > 0) { //checks if you're in faq section
            console.log("WE ARE IN FAQ BABYYYY");
            $('nav ul li a').removeClass();
            $('#faqlink').addClass('active');
        } else if (sponsorsDist <= 0 && organizersDist > 0) { //checks if you're in sponsors section
            $('nav ul li a').removeClass();
            $('#sponsorslink').addClass('active');
        } else { // checks if you're in anywhere but the ones checked before, ie contact section
            $('nav ul li a').removeClass();
            $('#contactlink').addClass('active');
        }     
    });
});    

