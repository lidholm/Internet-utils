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
        message.message = self.request.get("message")
        message.put()
        
        self.response.write("Saved")
        
class GetHandler(MessageHandler):
    def get(self):
        message = self.getMessage()
        output = message.message.replace("*", "\n*")
        self.response.write(output)

class HtmlHandler(MessageHandler):
    def get(self):
        #path = os.path.join(os.path.dirname(__file__), "static","html","chicago.html")
        #f = open(path)
        #webpage = f.read()
        #f.close()
        webpage = """<html ng-app="chicagoApp" xmlns="http://www.w3.org/1999/xhtml">

  <head>
    <title>Chicago</title>
    <script src="libraries/jquery.min.js"></script>
    <script src="libraries/angular.min.js"></script>
    <script src="js/scripts.js"></script>
    <link rel="stylesheet" href="/css/styles.css" />
  </head>

  <body ng-controller="ChicagoCtrl">
    <table><tr><td class="square">
      <div id="content">
        Time left until I'm in Chicago:
        <div id="countdown">
          <p class="days">00</p>
          <p class="timeRefDays">days</p>
          <!--  
          <p class="hours">00</p>
          <p class="timeRefHours">hours</p>
          <p class="minutes">00</p>
          <p class="timeRefMinutes">minutes</p>
          <p class="seconds">00</p>
          <p class="timeRefSeconds">seconds</p>
          -->
        </div>
      </div>
    </td></tr></table>

    <div id="todo1">
      
      <p class="header">Things to do</p>
      <textarea rows="80" cols="80" border="0" ng-model="todo" ng-change='newValue()'>
      </textarea>
      <div id="saveInfo">{{ todoHasChanged ? 'Not saved!' : 'Saved' }}</div>
    </div>

  </body>
</html>
""" 
        self.response.out.write(webpage)
