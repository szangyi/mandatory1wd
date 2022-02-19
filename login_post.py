from bottle import post, request, redirect, response
import re
import uuid
import g
import jwt
import time


##############################
@post("/login")
def _():
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

  # VALIDATE   
  if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
    return redirect("/login?error=user_email")

  user_email = request.forms.get("user_email")

  if len(request.forms.get("user_password")) < 6:
    return redirect(f"/login?error=user_password&user_email={user_email}")
  if len(request.forms.get("user_password")) > 50:
    return redirect(f"/login?error=user_password&user_email={user_email}")

  user_password = request.forms.get("user_password")

  #dictionairy
  # user = {
    # "email" : user_email,
    # "password" : user_password,
    # "iat" : int(time.time())
  # }


  
  for user in g.USERS:
    # SUCCESS
    print("#"*10)
    print("this is the user")
    print(user)
    if user["password"] == user_password and user["email"] == user_email:
      user_session_id = str(uuid.uuid4())
      # g.SESSIONS.append(user_session_id)
      # g.SESSIONS[user_session_id] = encoded_jwt         #create a key in sessions
      g.SESSIONS[user_session_id] = user         #create a key in sessions
      print("#"*3)
      print(g.SESSIONS)
      response.set_cookie("user_session_id", user_session_id)
      encoded_jwt = jwt.encode(user, "superkey", algorithm="HS256")
      print("#"*30)
      print(encoded_jwt) 
      # response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
      response.set_cookie(encoded_jwt, user_session_id, secret=g.COOKIE_SECRET)
      return redirect("/tweets")
    # FAIL
    else: 
      return redirect ("/login")
    
  
