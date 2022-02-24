# from urllib import response
from bottle import get, view, request, redirect, response
import g

#   user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)


##############################
@get("/admin")
@view("admin")
def _():
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
  user_session_id = request.get_cookie("user_session_id")
  print("#"*40)
  print(g.SESSIONS)
  if not user_session_id:
    return redirect("/login")
  
  # if the user is not logged in:
  if user_session_id not in g.SESSIONS:
    return redirect("/login")
  user = g.SESSIONS[user_session_id]
  return dict(user=user)