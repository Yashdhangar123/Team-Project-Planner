from abc import ABC, abstractmethod

class UserBase(ABC):
    @abstractmethod
    def create_user(self, input_json: str) -> str:
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> str:
        pass
    
    @abstractmethod
    def get_all_users(self) -> str:
        pass
    
    @abstractmethod
    def update_user(self, input_json: str) -> str:
        pass
    
    @abstractmethod
    def delete_user(self, user_id: int) -> str:
        pass