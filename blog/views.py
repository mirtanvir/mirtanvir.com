# -*- coding: utf-8 -*-
import gdata.blogger.client
import gdata.client
import gdata.data
import atom.data
import time, hashlib, urllib, hmac, base64, random, webbrowser

from common import constants
from django.shortcuts import render_to_response

def list_blog_entries(request):
  blogger_service = gdata.blogger.client.BloggerClient()
  timestamp = str(int(time.time()))
  nonce = gen_nonce()
  base_url = 'http://www.blogger.com/feeds/'+ constants.blogger_id +'/posts/default'
  base_url_encoded = urllib.quote_plus(base_url)
  sig_base_string = "GET&http%3A%2F%2Fwww.blogger.com%2Ffeeds%2F7553538379541822977%2Fposts%2Fdefault%2F&oauth_consumer_key%3Dwww.mirtanvir.com%26oauth_nonce%3D2ebd7a944174149b7d524a93355d7b47%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1262032018%26oauth_token%3D1%252FRfc30NMwRShkcdgui__3gQ%26oauth_version%3D1.0"
  oauth_parameters = 'oauth_version=1.0&oauth_nonce='+ nonce +'&oauth_timestamp='+ timestamp +'&oauth_consumer_key=www.mirtanvir.com&oauth_token=' + urllib.quote_plus( constants.access_token ) + '&oauth_signature_method=HMAC-SHA1'  
  oauth_parameters_encoded = urllib.quote_plus(oauth_parameters)
  final_string_to_sign = "GET&http%3A%2F%2Fwww.blogger.com%2Ffeeds%2F7553538379541822977%2Fposts%2Fdefault%2F&oauth_consumer_key%3Dwww.mirtanvir.com%26oauth_nonce%3D"+ nonce +"%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D"+ timestamp +"%26oauth_token%3D1%252FRfc30NMwRShkcdgui__3gQ%26oauth_version%3D1.0"
  key = constants.Consumer_Secret + '&' + constants.token_secret
  signature = base64.b64encode(hmac.new(key, final_string_to_sign, hashlib.sha1).digest())
  signature_urlencoded = urllib.quote_plus(signature)
  url = base_url + '/?' + oauth_parameters + '&oauth_signature=' + signature_urlencoded
  feed = blogger_service.GetFeed(url)
  return render_to_response('blog/blog_list.html', {'blogs': feed,})

def show_single_blog(request):
  pass

def gen_nonce():
    return hashlib.md5(str(int(time.time())) + str(random.random())).hexdigest() 