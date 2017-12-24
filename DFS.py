# class Visitor:
#     def visit(self, node):
#         pass
import json


class DFS:
    PERMANENT = 'p'
    TEMPORARY = 't'

    def __init__(self, graph):
        self.__sorted_nodes = []
        self.__valid_menus = []
        self.__invalid_menus = []
        self.__graph = graph
        self.__marks = {}
        self.__output = {}

    @property
    def output(self):
        self.__topological_sort()
        self.__output = {"valid_menus": [], "invalid_menus": []}
        for item in self.__valid_menus:
            self.__output["valid_menus"].append({"root_id": item[0], "children": item[1:]})
        for item in self.__invalid_menus:
            self.__output["invalid_menus"].append({"root_id": item[0], "children": item[1:]})
        return dict(self.__output)

    def json_format(self):
        return json.dumps(dict(self.output))

    def __topological_sort(self):
        for node_id in self.__graph:
            # Run DFS and topological sort on each root node
            if self.__graph[node_id].is_root:
                self.__sorted_nodes = []
                valid = self.__visit(node_id)
                # Child nodes are sorted
                if valid:
                    self.__valid_menus.append(sorted(self.__sorted_nodes[::-1]))
                else:
                    self.__invalid_menus.append(sorted(self.__sorted_nodes[::-1]))

    def __visit(self, node_id):
        # print("current node is", node_id)
        if node_id in self.__marks:
            if self.__marks[node_id] == 'p':
                # print("current node is", node_id)
                return True
            elif self.__marks[node_id] == 't':
                # print("current node is", node_id)
                self.__sorted_nodes.append(node_id)
                return False
                # Cycle Detected
        else:
            self.__marks[node_id] = 't'
            # b = all(self.visit(neighbor) for neighbor in self.graph[node_id].child_ids)
            b = True
            for neighbor in self.__graph[node_id].child_ids:
                tmp = self.__visit(neighbor)
                b = b and tmp
            self.__marks[node_id] = 'p'
            self.__sorted_nodes.append(node_id)
            return b
