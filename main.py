from GraphBuilder import JsonGraphBuilder
from DFS import DFS
from MenuReader import MenuReader


def challenge(n):
    mr = MenuReader(n)
    gb = JsonGraphBuilder()
    gb.build(mr.get_menus())
    gr = gb.graph
    # print(gr.values())
    dfs = DFS(gr)
    # return dfs.output
    return dfs.json_format()


if __name__ == "__main__":
    print(challenge(1))
    print(challenge(2))
