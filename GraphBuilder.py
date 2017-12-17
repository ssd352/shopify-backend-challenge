import json


class GraphNode:
    def __init__(self, node_id, data, child_ids):
        self.neighbors = []
        self.node_id = node_id
        self.data = data
        self.child_ids = list(child_ids)

    def __str__(self):
        return '{"id": {}, "data": {}, "child_ids": {}}'.format(self.node_id, self.data, str(self.child_ids))

    # def __repr__(self):
    #     return '{"id": {}, "data": {}, "child_ids": {}}'.format(self.node_id, self.data, repr(self.child_ids))

    # def add_neighbor(self, another_node):
    #     self.neighbors.append(another_node)


class GraphBuilder:
    pass


class JsonGraphBuilder(GraphBuilder):
    """
    This class adds
    """
    def __init__(self):
        self.node_map = {}

    def build(self, json_obj):
        for item in json_obj["menus"]:
            node_id = item["id"]
            data = item["data"]
            child_ids = item["child_ids"]
            self.node_map[item["id"]] = GraphNode(node_id=node_id, child_ids=child_ids, data=data)


if __name__ == "__main__":
    j = json.loads('{"menus": [{"id": 1, "data": "House", "child_ids": [3]}, {"id": 2, "data": "Company", "child_ids": [4, 5, 8]}, {"id": 3, "data": "Living Room", "parent_id": 1, "child_ids": [7]}, {"id": 4, "data": "Meeting Rooms", "parent_id": 2, "child_ids": []}, {"id": 5, "data": "Kitchen", "parent_id": 2, "child_ids": [6]}], "pagination": {"current_page": 1, "per_page": 5, "total": 15}}')
    gb = JsonGraphBuilder()
    gb.build(j)
