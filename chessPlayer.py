from tree import *
from rule import *

def opponent(player):
    if player == 10:
        return 20
    if player == 20:
        return 10

def GenNewBoard(board, currentPos, newPos):
    newBoard = list(board)
    newBoard[newPos] = board[currentPos]
    newBoard[currentPos] = 0

    return newBoard

def GenerateChildren(node, player):
    white = [10,11,12,13,14,15]
    black = [20,21,22,23,24,25]
    board = node.store[0]
    white_pos = GetPlayerPositions(board, 10)
    black_pos = GetPlayerPositions(board, 20)

    if player == 10:
        for currentPos in white_pos:
            # print("currentPos")
            # print(currentPos)
            white_legal = GetPieceLegalMoves(board, currentPos)
            # print(white_legal)
            for newPos in white_legal:
                node.AddSuccessor(Tree(GenNewBoard(board, currentPos, newPos)))

    if player == 20:
        for currentPos in black_pos:
            white_legal = GetPieceLegalMoves(board, currentPos)
            for newPos in white_legal:
                node.AddSuccessor(Tree(GenNewBoard(board, currentPos, newPos)))

    return node

def TreeDeepening(board, player):
    GameTree = Tree(board)
    node = GenerateChildren(GameTree, player) # Depth 1 - PLAYER'S BOARD
    for child in node.store[1]:
        GenerateChildren(child, opponent(player)) # Depth 2 - OPPONENT'S BOARD
        for i in child.store[1]:
            GenerateChildren(i, player) # Depth 3 - PLAYER'S BOARD
            # for j in i.store[1]:
            #     GenerateChildren(j, opponent(player)) # Depth 4
            #     for k in j.store[1]:
            #         GenerateChildren(k, player) # Depth 5
            #         for f in k.store[1]:
            #             GenerateChildren(f, opponent(player)) # Depth 6
            #             for l in f.store[1]:
            #                 GenerateChildren(l, player) # Depth 7

    return GameTree

def findNewPosition(board, best): # Find difference between two boards TESTED!
    move = []
    for i in range(64):
        if board[i] != 0 and best[i] == 0:
            original_position = i
            move += [original_position]

    for i in range(64):
        if board[i] != board[move[0]] and best[i] == board[move[0]]:
                new_position = i
                move += [new_position]
    return move

def chessPlayer(board, player):
    status = True
    evalTree = TreeDeepening(board, player)
    candidateMoves = []

    # GET MOVE
    if player == 10:
        evalTree.store[2] = minimax(evalTree, depth=evalTree.get_depth(), alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True)
        best = bestBoard(evalTree, 10)
        move = findNewPosition(board, best)
        if len(move) == 0:
            status = False

        for child in evalTree.store[1]:
            child.store[2] = minimax(child, depth=child.get_depth(), alpha=float("-inf"), beta=float("inf"), maximizingPlayer=False)
            newMove = findNewPosition(board, child.store[0])
            candidateMoves += [[newMove] + [child.store[2]]]

        return [status, move, candidateMoves, evalTree]

    if player == 20:
        evalTree.store[2] = minimax(evalTree, depth=evalTree.get_depth(), alpha=float("-inf"), beta=float("inf"), maximizingPlayer=False)
        best = bestBoard(evalTree, 20)
        move = findNewPosition(board, best)
        if len(move) == 0:
            status = False

        for child in evalTree.store[1]:
            child.store[2] = minimax(child, depth=child.get_depth(), alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True)
            newMove = findNewPosition(board, child.store[0])
            candidateMoves += [[newMove] + [child.store[2]]]

        return [status, move, candidateMoves, evalTree]








'''

PSEUDOCODE:

* name: chessPlayer
* return values: the 4-list [ status, move, candidateMoves, evalTree]
* arguments: board, player

where: status = True when the function succeeded
                False when the function can not compute a move
                      due to some error condition

       move is a 2-list that consists of two numbers between 0 and 63
        move[0] is the location of the piece chessPlayer intends to move
        move[1] is the location on the board that chessPlayer intends to
                move the aforementioned piece (at move[0]) to

       candidateMoves is a list of 2-lists where:
         candidateMoves[i][0] is a 2-list corresponding to a move
         candidateMoves[i][1] is some floating point number that is a measure
                           of how good or bad the move
                           candidateMoves[i][0] is
         candidateMoves MUST include "move"
         e.g., [ [[1, 5], 0.5],
                 [[10, 25], 0.25],
                 [[63, 0], 0.75] ]
         is a list of three candidate moves.

       evalTree can be:
           * None if you did not use a tree to evaluate potential cases
           * a tree if you did use a tree to evaluate potential cases.
             If you used a tree, return that tree via this return value.
             Specifically, return a LIST that is the level order traversal
             of your tree.


'''










# def GetNodesAtLevel(root, k): #k = distance from root
#     if root.store[0] == [] and root.store[1] == []:
#         return None
#     if root.store[1] == []:
#         return [Tree(root.store[0])]
#     else:
#         lst = []
#         for node in root.store[1]:
#             lst += GetNodesAtLevel(node, k - 1)
#         return lst # a list of nodes

