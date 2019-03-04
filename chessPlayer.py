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
