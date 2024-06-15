from abc import ABC, abstractmethod

class IconStrategy(ABC):
    def __init__(self) -> None:
        self.container_icon = None
        self.leaf_icon = None
    
    @abstractmethod
    def set_icons(icon_name:str=None) -> None:
        pass

class PokerFaceIconStrategy(IconStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def set_icons(self, icon_name: str = None) -> None:
        self.container_icon = '♢'
        self.leaf_icon = '♧'

class MoonsunIconStrategy(IconStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def set_icons(self, icon_name: str = None) -> None:
        self.container_icon = '☾'
        self.leaf_icon = '☼'
