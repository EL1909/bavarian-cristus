$(document).ready(function() {
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

    // Fade out all elements after 2.5 seconds and then show the running text
    setTimeout(function() {
        $(".gold-banner").fadeOut(function() {
            $("#about").fadeIn();

            // Start the running text behavior after #about fades in
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
                        $paragraphs.eq(currentIndex - 1).addClass('inactive').fadeIn(500); // Show previous inactive paragraph
                    }

                    // Show the current active paragraph
                    $paragraphs.eq(currentIndex).removeClass('inactive').addClass('active').fadeIn(500);

                    // Dim and show the next paragraph if applicable
                    if (currentIndex < $paragraphs.length - 1) {
                        $paragraphs.eq(currentIndex + 1).addClass('inactive').fadeIn(500); // Show next inactive paragraph
                    }
                }

                // Initially show the first paragraph as active, 3 seconds after the fadeOut
                setTimeout(function() {
                    $paragraphs.eq(0).addClass('active').fadeIn(1000);

                    // Start the automatic paragraph change
                    intervalId = setInterval(function() {
                        // Move to the next paragraph only if not on the last one
                        if (currentIndex < $paragraphs.length - 1) {
                            currentIndex++;
                            showCurrentParagraph(); // Show the new current paragraph
                        } else {
                            clearInterval(intervalId); // Stop the interval at the last paragraph
                        }
                    }, 5000); // Change interval time
                }, 1000);  // 1-second delay after showing the #about section

                // Click to manually change paragraphs
                $paragraphs.on('click', function() {
                    clearInterval(intervalId); // Stop the automatic changes on click
                    currentIndex = (currentIndex + 1) % $paragraphs.length;  // Loop back to the first paragraph
                    showCurrentParagraph();  // Show the clicked paragraph

                    // Restart the interval after changing the paragraph
                    if (currentIndex === $paragraphs.length - 1) {
                        clearInterval(intervalId); // Stop the interval if on the last paragraph
                    } else {
                        intervalId = setInterval(function() {
                            currentIndex++;
                            if (currentIndex >= $paragraphs.length) {
                                currentIndex = $paragraphs.length - 1; // Stop at the last paragraph
                                clearInterval(intervalId); // Stop the interval
                            }
                            showCurrentParagraph(); // Show the new current paragraph
                        }, 5000); // Change interval time
                    }
                });
            });
        });
    }, 3000);
    

    // 2. Handle tab switching
    $("#gallery-tab").click(function() {
        $("#about").hide();
        $("#gallery").show();
        // Remove 'active' class from all tabs
        $(".about-tab").removeClass("active");
        // Add 'active' class to the clicked tab
        $(this).addClass("active");
    });

    $("#about-tab").click(function() {
        $("#about").show();
        $("#gallery").hide();
        // Remove 'active' class from all tabs
        $(".gallery-tab").removeClass("active");
        // Add 'active' class to the clicked tab
        $(this).addClass("active");
    });

    // Post-slides in home
    const $slides = $('.post-list-slide');
    let slideIndex = 0;
    const totalSlides = $slides.length;

    // Initially, show the first slide only
    $slides.eq(slideIndex).addClass('active');

    // Function to change post on button click
    function showNextPost() {
        // Hide the current active slide
        $slides.eq(slideIndex).removeClass('active');

        // Update slideIndex for the next post
        slideIndex = (slideIndex + 1) % totalSlides;  // Loop back to first post after last

        // Show the new active slide
        $slides.eq(slideIndex).addClass('active');
    }

    // Automatically change post every 5 seconds
    setInterval(showNextPost, 8000);

    // On button click, show the next post
    $('#postcard-gallery-btn').on('click', function () {
        showNextPost();
    });

    // Event listener for opening the modal
    $('#open-postcard-modal').click(function(e) {
        e.preventDefault(); // Prevent the default anchor click behavior

        // Get data from the clicked card
        var title = $(this).data('title');
        var slug = $(this).data('slug');
        var image = $(this).data('image');
        var description = $(this).data('description');

        // Set the modal content
        $('#postcardModalSlug').text(slug);
        $('#postcardModalLabel').text(title);
        $('#modalImage').attr('src', image);
        $('#recipientMessage').text(description);

    });

});

// Footer Behavior
let footer = $('footer');
let footerHeight = footer.outerHeight();
let lastScrollTop = 0;

// Show/hide footer as the user scrolls
$(window).scroll(function() {
    let st = $(this).scrollTop();

    if (st > lastScrollTop) {
        // Scrolling down
        footer.css('bottom', '0'); // Show footer
    } else {
        // Scrolling up
        footer.css('bottom', -footerHeight + 'px'); // Hide footer
    }
    lastScrollTop = st;

});