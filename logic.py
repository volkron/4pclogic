import random
import time

# This is used to validate moves so pieces do not go off the board.
keys = [
                   36,  37,  38,  39,  40,  41,  42,  43,
                   52,  53,  54,  55,  56,  57,  58,  59,
                   68,  69,  70,  71,  72,  73,  74,  75,
    81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94,
    97,  98,  99,  100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
    129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
    145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158,
    161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174,
    177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190,
    193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206,
                   212, 213, 214, 215, 216, 217, 218, 219,
                   228, 229, 230, 231, 232, 233, 234, 235,
                   244, 245, 246, 247, 248, 249, 250, 251
]

# Used for promotion.
promo = [2, 3, 4, 5]
promotion = [
    [81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94],
    [43,  59,  75,  91,  107, 123, 139, 155, 171, 187, 203, 219, 235, 251],
    [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206],
    [36,  52,  68,  84,  100, 116, 132, 148, 164, 180, 196, 212, 228, 244]
]

# The starting postion in 4pc.
start = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, [2, 4], [2, 2], [2, 3], [2, 6], [2, 5], [2, 3], [2, 2], [2, 4], 0, 0, 0, 0, 0, 0, 0, 0, [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [1, 4], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 4], 0,
    0, [1, 2], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 2], 0, 0, [1, 3], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 3], 0, 0, [1, 6], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 5], 0, 0, [1, 5], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 6], 0,
    0, [1, 3], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 3], 0, 0, [1, 2], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 2], 0, 0, [1, 4], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 4], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 0, 0, 0, 0, 0, 0, 0, 0, [0, 4], [0, 2], [0, 3], [0, 5], [0, 6], [0, 3], [0, 2], [0, 4], 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# Pawn start squares for double pawn moves.
starter = [52, 53, 54, 55, 56, 57, 58, 59, 82, 98, 114, 130, 146, 162, 178, 194, 93, 109, 125, 141, 157, 173, 189, 205, 228, 229, 230, 231, 232, 233, 234, 235]

# Basic directions on the 4pc board.
N, E, S, W = -16, 1, 16, -1

# This is used to help generate moves.
directions = [
    [N + W, N + E],
    [E + N, E + S],
    [N + N + E, E + N + E, E + S + E, S + S + E, S + S + W, W + S + W, W + N + W, N + N + W],
    [N + E, S + E, S + W, N + W],
    [N, E, S, W],
    [N, E, S, W, N + E, S + E, S + W, N + W],
    [N, E, S, W, N + E, S + E, S + W, N + W]
]

kings_locator = [246, 129, 39, 158]                      # Used to know where the king goes in the event of castling.
enpas_locator = [N, E, S, W, N + E, N + W, S + E, N + W] # Used to detect which pawn to remove in the event of an enpassant.

# Logic for the game.
class Position:
    def __init__(self, color, board, halfmoves, castling, enpassants, history):
        # intialize class vars.
        self.board = board
        self.color = color
        self.halfmoves = halfmoves
        self.castling = castling
        self.enpassants = enpassants
        self.history = history

    def drawed(self):
        # Is this position drawn.
        return self.stalemated() or self.repetition() or self.halfmoved()

    def ended(self):
        # Is the game over.
        return self.mated() or self.stalemated() or self.repetition() or self.halfmoved()

    def halfmoved(self):
        # Is this a halfmoves.
        return self.halfmoves > 49
    
    def checked(self, a = -1, b = -1):
        # is the current or specified color in check.
        x = 0
        if b != -1 and self.valid(b):
            for m, n in enumerate(self.board):
                return self.threat(m, b)
        else:
            if a == -1: a = self.color
            for o, p in enumerate(self.board):
                if p != 0 and p[0] == a and p[1] == 6:
                    x = 1
                    for q, r in enumerate(self.board):
                        return r != 0 and not self.opposite(a, r[0]) and self.threat(q, o)
        return x == 0
    
    def mated(self, a = -1):
        # Is the current or specified color mated.
        if a == -1: a = self.color
        return self.checked(a) and len(self.moves(a)) == 0

    def reset(self):
        # Reset the position to the start 4pc position.
        self.board = start
        self.color = 0
        self.castling = [[True, True, [249, 250], [247, 246, 245]], [True, True, [113, 97], [145, 161, 177]], [True, True, [38, 37], [40, 41, 42]], [True, True, [174, 190], [142, 126, 110]]]
        self.halfmoves = 0
        self.enpassants = []
        self.history = []

    def move(self, a):
        # Preform a move.
        m = (self.color + 1) % 4
        k = self.castling[:]
        h = self.halfmoves
        y = self.enpassants[:]
        t = self.board[:]
        r = self.history[:]
        if self.board[a[0]][1] == 0 or self.board[a[0]][1] == 1:
            t[a[1]] = t[a[0]]
            t[a[0]] = 0
            if len(a) > 2 and a[2] != -1: t[a[2]] == 0
            if len(a) > 3 and a[3] != -1: t[a[1]] = a[3]
            if len(a) > 4: y[self.color] = a[4]
            h = 0
        else:
            if t[a[1]] != 0: h = 0
            elif self.color == 0: h += 1
            t[a[1]] = t[a[0]]
            t[a[0]] = 0
            if t[a[1]][1] == 4 and (a == 244 or a == 193 or a == 43 or a == 94) and self.castling[self.color][0]: k[self.color][0] = False
            if t[a[1]][1] == 4 and (a == 251 or a == 81 or a == 36 or a == 206) and self.castling[self.color][1]: k[self.color][1] = False
            if t[a[1]][1] == 6 and (a == 248 or a == 129 or a == 39 or a == 158):
                k[self.color][0] = False
                k[self.color][1] = False
            if t[a[1]][1] == 6 and not self.threat(a[0], a[1]):
                swap = self.swap(a[1])
                t[swap[1]] = t[swap[0]]
                t[swap[0]] = 0
            y[self.color] = 0
        r.append([self.color, self.board, self.halfmoves, self.castling, self.enpassants])
        return Position(m, t, h, k, y, r)
            
    def moves(self, a = -1):
        # Get a list of avaliable moves.
        s, v, w, ww = [], [], 0, 0
        if a == -1: a = self.color
        for m, n in enumerate(self.board):
            if n != 0 and n[0] == a:
                for o, p in enumerate(self.board):
                    if not self.valid(o):
                        continue
                    if p == 0 and (n[1] != 0 and n[1] != 1) and self.threat(m, o):
                        s.append([m, o])
                    elif (n[1] == 0 or n[1] == 1) and self.threat(m, o) and self.enpassant(o, a):
                        if self.promotion(a, o):
                            for cc in promo: s.append([m, o, m + enpas_locator[a], cc])
                        else: s.append([m, o, m + enpas_locator[a]])
                    elif (n[1] == 0 or n[1] == 1) and o == m + enpas_locator[a] and p == 0:
                        if self.promotion(a, o):
                            for bb in promo: s.append([m, o, -1, bb])
                        else: s.append([m, o])
                    elif (n[1] == 0 or n[1] == 1) and o == m + (enpas_locator[a] * 2) and self.starter(m) and self.board[m + enpas_locator[a]] == 0:
                        if self.promotion(a, o):
                            for aa in promo: s.append([m, o, -1, aa, o - enpas_locator[a]])
                        else: s.append([m, o, -1, -1, o - enpas_locator[a]])
                    elif p != 0 and not self.opposite(p[0], a) and self.threat(m, o): s.append([m, o])
        for u in s:
            t = self.board[:]
            t[u[1]] = t[u[0]]
            t[u[0]] = 0
            if len(u) > 2:
                if u[2] != -1: t[u[2]] == 0
            if not self.checked(a):
                v.append(u)
        if self.castling[a][0] and not self.checked(a):
            for x in self.castling[a][2]:
                if self.board == 0:
                    for y, z in enumerate(self.board):
                        if self.threat(y, x):
                            w += 1
                            break
                    if w == 0: v.append([kings_locator[a], self.castling[a][2][1]])
        if self.castling[a][1] and not self.checked(a):
            for xx in self.castling[a][3]:
                if self.board == 0:
                    for yy, zz in enumerate(self.board):
                        if self.threat(yy, xx):
                            ww += 1
                            break
                    if ww == 0: v.append([kings_locator[a], self.castling[a][3][1]])
        return v

    def render(self):
        # Render the board.
        g = m = r = ""
        a = iter(self.board[:])
        for c in range(36): next(a)
        print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
        for d in range(3):
            for e in range(8):
                f = next(a)
                if f == 0: g += "     |"
                else: g += " " + str(f[0]) + "." + str(f[1]) + " |"
            if d < 2:
                for h in range(8): next(a)
            print("|-----|-----|-----|" + g + "-----|-----|-----|\n")
            print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
            g = ""
        for j in range(5): next(a)
        for k in range(8):
            for l in range(14):
                t = next(a)
                if t == 0: m += "     |"
                else: m += " " + str(t[0]) + "." + str(t[1]) + " |"
            if k < 7:
                for i in range(2): next(a)
            print("|" + m)
            print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
            m = ""
        for n in range(5): next(a)
        for o in range(3):
            for p in range(8):
                q = next(a)
                if q == 0: r += "     |"
                else: r += " " + str(q[0]) + "." + str(q[1]) + " |"
            if o < 2:
                for s in range(8): next(a)
            print("|-----|-----|-----|" + r + "-----|-----|-----|\n")
            print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
            r = ""

    def repetition(self):
        # Is this position drawn by repitition.
        b = 0
        for a in self.history:
            if a[0] == self.color and a[1] == self.board: b += 1
        return b == 2

    def stalemated(self, a = -1):
        # Is the current or specified locor stalemated.
        if a == -1: a = self.color
        return not self.checked(a) and len(self.moves(a)) == 0

    def undo(self):
        # Undo a played move.
        pos = self.history.pop()
        return Position(pos[0], pos[1], pos[2], pos[3], pos[4], self.history)

    def enpassant(self, b, a = -1):
        # Enpassant Helper.
        if a == -1: a = self.color
        if a == 0 or a == 2: return self.enpassants[1] == b or self.enpassants[3] == b
        if a == 1 or a == 3: return self.enpassants[0] == b or self.enpassants[2] == b

    def threat(self, a, b):
        # Used for move generation.
        if self.board[a] != 0 and self.valid(a) and self.valid(b):
            for d in directions[self.board[a][1]]:
                m = a + d
                n = m
                if self.board[a][1] == 3 or self.board[a][1] == 4 or self.board[a][1] == 5:
                    while self.valid(n):
                        if self.board[n] != 0 and n != b: break
                        if n == b: return True
                        n += d
                else:
                    if self.board[a][1] == 0 or self.board[a][1] == 1:
                        if self.board[a][0] == 2 or self.board[a][0] == 3: m = m - (d * 2)
                    if m == b: return True
        return False

    def opposite(self, a, b):
        # Determine whos on whos team.
        m = a
        if a != b: m = (a + 2) % 4
        if m != b: return False
        return True

    def promotion(self, a, b):
        # Promotion Helper.
        if b in promotion[a]: return True
        return False
        
    def starter(self, a):
        # Pawn Starter Helper.
        if a in starter: return True
        return False

    def swap(self, a):
        # Move Helper.
        if a == 246: return [244, 247]
        if a == 250: return [251, 249]
        if a == 97: return [81, 113]
        if a == 161: return [193, 145]
        if a == 37: return [36, 38]
        if a == 41: return [43, 40]
        if a == 126: return [94, 142]
        if a == 190: return [206, 174]
        return []

    def valid(self, a):
        # Used to prevent pieces from going off the board.
        if a in keys: return True
        return False

position = Position(0, start, 0, [[True, True, [249, 250], [247, 246, 245]], [True, True, [113, 97], [145, 161, 177]], [True, True, [38, 37], [40, 41, 42]], [True, True, [174, 190], [142, 126, 110]]], [0, 0, 0, 0], [])

x = 0
while x != 10:
    print("\n")
    print("Computer is thinking...\n")
    moves = position.moves()
    position = position.move(moves[random.randint(0, len(moves) - 0)])
    print("\n")
    position.render()
    print("\n")
    time.sleep(3)
    x += 1import random
import time

# This is used to validate moves so pieces do not go off the board.
keys = [
                   36,  37,  38,  39,  40,  41,  42,  43,
                   52,  53,  54,  55,  56,  57,  58,  59,
                   68,  69,  70,  71,  72,  73,  74,  75,
    81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94,
    97,  98,  99,  100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
    129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
    145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158,
    161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174,
    177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190,
    193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206,
                   212, 213, 214, 215, 216, 217, 218, 219,
                   228, 229, 230, 231, 232, 233, 234, 235,
                   244, 245, 246, 247, 248, 249, 250, 251
]

# Used for promotion.
promo = [2, 3, 4, 5]
promotion = [
    [81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94],
    [43,  59,  75,  91,  107, 123, 139, 155, 171, 187, 203, 219, 235, 251],
    [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206],
    [36,  52,  68,  84,  100, 116, 132, 148, 164, 180, 196, 212, 228, 244]
]

# The starting postion in 4pc.
start = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, [2, 4], [2, 2], [2, 3], [2, 6], [2, 5], [2, 3], [2, 2], [2, 4], 0, 0, 0, 0, 0, 0, 0, 0, [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [1, 4], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 4], 0,
    0, [1, 2], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 2], 0, 0, [1, 3], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 3], 0, 0, [1, 6], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 5], 0, 0, [1, 5], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 6], 0,
    0, [1, 3], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 3], 0, 0, [1, 2], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 2], 0, 0, [1, 4], [1, 1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [3, 1], [3, 4], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 0, 0, 0, 0, 0, 0, 0, 0, [0, 4], [0, 2], [0, 3], [0, 5], [0, 6], [0, 3], [0, 2], [0, 4], 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# Pawn start squares for double pawn moves.
starter = [52, 53, 54, 55, 56, 57, 58, 59, 82, 98, 114, 130, 146, 162, 178, 194, 93, 109, 125, 141, 157, 173, 189, 205, 228, 229, 230, 231, 232, 233, 234, 235]

# Basic directions on the 4pc board.
N, E, S, W = -16, 1, 16, -1

# This is used to help generate moves.
directions = [
    [N + W, N + E],
    [E + N, E + S],
    [N + N + E, E + N + E, E + S + E, S + S + E, S + S + W, W + S + W, W + N + W, N + N + W],
    [N + E, S + E, S + W, N + W],
    [N, E, S, W],
    [N, E, S, W, N + E, S + E, S + W, N + W],
    [N, E, S, W, N + E, S + E, S + W, N + W]
]

kings_locator = [246, 129, 39, 158]                      # Used to know where the king goes in the event of castling.
enpas_locator = [N, E, S, W, N + E, N + W, S + E, N + W] # Used to detect which pawn to remove in the event of an enpassant.

# Logic for the game.
class Position:
    def __init__(self, color, board, halfmoves, castling, enpassants, history):
        # intialize class vars.
        self.board = board
        self.color = color
        self.halfmoves = halfmoves
        self.castling = castling
        self.enpassants = enpassants
        self.history = history

    def drawed(self):
        # Is this position drawn.
        return self.stalemated() or self.repetition() or self.halfmoved()

    def ended(self):
        # Is the game over.
        return self.mated() or self.stalemated() or self.repetition() or self.halfmoved()

    def halfmoved(self):
        # Is this a halfmoves.
        return self.halfmoves > 49
    
    def checked(self, a = -1, b = -1):
        # is the current or specified color in check.
        x = 0
        if b != -1 and self.valid(b):
            for m, n in enumerate(self.board):
                return self.threat(m, b)
        else:
            if a == -1: a = self.color
            for o, p in enumerate(self.board):
                if p != 0 and p[0] == a and p[1] == 6:
                    x = 1
                    for q, r in enumerate(self.board):
                        return r != 0 and not self.opposite(a, r[0]) and self.threat(q, o)
        return x == 0
    
    def mated(self, a = -1):
        # Is the current or specified color mated.
        if a == -1: a = self.color
        return self.checked(a) and len(self.moves(a)) == 0

    def reset(self):
        # Reset the position to the start 4pc position.
        self.board = start
        self.color = 0
        self.castling = [[True, True, [249, 250], [247, 246, 245]], [True, True, [113, 97], [145, 161, 177]], [True, True, [38, 37], [40, 41, 42]], [True, True, [174, 190], [142, 126, 110]]]
        self.halfmoves = 0
        self.enpassants = []
        self.history = []

    def move(self, a):
        # Preform a move.
        m = (self.color + 1) % 4
        k = self.castling[:]
        h = self.halfmoves
        y = self.enpassants[:]
        t = self.board[:]
        r = self.history[:]
        if self.board[a[0]][1] == 0 or self.board[a[0]][1] == 1:
            t[a[1]] = t[a[0]]
            t[a[0]] = 0
            if len(a) > 2 and a[2] != -1: t[a[2]] == 0
            if len(a) > 3 and a[3] != -1: t[a[1]] = a[3]
            if len(a) > 4: y[self.color] = a[4]
            h = 0
        else:
            if t[a[1]] != 0: h = 0
            elif self.color == 0: h += 1
            t[a[1]] = t[a[0]]
            t[a[0]] = 0
            if t[a[1]][1] == 4 and (a == 244 or a == 193 or a == 43 or a == 94) and self.castling[self.color][0]: k[self.color][0] = False
            if t[a[1]][1] == 4 and (a == 251 or a == 81 or a == 36 or a == 206) and self.castling[self.color][1]: k[self.color][1] = False
            if t[a[1]][1] == 6 and (a == 248 or a == 129 or a == 39 or a == 158):
                k[self.color][0] = False
                k[self.color][1] = False
            if t[a[1]][1] == 6 and not self.threat(a[0], a[1]):
                swap = self.swap(a[1])
                t[swap[1]] = t[swap[0]]
                t[swap[0]] = 0
            y[self.color] = 0
        r.append([self.color, self.board, self.halfmoves, self.castling, self.enpassants])
        return Position(m, t, h, k, y, r)
            
    def moves(self, a = -1):
        # Get a list of avaliable moves.
        s, v, w, ww = [], [], 0, 0
        if a == -1: a = self.color
        for m, n in enumerate(self.board):
            if n != 0 and n[0] == a:
                for o, p in enumerate(self.board):
                    if not self.valid(o):
                        continue
                    if p == 0 and (n[1] != 0 and n[1] != 1) and self.threat(m, o):
                        s.append([m, o])
                    elif (n[1] == 0 or n[1] == 1) and self.threat(m, o) and self.enpassant(o, a):
                        if self.promotion(a, o):
                            for cc in promo: s.append([m, o, m + enpas_locator[a], cc])
                        else: s.append([m, o, m + enpas_locator[a]])
                    elif (n[1] == 0 or n[1] == 1) and o == m + enpas_locator[a] and p == 0:
                        if self.promotion(a, o):
                            for bb in promo: s.append([m, o, -1, bb])
                        else: s.append([m, o])
                    elif (n[1] == 0 or n[1] == 1) and o == m + (enpas_locator[a] * 2) and self.starter(m) and self.board[m + enpas_locator[a]] == 0:
                        if self.promotion(a, o):
                            for aa in promo: s.append([m, o, -1, aa, o - enpas_locator[a]])
                        else: s.append([m, o, -1, -1, o - enpas_locator[a]])
                    elif p != 0 and not self.opposite(p[0], a) and self.threat(m, o): s.append([m, o])
        for u in s:
            t = self.board[:]
            t[u[1]] = t[u[0]]
            t[u[0]] = 0
            if len(u) > 2:
                if u[2] != -1: t[u[2]] == 0
            if not self.checked(a):
                v.append(u)
        if self.castling[a][0] and not self.checked(a):
            for x in self.castling[a][2]:
                if self.board == 0:
                    for y, z in enumerate(self.board):
                        if self.threat(y, x):
                            w += 1
                            break
                    if w == 0: v.append([kings_locator[a], self.castling[a][2][1]])
        if self.castling[a][1] and not self.checked(a):
            for xx in self.castling[a][3]:
                if self.board == 0:
                    for yy, zz in enumerate(self.board):
                        if self.threat(yy, xx):
                            ww += 1
                            break
                    if ww == 0: v.append([kings_locator[a], self.castling[a][3][1]])
        return v

    def render(self):
        # Render the board.
        g = m = r = ""
        a = iter(self.board[:])
        for c in range(36): next(a)
        print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
        for d in range(3):
            for e in range(8):
                f = next(a)
                if f == 0: g += "     |"
                else: g += " " + str(f[0]) + "." + str(f[1]) + " |"
            if d < 2:
                for h in range(8): next(a)
            print("|-----|-----|-----|" + g + "-----|-----|-----|\n")
            print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
            g = ""
        for j in range(5): next(a)
        for k in range(8):
            for l in range(14):
                t = next(a)
                if t == 0: m += "     |"
                else: m += " " + str(t[0]) + "." + str(t[1]) + " |"
            if k < 7:
                for i in range(2): next(a)
            print("|" + m)
            print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
            m = ""
        for n in range(5): next(a)
        for o in range(3):
            for p in range(8):
                q = next(a)
                if q == 0: r += "     |"
                else: r += " " + str(q[0]) + "." + str(q[1]) + " |"
            if o < 2:
                for s in range(8): next(a)
            print("|-----|-----|-----|" + r + "-----|-----|-----|\n")
            print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n")
            r = ""

    def repetition(self):
        # Is this position drawn by repitition.
        b = 0
        for a in self.history:
            if a[0] == self.color and a[1] == self.board: b += 1
        return b == 2

    def stalemated(self, a = -1):
        # Is the current or specified locor stalemated.
        if a == -1: a = self.color
        return not self.checked(a) and len(self.moves(a)) == 0

    def undo(self):
        # Undo a played move.
        pos = self.history.pop()
        return Position(pos[0], pos[1], pos[2], pos[3], pos[4], self.history)

    def enpassant(self, b, a = -1):
        # Enpassant Helper.
        if a == -1: a = self.color
        if a == 0 or a == 2: return self.enpassants[1] == b or self.enpassants[3] == b
        if a == 1 or a == 3: return self.enpassants[0] == b or self.enpassants[2] == b

    def threat(self, a, b):
        # Used for move generation.
        if self.board[a] != 0 and self.valid(a) and self.valid(b):
            for d in directions[self.board[a][1]]:
                m = a + d
                n = m
                if self.board[a][1] == 3 or self.board[a][1] == 4 or self.board[a][1] == 5:
                    while self.valid(n):
                        if self.board[n] != 0 and n != b: break
                        if n == b: return True
                        n += d
                else:
                    if self.board[a][1] == 0 or self.board[a][1] == 1:
                        if self.board[a][0] == 2 or self.board[a][0] == 3: m = m - (d * 2)
                    if m == b: return True
        return False

    def opposite(self, a, b):
        # Determine whos on whos team.
        m = a
        if a != b: m = (a + 2) % 4
        if m != b: return False
        return True

    def promotion(self, a, b):
        # Promotion Helper.
        if b in promotion[a]: return True
        return False
        
    def starter(self, a):
        # Pawn Starter Helper.
        if a in starter: return True
        return False

    def swap(self, a):
        # Move Helper.
        if a == 246: return [244, 247]
        if a == 250: return [251, 249]
        if a == 97: return [81, 113]
        if a == 161: return [193, 145]
        if a == 37: return [36, 38]
        if a == 41: return [43, 40]
        if a == 126: return [94, 142]
        if a == 190: return [206, 174]
        return []

    def valid(self, a):
        # Used to prevent pieces from going off the board.
        if a in keys: return True
        return False

position = Position(0, start, 0, [[True, True, [249, 250], [247, 246, 245]], [True, True, [113, 97], [145, 161, 177]], [True, True, [38, 37], [40, 41, 42]], [True, True, [174, 190], [142, 126, 110]]], [0, 0, 0, 0], [])

x = 0
while x != 10:
    print("\n")
    print("Computer is thinking...\n")
    moves = position.moves()
    position = position.move(moves[random.randint(0, len(moves) - 0)])
    print("\n")
    position.render()
    print("\n")
    time.sleep(3)
    x += 1
