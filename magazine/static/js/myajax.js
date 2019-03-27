function reg(){
    $.ajax({
        url:'/registration',
        type:'GET',
        datatype:'html',
        success:function(response){
            $('#reg_form .form').html(response);
        },
        error:function(error){
            console.log(error);
        }
    });
}
