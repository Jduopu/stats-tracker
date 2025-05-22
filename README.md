# 🏈 Player Stat Tracker

A full-stack web application built with Flask (Python), HTML, CSS, and JavaScript to track football player performance in real time. Player data is stored in an SQLite database and can be viewed, added, and updated through a clean user interface.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Objective](#objective)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## 🧠 Overview

This project allows users to input football player stats — including name, position, touchdowns, yards, and tackles — and dynamically displays them in a sortable table. It demonstrates full-stack development with a Python Flask backend and a JavaScript-driven front end.

---

## 🎯 Objective

- Create a full-stack project that integrates front-end and back-end development.
- Provide a real-time form and table to manage player performance.
- Practice database interaction, API routing, and front-end display using native web tools.

---

## 🏗️ System Architecture

- `app.py`: Flask server, routing, and SQLite database logic.
- `templates/index.html`: The main UI page.
- `static/main.js`: JavaScript logic for form submission and table rendering.
- `static/style.css`: Styles for layout and responsiveness.
- `database.db`: SQLite database storing player information.

---

## ✅ Features

- Add new football players and their stats.
- View all players in a dynamic, sortable table.
- Real-time update of the table after form submission.
- Lightweight and easy to deploy locally or online.

---

## 🧰 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Front-End    | HTML, CSS, JavaScript |
| Back-End     | Python (Flask)     |
| Database     | SQLite             |
| Version Control | Git + GitHub    |

---

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jduopu/stat-tracker.git
   cd stat-tracker
2. **Set Up environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the app**
   ```bash
   python main.py
5. **Put in your browser**
   ```bash
   http://127.0.0.1:5000

---

## 🚀 Usage ##

- Fill out form to add new player
- Submitted stats are stored in the database and displayed in the table
- Data is updated without refreshing page

---

## 📁 File Structure ##
```bash
player-stat-tracker/
├── app.py
├── requirements.txt
├── database.db
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── main.js
└── README.md
```

---

## 🐛 Known Issues ##
- Table sorting is static (no dynamic sort yet).
- No input validation or edit/delete functionality.
- Stats are not yet grouped or filterable by team.

---

## 🚧 Future Improvements ##
- Add ability to edit and delete players
- Implement filtering and sorting by position or stat.
- Add login and user-based stat tracking.
- Deploy live using Render or Replit.
- Add charts to visualize performance over time.

---

## 🙌 Credits ##
Built by @Jduopu as part of a portfolio for full-stack web development.

---

## 📄 License ##
This project is licensed under the MIT License — see LICENSE for details.
