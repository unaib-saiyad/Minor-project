// User creation
var csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
$("#submit-login").click(function (event){
    var data = new FormData();
    data.append('csrfmiddlewaretoken', csrfmiddlewaretoken);
    data.append('email', $('#email').val());
    data.append('password', $('#password').val());

    let url = window.location.origin + "/api/login/";

    $.ajax({
        async: true,
        type: "POST",
        url: url,
        data: data,
        processData: false,
        contentType: false,
        beforeSend: function() {
            $('#submit-login').addClass('d-none');
            $('#hidden-load-submit').removeClass('d-none');
         },
        success: function (response) {
            window.open(window.location.origin+"/", '_self');
        },
        error: function(response){
            console.log(response);
            alert(response.responseJSON['Message']);
        },
        complete: function(){
            window.setTimeout(() => {
                $('#hidden-load-submit').addClass('d-none');
                $('#submit-login').removeClass('d-none');
            }, 200);
        }
    });
});