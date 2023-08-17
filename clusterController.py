from collections import deque
import time

from clock import Clock
from task import Task
import cluster


class Server:
    def __init__(self) -> None:
       
        self.task = None
        self.timeWhenStartedToWork = None
    
    
    def takeTask(self, task:Task,time:int) -> None:
        self.timeWhenStartedToWork = time
        self.task = task
    

    
    def isBusy(self,time:int) -> bool:
        return self.task and time <(self.timeWhenStartedToWork + self.task.task_duration )

class Controller:
    def __init__(self,cluster: cluster.Cluster, tasks:list[Task]) -> None:
        self.cluster = cluster
        self.taskQueue = deque(tasks)
        self.serversList = [Server() for _ in range(cluster.initial_instances)]
        self.clock = Clock()
        self.output = []
       

   
    def waitTillEnd(self)->None:
        newServerlist = [a for a in self.serversList if a.isBusy(self.clock.time)  ]
        newServerlist = sorted(newServerlist ,key=lambda x: x.timeWhenStartedToWork + x.task.task_duration)
        for server in newServerlist:
            self.registerOutput(server.task.id,server.task.task_timestamp,(server.timeWhenStartedToWork + server.task.task_duration))
        print(self.output)
    def registerOutput(self,id:int,task_timestamp:int,finish_timestamp:int) -> None:
        dic = {"id":id,
               "task_timestamp":task_timestamp,
               "finish_timestamp":finish_timestamp}
        self.output.append(dic)
       
    
   

    def clusterScaleing():
        pass

    def allocateTasks(self) -> None:

        if not self.taskQueue:
            print("i have no tasks in queue left")
            self.waitTillEnd()
            return
            

        if self.taskQueue[0].task_timestamp > self.clock.time:
            print(f"{self.taskQueue[0].id} is waiting for his place")
            self.clock.setTime(self.taskQueue[0].task_timestamp)

        for i, server in enumerate(self.serversList):
            if server.task and self.clock.time <(server.timeWhenStartedToWork + server.task.task_duration ):
                print(f"server #{i+1} is busy")
                continue
            if server.task:
                self.registerOutput(server.task.id,server.task.task_timestamp,(server.timeWhenStartedToWork + server.task.task_duration))

            server.takeTask(self.taskQueue.popleft(),self.clock.time)
            print(f"server #{i+1} recived new task #{server.task.id}")
            break
        else:
            self.clock.advance(1)
        
        self.allocateTasks()

    
