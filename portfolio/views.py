import gdata.blogger.client
import gdata.client
import gdata.data
import atom.data
import time, hashlib, urllib, hmac, base64, random, webbrowser

from common import constants
from django.shortcuts import render_to_response

def list_portfolio(request):
  