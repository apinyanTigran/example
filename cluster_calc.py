import json
from cluster import Cluster

with open('cluster_config.json', 'r') as f:
    data = json.load(f)

cluster = Cluster(data["min_instances"], data["max_instances"], data["up_check_interval"], data["tasks_in_queue"],
                  data["down_check_interval"], data["up_next_check_interval"])
