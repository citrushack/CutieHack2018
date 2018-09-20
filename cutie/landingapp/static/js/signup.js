 $(document).ready(function (){
            $("#nextSection1").click(function (){
                $('html, body').animate({
                    scrollTop: $("#wrapper2").offset().top
                }, 500);
            });
            $("#nextSection2").click(function (){
                $('html, body').animate({
                    scrollTop: $("#wrapper3").offset().top
                }, 500);
            });
            $("#prevSection2").click(function (){
                $('html, body').animate({
                    scrollTop: 0
                }, 500);
            });
            $("#prevSection3").click(function (){
                $('html, body').animate({
                    scrollTop: $("#wrapper2").offset().top
                }, 500);
            });

        });