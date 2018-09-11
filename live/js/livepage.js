//file for js code
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

//changes active nav link on scroll
$(document).ready(function() { //(document).ready: let file know that it is jQuery
    $(window).scroll(function(){
        var scrollTop       = $(window).scrollTop() + 10, // top of browser + 10px
            scheduleOffset    = $('#schedule').offset().top,
            scheduleDist      = (scheduleOffset - scrollTop), // stores current distance between top of browser and "about" section
            mapOffset       = $('#map').offset().top,
            mapDist         = (mapOffset - scrollTop), // stores current distance between top of browser and "faq" section
            speakersOffset  = $('#speakers').offset().top,
            speakersDist    = (speakersOffset - scrollTop); // stores current distance between top of browser and "sponsors" section
            resourcesOffset  = $('#resources').offset().top,
            resourcesDist    = (resourcesOffset - scrollTop); // stores current distance between top of browser and "sponsors" section
            sponsorsOffset  = $('#sponsors').offset().top,
            sponsorsDist    = (sponsorsOffset - scrollTop); // stores current distance between top of browser and "sponsors" section

        if (scheduleDist > 0) { //checks if you're in home section
            $('nav ul li a').removeClass();
            $('#homelink').addClass('active');
        } else if (scheduleDist <= 0 && mapDist > 0) { //checks if you're in schedule section
            $('nav ul li a').removeClass();
            $('#schedulelink').addClass('active');
        } else if (mapDist <= 0 && resourcesDist > 0) { //checks if you're in map section
            $('nav ul li a').removeClass();
            $('#maplink').addClass('active');
        } else if (resourcesDist <= 0 && speakersDist > 0) { //checks if you're in resources section
            $('nav ul li a').removeClass();
            $('#resourceslink').addClass('active');
        } else if (speakersDist <= 0 && sponsorsDist > 0) { //checks if you're in speakers section
              $('nav ul li a').removeClass();
              $('#speakerslink').addClass('active');
        } else if (sponsorsDist <= 0 && !((window.innerHeight + window.scrollY) >= document.body.offsetHeight)) { //checks if you're in sponsors section, but haven't hit the bottom of page
            $('nav ul li a').removeClass();
            $('#sponsorslink').addClass('active');
        }
    });
});
