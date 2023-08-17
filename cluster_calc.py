#!/opt/homebrew/bin/python3 

import json
import argparse
import pathlib

from cluster import Cluster
from task import Task
from clusterController import Controller

# setting up CLI
parser = argparse.ArgumentParser(description="cluster task prediction")
parser.add_argument('--cluster', help = 'path to the cluster configuration JSON file')
parser.add_argument('--tasks', help = 'path to the task configuration JSON file')

# reciveing arguments
args = parser.parse_args()
##clusterConfigP = args.cluster
##taskConfigP = args.tasks 
clusterConfigP = "cluster_config.json"
taskConfigP = "tasks.json" 
def clusterPrediction(clusterConfigP,taskConfigP):
    cluster = Cluster.clusterFromJSON(clusterConfigP)

    tasks = Task.taskListFromJSON(taskConfigP) #DONT forget this is a list of class type 'Task'
    tasks = sorted(tasks, key=lambda x: x.task_timestamp)

    controller = Controller(cluster, tasks)
    controller.allocateTasks()
   


if __name__ == "__main__":
    clusterPrediction(clusterConfigP,taskConfigP)
