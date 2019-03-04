class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Tree:
    def __init__(self, x):
        self.store = [x, [], 0]

    def isEmpty(self):
        for i in self.store:
            if len(i) != 0:
                return False
        return True

    def AddSuccessor(self, x):
        self.store[1] = self.store[1] + [x]
        return True

    def Get_DepthFirst(self, prefix):
        print(prefix + str(self.store[0]))
        for i in self.store[1]:
            i.Get_DepthFirst(2 * prefix)
        return True

    def Print_DepthFirst(self):
        return self.Get_DepthFirst("   ")

    def Get_LevelOrder(self):
        lst = []
        x = Queue()
        x.enqueue(self.store)
        while not x.isEmpty():
            r = x.dequeue()
            lst.append(r[0])
            for i in r[1]:
                x.enqueue(i.store)
        print(lst)
        return lst

    def get_depth(self):
        if not self.store[1]:
            return 0

        max_val = 0
        for i in self.store[1]:
            d = i.get_depth()
            if d > max_val:
                max_val = d
        return max_val + 1

    def getLeaveNodes(self):
        if not self.store:
            return None
        if self.store[0] != [] and not self.store[1]:
            return [self.store[0]]
        else:
            lst = []
            for each in self.store[1]:
                lst += each.getLeaveNodes()
            return lst

    def isGameOver(self):
        king = [15,25]
        for piece in self.store[0]:
            if piece in king:
                return False

        print("\n CHECK MATE. GAME OVER!")
        return True

def findPieceIndex(board, piece):
    lst = []
    for i in range(64):
        if board[i] == piece:
            lst += [i]
    return lst

def boardEval(board):
    pawnEvalWhite = [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
        1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
        0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
        0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
        0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
        0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ]

    pawnEvalBlack = pawnEvalWhite[::-1]

    knightEval = [
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
        -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
        -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
        -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
        -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
        -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0
    ]

    bishopEvalWhite = [
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
        -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
        -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
        -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
        -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
        -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
        -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
    ]

    bishopEvalBlack = bishopEvalWhite[::-1]

    rookEvalWhite = [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0
    ]

    rookEvalBlack = rookEvalWhite[::-1]

    evalQueen = [
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
        -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
        -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
        -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
        0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
        -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
        -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0
    ]

    kingEvalWhite = [
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
        -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
        2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
        2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0
    ]

    kingEvalBlack = kingEvalWhite[::-1]

    '''
    Piece:   | Value:     | White's relative Strength:
    --------------------------------------------------
    Pawn:    | offset+0  |  + 10
    Knight:  | offset+1  |  + 30
    Bishop:  | offset+2  |  + 30
    Rook:    | offset+3  |  + 50
    Queen:   | offset+4  |  + 900
    King:    | offset+5  |  + 90

    '''

    sum = 0
    # Sum white pieces values
    for i in findPieceIndex(board,10):
        sum += pawnEvalWhite[i] * 10
    for i in findPieceIndex(board, 11):
        sum += knightEval[i] * 30
    for i in findPieceIndex(board, 12):
        sum += bishopEvalWhite[i] * 30
    for i in findPieceIndex(board, 13):
        sum += rookEvalWhite[i] * 50
    for i in findPieceIndex(board, 14):
        sum += evalQueen[i] * 900
    for i in findPieceIndex(board, 15):
        sum += kingEvalWhite[i] * 90

    # Sum black pieces values
    for i in findPieceIndex(board, 20):
        sum += pawnEvalBlack[i] * -10
    for i in findPieceIndex(board, 21):
        sum += knightEval[i] * -30
    for i in findPieceIndex(board, 22):
        sum += bishopEvalBlack[i] * -30
    for i in findPieceIndex(board, 23):
        sum += rookEvalBlack[i] * -50
    for i in findPieceIndex(board, 24):
        sum += evalQueen[i] * -900
    for i in findPieceIndex(board, 25):
        sum += kingEvalBlack[i] * -90

    return sum

def minimax(tree, depth, alpha, beta, maximizingPlayer):
    if tree.store[1] == [] or tree.isGameOver() or tree.get_depth() == 0:
        return boardEval(tree.store[0])

    elif maximizingPlayer == True and tree.store[1] != []:
        maxEval = float("-inf")

        for child in tree.store[1]:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)

            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        tree.store[2] = maxEval
        return maxEval

    elif maximizingPlayer == False and tree.store[1] != []:
        minEval = float("inf")
        for child in tree.store[1]:
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        tree.store[2] = minEval
        return minEval

def bestBoard(tree, player):
    if tree.store[1] == []:
        return tree.store[0]
    else:
        if player == 10:
            best = float("-inf")
            for child in tree.store[1]:
                if child.store[2] > best:
                    best = child.store[2]
                    value = child.store[0]

        if player == 20:
            best = float("inf")
            for child in tree.store[1]:
                if child.store[2] < best:
                    best = child.store[2]
                    value = child.store[0]
    return value