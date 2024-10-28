$(document).ready(function() {
    let cropper;
    let transactionID = null;
    let paymentStatus = "pending"

    // Modal behavior
    $('.open-postcard-modal').click(function(e) {
        e.preventDefault(); 

        // Clear previous modal content (optional: depends on what needs to be reset)
        $('#postcardModalSlug').text('');     // Clear slug
        $('#postcardModalLabel').text('');    // Clear title
        $('#modalImage').attr('src', '');     // Clear image
        $('#recipientMessage').text('');      // Clear description
        
        var title = $(this).data('title');
        var slug = $(this).data('slug');
        var image = $(this).data('image');
        var description = $(this).data('description');

        $('#sendPostcardBtn').data('slug', slug);
        $('#postcardModalLabel').text(title);
        $('#modalImage').attr('src', image);
        $('#recipientMessage').text(description);

        // Initialize PayPal buttons (independent of postcardData)
        initPayPalButtons(slug);
    });

    function initPayPalButtons(slug) {
        // clear previous rendered buttons
        $('#paypal-button-container').empty();
        // PayPal button setup
        paypal.Buttons({
            createOrder: function (data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value: '5'
                        }
                    }]
                }).then(function(orderId) {
                    console.log("Order ID created:", orderId);
                    // Call the function to create payment object
                    let payer = $("#from_name").val();
                    handlePaymentObject(orderId, 'pending', slug, payer);
                    return orderId;
                });
            },
            onApprove: function (data, actions) {
                return actions.order.capture().then(function(details) {
                    console.log("Payment completed by " + details.payer.name.given_name);
                    console.log("onApprove orderID:", data.orderID);
                    transactionID = data.orderID;
                    paymentStatus = 'approved';   // Should print a valid order ID
                    let payerName = details.payer.name.given_name;
                    handlePaymentObject(data.orderID, paymentStatus, slug, payerName);
                });
            },
            onError: function(err) {
                console.error(err); // Handle errors here
                alert('There was an error processing the payment. Please try again.');
            }
        }).render('#paypal-button-container');
    }


    // Function to create a payment object
    function handlePaymentObject(orderId, status = 'pending', slug, payer = null) {
        if (!payer) {
            payer = $('#from_name').val() || null;
        }
        
        $.ajax({
            method: "POST",
            url: "/handle_payment/",
            data: JSON.stringify({ 
                orderId: orderId,
                status: status,
                slug: slug,
                payer: payer
             }),
            contentType: "application/json",
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response) {
                console.log('Payment object processed:', response);
            },
            error: function(error) {
                console.log("Error processing payment object:", error);
            }
        });
    }


    // Collect postcard data and include transaction ID
    function collectPostcardData(transactionID, paymentStatus) {
        return {
            image_url: $('#image_url').val(),
            from_name: $('#from_name').val(),
            from_street1: $('#from_street1').val(),
            from_street2: $('#from_street2').val(),
            from_city: $('#from_city').val(),
            from_state: $('#from_state').val(),
            from_postcode: $('#from_postcode').val(),
            from_country: $('#from_country').val(),
            message: $('#message').val(),
            to_name: $('#to_name').val(),
            to_street1: $('#to_street1').val(),
            to_street2: $('#to_street2').val(),
            to_city: $('#to_city').val(),
            to_state: $('#to_state').val(),
            to_postcode: $('#to_postcode').val(),
            to_country: $('#to_country').val(),
            payment_status: paymentStatus,
            transaction_id: transactionID // Include the transaction ID
        };
    }


    // Validate postcard data
    function validatePostcardData() {
        let postcardData = collectPostcardData(); // Get the postcard data
        if (!postcardData.to_name || !postcardData.to_street1 || !postcardData.to_city || !postcardData.to_state || !postcardData.to_postcode || !postcardData.to_country) {
            alert('Please fill out all the required recipient fields.');
            return false;
        }
        return true; // All fields are filled
    };


    // Function to send postcard data to the backend
    function sendPostcardToBackend(postcardData, slug) {
        $.ajax({
            url: `/${slug}/send_postcard/`, 
            type: 'POST',
            data: JSON.stringify(postcardData),
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(response) {
                alert('Postcard sent successfully!');
                $('#postcardModal').modal('hide');
            },
            error: function(xhr, status, error) {
                alert('There was an error in AJAX sending the postcard');
            }
        });
    };
    

    // Handle "Send Postcard" button click
    $('#sendPostcardBtn').click(function(e) {
        e.preventDefault(); // Prevent default form submission or action
        let postcardData = collectPostcardData(transactionID, paymentStatus); // Make sure this function collects the current input data
        let slug = $(this).data('slug');
        // Collect data before transaction 
        if (!validatePostcardData()) {
            return; // Exit if validation fails
        }

        // Check if payment was completed
        if (!paymentStatus !== 'approved') {
            // Create a payment object in your database with status 'not approved'
            sendPostcardToBackend(postcardData, slug, 'not approved');
            alert('Please complete the payment before sending the postcard.');
            return false; // Prevent further actions if payment not made
        }

        // Log the data being sent to ClickSend -DEBUG-
        console.log("Sending the following data to ClickSend:", postcardData, slug);

        // Payment is completed, now send the postcard
        sendPostcardToBackend(postcardData, slug); // Call function to send postcard to backend
        // Proceed with sending the postcard
        alert('Postcard sent!'); // Replace with actual postcard sending logic
    });


    // Handle tab switching
    $("#front-tab").click(function() {
        $("#print-data").hide();
        $("#print-image").show();
        $("#back-tab").removeClass("active");
        $(this).addClass("active");
    });


    $("#back-tab").click(function() {
        $("#print-image").hide();
        $("#print-data").show();
        $("#front-tab").removeClass("active");
        $(this).addClass("active");
    });

    // Open the cropping tool
    $('#open-crop-tool').on('click', function() {
        $('#edit-buttons').toggle()
        const image = document.getElementById('modalImage');
        // Check if cropper already exists
        if (cropper) {
            cropper.destroy(); // Destroy existing cropper instance
        }
        cropper = new Cropper(image, {
            aspectRatio: 1.5, // Adjust the aspect ratio to match postcard dimensions
            viewMode: 1,      // Restrict the crop box to stay within the image
        });
    });

    // Destroy Cropper when modal is hidden
    $('#postcardModal').on('hidden.bs.modal', function () {
        cropper.destroy();
        cropper = null;
    });


    // Rotate left
    $('#rotate-left').on('click', function() {
        cropper.rotate(-90); // Rotate 90 degrees counter-clockwise
    });


    // Rotate right
    $('#rotate-right').on('click', function() {
        cropper.rotate(90); // Rotate 90 degrees clockwise
    });


    // Handle crop and set the cropped image
    $('#crop-button').on('click', function() {
        if (cropper) {
            const croppedCanvas = cropper.getCroppedCanvas();
            const croppedImage = croppedCanvas.toDataURL(); // Get cropped image as base64

            // Replace the original image with the cropped image
            $('#modalImage').attr('src', croppedImage);
            // Set the cropped image in a hidden input or form field
            $('#image_url').val(croppedImage);
            $('#edit-buttons').toggle()

            // Destroy the cropper instance if you want to reset it for the next crop
            cropper.destroy();
            cropper = null;
        }
    });

    

    

    

    

    

});