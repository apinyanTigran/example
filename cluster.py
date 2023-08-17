import json
class Cluster:
    def __init__(self, min_instances, max_instances, up_check_interval, tasks_in_queue, down_check_interval,
                 up_next_check_interval,initial_instances):
        self.min_instances = min_instances
        self.max_instances = max_instances
        self.up_check_interval = up_check_interval
        self.tasks_in_queue = tasks_in_queue
        self.initial_instances = initial_instances
        self.down_check_interval = down_check_interval
        self.up_next_check_interval = up_next_check_interval
    
    @classmethod
    def clusterFromJSON(cls, file_path:str) -> str:
        try:
        
            with open(file_path) as f:
                config = json.load(f)
                return Cluster(**config)
        except FileNotFoundError:
            print(f'Error: JSON file {file_path} not found')
        except json.JSONDecodeError:
            print(f'Error: Invalid JSON file {file_path}')

    
