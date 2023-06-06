class Task:
    id = 0
    ask_timestamp = 0
    task_duration = 0
    def __init__(self,id , ask_timestamp,task_duration):
        self.id = id
        self.task_duration = task_duration
        self.ask_timestamp = ask_timestamp

