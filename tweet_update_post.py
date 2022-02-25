from bottle import post, redirect, request
import g

##############################

@post("/tweet_update/<tweet_id>")
def _(tweet_id):
    tweet_id = request.forms.get("tweet_id")
    tweet_title = request.forms.get("tweet_title")
    tweet_desc = request.forms.get("tweet_desc")
    
    user_session_id = request.get_cookie("user_session_id")

    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    
    for  tweet in g.TWEETS:
        if tweet["id"] == tweet_id:
            tweet.update({"title":tweet_title, "desc": tweet_desc})
    return redirect("/tweets")