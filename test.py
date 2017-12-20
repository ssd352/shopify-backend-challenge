from GraphBuilder import JsonGraphBuilder
from DFS import DFS
import json


if __name__ == "__main__":
    json_obj = json.loads("""{
  "menus":[
    {
      "id":1,
      "data":"House",
      "child_ids":[3]
    },
    {
      "id":2,
      "data":"Company",
      "child_ids":[4]
    },
    {
      "id":3,
      "data":"Kitchen",
      "parent_id":1,
      "child_ids":[5]
    },
    {
      "id":4,
      "data":"Meeting Room",
      "parent_id":2,
      "child_ids":[6]
    },
    {
      "id":5,
      "data":"Sink",
      "parent_id":3,
      "child_ids":[1]
    },
    {
      "id":6,
      "data":"Chair",
      "parent_id":4,
      "child_ids":[]
    }
  ]}""")
    gb = JsonGraphBuilder()
    gb.build(json_obj)
    gr = gb.graph
    dfs = DFS(gr)
    # valids, invalids = dfs.topological_sort()
    print(dfs.topological_sort())
