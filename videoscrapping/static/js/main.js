var init = function() {

    $('div.item').on('click',function(){
        location.href=$(this).attr('href');
    });


    $('ul#menu-channels li').on('click',function(){
        $('ul#menu-channels li').removeClass('active');
        $(this).addClass('active');

        $('div.item[ref="'+$(this).attr('ref')+'"]').fadeIn();
        $('div.item[ref!="'+$(this).attr('ref')+'"]').fadeOut();

    });

    $(function() {
        $("img.lazy").lazyload();
    });

};

$(document).on('ready',init);