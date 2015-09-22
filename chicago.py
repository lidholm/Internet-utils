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
import webapp2
import os


from google.appengine.api import channel
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.ext import ndb

class Message(ndb.Model):
    message = ndb.StringProperty()

class MessageHandler(webapp2.RequestHandler):
    def getMessage(self):
        message_k = ndb.Key('Message', 'message1')
        message = message_k.get()
        return message
    
    def createMessage(self):
        for message in Message.query().fetch(limit = 100):
            message.key.delete()
        message = Message(message='Message', id='message1')
        return message
    
class PutHandler(MessageHandler):
    def get(self):
        
        message = self.getMessage()
        if message is None:
            message = self.createMessage()
        message.message = self.request.get("hej")
        message.put()
        
        self.response.write("Saved")
        
class GetHandler(MessageHandler):
    def get(self):
        message = self.getMessage()
        self.response.write(str(message))

class HtmlHandler(MessageHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), "static","html","chicago.html")
        f = open(path)
        webpage = f.read()
        f.close() 
        self.response.out.write(webpage)

