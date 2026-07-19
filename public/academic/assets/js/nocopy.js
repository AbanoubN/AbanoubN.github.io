$(document).ready(function () {
    //to disable the entire page 
    $('body').bind('cut copy paste', function (e) {
        e.preventDefault();
    });
    
    //to disable a section
    $('#id').bind('cut copy paste', function (e) {
        e.preventDefault();
    });

    $("body").on("contextmenu",function(e){
        return false;
    });
    
    //to disable a section
    $("#id").on("contextmenu",function(e){
        return false;
    });
});
