import simplejson as sj
from django import http

def send_as_json(dict):
  json = sj.dumps(dict)
  return http.HttpResponse(json, type="application/json")