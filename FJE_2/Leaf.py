from Style import StyleStrategy
from Icon import IconStrategy

class Leaf():
    def __init__(self, icon: IconStrategy, key: str, value: str) -> None:
        self.key = key
        self.icon = icon.leaf_icon
        self.value = value
    
    def draw(self, style: StyleStrategy, prefix: str, max_width: int, is_last: bool) -> list:
        print_line, _ = style.draw_leaf(self.icon, self.key, self.value, prefix, max_width, is_last)
        return print_line