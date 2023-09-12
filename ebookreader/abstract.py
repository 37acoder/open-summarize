from abc import ABC, abstractmethod
from text.basic import Text


class Index:
    def __init__(self, index:dict) -> None:
        self.index = index

    @abstractmethod
    def iter():
        yield ["Part", "Section"], Text("")


class Ebook(ABC):
    @abstractmethod
    def index(self) -> Index: 
        pass
