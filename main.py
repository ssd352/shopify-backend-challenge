from GraphBuilder import JsonGraphBuilder
from DFS import DFS
from MenuReader import MenuReader


if __name__ == "__main__":
    mr = MenuReader()
    gb = JsonGraphBuilder()
    while mr.has_next():
        gb.build(mr.get_next())
    gr = gb.graph
    dfs = DFS(gr)
    print(dfs.topological_sort())
    # print('valids are', valids, 'invalids are', invalids)
