import json
import sys
import os

# Add the directory of this file to the Python path (optional if running from root)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from implementation.user_manager import UserManager
from implementation.team_manager import TeamManager
from implementation.board_manager import BoardManager


def main():
    print("🚀 Starting Team Project Planner Test Suite")

    # Initialize managers
    try:
        user_mgr = UserManager()
        team_mgr = TeamManager()
        board_mgr = BoardManager()
        print("✅ Managers initialized successfully")
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        return

    # Test User Flow
    try:
        print("\n=== Testing User Creation ===")
        user_data = {
            "user_id": 1,
            "name": "Alice",
            "email": "alice@example.com"
        }
        result = user_mgr.create_user(json.dumps(user_data))
        print("User creation result:", result)
    except Exception as e:
        print(f"❌ User test failed: {e}")

    # Test Team Flow
    try:
        print("\n=== Testing Team Creation ===")
        team_data = {
            "team_id": 101,
            "name": "Development Team",
            "members": [1]
        }
        result = team_mgr.create_team(json.dumps(team_data))
        print("Team creation result:", result)
    except Exception as e:
        print(f"❌ Team test failed: {e}")

    # Test Task Flow
    try:
        print("\n=== Testing Task Creation ===")
        task_data = {
            "task_id": 1001,
            "title": "Implement API",
            "description": "Create REST endpoints",
            "team_id": 101,
            "assigned_to": 1,
            "status": "To Do",
            "due_date": "2023-12-31"
        }
        result = board_mgr.create_task(json.dumps(task_data))
        print("Task creation result:", result)
    except Exception as e:
        print(f"❌ Task test failed: {e}")

    # Display Final State
    print("\n=== Final System State ===")
    try:
        users = user_mgr.get_all_users()
        teams = team_mgr.get_all_teams()
        tasks = board_mgr.get_all_tasks()
        print("Users:", users)
        print("Teams:", teams)
        print("Tasks:", tasks)
    except Exception as e:
        print(f"❌ Data retrieval failed: {e}")


if __name__ == "__main__":
    main()
