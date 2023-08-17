from typing import Self
import json
import argparse
class Task:
    
    def __init__(self, id, task_timestamp,task_duration):

        self.id = id
        self.task_duration = task_duration
        self.task_timestamp = task_timestamp
    
    @classmethod
    def taskListFromJSON(cls, file_path: str) -> list[Self]:
        try:

            with open(file_path) as f:
                config = json.load(f)
            tasks = []
            for task_data in config['tasks']:
                task = cls(**task_data)
                tasks.append(task)
            return tasks
        except FileNotFoundError:
            print(f'Error: JSON file {file_path} not found')
        except json.JSONDecodeError:
            print(f'Error: Invalid JSON file {file_path}')
   
        # parse JSON path and return object list
       
