// User creation
var csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
$("#submit-register").click(function (event){
    var data = new FormData();
    data.append('csrfmiddlewaretoken', csrfmiddlewaretoken);
    data.append('username', $('#username').val());
    data.append('email', $('#email').val());
    data.append('password', $('#password').val());
    data.append('full_name', $('#full-name').val());
    data.append('address', $('#address').val());
    data.append('mobile', $('#mobile').val());

    let url = window.location.origin + "/api/register/";

    $.ajax({
        async: true,
        type: "POST",
        url: url,
        data: data,
        processData: false,
        contentType: false,
        beforeSend: function() {
            $('#submit-register').addClass('d-none');
            $('#hidden-load-submit').removeClass('d-none');
         },
        success: function (response) {
            window.open(window.location.origin+"/login/", '_self');
        },
        error: function(response){
            alert(response.responseJSON['Message']);
        },
        complete: function(){
            window.setTimeout(() => {
                $('#hidden-load-submit').addClass('d-none');
                $('#submit-register').removeClass('d-none');
            }, 200);
        }
    });
});