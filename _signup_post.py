from bottle import post, request, redirect
import re #import regex
import g
import uuid


##############################
@post("/signup")
def _():

  # VALIDATE

  ##############################  NAME
  if not request.forms.get("user_name"):
     return redirect("signup?error=user_name")

  user_name = request.forms.get("user_name")
  
  ##############################  LASTNAME
  if not request.forms.get("user_lastname"):
    return redirect("signup?error=user_lastname")

  user_lastname = request.forms.get("user_lastname")

  ##############################  EMAIL
  #if there is no e-mail -> error
  if not request.forms.get("user_email"):
    return redirect(f"/signup?error=user_email&user_name={user_name}&user_lastname={user_lastname}")
  #if given e-mail does not match regex -> error
  if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
    return redirect(f"/signup?error=user_email&user_name={user_name}&user_lastname={user_lastname}")

  user_email = request.forms.get("user_email")
  
  ##############################  PASSWORD
  #if there is no password -> error
  if not request.forms.get("user_password"):
    return redirect(f"/signup?error=user_password&user_email={user_email}&user_name={user_name}&user_lastname={user_lastname}")
  #if given password less than 6char -> error
  if len(request.forms.get("user_password")) < 6:
    return redirect(f"/signup?error=user_password&user_email={user_email}&user_name={user_name}&user_lastname={user_lastname}")
  #if given password more than 50char -> error
  if len(request.forms.get("user_password")) > 50:
    return redirect(f"/signup?error=user_password&user_email={user_email}&user_name={user_name}&user_lastname={user_lastname}")

  user_password = request.forms.get("user_password")


  
  user_id = str(uuid.uuid4())
  user = {"id":user_id, "email":user_email, "name":user_name, "lastname":user_lastname, "password":user_password}
  g.USERS.append(user)
  return redirect(f"signup-ok?user-email={user_email}&user-name={user_name}&user-lastname={user_lastname}&user-password={user_password}")

