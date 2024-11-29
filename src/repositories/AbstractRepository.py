from abc import ABC, abstractmethod
from src.entity.Task import Task
from typing import List


class TaskRepositoryInterface(ABC):

    @abstractmethod
    def create_task(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_task_by_id(self, task_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_all_tasks(self) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def get_all_tasks_by_category(self, task_category: str) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def find_task_by_category(self, task_category: str) -> Task:
        raise NotImplementedError

    @abstractmethod
    def find_task_by_id(self, task_id: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    def find_task_by_keyword(self, task_keyword: str) -> Task:
        raise NotImplementedError

    @abstractmethod
    def find_task_by_status(self, task_status: str) -> Task:
        raise NotImplementedError

    @abstractmethod
    def update_task_status(self, task_id: int, new_status: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update_task_description(self, task_id: int, new_description: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update_task_title(self, task_id: int, new_title: str) -> bool:
        raise NotImplementedError
