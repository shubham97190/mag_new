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
function reg1(){
    $.ajax({
        url:'/registration',
        type:'POST',
        datatype:'html',
        success:function(response){
           
        },
        error:function(error){
            console.log(error);
        }
    });
}