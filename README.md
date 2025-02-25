# goit-pythonweb-hw-03

Homework 3. Fullstack Web Development with Python at GoIT Neoversity

# Simple Web Server

This is a basic web application built using Python's built-in HTTP server and Jinja2 for templating. The application allows users to send and view messages, and it handles static files like CSS and images.

## Features
- Serves static HTML pages (`index.html`, `message.html`, and `error.html`).
- Processes form submissions to store messages in a JSON file (`storage/data.json`).
- Displays stored messages in a `/read` route.
- Handles 404 errors with a custom `error.html` page.
- Supports running both in a local Python environment and inside a Docker container.

## Prerequisites
Make sure you have the following installed:
- **Python 3.10+** (Recommended: Python 3.13)
- **Docker** (optional, for containerized execution)

---

## Running Locally with Python

### 1. Clone the Repository
```sh
 git clone https://github.com/stdev33/goit-pythonweb-hw-03.git
 cd goit-pythonweb-hw-03
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Start the Server
```sh
python server.py
```

### 5. Open in Browser
Visit: **[http://localhost:3000](http://localhost:3000)**

---

## Running with Docker

### 1. Build the Docker Image
```sh
docker build -t simple_web_server .
```

### 2. Run the Container
```sh
docker run -d -p 3000:3000 -v $(pwd)/storage:/app/storage simple_web_server
```

> **Note:** The `-v $(pwd)/storage:/app/storage` flag ensures that the messages are stored persistently outside the container.

### 3. Open in Browser
Visit: **[http://localhost:3000](http://localhost:3000)**

---

## Project Structure
```
.
├── server.py            # Main Python server script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── storage/             # Folder for storing messages
│   ├── data.json        # JSON file storing messages
├── templates/           # HTML templates
│   ├── index.html       # Homepage
│   ├── message.html     # Message form page
│   ├── error.html       # 404 error page
│   ├── read.html        # Page to view messages
├── static/              # Static files
│   ├── style.css        # Stylesheet
│   ├── logo.png         # Logo image
└── README.md            # This documentation file
```

---

## API Routes
| Route            | Method | Description |
|-----------------|--------|-------------|
| `/` or `/index.html` | GET | Displays the homepage |
| `/message.html` | GET | Shows the message submission form |
| `/message` | POST | Handles message form submission and stores data in `data.json` |
| `/read` | GET | Displays all stored messages |
| `/static/*` | GET | Serves static files (CSS, images) |
| `*` | 404 | Custom error page for unknown routes |


---
