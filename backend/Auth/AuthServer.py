from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from flask import session


# Load environment variables
load_dotenv('backend/Auth/.env')

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Google OAuth setup
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Only for development

google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    scope=["profile", "email"],
    redirect_url=os.getenv("GOOGLE_REDIRECT_URI")  # ✅ Use the one from .env
)
app.register_blueprint(google_bp, url_prefix="/auth")

# MongoDB setup
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGO_DB_NAME")

if not mongo_uri or not db_name:
    raise ValueError("Missing MongoDB credentials in .env")

client = MongoClient(mongo_uri)
db = client[db_name]
users_collection = db["users"]

def save_user_to_db(user_info):
    user_email = user_info.get("email")
    if not user_email:
        return

    existing_user = users_collection.find_one({"email": user_email})
    if not existing_user:
        users_collection.insert_one({
            "google_id": user_info.get("id"),
            "name": user_info.get("name"),
            "email": user_info.get("email"),
            "picture": user_info.get("picture")
        })
    else:
        users_collection.update_one(
            {"email": user_email},
            {"$set": {
                "name": user_info.get("name"),
                "picture": user_info.get("picture")
            }}
        )

@app.route("/")
def home():
    return '<a href="/auth/google">Login with Google</a>'

@app.route("/auth/callback")
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    if not resp.ok:
        return "Failed to fetch user info.", 500
    print("Session state:", session.get("google_oauth_state"))
    if not google.authorized:
        return redirect(url_for("google.login"))

    user_info = resp.json()
    save_user_to_db(user_info)

    return f"""
    <h1>Welcome, {user_info['name']}</h1>
    <p>Email: {user_info['email']}</p>
    <img src="{user_info['picture']}" alt="Profile Picture" width="100">
    """

if __name__ == "__main__":
    app.run(debug=False, port=5000)
