from bottle import post, request, redirect
import re #import regex
import g

##############################
@post("/login")
def _():
  # VALIDATE

  #if there is no e-mail -> error
  if not request.forms.get("user_email"):
    return redirect("login?error=user_email")
  #if given e-mail does not match regex -> error
  if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
    return redirect("login?error=user_email")

  user_email = request.forms.get("user_email")
  
  #if there is no password -> error
  if not request.forms.get("user_password"):
    return redirect(f"/login?error=user_password&user_email={user_email}")
  #if given password less than 6char -> error
  if len(request.forms.get("user_password")) < 6:
    return redirect(f"/login?error=user_password&user_email={user_email}")
  #if given password more than 50char -> error
  if len(request.forms.get("user_password")) > 50:
    return redirect(f"/login?error=user_password&user_email={user_email}")

  user_password = request.forms.get("user_password")

  
  for user in g.USERS:
    # SUCCESS
    if user["password"] == user_password and user["email"] == user_email:
      return redirect("/admin")

    # FAIL
  return redirect ("/login")

