import gdata.photos.service
import gdata.media
import gdata.geo
import logging

from common import constants
from django import http
from django.shortcuts import render_to_response
from google.appengine.api import urlfetch
from ragendja import template #render_to_response as rtr
from xml.dom import minidom 

username = "mir.tanvir.hossain"

def list_albums(request):
  username = "mir.tanvir.hossain";
  gd_client = gdata.photos.service.PhotosService()
  albums = gd_client.GetUserFeed(user=username)
  album_list = []
  for album in albums.entry:
    dom = minidom.parseString(album.ToString())
    title = dom.getElementsByTagName("ns1:title")[0].firstChild.data
    thumb_url = dom.getElementsByTagName("ns1:thumbnail")[0].attributes['url'].value
    try:
      description = dom.getElementsByTagName("ns1:description")[0].firstChild.data
    except AttributeError, e:
      description = ""  
    album_id = dom.getElementsByTagName("ns1:id")[0].firstChild.data
    temp_album =  Album(title, thumb_url, album_id, description)
    album_list.append(temp_album)
    temp_album = None
  return render_to_response( 'photos/album_list.html', {'albums': album_list,})

def list_album_pictures(request, id):
  #photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (username, id))
  #thumb_list = []
  #for photo in photos.entry:
  #  thumb_list.append(photo.media.thumbnail[1].url)
  return render_to_response('photos/album.html', {'album_id': id,})

def get_photoID_by_index(username, album_id, index):
  photo = urlfetch.fetch('http://picasaweb.google.com/data/feed/api/user/%s/albumid/%s/?kind=photo&max-results=1&start-index=%s' % (username, album_id, index))
  if photo.status_code == 200:
    photo_dom = minidom.parseString(photo.content)
    logging.debug(photo_dom)
    try:
      return photo_dom.getElementsByTagName('gphoto:id')[1].firstChild.data
    except IndexError, e:
      return None
  else:
    return None

def show_single_photo(request, album_id, photo_id):
  try:
    start_index = int(request.GET['index'])
  except KeyError, e:
    start_index = None
  
  gd_client = gdata.photos.service.PhotosService()
  albums = gd_client.GetUserFeed(user=username) #/photoid/%s
  photo = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s/photoid/%s/' % (username, album_id, photo_id))
  dom = minidom.parseString(photo.ToString())
  url = dom.getElementsByTagName("ns1:content")[0].attributes['url'].value
  
  next_index = None
  prev_index = None
  prev_photo_id = None
  next_photo_id = None
  if start_index:
    next_photo_id = get_photoID_by_index(constants.username, album_id, start_index + 1 )
    if next_photo_id:
      next_index = start_index + 1
    else:
      next_index = None
    if start_index > 0:
      prev_index = start_index - 1
      prev_photo_id = get_photoID_by_index(constants.username, album_id, prev_index)
    else:
      prev_photo_id = None
      prev_index = None
  logging.debug('next_id:%s prev_id: %s' %(next_photo_id, prev_photo_id))

  return render_to_response('photos/single_photo.html', {'photo_url': url, 'album_id': album_id, 'next_id':next_photo_id, 'next_index': next_index, 'prev_id': prev_photo_id, 'prev_index': prev_index ,})


class Album():
  def __init__(self, title, thumbnail_url, album_id, description ):
    self.title = title
    self.thumbnail_url = thumbnail_url
    self.id = album_id
    self.description = description