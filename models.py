import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from django.utils import simplejson
from google.appengine.ext import db


class App(db.Model):
    appname = db.StringProperty()
    isValid = db.BooleanProperty()

class MyKey(db.Model):
    deviceIds = db.StringListProperty()
    coupon = db.StringProperty()
    isValid = db.BooleanProperty()
    appref = db.ReferenceProperty(App,collection_name="mykeys")
