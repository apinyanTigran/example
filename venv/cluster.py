class Cluster:
    min_instances = 0
    max_instances = 0
    up_check_interval = 0
    tasks_in_queue = 0
    down_check_interval = 0
    up_next_check_interval = 0

    initial_instances = 3
    start_duration = 0

    def __init__(self, min_instances, max_instances, up_check_interval, tasks_in_queue, down_check_interval,
                 up_next_check_interval):
        self.min_instances = min_instances
        self.max_instances = max_instances
        self.up_check_interval = up_check_interval
        self.tasks_in_queue = tasks_in_queue
        self.down_check_interval = down_check_interval
        self.up_next_check_interval = up_next_check_interval
