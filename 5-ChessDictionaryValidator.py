# Build the board
horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
vertical = [1, 2, 3, 4, 5, 6, 7, 8]
boardNumbers = []
for h in range(len(horizontal)):
    for v in range(len(vertical)):
        boardNumber = str(vertical[v]) + horizontal[h]
        boardNumbers.append(boardNumber)

# print(boardNumbers)

# Build the chess pieces
chessPieceNames = ['bking', 'wking', 'bqueen', 'wqueen', 'bknight', 'wknight', 'bbishop', 'wbishop', 'bpawn', 'wpawn']

chessPieceNumbers = [1, 1, 1, 1, 2, 2, 2, 2, 8, 8]

chessPieces = {}

for i, chessPieceName in enumerate(chessPieceNames):
    for j, chessPieceNumber in enumerate(chessPieceNumbers):
        if (i == j):
            chessPieces.setdefault(chessPieceName, chessPieceNumber)

# print(chessPieces)

def isValidChessBoard(board):

    # Check board numbers
    for key in board.keys():
        if key not in boardNumbers:
            print(key + ' is not in chess board')
            return False

    # Check board pieces
    for value in board.values():
        if value not in chessPieces:
            print(value + ' is not in chess pieces')
            return False

    # Get the pieces of the board along with the count
    boardValues = list(board.values())
    boardValuesCount = {}

    for boardValue in boardValues:
        boardValuesCount.setdefault(boardValue, 0)
        boardValuesCount[boardValue] = boardValuesCount[boardValue] + 1

    # print(boardValuesCount)

    # Check board pieces count to be less than or equal to chess pieces
    for chessPieceKey, chessCount in chessPieces.items():
        for boardPieceKey, boardCount in boardValuesCount.items():
            if (chessPieceKey == boardPieceKey and boardCount > chessCount):
                print(boardPieceKey + ' has more than ' + str(chessCount) + ' piece(s)')
                return False

    return True

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '2c': 'wpawn', '5g': 'wpawn'}

print(isValidChessBoard(chessBoard))