from bottle import post, request, redirect
import uuid
import re
import g

##############################
@post("/signup")
def _():

  # VALIDATE
  if not request.forms.get("user_name"):
    return redirect(f"/signup?error=user_name")
  user_name = request.forms.get("user_name")
  if not request.forms.get("user_lastname"):
    return redirect(f"/signup?error=user_lastname&user_name={user_name}")
  user_lastname = request.forms.get("user_lastname")
  if not request.forms.get("user_email"):
    return redirect(f"/signup?error=user_email&user_name={user_name}&user_lastname={user_lastname}")
  user_email = request.forms.get("user_email")
  if not request.forms.get("user_password"):
    return redirect(f"/signup?error=user_password&user_name={user_name}&user_lastname={user_lastname}&user_email={user_email}")
  user_password = request.forms.get("user_password")

  user_id = str(uuid.uuid4())
  
  user = {"id":user_id, "email":user_email, "name":user_name, "lastname":user_lastname, "password":user_password}
  g.USERS.append(user)
  print("#"*10)
  print("these are the users")
  print(g.USERS)
  return redirect(f"signup-ok?user-email={user_email}&user-name={user_name}&user-lastname={user_lastname}&user-password={user_password}")