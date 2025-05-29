import json
import os
from datetime import datetime
from typing import Dict, List
from base.project_board_base import ProjectBoardBase

class BoardManager(ProjectBoardBase):
    VALID_STATUSES = {"To Do", "In Progress", "Done"}
    
    def __init__(self, db_path: str = "db/boards.json", team_db_path: str = "db/teams.json"):
        self.db_path = db_path
        self.team_db_path = team_db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        if not os.path.exists(self.db_path) or os.path.getsize(self.db_path) == 0:
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_tasks(self) -> List[Dict]:
        with open(self.db_path, 'r', encoding='utf-8-sig') as f:
            return json.load(f)

    def _save_tasks(self, tasks: List[Dict]) -> None:
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)

    def _load_teams(self) -> List[Dict]:
        if not os.path.exists(self.team_db_path):
            return []
        with open(self.team_db_path, 'r', encoding='utf-8-sig') as f:
            return json.load(f)

    def create_task(self, input_json: str) -> str:
        try:
            data = json.loads(input_json)
            required_fields = ["task_id", "title", "team_id", "assigned_to", "status"]
            if not all(k in data for k in required_fields):
                raise ValueError(f"Missing required fields: {required_fields}")
            
            if data['status'] not in self.VALID_STATUSES:
                raise ValueError(f"Invalid status. Must be one of: {self.VALID_STATUSES}")

            teams = self._load_teams()
            team = next((t for t in teams if t['team_id'] == data['team_id']), None)
            if not team:
                raise ValueError(f"Team ID {data['team_id']} not found")
                
            if data['assigned_to'] not in team['members']:
                raise ValueError(f"User {data['assigned_to']} is not in team {data['team_id']}")

            tasks = self._load_tasks()
            if any(t['task_id'] == data['task_id'] for t in tasks):
                raise ValueError(f"Task ID {data['task_id']} already exists")
                
            tasks.append(data)
            self._save_tasks(tasks)
            return json.dumps({
                "status": "success",
                "task": data,
                "timestamp": datetime.now().isoformat()
            })
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {str(e)}")

    def get_task(self, task_id: int) -> str:
        tasks = self._load_tasks()
        task = next((t for t in tasks if t['task_id'] == task_id), None)
        if not task:
            raise ValueError(f"Task ID {task_id} not found")
        return json.dumps(task)

    def get_all_tasks(self) -> str:
        return json.dumps(self._load_tasks())

    def update_task_status(self, input_json: str) -> str:
        try:
            data = json.loads(input_json)
            if not all(k in data for k in ["task_id", "status"]):
                raise ValueError("Missing task_id or status")
            
            if data['status'] not in self.VALID_STATUSES:
                raise ValueError(f"Status must be one of: {self.VALID_STATUSES}")

            tasks = self._load_tasks()
            for i, task in enumerate(tasks):
                if task['task_id'] == data['task_id']:
                    tasks[i]['status'] = data['status']
                    self._save_tasks(tasks)
                    return json.dumps({
                        "status": "success",
                        "updated_task": tasks[i]
                    })
            
            raise ValueError(f"Task ID {data['task_id']} not found")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {str(e)}")

    def delete_task(self, task_id: int) -> str:
        tasks = self._load_tasks()
        remaining = [t for t in tasks if t['task_id'] != task_id]
        
        if len(remaining) == len(tasks):
            raise ValueError(f"Task ID {task_id} not found")
            
        self._save_tasks(remaining)
        return json.dumps({
            "status": "success",
            "deleted_task_id": task_id,
            "remaining_tasks": len(remaining)
        })
