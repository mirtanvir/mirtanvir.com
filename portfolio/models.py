from django.db.models import permalink, signals
from google.appengine.ext import db
from ragendja.dbutils import cleanup_relations

class Portfolio(db.Model):
  title = db.StringProperty(required=True)
  description = db.TextProperty(required=True)
  url = db.URLProperty()
  screen_shot = db.BlobProperty()
  
class Category(db.Model):
  title = db.StringProperty(required)
  