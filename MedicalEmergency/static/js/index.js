$("#emergency-btn").click(function(){
    let url = window.location.origin + "/api/meeting/";
    $.ajax({
        async: true,
        type: "GET",
        url: url,
        processData: false,
        contentType: false,
        success: function (response) {
            window.open(response['link'], '_self');
        },
        error: function(response){
            console.log(response);
            alert(response.responseJSON['Message']);
        },
    });
  });