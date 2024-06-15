from abc import ABC, abstractmethod
from typing import List, Union


class StyleStrategy(ABC):
    @abstractmethod
    def draw_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) -> Union[List[str], str]:
        pass

    @abstractmethod
    def draw_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) -> Union[List[str], str]:
        pass



class TreeStyleStrategy(StyleStrategy):
    def draw_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) -> Union[List[str], str]:
        connector = "└─" if is_last else "├─"
        print_line = f"{prefix}{connector}{icon}{key}"
        extension = "   " if is_last else "│  "
        return [print_line], prefix + extension

    def draw_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) -> Union[List[str], str]:
        connector = "└─" if is_last else "├─"
        if value == 'None':
            print_line = f"{prefix}{connector}{icon}{key}"
        else:
            print_line = f"{prefix}{connector}{icon}{key}: {value}"
        return [print_line], ''  # Changed from tuple to individual return values



class RectangleStyleStrategy(StyleStrategy):
    def draw_container(self, icon: str, key: str, prefix: str, max_width: int, is_last: bool) -> Union[list,str]:
        line = f"{'├─'}{icon}{key} {'─' * (max_width - len(prefix) - len(key) - len('├─') - 2)}{'─┤'}"
        print_line = f"{prefix}{line}"
        extension = f"{'│'}  "
        return [print_line],prefix+extension

    def draw_leaf(self, icon: str, key: str, value: str, prefix: str, max_width: int, is_last: bool) -> Union[list,str]:
        if value == 'None':
            line = f"{'├─'}{icon}{key} {'─' * (max_width-len(prefix)-len(key)-len('├─')-2)}{'─┤'}"
            print_line = f"{prefix}{line}"
        else:
            line = f"{'├─'}{icon}{key}: {value} {'─' * (max_width - len(prefix) - len(key) - len('├─') - len(value) - 4)}{'─┤'}"
            print_line = f"{prefix}{line}"
        return [print_line],''
