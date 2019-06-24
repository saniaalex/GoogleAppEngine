#!/usr/bin/env python
#


import webapp2

from google.appengine.api import memcache
from google.appengine.api import users
import time

def prime(n):
  
  n=int(n)
  cachedPrime = memcache.get(str(n))
  if cachedPrime != None:
    return cachedPrime
  if n==0 | n==1:
    x=0
    return x
  else:
    count=0
  
  for i in range(n+2):
    if n%(i+2)==0:
      count=count+1
  if count==1:
    x=1
    return x   
  else:
    x=0
    return x
  memcache.set(str(n),x)
  return x
class MainPage(webapp2.RequestHandler):
  def get(self):
    user=users.get_current_user()
    if user:
     
      self.response.out.write('<html><body bgcolor="#99ff99"><center> <h1> Hello ')
      self.response.write(user.nickname() + "</h1>")
      start=time.time()
    
      self.response.out.write('<h1> Prime Number Validator </h1>')
      self.response.out.write('<br>')
    
  
      self.response.out.write('<br><br>')
      self.response.out.write('<form method="GET">')
      self.response.out.write('Enter a number<input name="n" type="text">')
      self.response.out.write('<input type="submit" value="Submit number">')
      self.response.out.write('<br> <br>')
      self.response.out.write('<h2>')

      if 'n' in self.request.GET.keys():
        if(prime(self.request.GET['n'])==0):
          self.response.out.write(self.request.GET['n'] + " is not prime")
        else:
          self.response.out.write(self.request.GET['n'] + " is prime")
      self.response.out.write('<br> <br>')
      elapsed=time.time() - start
      self.response.out.write('Time taken:' + str(elapsed))
      self.response.out.write('</h2>')
      self.response.out.write('</form> </center></body></html>')
      self.response.out.write('<a href="'+users.create_logout_url('/'))
      self.response.out.write('"> Click me to log off</a>')
    else:
      self.response.out.write('<a href="'+users.create_login_url('/'))
      self.response.out.write('"> Click me to log in</a>')

   
   

app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)