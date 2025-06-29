from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Path to store events
EVENT_FILE = "events.json"

# Load existing events or create empty list
if os.path.exists(EVENT_FILE):
    with open(EVENT_FILE, "r") as f:
        events = json.load(f)
else:
    events = []

# Helper function to save events to file
def save_events():
    with open(EVENT_FILE, "w") as f:
        json.dump(events, f, indent=4)

# Home route
@app.route('/')
def home():
    return "✅ Event Scheduler API is running."

# List all available routes (debug tool)
@app.route('/routes')
def list_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    # Validate input
    if not all(k in data for k in ('title', 'description', 'start_time', 'end_time')):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M')
        datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD HH:MM"}), 400

    data['id'] = len(events) + 1
    events.append(data)
    save_events()
    return jsonify({"message": "Event created", "event": data}), 201

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    sorted_events = sorted(events, key=lambda x: x['start_time'])
    return jsonify(sorted_events), 200

# Update an event by ID
@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    for event in events:
        if event['id'] == id:
            event.update(request.json)
            save_events()
            return jsonify({"message": "Event updated", "event": event}), 200
    return jsonify({"error": "Event not found"}), 404

# Delete an event by ID
@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    global events
    events = [event for event in events if event['id'] != id]
    save_events()
    return jsonify({"message": f"Event {id} deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
