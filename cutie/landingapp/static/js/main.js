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

//changes active nav link on scroll
$(document).ready(function() {
    $(window).scroll(function(){
        var scrollTop       = $(window).scrollTop() + 10, // top of browser + 10px
            whatisOffset    = $('#aboutUs').offset().top,
            whatisDist      = (whatisOffset - scrollTop), // stores current distance between top of browser and "about" section
            faqOffset       = $('#faq').offset().top,
            faqDist         = (faqOffset - scrollTop), // stores current distance between top of browser and "faq" section
            sponsorsOffset  = $('#sponsors').offset().top,
            sponsorsDist    = (sponsorsOffset - scrollTop); // stores current distance between top of browser and "sponsors" section
            

        if (whatisDist > 0) { //checks if you're in home section
            $('ul li div').removeClass('active');   
            $('#homelink').addClass('active');
        } else if (whatisDist <= 0 && faqDist > 0) { //checks if you're in about section
            $('ul li div').removeClass('active'); 
            $('#aboutlink').addClass('active');
        } else if (faqDist <= 0 && sponsorsDist > 0) { //checks if you're in faq section
            $('ul li div').removeClass('active'); 
            $('#faqlink').addClass('active');
        } else if (sponsorsDist <= 0 && !((window.innerHeight + window.scrollY) >= document.body.offsetHeight)) { //checks if you're in sponsors section, but haven't hit the bottom of page
            $('ul li div').removeClass('active'); 
            $('#sponsorslink').addClass('active');
        } else if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) { // you're at the bottom of the page
            $('ul li div').removeClass('active'); 
            $('#contactlink').addClass('active');
        }     
    });
});    


