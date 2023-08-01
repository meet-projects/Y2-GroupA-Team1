from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import session as login_session
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyAH2CsLDvAhWYodhka7Cxw_6DEGXtyRYRo",
  "authDomain": "events-740e0.firebaseapp.com",
  "databaseURL": "https://events-740e0-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "events-740e0",
  "storageBucket": "events-740e0.appspot.com",
  "messagingSenderId": "684981708137",
  "appId": "1:684981708137:web:164371104aa37a90fe89f8",
  "measurementId": "G-YL9NK5T6CF",
  "databaseURL":"https://events-740e0-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db =firebase.database()
app = Flask(__name__, template_folder='templets', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key '


#Code goes below here 

@app.route('/')
def home():
    return render_template('new_index.html')

#Code goes above here

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/cal')
def cal():
    return render_template("cal.html")

@app.route('/fetch_events/<string:selected_date>')
def fetch_events(selected_date):
    # Assuming your Firebase database structure is something like this:
    # /events
    #    - date1
    #        - event1
    #        - event2
    #    - date2
    #        - event3
    #        - event4

    # Retrieve events for the selected date from the Firebase database
    events = []
    try:
        events_snapshot = db.child('events').child(selected_date).get()
        if events_snapshot:
            events = events_snapshot.val()
            print(events)
            events = next(iter(events.values()))
    except Exception as e:
        # Handle any errors that might occur while fetching events
        print("Error fetching events:", e)
        return jsonify({"error": "Error fetching events."}), 500

    # Here, you should format the events data as needed for your HTML template
    # For example, you can convert the events dictionary to a list of dictionaries
    # that contains event details like title, description, etc.

    # Finally, return the formatted events data as JSON response
    return jsonify(events), 200


events = [
    "Attending a concert",
    "Going on a road trip",
    "Birthday party celebration",
    "Hiking in the mountains",
    "Picnic at the park",
    "Movie night with friends",
    "Visiting a museum",
    "Beach day and surfing",
    "Trying a new restaurant",
    "Karaoke night",
    "Volunteering at a local shelter",
    "Attending a sports game",
    "Camping in the wilderness",
    "Exploring a new city",
    "Cooking a fancy dinner",
    "Attending a comedy show",
    "Art and craft workshop",
    "Book club meeting",
    "Attending a dance class",
    "Gardening in the backyard",
    "Stargazing on a clear night",
    "Attending a theater performance",
    "Spa and relaxation day",
    "Visiting an amusement park",
    "Game night with board games",
    "Attending a cultural festival",
    "Trying out a new sport",
    "Visiting a zoo or aquarium",
    "Attending a poetry reading",
    "Solving escape room puzzles",
    "Going to a farmers' market"
]
def create_fake_events(events):
    for day in range(1,32):
        db.child("events").child(day).push(events[day-1])@app.route('/fetch_events/<string:selected_date>')
def fetch_events(selected_date):
    # Assuming your Firebase database structure is something like this:
    # /events
    #    - date1
    #        - event1
    #        - event2
    #    - date2
    #        - event3
    #        - event4

    # Retrieve events for the selected date from the Firebase database
    events = []
    try:
        events_snapshot = db.child('events').child(selected_date).get()
        if events_snapshot:
            events = events_snapshot.val()
            print(events)
            events = next(iter(events.values()))
    except Exception as e:
        # Handle any errors that might occur while fetching events
        print("Error fetching events:", e)
        return jsonify({"error": "Error fetching events."}), 500

    # Here, you should format the events data as needed for your HTML template
    # For example, you can convert the events dictionary to a list of dictionaries
    # that contains event details like title, description, etc.

    # Finally, return the formatted events data as JSON response
    return jsonify(events), 200


events = [
    "Attending a concert",
    "Going on a road trip",
    "Birthday party celebration",
    "Hiking in the mountains",
    "Picnic at the park",
    "Movie night with friends",
    "Visiting a museum",
    "Beach day and surfing",
    "Trying a new restaurant",
    "Karaoke night",
    "Volunteering at a local shelter",
    "Attending a sports game",
    "Camping in the wilderness",
    "Exploring a new city",
    "Cooking a fancy dinner",
    "Attending a comedy show",
    "Art and craft workshop",
    "Book club meeting",
    "Attending a dance class",
    "Gardening in the backyard",
    "Stargazing on a clear night",
    "Attending a theater performance",
    "Spa and relaxation day",
    "Visiting an amusement park",
    "Game night with board games",
    "Attending a cultural festival",
    "Trying out a new sport",
    "Visiting a zoo or aquarium",
    "Attending a poetry reading",
    "Solving escape room puzzles",
    "Going to a farmers' market"
]
def create_fake_events(events):
    for day in range(1,32):
        db.child("events").child(day).push(events[day-1])

if __name__ == '__main__':
    app.run(debug=True, port=5003)
