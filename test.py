from tree import *
from chessPlayer import *


def main():
    original = [23, 21, 22, 24, 25, 22, 21, 23,
             20, 20, 20, 20, 20, 20, 20, 20,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             10, 10, 10, 10, 10, 10, 10, 10,
             13, 11, 12, 14, 15, 12, 11, 13]

    black_1 = [23, 21, 22, 24, 25, 22, 21, 23,
             20, 20, 20, 20, 20, 20, 20, 20,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 10, 0, 0, 0, 0,
             10, 10, 10, 0, 10, 10, 10, 10,
             13, 11, 12, 14, 15, 12, 11, 13]

    black_2 = [23, 21, 22, 24, 25, 22, 21, 23,
               20, 20, 20, 20, 20, 20, 20, 20,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 11, 0, 0, 0, 0, 0,
               10, 10, 10, 10, 10, 10, 10, 10,
               13, 0, 12, 14, 15, 12, 11, 13]

    white_11 = [23, 21, 22, 24, 25, 22, 21, 23,
             20, 20, 20, 0, 20, 20, 20, 20,
             0, 0, 0, 20, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 10, 0, 0, 0, 0,
             10, 10, 10, 0, 10, 10, 10, 10,
             13, 11, 12, 14, 15, 12, 11, 13]

    white_12 = [23, 0, 22, 24, 25, 22, 21, 23,
               20, 20, 20, 20, 20, 20, 20, 20,
               0, 0, 21, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 10, 0, 0, 0, 0,
               10, 10, 10, 0, 10, 10, 10, 10,
               13, 11, 12, 14, 15, 12, 11, 13]

    white_21 = [23, 0, 22, 24, 25, 22, 21, 23,
               20, 20, 20, 20, 20, 20, 20, 20,
               21, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 11, 0, 0, 0, 0, 0,
               10, 10, 10, 10, 10, 10, 10, 10,
               13, 0, 12, 14, 15, 12, 11, 13]

    white_22 = [23, 21, 22, 24, 25, 22, 21, 23,
               0, 20, 20, 20, 20, 20, 20, 20,
               20, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 11, 0, 0, 0, 0, 0,
               10, 10, 10, 10, 10, 10, 10, 10,
               13, 0, 12, 14, 15, 12, 11, 13]


    GameTree = Tree(original)
    node_black_1 = Tree(black_1)
    node_black_2 = Tree(black_2)
    node_white_11 = Tree(white_11)
    node_white_12 = Tree(white_12)
    node_white_21 = Tree(white_21)
    node_white_22 = Tree(white_22)

    node_black_1.AddSuccessor(node_white_11)
    node_black_1.AddSuccessor(node_white_12)
    node_black_2.AddSuccessor(node_white_21)
    node_black_2.AddSuccessor(node_white_22)
    GameTree.AddSuccessor(node_black_1)
    GameTree.AddSuccessor(node_black_2)

    # white_pos = GetPlayerPositions(original, 10)
    # for pos in white_pos:
    #     print(pos)
    #     r = GetPieceLegalMoves(original, pos)
    #     print(r)
    #     for newPos in r:
    #
    #         print(GenNewBoard(original, pos, newPos))

    # print("GEN NEW BOARD: ")
    # rval = original
    # currentPos = 0
    # newPos = 16
    # print(GenNewBoard(rval, currentPos, newPos))
    # print(rval)


    #
    print("CHESS PLAYER: ")
    #
    # r = TreeDeepening(original, 10)
    #
    # r.Print_DepthFirst()

    rval = chessPlayer(original, 20)
    print(rval)
    print(len(rval[2]))

   #rval[3].Print_DepthFirst()
    # print("MINIMAX VALUE IS: ")
    # GameTree.store[2] = minimax(GameTree, depth=GameTree.get_depth(), alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True)
    # print(GameTree.store[2])
    #
    # node_lst = []
    # subnode_lst = []
    #
    # for node in GameTree.store[1]:
    #     print("NODE: ")
    #     print(node.store[0])
    #     node.store[2] =  minimax(node, depth=node.get_depth(), alpha=float("-inf"), beta=float("inf"), maximizingPlayer=False)
    #     node_lst += [node.store[2]]
    #     for subnode in node.store[1]:
    #         print("SUBNODES: ")
    #         print(subnode.store[0])
    #         subnode.store[2] = minimax(subnode, depth=subnode.get_depth(), alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True)
    #         subnode_lst += [subnode.store[2]]
    #
    # print("QUALITY OF NODES: ")
    # print(node_lst)
    #
    # print("QUALITY OF SUBNODES: ")
    # print(subnode_lst)
    #
    # print("BEST CANDIDATE MOVE FOR WHITE: ")
    # print(bestBoard(GameTree,10))
    # print(bestBoard(GameTree,10) == black_2)
    #
    # print("FIND NEXT MOVE: ")
    # print(findNewPosition(original, black_1))

    # print("NODES AT LEVEL 2: ")
    # leaves = GetNodesAtLevel(GameTree, 2) # List of nodes
    # leaves[0].AddSuccessor(Tree(white_11))
    # print(leaves[0].store[1])
    # print(len(leaves))

    # print("TREE STRUCTURE: ")
    # GameTree.Print_DepthFirst()
    # print("\n LEVEL ORDER TRAVERSAL: ")
    # GameTree.Get_LevelOrder()
    # print(GameTree.isGameOver())
    # print("\n DEPTH OF TREE IS: ")
    # print(GameTree.get_depth())
    # print("\n GET LEAVE NODES: ")
    # print(GameTree.getLeaveNodes())
    #
    # test_board = [0] * 64
    # test_board[8] = 10
    # print(boardEval(board))

main()