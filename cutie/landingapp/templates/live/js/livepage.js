//file for js code

// countdown
var countDownDate = new Date("Nov 11, 2018  21:00:00").getTime();
var x = setInterval(function() {
  var now = new Date().getTime();
  var distance = countDownDate - now;
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("cntdwn").innerHTML = hours + " Hours, " + minutes + " Minutes, and " + seconds + " Seconds ";
}, 100);

//changes active nav link on scroll
$(document).ready(function() {
    $(window).scroll(function(){
        var scrollTop       = $(window).scrollTop() + 10, // top of browser + 10px
            scheduleOffset    = $('#schedule').offset().top,
            scheduleDist      = (scheduleOffset - scrollTop), // stores current distance between top of browser and "schedule" section
            mapOffset       = $('#map').offset().top,
            mapDist         = (mapOffset - scrollTop), // stores current distance between top of browser and "map" section
            resourcesOffset  = $('#resources').offset().top,
            resourcesDist    = (resourcesOffset - scrollTop); // stores current distance between top of browser and "resources" section
            speakersOffset  = $('#judges').offset().top,
            speakersDist    = (speakersOffset - scrollTop); // stores current distance between top of browser and "speakers" section
            sponsorsOffset  = $('#sponsors').offset().top,
            sponsorsDist    = (sponsorsOffset - scrollTop); // stores current distance between top of browser and "speakers" section

            // console.log("===========");
            // console.log("SCHEDULE DIST IS: " + scheduleDist);
            // console.log("MAP DIST IS: " + mapDist);
            // console.log("RESOURCES DIST IS: " + resourcesDist);
            // console.log("SPEAKERS DIST IS: " + speakersDist);
            // console.log("SPONSORS DIST IS: " + sponsorsDist);

            if (scheduleDist > 19) { //checks if you're in home section
                      $('nav ul li a').removeClass();
                      $('#homelink').addClass('active');
                  } else if (scheduleDist <= 19 && mapDist > 62) { //checks if you're in schedule section
                      $('nav ul li a').removeClass();
                      $('#schedulelink').addClass('active');
                  } else if (mapDist <= 62 && resourcesDist > 88) { //checks if you're in map  section
                      $('nav ul li a').removeClass();
                      $('#maplink').addClass('active');
                  } else if (resourcesDist <= 88 && speakersDist > 73) { //checks if you're in resources section
                      $('nav ul li a').removeClass();
                      $('#resourceslink').addClass('active');
                  } else if (speakersDist <= 73 && sponsorsDist > 57) { //checks if you're in speakers section
                      $('nav ul li a').removeClass();
                      $('#judgeslink').addClass('active');
                  } else if (sponsorsDist <= 57 && !((window.innerHeight + window.scrollY) >= document.body.offsetHeight)) { //checks if you're in sponsors section, but haven't hit the bottom of page
                      $('nav ul li a').removeClass();
                      $('#sponsorslink').addClass('active');
                  }
              });
          });
