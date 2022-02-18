from bottle import get, view, request, response
import g

##############################
# Query string will be used in this route
# Eg: /login?error=user_email
# Eg: /login?error=user_password
# Eg: /login?error=user_password&user_email=a@a.cm
@get("/login")
@view("login")
def _():
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
  print("logiiiiiiiiiiiiiiiin")
  print(g.SESSIONS)
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  user_password = request.params.get("user_password")
  return dict(error=error, user_email=user_email, user_password=user_password)