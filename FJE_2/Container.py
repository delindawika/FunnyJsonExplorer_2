from Style import StyleStrategy
from Icon import IconStrategy
from Iterator import ContainerIterator

class Container():
    def __init__(self, icon: IconStrategy, key: str, value: str) -> None:
        self.key = key
        self.value = value 
        self.icon = icon.container_icon
        self.iter = ContainerIterator()
    
    def add(self, component) -> None:
        self.iter.children.append(component)
    
    def draw(self, style: StyleStrategy, prefix: str, max_width: int, is_last: bool) -> list:
        print_list = []
        print_line, next_prefix = style.draw_container(self.icon, self.key, prefix, max_width, is_last)
        print_list += print_line
        while self.iter.has_next():
            is_last = len(self.iter.children) == 1
            component = self.iter.next()
            print_line = component.draw(style, next_prefix, max_width, is_last)
            print_list += print_line
        return print_list
