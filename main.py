#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from handlers import *

# example - http://localhost:8085/random/directball to get a key for directball
# example2 - http://localhost:8085/check/directball/dbsbd?deviceid=adeus to check application "directball" for coupon "dbsbd" with deviceid "adeus"

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          (r'/random/(.*)',RandomKeyHandler),
                                          (r'/check/(.*)/(.*)',CheckKeyHandler),
                                          ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
