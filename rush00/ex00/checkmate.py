def checkmate(board):
    # print("k" not in board)
    if (board.count("k") + board.count("K")) > 1:
        print("Too much king")
        return
   
    if "k" not in board and "K" not in board:
        print("No King krub nong")
        return
    
    board = board.strip("\n").split("\n")
    # print(len(board), len(board[0]))
    for i in range(len(board)):
        if (len(board) != len(board[i])):
            print("Invalid board")
            return
    kPositionX, kPositionY = None, None
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'K' or board[row][col] == 'k':
                # kPositionX = row
                # kPositionY = col
                kPositionX = col
                kPositionY = row
    # print(kPositionX, kPositionY)
    # king -> 1, 1

    # ------------------------------------ PAWN CHECK ------------------------------------
    # check if bottom corner left of king or bottom corner right of king is p or P
    pawnAvaliablePosition1 = (kPositionX - 1, kPositionY + 1)
    pawnAvaliablePosition2 = (kPositionX + 1, kPositionY + 1)
    
    # if (kPositionX > 0 or kPositionX < len(board[0]) - 1 )and kPositionY != len(board) - 1 : 

    x1, y1 = pawnAvaliablePosition1
    if 0 <= x1 < len(board) and 0 <= y1 < len(board): # dont allow negative index
        if board[y1][x1] in ("p", "P"):
            print("Success")
            return

    x2, y2 = pawnAvaliablePosition2
    if 0 <= x2 < len(board) and 0 <= y2 < len(board):
        if board[y2][x2] in ("p", "P"):
            print("Success")
            return
    # ------------------------------------ QUEEN ROOK CHECK ------------------------------------
    # col changes
    for xRight in range(kPositionX + 1, len(board)):
        piece = board[kPositionY][xRight]
        if piece != ".": # prevent blocking
            # K P R found pawn break
            if piece.upper() in ("R","Q"):
                print("Success")
                return
            break

    for xLeft in range(kPositionX - 1, -1, -1):
        piece = board[kPositionY][xLeft]
        if piece != ".": # prevent blocking
            if piece.upper() in ("R","Q"):
                print("Success")
                return
            break

    # rows changes
    for yDown in range(kPositionY + 1, len(board)):
        piece = board[yDown][kPositionX]
        if piece != ".":
            if piece.upper() in ("R", "Q"):
                print("Success")
                return
            break
    for yUp in range(kPositionY - 1, -1, -1):
        piece = board[yUp][kPositionX]
        if piece != ".":
            if piece.upper() in ("R", "Q"):
                print("Success")
                return
            break
    # ------------------------------------ BISHOP QUEEN CHECK ------------------------------------
    n = len(board)
    x, y = kPositionX + 1, kPositionY + 1
    while 0 <= x < n and 0 <= y < n:
        piece = board[y][x]
        if piece != ".":
            if piece.upper() in ("B", "Q"):
                print("Success")
                return
            break
        x += 1
        y += 1

    # down-left
    x, y = kPositionX - 1, kPositionY + 1
    while 0 <= x < n and 0 <= y < n:
        piece = board[y][x]
        if piece != ".":
            if piece.upper() in ("B", "Q"):
                print("Success")
                return
            break
        x -= 1
        y += 1

    # up-right
    x, y = kPositionX + 1, kPositionY - 1
    while 0 <= x < n and 0 <= y < n:
        piece = board[y][x]
        if piece != ".":
            if piece.upper() in ("B", "Q"):
                print("Success")
                return
            break
        x += 1
        y -= 1

    # up-left
    x, y = kPositionX - 1, kPositionY - 1
    while 0 <= x < n and 0 <= y < n:
        piece = board[y][x]
        if piece != ".":
            if piece.upper() in ("B", "Q"):
                print("Success")
                return
            break
        x -= 1
        y -= 1

    print("Fail")

            