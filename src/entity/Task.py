from datetime import datetime


class Task:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, id: int, title: str, description: str,
                 category: str, date_exp: str,
                 priority: str, status: str = "Не выполнена"):
        self.id, self.title = id, title
        self.description, self.category = description, category
        self.date_exp, self.priority = self.validate_date(date_exp), priority
        self.status = status

    @staticmethod
    def validate_date(date_str: str) -> str:

        try:
            datetime.strptime(date_str, Task.DATE_FORMAT)
            return date_str
        except ValueError:
            raise ValueError(f"Дата должна быть в формате {Task.DATE_FORMAT}, получено: '{date_str}'")

    def __repr__(self):
        return (f"Task(id={self.id}, title={self.title}, description={self.description}, "
                f"category={self.category}, data_exp={self.date_exp}, priority={self.priority})")
