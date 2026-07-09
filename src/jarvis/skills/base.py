from abc import ABC, abstractmethod


class Skill(ABC):

    @property
    @abstractmethod
    def intent(self):
        pass

    @abstractmethod
    def execute(self, understanding):
        pass
