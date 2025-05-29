import json
import os
from typing import Dict, List
from base.team_base import TeamBase

class TeamManager(TeamBase):
    def __init__(self, db_path: str = "db/teams.json", user_db_path: str = "db/users.json"):
        self.db_path = db_path
        self.user_db_path = user_db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        if not os.path.exists(self.db_path) or os.path.getsize(self.db_path) == 0:
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_teams(self) -> List[Dict]:
        with open(self.db_path, 'r', encoding='utf-8-sig') as f:  # <== changed here
            return json.load(f)

    def _save_teams(self, teams: List[Dict]) -> None:
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(teams, f, indent=2, ensure_ascii=False)

    def create_team(self, input_json: str) -> str:
        try:
            data = json.loads(input_json)
            if not all(k in data for k in ["team_id", "name", "members"]):
                raise ValueError("Missing required fields: team_id, name, members")
            
            teams = self._load_teams()
            if any(t['team_id'] == data['team_id'] for t in teams):
                raise ValueError(f"Team ID {data['team_id']} already exists")
                
            teams.append(data)
            self._save_teams(teams)
            return json.dumps({"status": "success", "team": data})
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")

    def get_team(self, team_id: int) -> str:
        teams = self._load_teams()
        team = next((t for t in teams if t['team_id'] == team_id), None)
        if not team:
            raise ValueError(f"Team ID {team_id} not found")
        return json.dumps(team)

    def get_all_teams(self) -> str:
        return json.dumps(self._load_teams())

    def update_team(self, input_json: str) -> str:
        try:
            data = json.loads(input_json)
            if "team_id" not in data:
                raise ValueError("Missing team_id field")
            
            teams = self._load_teams()
            for i, team in enumerate(teams):
                if team['team_id'] == data['team_id']:
                    teams[i].update(data)
                    self._save_teams(teams)
                    return json.dumps({"status": "success", "team": teams[i]})
            
            raise ValueError(f"Team ID {data['team_id']} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")

    def delete_team(self, team_id: int) -> str:
        teams = self._load_teams()
        remaining = [t for t in teams if t['team_id'] != team_id]
        
        if len(remaining) == len(teams):
            raise ValueError(f"Team ID {team_id} not found")
            
        self._save_teams(remaining)
        return json.dumps({"status": "success", "deleted_team_id": team_id})
