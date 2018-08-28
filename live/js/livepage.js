//file for js code
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

// countdown

var countDownDate = new Date("Nov 10, 2018  09:00:00").getTime();
var x = setInterval(function() {
  var now = new Date().getTime();
  var distance = countDownDate - now;
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("cntdwn").innerHTML = days + " Days, " + hours + " Hours, " + minutes + " Minutes, and " + seconds + " Seconds ";

  if(distance < 0)
  {
    clearInterval(x);
    document.getElementById("cntdwn").innerHTML = "Event now in session!";
  }
}, 1000);
