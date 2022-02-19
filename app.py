from bottle import error, get, run, static_file, view


##############################
import home_get             # GET  
import signup_get           # GET   
import login_get            # GET
import users_get            # GET
import items_get            # GET
import admin_get            # GET
import signup_ok_get        # GET
import logout_get           # GET
import tweets_get           # GET

import signup_post          # POST
import login_post           # POST
import delete_item_post     # POST
import add_tweet_post       # POST
import delete_tweet_post    #POST

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@error(404)
@view("404")
def _(error):
  print(error)
  return

##############################
run(host="127.0.0.1", port=4444, debug=True, reloader=True)















