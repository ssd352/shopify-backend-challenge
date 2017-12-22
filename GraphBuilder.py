import json


class GraphNode:
    def __init__(self, node_id, data, child_ids, is_root=False):
        self.neighbors = []
        self.node_id = node_id
        self.data = data
        self.is_root = is_root
        self.child_ids = list(child_ids)

    def __str__(self):
        return '{{"id": {}, "data": {}, "child_ids": {}, "is_root": {}}}'.format(self.node_id, self.data,
                                                                                 str(self.child_ids), self.is_root)

    def __repr__(self):
        return '{{"id": {}, "data": {}, "child_ids": {}, "is_root": {}}}'.format(self.node_id, self.data,
                                                                                 str(self.child_ids), self.is_root)

    # def accept(self, visitor):
    #     visitor.visit(self)

    # def add_neighbor(self, another_node):
    #     self.neighbors.append(another_node)


class GraphBuilder:
    def build(self, obj):
        pass


class JsonGraphBuilder(GraphBuilder):
    """
    This class adds
    """
    def __init__(self):
        self.__graph = {}
        # self.__visitor = None

    @property
    def graph(self):
        return dict(self.__graph)

    # @visitor.setter
    # def visitor(self, visitor):
    #     self.__visitor = visitor

    def accept(self, visitor):
        for node in self.node_map.values():
            node.accept(visitor)

    def build(self, json_obj):
        for item in json_obj:
            node_id = item["id"]
            data = item["data"]
            child_ids = item["child_ids"]
            if "parent_id" in item:
                self.__graph[item["id"]] = GraphNode(node_id=node_id, child_ids=child_ids, data=data, is_root=False)
            else:
                self.__graph[item["id"]] = GraphNode(node_id=node_id, child_ids=child_ids, data=data, is_root=True)
            # print(self.node_map)


if __name__ == "__main__":
    gb = JsonGraphBuilder()
    j = json.loads('[{"id": 1, "data": "House", "child_ids": [3]}, {"id": 2, "data": "Company", "child_ids": [4, 5, 8]}, {"id": 3, "data": "Living Room", "parent_id": 1, "child_ids": [7]}, {"id": 4, "data": "Meeting Rooms", "parent_id": 2, "child_ids": []}, {"id": 5, "data": "Kitchen", "parent_id": 2, "child_ids": [6]}, {"id": 6, "data": "Oven", "parent_id": 5, "child_ids": []}, {"id": 7, "data": "Table", "parent_id": 3, "child_ids": [15]}, {"id": 8, "data": "HR", "parent_id": 2, "child_ids": []}, {"id": 9, "data": "Computer", "child_ids": [10, 11, 12]}, {"id": 10, "data": "CPU", "parent_id": 9, "child_ids": []}, {"id": 11, "data": "Motherboard", "parent_id": 9, "child_ids": []}, {"id": 12, "data": "Peripherals", "parent_id": 9, "child_ids": [13, 14]}, {"id": 13, "data": "Mouse", "parent_id": 12, "child_ids": []}, {"id": 14, "data": "Keyboard", "parent_id": 12, "child_ids": []}, {"id": 15, "data": "Chair", "parent_id": 7, "child_ids": [1]}]')
    gb.build(j)
    print(gb.graph)

    gb = JsonGraphBuilder()
    j = json.loads('[{"id": 1, "data": "House", "child_ids": [3, 4]}, {"id": 2, "data": "Company", "child_ids": [8, 9, 11]}, {"id": 3, "data": "Kitchen", "parent_id": 1, "child_ids": [5, 18]}, {"id": 4, "data": "Living Room", "parent_id": 1, "child_ids": [6, 7, 19]}, {"id": 5, "data": "Sink", "parent_id": 3, "child_ids": []}, {"id": 6, "data": "TV", "parent_id": 4, "child_ids": []}, {"id": 7, "data": "Chair", "parent_id": 4, "child_ids": [20]}, {"id": 8, "data": "Meeting Rooms", "parent_id": 2, "child_ids": []}, {"id": 9, "data": "Kitchen", "parent_id": 2, "child_ids": [10]}, {"id": 10, "data": "Oven", "parent_id": 9, "child_ids": []}, {"id": 11, "data": "HR", "parent_id": 2, "child_ids": []}, {"id": 12, "data": "Computer", "child_ids": [13, 14, 15]}, {"id": 13, "data": "CPU", "parent_id": 12, "child_ids": []}, {"id": 14, "data": "Motherboard", "parent_id": 12, "child_ids": []}, {"id": 15, "data": "Peripherals", "parent_id": 12, "child_ids": [16, 17, 21]}, {"id": 16, "data": "Mouse", "parent_id": 15, "child_ids": []}, {"id": 17, "data": "Keyboard", "parent_id": 15, "child_ids": []}, {"id": 18, "data": "Chair", "parent_id": 3, "child_ids": []}, {"id": 19, "data": "Table", "parent_id": 4, "child_ids": []}, {"id": 20, "data": "Pad", "parent_id": 7, "child_ids": [1]}, {"id": 21, "data": "Headphones", "parent_id": 15, "child_ids": []}]')
    gb.build(j)
