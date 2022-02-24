from bottle import get, request, redirect, response
import g

##############################

@get("/logout")
def _(): 
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
  user_session_id = request.get_cookie("user_session_id")
  g.SESSIONS.pop(user_session_id)
  
  # Delete the cookies from the browser
  response.set_cookie("user_session_id", "", expires=0)
  return redirect("/login")