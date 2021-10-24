// ---------------------------------------------------------------------------------------------------------------
$(document).ready(function () {
    $('#vehicle_manufacturer_selector').on('change', function () {
        let vehicle_manufacturer_selector_id = $(this).find(":selected").attr("data-vmsid");
        if ($(this).find(":selected").val() != "vehicle_manufacturer_default") {
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:8000/vehicle_models_view/",
                data: {
                    'vehicle_manufacturer_selector_id': vehicle_manufacturer_selector_id,
                    'operation': 'vehicle_manufacturer_select',
                },
                dataType: "json",
                success: (response) => {
                    console.log(response);

                    $('.vehicle_model_option').remove()

                    for (let i = 0; i < response.length; i++) {
                        $('#vehicle_model_selector').append(`<option class="vehicle_model_option" data-vmodelsid="${response[i]['id']}" value="${response[i]['id']}">${response[i]['name']}</option>`)
                    }


                    $('#vehicle_model_selector').removeAttr('disabled');

                },
                error: function (xhr, status, error) {
                    // log in console the error if any error occurred
                    console.log('error');
                }
            });
        } else {
            $('#vehicle_model_selector').prop('disabled', true);
        }
    })

    $('#vehicle_model_selector').on('change', function () {
        let vehicle_model_selector_id = $(this).find(":selected").attr("data-vmodelsid");
        if ($(this).find(":selected").val() != "vehicle_model_default") {
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:8000/vehicle_images_view/",
                data: {
                    'vehicle_model_selector_id': vehicle_model_selector_id,
                    'operation': 'vehicle_model_select',
                },
                dataType: "json",
                success: (response) => {
                    console.log(response);

                    $('.vehicle_image_option').remove()

                    for (let i = 0; i < response.length; i++) {
                        $('#vehicle_image_selector').append(`<option class="vehicle_image_option" value="${response[i]['image']}">${response[i]['image_file_name']}</option>`)
                    }

                    if (response.length > 0) {
                        $('#vehicle_image_selector').removeAttr('disabled');
                    } else {
                        $('#vehicle_image_selector').prop('disabled', true);
                    }

                    if (response.length > 0) {
                        $('#images_count_alert').fadeIn()
                        $('#images_count').text(response.length)
                        $("#notfound_alert").fadeOut()
                    } else {
                        $('#images_count_alert').fadeOut()
                        $("#download_alert").fadeOut()
                        $("#notfound_alert").fadeIn()
                        $('#display_image').attr('src', "static/images/images-regular.svg")
                    }

                },
                error: function (xhr, status, error) {
                    // log in console the error if any error occurred
                    console.log('error');
                }
            });
        } else {
            $('#vehicle_image_selector').prop('disabled', true);
        }
    })

    $('#vehicle_image_selector').on('change', function () {
        if ($(this).find(":selected").val() != "vehicle_image_default") {
            $('#display_image').attr('src', $(this).find(":selected").val())
            $('#download_link').attr('href', $(this).find(":selected").val())
            $("#download_alert").fadeIn()
        } else {
            $('#display_image').attr('src', "static/images/images-regular.svg")
            $("#download_alert").fadeOut()

        }
    })

});
// ---------------------------------------------------------------------------------------------------------------


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
