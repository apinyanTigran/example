import json
import argparse


from cluster import Cluster
from Task import Task

parser = argparse.ArgumentParser(description="cluster task prediction")

parser.add_argument('--cluster', help = 'path to the cluster configuration JSON file')
parser.add_argument('--tasks', help = 'path to the task configuration JSON file')
parser.add_argument('--output', help = 'path to the output JSON file')

args = parser.parse_args()
clusterConfigP = args.cluster
taskConfigP = args.tasks
outputFileP = args.output
def main (clusterConfigP,taskConfigP):
    cluster = read_cluster_config(clusterConfigP)

    tasks = read_task_config(taskConfigP)
    
def read_cluster_config(file_path):

         try:
        
            with open(file_path) as f:
                config = json.load(f)
                return Cluster(**config)
         except FileNotFoundError:
            print(f'Error: JSON file {file_path} not found')
         except json.JSONDecodeError:
            print(f'Error: Invalid JSON file {file_path}')
   

def read_task_config(file_path):
    try:

        with open(file_path) as f:
            config = json.load(f)
        tasks = []
        for task_data in config['tasks']:
            task = Task(**task_data)
            tasks.append(task)
        return tasks
    except FileNotFoundError:
            print(f'Error: JSON file {file_path} not found')
    except json.JSONDecodeError:
            print(f'Error: Invalid JSON file {file_path}')
   


main(clusterConfigP,taskConfigP)



