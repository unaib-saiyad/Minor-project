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

function productView(product_id){
    let url = window.location.origin + "/api/productView/"+product_id;
    $.ajax({
        async: true,
        type: "GET",
        url: url,
        processData: false,
        contentType: false,
        success: function (response) {
            window.open(window.location.origin+"/product_view/"+product_id, '_self');
        },
        error: function(response){
            console.log(response);
            alert(response.responseJSON['Message']);
        },
    });
}