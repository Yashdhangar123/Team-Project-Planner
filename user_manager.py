import json
import os
from datetime import datetime
from typing import Dict, List
from base.user_base import UserBase

class UserManager(UserBase):
    def __init__(self, db_path: str = "db/users.json"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        if not os.path.exists(self.db_path) or os.path.getsize(self.db_path) == 0:
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_users(self) -> List[Dict]:
        with open(self.db_path, 'r', encoding='utf-8-sig') as f:  # <== changed here
            return json.load(f)

    def _save_users(self, users: List[Dict]) -> None:
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)

    def create_user(self, input_json: str) -> str:
        try:
            data = json.loads(input_json)
            if not all(k in data for k in ["user_id", "name"]):
                raise ValueError("Missing required fields: user_id and name")
            
            users = self._load_users()
            if any(u['user_id'] == data['user_id'] for u in users):
                raise ValueError(f"User ID {data['user_id']} exists")
                
            users.append(data)
            self._save_users(users)
            return json.dumps({
                "status": "success",
                "user": data,
                "timestamp": datetime.now().isoformat()
            })
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")

    def get_user(self, user_id: int) -> str:
        users = self._load_users()
        user = next((u for u in users if u['user_id'] == user_id), None)
        if not user:
            raise ValueError(f"User ID {user_id} not found")
        return json.dumps(user)

    def get_all_users(self) -> str:
        return json.dumps(self._load_users())

    def update_user(self, input_json: str) -> str:
        try:
            data = json.loads(input_json)
            if "user_id" not in data:
                raise ValueError("Missing user_id field")

            users = self._load_users()
            for i, user in enumerate(users):
                if user['user_id'] == data['user_id']:
                    users[i].update(data)
                    self._save_users(users)
                    return json.dumps({
                        "status": "success",
                        "updated_user": users[i]
                    })
            
            raise ValueError(f"User ID {data['user_id']} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")

    def delete_user(self, user_id: int) -> str:
        users = self._load_users()
        new_users = [u for u in users if u['user_id'] != user_id]
        
        if len(new_users) == len(users):
            raise ValueError(f"User ID {user_id} not found")
            
        self._save_users(new_users)
        return json.dumps({
            "status": "success",
            "deleted_user_id": user_id,
            "remaining_users": len(new_users)
        })
