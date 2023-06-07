import json
import argparse


from cluster import Cluster
from Task import Task

parser = argparse.ArgumentParser(description="cluster task prediction")

parser.add_argument('--cluster', help='path to the cluster configuration JSON file')
parser.add_argument('--tasks', help='path to the task configuration JSON file')
parser.add_argument('--output', help='path to the output JSON file')

args = parser.parse_args()
clusterConfigP = args.cluster
taskConfigP = args.tasks
outputFileP = args.output
def main (clusterConfigP,taskConfigP):
    cluster = read_cluster_config(clusterConfigP)

    tasks = read_task_config(taskConfigP)
    
def read_cluster_config(file_path):
    with open(file_path) as f:
        config = json.load(f)
    print(config)
    return Cluster(**config)

def read_task_config(file_path):
    with open(file_path) as f:
        config = json.load(f)
    tasks = []
    for task_data in config['tasks']:
        task = Task(**task_data)
        tasks.append(task)
    print(tasks)
    return tasks


main(clusterConfigP,taskConfigP)



