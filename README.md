# Team Project Planner
A simple Python-based Team Project Planner application that allows managing users, teams, and tasks using JSON files for persistent storage.

---

## Features

- **User Management**: Create, update, retrieve, and delete users.
- **Team Management**: Create, update, retrieve, and delete teams with members.
- **Task Management**: Create, update, retrieve, and delete tasks assigned to team members.
- **Data Persistence**: Uses JSON files to save and load data.
- **Input Validation**: Ensures data integrity and correct JSON formats.
- **Simple CLI Testing**: Includes a test script to validate functionality of core components.

---

## Technologies Used

- Python 3.7+
- Standard Python libraries: `json`, `os`, `datetime`, `typing`

No external dependencies are required, making this project lightweight and easy to run.

---


1. **Clone the repository**

   ```bash
   git clone https://github.com/Yashdhangar123/Team-Project-Planner.git
   cd team-project-planner
 if need any help contact : 9819511766

**Project Structure**
.
├── base/
│   ├── project_board_base.py    # Abstract base class for board management
│   ├── team_base.py             # Abstract base class for team management
│   └── user_base.py             # Abstract base class for user management
├── db/                         # JSON data files (created automatically)
│   ├── users.json
│   ├── teams.json
│   └── boards.json
├── implementation/
│   ├── board_manager.py         # Task management implementation
│   ├── team_manager.py          # Team management implementation
│   └── user_manager.py          # User management implementation
├── test.py                     # Test script to run example flows
├── requirements.txt            # Python dependencies
└── README.md                   # This file


## The implementation of the project :
1. Create Project Structure
Open Command Prompt (cmd) and run:
cmd
mkdir factwise-python
cd factwise-python
mkdir db implementation base
type nul > db\users.json
type nul > db\teams.json
type nul > db\boards.json
type nul > implementation\__init__.py
type nul > base\user_base.py
type nul > base\team_base.py
type nul > base\project_board_base.py
type nul > test.py

2. Initialize JSON Files
cmd
echo [] > db\users.json
echo [] > db\teams.json
echo [] > db\boards.json

3. Add Code to Files
Copy the code provided earlier into each corresponding file:
base/user_base.py
base/team_base.py
base/project_board_base.py
implementation/user_manager.py
implementation/team_manager.py
implementation/board_manager.py
test.py

4. Run the Project
cmd
python test.py

5.Output:
 Starting Team Project Planner Test Suite
 Managers initialized successfully

=== Testing User Creation ===
{"status": "success", "user": {...}, "timestamp": ...}

=== Testing Team Creation ===
{"status": "success", "team": {...}, "timestamp": ...}

=== Testing Task Creation ===
{"status": "success", "task": {...}, "timestamp": ...}

=== Final System State ===
Users: [...]
Teams: [...]
Tasks: [...]
