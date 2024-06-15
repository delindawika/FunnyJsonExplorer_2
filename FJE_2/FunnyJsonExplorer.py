import argparse
import json
from Style import TreeStyleStrategy, RectangleStyleStrategy
from Icon import PokerFaceIconStrategy, MoonsunIconStrategy
from Container import Container
from Leaf import Leaf

class FunnyJsonExplorer:
    """
    A class to explore and visualize JSON data using various styles and icons.
    """
    def __init__(self, style: str, icon: str):
        self.json_data = None
        self.style = style
        self.icon = icon
        self.max_width = 0
        self.root = None
        self.print_list = []

    def load(self, file_name: str):
        """Load JSON data from a specified file."""
        with open(file_name, 'r') as json_file:
            self.json_data = json.load(json_file)
        self.build_json_tree()

    def build_json_tree(self):
        if self.style == "tree":
            self.style=TreeStyleStrategy()
        elif self.style == "rectangle":
            self.style= RectangleStyleStrategy()
        if self.icon == "poker-face":
            self.icon= PokerFaceIconStrategy()
        elif self.icon == "moon-sun":
            self.icon= MoonsunIconStrategy()

        self.icon.set_icons(self.icon)

        self.max_width = self.get_max_width(self.json_data)
        self.root = self.parse_json(self.json_data)

    def get_max_width(self, data, level=0):
        if isinstance(data, dict):
            max_width = max([len(key) + self.get_max_width(value, level + 1) for key, value in data.items()], default=0)
            return max_width + 4
        elif isinstance(data, list):
            max_width = max([self.get_max_width(item, level + 1) for item in data], default=0)
            return max_width + 4
        elif isinstance(data, str):
            return len(data) + 4
        return 0

    def parse_json(self, data):
        if isinstance(data, dict):
            container = Container(self.icon, '', '')
            for key, value in data.items():
                child = self.parse_json(value)
                child.key = key
                container.add(child)
            return container
        else:
            return Leaf(self.icon, "", str(data))

    def show(self):
        print_list = []
        iterator = self.root.iter
        while iterator.has_next():
            is_last = len(iterator.children) == 1
            component = iterator.next()
            print_line = component.draw(self.style, "", self.max_width, is_last)
            print_list += print_line
        new_print_list = []
        for index,l in enumerate(print_list):
            if index==0:
                for i,s in enumerate(l):
                    if s=="├":
                        l = l[:i]+"┌─"+l[i+2:]
                    elif s=="┤":
                        l = l[:i-1]+"─┐"+l[i+1:]
            elif index==len(print_list)-1:
                for i,s in enumerate(l):
                    if i==0 and s=="│":
                        l = l[:i]+"└─"+l[i+2:]
                    elif s=="│" or s=="├":
                        l = l[:i-1]+"─┴─"+l[i+2:]
                    elif s=="┤":
                        l = l[:i-1]+"─┘"+l[i+1:]
            new_print_list.append(l)
        self.print_list = new_print_list
        for line in self.print_list:
            print(line)


def main():
    parser = argparse.ArgumentParser(description="Process a JSON file with style and icon options.")
    parser.add_argument('-f', '--file', required=True, help="Path to the JSON file")
    parser.add_argument('-s', '--style', choices=['tree', 'rectangle'], default='tree', help="Visualization style")
    parser.add_argument('-i', '--icon', choices=['poker-face', 'moon-sun'], default='poker-face', help="Icon family for visualization")
    
    args = parser.parse_args()

    fje = FunnyJsonExplorer(args.style, args.icon)
    fje.load(args.file)
    fje.show()

if __name__ == "__main__":
    main()
