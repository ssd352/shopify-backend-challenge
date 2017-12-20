from GraphBuilder import JsonGraphBuilder
from DFS import DFS
from MenuReader import MenuReader


def challenge(n):
    mr = MenuReader(n)
    gb = JsonGraphBuilder()
    while mr.has_next():
        gb.build(mr.get_next())
    gr = gb.graph
    # print(gr.values())
    dfs = DFS(gr)
    print(dfs.topological_sort())
    print()


if __name__ == "__main__":
    challenge(1)
    challenge(2)
