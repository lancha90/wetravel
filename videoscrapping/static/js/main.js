

var search_video = function(){
    search_text=$('.menu #input-search').val();
    if(search_text.trim().length > 0 ){
        $('div.item').fadeOut();

        $( "div.item:contains('"+search_text+"')").fadeIn(function(){
            $(window).trigger('scroll');
        });
    }
};

var init = function() {

    jQuery.expr[':'].contains = function(a, i, m) {
        return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };

    $('div.item').on('click',function(){
        location.href=$(this).attr('href');
    });

    $('.menu #btn-search').on('click',search_video);
    $('.menu #input-search').keypress(function(e) {
        if(e.which == 13) {
            search_video();
        }
    });

    $('ul#menu-channels li').on('click',function(){
        $('ul#menu-channels li').removeClass('active');
        $(this).addClass('active');
        ref=$(this).attr('ref');
        //$('div.item[ref="'+ref+'"] img.lazy').slice(0,12).show().lazyload();

        if(ref!=0){
            $('div.item[ref="'+ref+'"]').fadeIn();
            $('div.item[ref!="'+ref+'"]').fadeOut(function(){
                $(window).trigger('scroll');
            });
        }else{
            $('div.item').fadeIn();
        }    


    });

    $(function() {
        $("img.lazy").lazyload();
    });

};

$(document).on('ready',init);