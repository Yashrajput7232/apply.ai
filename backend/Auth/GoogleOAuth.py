import flask
from flask import jsonify, url_for
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from flask import session, redirect  # Import session and redirect

app = flask.Flask(__name__)  # Correctly initialize the Flask app

load_dotenv('backend/Auth/.env')  # Load environment variables

app.secret_key = os.getenv("FLASK_SECRET_KEY")  # Set the secret key for session management

oauth = OAuth(app)  # Pass the existing app instance to OAuth

google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile",
        # "prompt": "consent",
        # "access_type": "offline",
        # "include_granted_scopes": True,
    }
)

def save_user_to_db(user_info):
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client.get_database("apply-ai")
    users_collection = db.get_collection("users")
    
    # Check if user already exists
    existing_user = users_collection.find_one({"email": user_info["email"]})
    if not existing_user:
        # Insert new user
        users_collection.insert_one({
            "name": user_info["name"],
            "email": user_info["email"],
            "picture": user_info.get("picture"),
            "sub": user_info["sub"]
        })
        print(f"User {user_info['email']} added to the database.")
    else:
        print(f"User {user_info['email']} already exists in the database.")
    
    client.close()
    
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200   


@app.route("/login/google")
def login():
    try:
        # Use the Referer header to determine the frontend base URL
        referer = flask.request.headers.get('Referer')
        if referer:
            # Extract the base URL from the Referer header
            base_url = referer.rstrip('/')
            session['next_url'] = f"{base_url}/dashboard"
        else:
            # Fallback to default if Referer is not available
            session['next_url'] = '/dashboard'

        # Redirect to Google's OAuth authorization endpoint
        redirect_uri = os.getenv("GOOGLE_REDIRECT_URI", url_for('authorize', _external=True))
        return google.authorize_redirect(redirect_uri)
    except Exception as e:
        return f"An error occurred during Google login: {str(e)}", 500


@app.route("/authorize/google")
def authorize():
    try:
        # Exchange the authorization code for a token
        token = google.authorize_access_token()
        userinfo_endpoint = google.server_metadata['userinfo_endpoint']
        res = google.get(userinfo_endpoint)
        user_info = res.json()
    except Exception as e:
        print(f"Authorization Error: {e}")
        return f"An error occurred during authorization: {str(e)}", 500

    # Save user info to the database
    save_user_to_db(user_info)

    # Redirect to the original URL or fallback to /dashboard
    next_url = session.pop('next_url', '/dashboard')
    return redirect(next_url)

if __name__ == "__main__":
    app.run(debug=True, port=5000)