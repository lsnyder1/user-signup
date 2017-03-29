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
import cgi
import re
password=""
confirm_password=""
username=""
uner=""
pwer=""
e_mail=""
emer=""

def isusernamevalid(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def ispwordvalid(password,confirm_password):
    USER_RE = re.compile(r"^.{3,20}$")
    if password==confirm_password and USER_RE.match(password):
        return True
    else:
        return False

def isemailvalid(e_mail):
    USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    if USER_RE.match(e_mail) or e_mail=="":
        return True
    else:
        return False


def build_page(username,uner,pwer,e_mail,emer):
    headline="<h1>User Signup</h1>"
    table="""<table>
                <tbody>
            <tr><td><label>Username</label></td><td><input name=username type=text value=%s>%s</td></tr>
            <tr><td><label>Password</label></td><td><input name=password type=password></td></tr>
            <tr><td><label>Confirm Password</label></td><td><input name=confirm_password type=password>%s</td></tr>
            <tr><td><label>E-mail(optional)</label></td><td><input name=e_mail type=text value=%s>%s</td></tr>
                </tbody>
            </table>
            """%(username,uner,pwer,e_mail,emer)
    submit="<input type= 'submit'/>"
    form="<form method=post>"+headline+table+submit+"</form>"
    return form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content=build_page("","","","","")
        self.response.write(content)

    def post(self):
        username=cgi.escape(self.request.get("username"))
        password=self.request.get("password")
        confirm_password=self.request.get("confirm_password")
        e_mail=cgi.escape(self.request.get("e_mail"))
        if isusernamevalid(username) and ispwordvalid(password,confirm_password) and isemailvalid(e_mail):
            self.redirect("/Welcome?username="+username)
        else:
            if isusernamevalid(username):
                uner=""
            else:
                uner="Your username is invalid."
            if ispwordvalid(password,confirm_password):
                pwer=""
            else:
                pwer="Your passwords don't match."
            if isemailvalid(e_mail):
                emer=""
            else:
                emer="Your email address appears to be invalid."
            content=build_page(username,uner,pwer,e_mail,emer)
            self.response.write(content)

class SuccessPage(webapp2.RequestHandler):
    def get(self):
        head="<h1>Welcome"+username+"</h1>"
        self.response.write(head)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Welcome',SuccessPage)
], debug=True)
