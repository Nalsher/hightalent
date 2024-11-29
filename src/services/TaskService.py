from src.repositories.AbstractRepository import TaskRepositoryInterface
from src.entity.Task import Task


class TaskService:
    def __init__(self, repository: TaskRepositoryInterface):
        self.repository = repository

    def create_task(self, task_id: int, task_title: str, task_description: str,
                    task_category: str, task_date: str, task_priority: str) -> None:

        new_task = Task(id=task_id, title=task_title, description=task_description,
                        category=task_category, date_exp=task_date, priority=task_priority)
        self.repository.create_task(new_task)

    def delete_task(self, task_id: int | None = None) -> bool:
        if task_id:
            self.repository.delete_task_by_id(task_id)

    def find_task(self, task_id: str | None = None, task_keyword: str | None = None,
                  task_status: str | None = None, task_category: str | None = None) -> Task:

        if task_category:
            return self.repository.find_task_by_category(task_category)

        if task_id:
            return self.repository.find_task_by_id(int(task_id))

        if task_keyword:
            return self.repository.find_task_by_keyword(task_keyword)

        if task_status:
            return self.repository.find_task_by_status(task_status)

    def update_task(self, task_id: int | None = None, task_title: str | None = None,
                    task_description: str | None = None, task_status: str | None = None) -> bool:
        if task_title:
            return self.repository.update_task_title(task_id, task_title)

        if task_description:
            return self.repository.update_task_description(task_id, task_description)

        if task_status:
            return self.repository.update_task_status(task_id, task_status)

    def find_all_tasks(self):
        return self.repository.get_all_tasks()

    def find_all_tasks_by_category(self, task_category: str):
        return self.repository.get_all_tasks_by_category(task_category)
