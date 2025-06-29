
# 📅 Event Scheduler System

A RESTful API built using **Python Flask** to create, view, update, and delete scheduled events. Event data is stored in a JSON file on the server to ensure persistence between sessions.

---

## 🚀 Features

- ✅ Create events
- 📖 View all events (sorted by start time)
- ✏️ Update existing events
- ❌ Delete events
- 💾 Persistent storage using `events.json`

---

## ⚙️ Tech Stack

- Python 3.x
- Flask
- JSON (for storage)

---

## 📁 Project Structure

```

event\_scheduler/
│
├── app.py              # Main Flask application
├── events.json         # Stores event data (auto-created)
├── requirements.txt    # Python dependencies
└── README.md           # Instructions file

````

---

## 🛠️ Setup Instructions

### ✅ Step 1: Clone or Download

```bash
git clone https://github.com/karansharama24/event-scheduler.git
cd event-scheduler
````

---

### ✅ Step 2: Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # For Windows
# OR
source venv/bin/activate     # For Linux/macOS
```

---

### ✅ Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ Step 4: Run the App

```bash
python app.py
```

Flask will start at:

```
http://127.0.0.1:5000/
```

---

## 🔌 API Endpoints & Sample Requests

---

### 📥 Create Event (POST `/events`)

#### Request:

```bash
curl -X POST http://127.0.0.1:5000/events \
-H "Content-Type: application/json" \
-d '{
  "title": "Team Meeting",
  "description": "Weekly sync-up",
  "start_time": "2025-07-01 10:00",
  "end_time": "2025-07-01 11:00"
}'
```

#### Output:

```json
{
  "message": "Event created",
  "event": {
    "id": 1,
    "title": "Team Meeting",
    "description": "Weekly sync-up",
    "start_time": "2025-07-01 10:00",
    "end_time": "2025-07-01 11:00"
  }
}
```

---

### 📖 View Events (GET `/events`)

#### Request:

```bash
curl http://127.0.0.1:5000/events
```

#### Output:

```json
[
  {
    "id": 1,
    "title": "Team Meeting",
    "description": "Weekly sync-up",
    "start_time": "2025-07-01 10:00",
    "end_time": "2025-07-01 11:00"
  }
]
```

---

### ✏️ Update Event (PUT `/events/1`)

#### Request:

```bash
curl -X PUT http://127.0.0.1:5000/events/1 \
-H "Content-Type: application/json" \
-d '{
  "description": "Updated description",
  "end_time": "2025-07-01 11:30"
}'
```

#### Output:

```json
{
  "message": "Event updated",
  "event": {
    "id": 1,
    "title": "Team Meeting",
    "description": "Updated description",
    "start_time": "2025-07-01 10:00",
    "end_time": "2025-07-01 11:30"
  }
}
```

---

### ❌ Delete Event (DELETE `/events/1`)

#### Request:

```bash
curl -X DELETE http://127.0.0.1:5000/events/1
```

#### Output:

```json
{
  "message": "Event 1 deleted"
}
```

---

## 📤 Postman Collection

You can import the provided Postman collection (JSON file) to test all endpoints with ease.

> Don't forget to set **raw > JSON** in the Body tab when sending POST/PUT requests in Postman.

---

## 🧪 Sample Input Format

```json
{
  "title": "Doctor Visit",
  "description": "Routine health checkup",
  "start_time": "2025-07-02 09:00",
  "end_time": "2025-07-02 10:00"
}
```

Time format must be:

```
YYYY-MM-DD HH:MM (24-hour clock)
```

---

## 👤 Author

**Karan Sharma**
Aspiring Cloud & DevOps Engineer

---

## 📃 License

Free to use for educational or assessment purposes.
