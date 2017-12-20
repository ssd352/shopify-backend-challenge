class Visitor:
    def visit(self, node):
        pass


class DFS(Visitor):
    PERMANENT = 'p'

    def __init__(self, graph):
        self.sorted_nodes = []
        self.valid_menus = []
        self.invalid_menus = []
        self.graph = graph
        self.marks = {}

    def __json_format(self):
        output = {"valid_menus": [], "invalid_menus": []}
        for item in self.valid_menus:
            output["valid_menus"].append({"root_id": item[0], "children": item[1:]})
        for item in self.invalid_menus:
            output["invalid_menus"].append({"root_id": item[0], "children": item[1:]})
        return output

    def topological_sort(self):
        for node_id in self.graph:
            if node_id not in self.marks:
                self.sorted_nodes = []
                valid = self.visit(node_id)
                if valid:
                    self.valid_menus.append(list(self.sorted_nodes[::-1]))
                else:
                    self.invalid_menus.append(list(self.sorted_nodes[::-1]))
        return self.__json_format()

    def visit(self, node_id):
        if node_id in self.marks:
            if self.marks[node_id] == 'p':
                return True
            elif self.marks[node_id] == 't':
                self.sorted_nodes.append(node_id)
                return False
                # Cycle Detected
        else:
            self.marks[node_id] = 't'
            b = True
            for neighbor in self.graph[node_id].child_ids:
                b = b and self.visit(neighbor)
            self.marks[node_id] = 'p'
            self.sorted_nodes.append(node_id)
            return b
