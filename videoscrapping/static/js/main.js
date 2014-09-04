var init = function() {

    $('div.item').on('click',function(){
        location.href=$(this).attr('href');
    });


    $('ul#menu-channels li').on('click',function(){
        $('ul#menu-channels li').removeClass('active');
        $(this).addClass('active');
        ref=$(this).attr('ref');

        if(ref!=0){

            $('div.item[ref="'+ref+'"]').fadeIn();
            $('div.item[ref!="'+ref+'"]').fadeOut();
        }else{
            $('div.item').fadeIn();
        }

    });

    $(function() {
        $("img.lazy").lazyload();
    });

};

$(document).on('ready',init);