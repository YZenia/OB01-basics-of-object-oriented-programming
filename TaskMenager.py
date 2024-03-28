from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = "не выполнено"

    def mark_as_done(self):
        self.status = "выполнено"

    def __str__(self):
        return f"Описание: {self.description}, Срок выполнения: {self.due_date}, Статус: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()

    def get_current_tasks(self):
        return [task for task in self.tasks if task.status == "не выполнено"]

# Пример использования
manager = TaskManager()
manager.add_task("Купить молоко", datetime.now())
manager.add_task("Позвонить маме", datetime.now())
print("Текущие задачи:")
for task in manager.get_current_tasks():
    print(task)
manager.mark_task_as_done("Купить молоко")
print(f"Текущие задачи после выполнения одной из них:")
for task in manager.get_current_tasks():
    print(task)
