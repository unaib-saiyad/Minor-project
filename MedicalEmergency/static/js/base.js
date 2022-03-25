// User creation
var csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
$("#logout-btn").click(function (event){
    let url = window.location.origin + "/api/logout/";

    $.ajax({
        async: true,
        type: "GET",
        url: url,
        processData: false,
        contentType: false,
        success: function (response) {
            window.open(window.location.origin+"/login/", '_self');
        },
        error: function(response){
            console.log(response);
            alert(response.responseJSON['Message']);
        },
    });
});

$(document).ready(function(){
    let path = window.location.pathname;
    if(path == "/"){
        $('#base-nav').addClass('active');
    }
    else if(path == "/medicine_order/"){
        $('#medicine-nav').addClass('active');
    }
    else if(path == "/blood_donation/"){
        $('#blood-nav').addClass('active');
    }
    else if(path == "/doctor_appointment/"){
        $('#doctor-nav').addClass('active');
    }
});

