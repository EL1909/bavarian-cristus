$(document).ready(function() {
    // Function for running text behavior
    function startRunningText() {
        $('.running-text').each(function() {
            var container = $(this);
            var $paragraphs = container.find('p');
            let currentIndex = 0;
            let intervalId;

            // Function to show the current paragraph based on the index
            function showCurrentParagraph() {
                // Hide all paragraphs first
                $paragraphs.hide();

                // Dim and show the previous paragraph if applicable
                if (currentIndex > 0) {
                    $paragraphs.eq(currentIndex - 1).addClass('inactive').fadeIn(800); // Show previous inactive paragraph
                }

                // Show the current active paragraph
                $paragraphs.eq(currentIndex).removeClass('inactive').addClass('active').fadeIn(800);

                // Dim and show the next paragraph if applicable
                if (currentIndex < $paragraphs.length - 1) {
                    $paragraphs.eq(currentIndex + 1).addClass('inactive').fadeIn(800); // Show next inactive paragraph
                }
            }

            // Initially show the first paragraph as active, 3 seconds after the fadeOut
            setTimeout(function() {
                $paragraphs.eq(0).addClass('active').fadeIn(800);

                // Start the automatic paragraph change
                intervalId = setInterval(function() {
                    // Move to the next paragraph only if not on the last one
                    if (currentIndex < $paragraphs.length - 1) {
                        currentIndex++;
                        showCurrentParagraph(); // Show the new current paragraph
                    } else {
                        clearInterval(intervalId); // Stop the interval at the last paragraph
                    }
                }, 3000); // Change interval time
            }, 500);  // 1-second delay after showing the #about section

            $paragraphs.on('click', function() {
                clearInterval(intervalId);
                currentIndex = (currentIndex + 1) % $paragraphs.length;
                showCurrentParagraph();

                if (currentIndex === $paragraphs.length - 1) {
                    clearInterval(intervalId);
                } else {
                    intervalId = setInterval(function() {
                        currentIndex++;
                        if (currentIndex >= $paragraphs.length) {
                            currentIndex = $paragraphs.length - 1;
                            clearInterval(intervalId);
                        }
                        showCurrentParagraph();
                    }, 5000);
                }
            });
        });
    };

    // Ensure #about is hidden by default
    $("#about").hide(); 
    $(".gold-banner").fadeIn();

    // Show #gb1 after 1 second
    setTimeout(function() {
        $("#gb1").fadeIn();
    }, 500);

    // Show #gb2 after 1.5 seconds
    setTimeout(function() {
        $("#gb2").fadeIn();
    }, 1200);

    // Fade out gold banner
    setTimeout(function() {
        $(".gold-banner").fadeOut();
    }, 3000);
    
    // Handle tab switching
    $("#gallery-tab").click(function() {
        // Hide #about and show gallery
        $("#about").hide(); // Ensure #about is hidden when switching tabs
        $("#gallery").show();
        // Remove active class from #about-tab and add to #gallery-tab
        $("#about-tab").removeClass("active");
        $(this).addClass("active");
    });

    $("#about-tab").click(function() {
        $("#gallery").hide();
        $("#about").fadeIn();
        $("#gallery-tab").removeClass("active");
        $(this).addClass("active");

        // Call running text function
        startRunningText();
    });

    // Post-slides in home
    const $slides = $('.post-list-slide');
    let slideIndex = 0;
    const totalSlides = $slides.length;

    $slides.eq(slideIndex).addClass('active');

    function showNextPost() {
        $slides.eq(slideIndex).removeClass('active');
        slideIndex = (slideIndex + 1) % totalSlides;
        $slides.eq(slideIndex).addClass('active');
    }

    setInterval(showNextPost, 8000);

    $('#postcard-gallery-btn').on('click', function () {
        showNextPost();
    });

});

// Footer Behavior
let footer = $('footer');
let footerHeight = footer.outerHeight();
let lastScrollTop = 0;

$(window).scroll(function() {
    let st = $(this).scrollTop();

    if (st > lastScrollTop) {
        footer.css('bottom', '0'); // Show footer
    } else {
        footer.css('bottom', -footerHeight + 'px'); // Hide footer
    }
    lastScrollTop = st;
});
