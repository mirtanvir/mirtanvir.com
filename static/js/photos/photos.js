$(document).ready(function(){
  var album_id = $("#album_id").html();
  $.post("/photos/rpc/get_thumb_list", {"album_id": album_id },
   function (data){
     var table_data = [], j = 0;
     var tr = $('<tr>');
     var td = $('<td>');
     var table = $('<table>');
     number_of_photos = data.length;
     $.each(data, function(i, value) {
        if (j==0) {
          tr = $('<tr>');  
        }
        var photo_id = value.photo_id;
        var url = $('<a>');
       url.attr('href', '/photos/album/' + album_id + '/photo/' + photo_id + '/?index=' + (i + 1));
        var img = $('<img />');
        img.attr('src', value.thumb_url);
        img.attr('title', photo_id);
        url.html(img);
        $('<td>').html(url).appendTo(tr);
        j++;
        if (j===8) {
          j=0;
          tr.appendTo(table);
        }
       
     });
     tr.appendTo(table);
     $("#one_album").append(table);
   }, 'json');
  
});
