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
verify=""
username=""
uner=""
pwer=""
pmater=""
email=""
emer=""

def isusernamevalid(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def ispwordvalid(password):
    USER_RE = re.compile(r"^.{3,20}$")
    if USER_RE.match(password):
        return True
    else:
        return False

def ispwordmatch(password,verify):
    if password==verify:
        return True
    else:
        return False

def isemailvalid(email):
    USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    if USER_RE.match(email) or email=="":
        return True
    else:
        return False


def build_page(username,uner,pwer,pmater,email,emer):
    head="""<!DOCTYPE html>
                <html>
                    <head>
                        <title>
                            User Signup
                        </title>
                        <style>
                        body {background-color: powderblue;}
                        h1   {color: blue;}
                        .error    {color: red;}
                        </style>
                    </head>
                    <body>"""
    headline="<h1>User Signup</h1>"
    table="""<table>
                <tbody>
            <tr><td><label>Username</label></td><td><input name=username type=text value=%s></td>%s</tr>
            <tr><td><label>Password</label></td><td><input name=password type=password></td>%s</tr>
            <tr><td><label>Confirm Password</label></td><td><input name=verify type=password></td>%s</tr>
            <tr><td><label>E-mail(optional)</label></td><td><input name=email type=text value=%s></td>%s</tr>
                </tbody>
            </table>
            </body>
            """%(username,uner,pwer,pmater,email,emer)
    submit="<input type= 'submit'/>"
    form="<form method=post>"+head+headline+table+submit+"</form>"
    return form

def build_success_page(username):
    head="<h1>Welcome %s</h1>"%(username)
    return head

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content=build_page("","","","","","")
        self.response.write(content)

    def post(self):
        username=cgi.escape(self.request.get("username"))
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=cgi.escape(self.request.get("email"))
        if isusernamevalid(username) and ispwordvalid(password) and ispwordmatch(password,verify) and isemailvalid(email):
            self.redirect("/Welcome?username="+username)
        else:
            if isusernamevalid(username):
                uner=""
            else:
                uner="<td class='error'>Your username is invalid.</td>"
            if ispwordvalid(password):
                pwer=""
            else:
                pwer="<td class='error'>Your password is not 3-20 chars."
            if ispwordmatch(password,verify):
                pmater=""
            else:
                pmater="<td class='error'>Your passwords don't match</td>"
            if isemailvalid(email):
                emer=""
            else:
                emer="<td class='error'>Your email address appears to be invalid.</td>"
            content=build_page(username,uner,pwer,pmater,email,emer)
            self.response.write(content)

class SuccessPage(webapp2.RequestHandler):
    def get(self):
        un=self.request.get("username")
        self.response.write(build_success_page(un))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Welcome',SuccessPage)
], debug=True)
