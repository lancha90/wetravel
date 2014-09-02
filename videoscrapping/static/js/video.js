var init = function() {
      $('button#like').on('click',function(){
                  like('/api/'+uuid+'/like',$(this));
            });
      $('button#unlike').on('click',function(){
                  like('/api/'+uuid+'/unlike',$(this));
            });

      
      $('div.over-info div.over-slide').delay( 1000 ).css('top','-90px');
      
};

var show_popup = function (message){
      //alert(message);
};

var like = function (link,button) {

      $('button#like, button#unlike').removeClass('select');
      

	$.ajax({
		url : link,
            type : 'GET',
            dataType : "json",
            timeout : 10000,
            crossDomain : true,
            success: function (_data) {
                  if(_data.code == 200){
                        $('#rating').text(_data.likes);
                        button.addClass('select');
                  }else if(_data.code == 201){
                        $('#rating').text(_data.likes);
                  }else if(_data.code == 400){
                        show_popup(_data.message);
                  }else if(_data.code == 401){
                        location.href = '/users/login?next='+location.pathname;
                  }
            }
		});

};


$(document).on('ready',init);