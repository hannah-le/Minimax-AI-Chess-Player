def GenBoard(board):
    # Create a dictionary for all players i.e. {"Black Knight: 21"}

    # Get position of white players
    empty_board = [0] * 64
    display_board = []
    for i in range(0, 64):
        if i % 2 == 0:
            display_board += ['#']
        else:
            display_board += ['_']

    white_player = GetPlayerPositions(board, 10)  # List of all white player positions
    black_player = GetPlayerPositions(board, 20)  # List of all black player positions

    for i in white_player:
        empty_board[i] = board[i]
        display_board[i] = board[i]
    for i in black_player:
        empty_board[i] = board[i]
        display_board[i] = board[i]

    row_0 = display_board[:7]
    row_1 = display_board[8:15]
    row_2 = display_board[16:23]
    row_3 = display_board[24:31]
    row_4 = display_board[32:39]
    row_5 = display_board[40:47]
    row_6 = display_board[48:55]
    row_7 = display_board[56:63]

    print(row_0)
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print(row_5)
    print(row_6)
    print(row_7)


def GetPlayerPositions(board, player):
    pos = []
    white_pos = [10, 11, 12, 13, 14, 15]
    black_pos = [20, 21, 22, 23, 24, 25]
    for i in range(0, 64):
        if board[i] in white_pos and player == 10:
            pos += [i]
        if board[i] in black_pos and player == 20:
            pos += [i]
    return pos


def isEnemy(piece, move):
    white = [10, 11, 12, 13, 14, 15]
    black = [20, 21, 22, 23, 24, 25]
    if piece in white and move in black:
        return True
    if piece in black and move in white:
        return True
    else:
        return False


def IsValidSpot(piece, move):  # piece, move: integer values of the piece. move = board[new_position]
    white = [10, 11, 12, 13, 14, 15]
    black = [20, 21, 22, 23, 24, 25]
    if piece in white and move not in white:
        return True
    if piece in black and move not in black:
        return True
    else:
        return False


def GetPieceLegalMoves(board, position):
    # Create a dictionary of all pieces and its according value
    # Check position number against dictionary to determine what piece it is
    # Get Legal moves
    # Assume that white at the bottom
    white = [10, 11, 12, 13, 14, 15]
    black = [20, 21, 22, 23, 24, 25]
    pawns = [10, 20]
    pawns_left_edge = [8, 16, 24, 32, 40, 48]
    pawns_right_edge = [15, 23, 31, 39, 47, 55, 63]
    knight = [11, 21]
    bishop = [12, 22]
    rook = [13, 23]
    queen = [14, 24]
    king = [15, 25]
    piece = board[position]
    legal_pos = []

    # PAWNS
    if piece in pawns:
        if position - 8 in range(0,64):
            if piece == 10 and board[position - 8] not in white:
                legal_pos += [position - 8]
                if position - 9 in range(64):
                    if board[position - 9] not in white and position not in pawns_left_edge:
                        legal_pos += [position - 9]
                if position - 7 in range(64):
                    if board[position - 7] not in white and position not in pawns_right_edge:
                        legal_pos += [position - 7]

        if position + 8 in range(0,64):
            if piece == 20 and board[position + 8] not in black:
                legal_pos += [position + 8]
                if position + 9 in range(0,64):
                    if board[position + 9] not in black and position not in pawns_right_edge:
                        legal_pos += [position + 9]
                if position + 7 in range(0,64):
                    if board[position + 7] not in black and position not in pawns_left_edge:
                        legal_pos += [position + 7]


    # KNIGHT           Note: Fix order of if statements
    if piece in knight:
        row = position // 8
        col = position % 8

        top_left = position - 17
        # Make sure knight only lands on unoccupied square or its enemy
        if top_left in range(0,64):
            if IsValidSpot(piece, board[top_left]):
                top_left_position = [top_left // 8, top_left % 8]  # row, col
                if top_left_position[0] == row - 2 and top_left_position[1] == col - 1:
                    legal_pos += [top_left]

        top_right = position - 15
        if top_right in range(0,64):
            if IsValidSpot(piece, board[top_right]):
                top_right_position = [top_right // 8, top_right % 8]
                if top_right_position[0] == row - 2 and top_right_position[1] == col + 1:
                    legal_pos += [top_right]

        right_up = position - 10
        if right_up in range(0,64):
            if IsValidSpot(piece, board[right_up]):
                right_up_position = [right_up // 8, right_up % 8]
                if right_up_position[0] == row - 1 and right_up_position[1] == col - 2:
                    legal_pos += [right_up]

        right_down = position + 6
        if right_down in range(0,64):
            if IsValidSpot(piece, board[right_down]):  # Spot is valid if it's not the same color OR empty
                right_down_pos = [right_down // 8, right_down % 8]
                if right_down_pos[0] == row + 1 and right_down_pos[1] == col - 2:
                    legal_pos += [right_down]

        left_up = position - 6
        if left_up in range(0,64):
            if IsValidSpot(piece, board[left_up]):
                left_up_pos = [left_up // 8, left_up % 8]
                if left_up_pos[0] == row - 1 and left_up_pos[1] == col + 2:
                    legal_pos += [left_up]

        left_down = position + 10
        if left_down in range(0,64):
            if IsValidSpot(piece, board[left_down]):
                left_down_pos = [left_down // 8, left_down % 8]
                if left_down_pos[0] == row + 1 and left_down_pos[1] == col + 2:
                    legal_pos += [left_down]

        bottom_left = position + 15
        if bottom_left in range(0, 64):
            if IsValidSpot(piece, board[bottom_left]):
                bottom_left_pos = [bottom_left // 8, bottom_left % 8]
                if bottom_left_pos[0] == row + 2 and bottom_left_pos[1] == col - 1:
                    legal_pos += [bottom_left]

        bottom_right = position + 17
        if bottom_right in range(0,64):
            if IsValidSpot(piece, board[bottom_right]):
                bottom_right_pos = [bottom_right // 8, bottom_right % 8]
                if bottom_right_pos[0] == row + 2 and bottom_right_pos[1] == col + 1:
                    legal_pos += [bottom_right]

    # ROOK
    if piece in rook or piece in queen:
        top = position
        down = position
        left = position
        right = position

        row = position // 8
        col = position % 8

        i = 1

        while i <= row:  # Count spaces above
            if IsValidSpot(piece, board[top - 8]):
                if top - 8 in range(0, 64):
                    legal_pos += [top - 8]
                    top -= 8
            i += 1

        j = 1
        while j <= 7 - row: # Count spaces below
            if IsValidSpot(piece, board[down + 8]):
                if down + 8 in range(0,64):
                    legal_pos += [down + 8]
                    down += 8
            j += 1

        k = 1
        while k <= col: # Count spaces to the left
            if IsValidSpot(piece, board[left - 1]):
                if left - 1 in range(0,64):
                    legal_pos += [left - 1]
                    left -= 1
            k += 1

        f = 1
        while f <= 7 - col: # Count spaces to the right
            if IsValidSpot(piece, board[right + 1]):
                if right + 1 in range(0,64):
                    legal_pos += [right + 1]
                    right += 1
            f += 1

    # BISHOP
    if piece in bishop or piece in queen:
        col = position % 8
        UL = position # - 9
        DL = position # + 7
        UR = position # - 7
        DR = position # + 9

        #Add the appropriate number to UL, UR, DL, DR
        i = 1
        while i <= col: # Count spaces to the left of the column --> UL, DL
            if UL - 9 in range(0,64):
                if IsValidSpot(piece, board[UL - 9]):
                    legal_pos += [UL - 9]
                    UL -= 9
            if DL + 7 in range(0, 64):
                if IsValidSpot(piece, board[DL + 7]):
                    legal_pos += [DL + 7]
                    DL += 7
            i += 1

        j = 1
        while j <= (7 - col) : # Count spaces to the right of the column --> UR, DR
            if UR - 7 in range(0, 64):
                if IsValidSpot(piece, board[UR - 7]):
                    legal_pos += [UR - 7]
                    UR -= 7
            if DR + 9 in range(0,64):
                if IsValidSpot(piece, board[DR + 9]):
                    legal_pos += [DR + 9]
                    DR += 9
            j += 1

    if piece in king:
        UL = position  # - 9
        DL = position  # + 7
        UR = position  # - 7
        DR = position  # + 9
        top = position
        down = position
        left = position
        right = position
        row = position // 8
        col = position % 8

        i = 1
        if i <= col: #--> UL, DL, Left
            if UL - 9 in range(0,64):
                if IsValidSpot(piece, board[UL - 9]):
                    legal_pos += [UL - 9]
            if DL + 7 in range(0, 64):
                if IsValidSpot(piece, board[DL + 7]):
                    legal_pos += [DL + 7]
            if left - 1 in range(0,64):
                if IsValidSpot(piece, board[left - 1]):
                        legal_pos += [left - 1]

        if i <= 7 - col: # --> DR, UR, right
            if UR - 7 in range(0, 64):
                if IsValidSpot(piece, board[UR - 7]):
                    legal_pos += [UR - 7]
            if DR + 9 in range(0,64):
                if IsValidSpot(piece, board[DR + 9]):
                    legal_pos += [DR + 9]
            if right + 1 in range(0,64):
                if IsValidSpot(piece, board[right - 1]):
                        legal_pos += [right - 1]

        if i <= row: #top
            if top - 8 in range(0, 64):
                if IsValidSpot(piece, board[top - 8]):
                    legal_pos += [top - 8]

        if i <= 7 - row: #bottom
            if down + 8 in range(0,64):
                if IsValidSpot(piece, board[down + 8]):
                    legal_pos += [down + 8]

    return legal_pos

def IsPositionUnderThreat(board, position, player):
    white = [10, 11, 12, 13, 14, 15]
    black = [20, 21, 22, 23, 24, 25]

    for i in range(0, 64):
        if player == 20 and board[i] in white:
            val = GetPieceLegalMoves(board, board[i])
            if val != None:
                if position in val:
                    return True
                    break

        if player == 10 and board[i] in black:
            val = GetPieceLegalMoves(board, board[i])
            if val != None:
                if position in val:
                    return True
                    break

    return False

