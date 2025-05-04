import requests
import logging
import time
import os
import flask
import threading

Logger = logging.getLogger(__name__)
google_auth_url = 'https://flask-google-oauth.onrender.com/health'
latex_api = 'https://latex-api-xx5f.onrender.com/health'
self_url='https://healtcheck.onrender.com/health2'

app = flask.Flask(__name__)  # Correctly initialize the Flask app

@app.route('/health', methods=['GET'])
def health_check():
    # Start the ping_services function in a separate thread
    thread = threading.Thread(target=ping_services, daemon=True)
    thread.start()
    
    # Return the health status immediately
    return {"status": "Healthcheck API is running"}, 200


@app.route('/health2', methods=['GET'])
def health_check2():

    return {"status": "Healthcheck API is running"}, 200


def ping_services():
    # This function will ping the Google Auth and Latex APIs every 5 minutes
    # and log the status of each service.
    while True:
        try:
            response = requests.get(google_auth_url)
            if response.status_code == 200:
                logging.info("Google Auth API is up and running.")
                logging.info(response.json())
        except requests.exceptions.RequestException as e:
            logging.error(f"Google Auth API is down: {e}")
            # Optionally, you can send an alert or take other actions here
        
        try:
            response = requests.get(latex_api)
            if response.status_code == 200:
                logging.info("Latex API is up and running.")
                logging.info(response.json())
        except requests.exceptions.RequestException as e:
            logging.error(f"Latex API is down: {e}")
            # Optionally, you can send an alert or take other actions here
        try:
            response = requests.get(self_url)
            if response.status_code == 200:
                logging.info("Health  API is up and running.")
                logging.info(response.json())
        except requests.exceptions.RequestException as e:
            logging.error(f"health  API is down: {e}")
            # Optionally, you can send an alert or take other actions here
        
        # Wait for 5 minutes before the next ping
        time.sleep(100)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)