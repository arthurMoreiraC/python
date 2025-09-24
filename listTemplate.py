
from abc import ABC, abstractmethod

class list(ABC):

    @abstractmethod
    def __init__(self):
        self.tasks = [False] * 100
        pass
    
    @abstractmethod
    def setTask(self, callback, index):
        self.tasks[index] = callback
    
    @abstractmethod
    def execTask(self, index):
        if self.tasks[index]:
            self.tasks[index]()
