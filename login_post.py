from bottle import post, request, redirect, response
import re
import uuid
import g
import jwt


##############################
@post("/login")
def _():
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

  # VALIDATE
  # VALIDATE if the form exist, at all inputs!!!!
  if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
    return redirect("/login?error=user_email")

  user_email = request.forms.get("user_email")

  if len(request.forms.get("user_password")) < 6:
    return redirect(f"/login?error=user_password&user_email={user_email}")
  if len(request.forms.get("user_password")) > 50:
    return redirect(f"/login?error=user_password&user_email={user_email}")

  user_password = request.forms.get("user_password")

  for user in g.USERS:
    if user["password"] == user_password and user["email"] == user_email:
      user_session_id = str(uuid.uuid4())
      # g.SESSIONS.append(user_session_id)
      # g.SESSIONS[user_session_id] = encoded_jwt         #create a key in sessions
      g.SESSIONS[user_session_id] = user         #create a key in sessions
      response.set_cookie("user_session_id", user_session_id)
      encoded_jwt = jwt.encode(user, "superkey", algorithm="HS256")
      # response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
      response.set_cookie(encoded_jwt, user_session_id, secret=g.COOKIE_SECRET)
      response.set_cookie("jwt", encoded_jwt, secret=g.COOKIE_SECRET)
      return redirect("/admin")
  print("#"*12)
  print("no match")
  return redirect(f"/login?error=wrong_usercredentials")
    
  
