from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import random
import string
from models import *

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')

MAX_SIZE = 8

class RandomKeyHandler(webapp.RequestHandler):
    def get(self,app):
        rapp = App.get_or_insert(key_name=app,appname=app,isValid=True)

        coupon = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(MAX_SIZE))

        mykey = MyKey(key_name="%s_%s" % (rapp.appname , coupon), coupon = coupon, isValid = True,appref=rapp)
        mykey.put()
        self.response.out.write("%s - %s" % (rapp.appname,coupon))

class CheckKeyHandler(webapp.RequestHandler):
    def get(self,app,coupon):
        self.response.headers['Content-Type'] = 'application/json'

        deviceId = self.request.get('deviceid','')
        isvalid = False
        rapp = App.get_by_key_name(app)
        if rapp and rapp.isValid:
            mykey = MyKey.get_by_key_name("%s_%s" % (rapp.appname , coupon))
            if mykey and mykey.isValid:
                isvalid = True
                mykey.deviceIds.append(deviceId)
                mykey.put()
        
        self.response.out.write({'result': isvalid})
