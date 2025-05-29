from abc import ABC, abstractmethod

class TeamBase(ABC):
    @abstractmethod
    def create_team(self, input_json: str) -> str:
        pass
    
    @abstractmethod
    def get_team(self, team_id: int) -> str:
        pass
    
    @abstractmethod
    def get_all_teams(self) -> str:
        pass
    
    @abstractmethod
    def update_team(self, input_json: str) -> str:
        pass
    
    @abstractmethod
    def delete_team(self, team_id: int) -> str:
        pass