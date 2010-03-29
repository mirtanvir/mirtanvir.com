import gdata.photos.service
import gdata.media
import gdata.geo

from ragendja import template
from common import constants

def album_thumb_images(request):
  album_id = request.POST['album_id']
  gd_client = gdata.photos.service.PhotosService()
  photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (constants.username, album_id))
  thumb_list = []
  for photo in photos.entry:
    thumb_list.append({'photo_id': photo.gphoto_id.text, 'thumb_url': photo.media.thumbnail[1].url})
  return template.JSONResponse(thumb_list)