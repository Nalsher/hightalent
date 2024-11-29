import json
from typing import List
from xml.dom import NotFoundErr

from src.repositories.AbstractRepository import TaskRepositoryInterface
from src.entity.Task import Task


class MockTaskRepository(TaskRepositoryInterface):

    def __init__(self, json_file: str):
        self.json_file = json_file
        self._load_tasks()

    def _load_tasks(self) -> bool:
        try:
            with open(self.json_file, "r") as file:
                file_data = json.load(file)
                self.tasks = [Task(**task) for task in file_data]
        except FileNotFoundError:
            self.tasks = []

    def _save_tasks(self) -> bool:
        with open(self.json_file, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def create_task(self, task: Task) -> None:
        for i in self.tasks:
            if i.id == task.id:
                raise ValueError
        self.tasks.append(task)
        self._save_tasks()

    def delete_task_by_id(self, task_id: int | None = None) -> bool:
        task_to_delete_by_id = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_delete_by_id:
            self.tasks.remove(task_to_delete_by_id)
            self._save_tasks()
            return True
        else:
            return False

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_all_tasks_by_category(self, task_category: str) -> List[Task]:
        tasks = [task for task in self.tasks if task.category == task_category]
        return tasks

    def find_task_by_id(self, task_id: int) -> Task:
        try:
            task_to_get = next((task for task in self.tasks if task.id == task_id), None)
            return task_to_get
        except:
            raise NotFoundErr

    def find_task_by_category(self, task_category: str) -> Task:
        try:
            task_to_get = next((task for task in self.tasks if task.category == task_category), None)
            return task_to_get
        except:
            raise NotFoundErr

    def find_task_by_keyword(self, task_keyword: str) -> Task:
        try:
            task_to_get = next((task for task in self.tasks if task_keyword in task.description), None)
            return task_to_get
        except:
            raise NotFoundErr

    def find_task_by_status(self, task_status: str) -> Task:
        try:
            task_to_get = next((task for task in self.tasks if task.status == task_status), None)
            return task_to_get
        except:
            raise NotFoundErr

    def update_task_title(self, task_id: int, new_title: str) -> bool:
        try:
            task_to_update = next((task for task in self.tasks if task.id == task_id), None)
            task_to_update.title = new_title
            self._save_tasks()
            return True
        except:
            raise NotFoundErr

    def update_task_status(self, task_id: int, new_status: str ) -> bool:
        try:
            task_to_update = next((task for task in self.tasks if task.id == task_id), None)
            task_to_update.status = new_status
            self._save_tasks()
            return True
        except:
            raise NotFoundErr

    def update_task_description(self, task_id: int, new_description: str) -> bool:
        try:
            task_to_update = next((task for task in self.tasks if task.id == task_id), None)
            task_to_update.description = new_description
            self._save_tasks()
            return True
        except:
            raise NotFoundErr
