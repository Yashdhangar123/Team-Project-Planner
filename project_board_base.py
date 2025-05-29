from abc import ABC, abstractmethod

class ProjectBoardBase(ABC):
    @abstractmethod
    def create_task(self, input_json: str) -> str:
        pass
    
    @abstractmethod
    def get_task(self, task_id: int) -> str:
        pass
    
    @abstractmethod
    def get_all_tasks(self) -> str:
        pass
    
    @abstractmethod
    def update_task_status(self, input_json: str) -> str:
        pass
    
    @abstractmethod
    def delete_task(self, task_id: int) -> str:
        pass