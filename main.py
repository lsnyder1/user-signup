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
username=""
e_mail=""
def build_page(username,e_mail):
    headline="<h1>User Signup</h1>"
    table="""<table>
                <tbody>
            <tr><td><label>Username</label></td><td><input name=username type=text value=%s></td></tr>
            <tr><td><label>Password</label></td><td><input name=password type=password></td></tr>
            <tr><td><label>Confirm Password</label></td><td><input name=confirm_password type=password></td></tr>
            <tr><td><label>E-mail(optional)</label></td><td><input name=e_mail type=text value=%s></td></tr>
                </tbody>
            </table>
            """%(username,e_mail)
    submit="<input type= 'submit'/>"
    form="<form method=post>"+headline+table+submit+"</form>"
    return form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content=build_page("","")
        self.response.write(content)

    def post(self):
        username=cgi.escape(self.request.get("username"))
        password=self.request.get("password")
        confirm_password=self.request.get("confirm_password")
        e_mail=cgi.escape(self.request.get("e_mail"))
        content=build_page(username,e_mail)
        self.response.write(content)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
