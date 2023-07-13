import numpy as np
import math


def checkRCvalid(N, r, c):
    flag = False
    if 0 <= r < N and 0 <= c < N:
        flag = True
    return flag


def checkAvailable(board, r, c):
    flag = False
    if board[r, c] == 0:
        flag = True
    return flag


def check(board, N, r, c):
    if checkRCvalid(N, r, c):
        if checkAvailable(board, r, c):
            return True
    return False


def countCheckers(N, rSize, board, i, x, index):  # Dem so quan co
    sl = 0
    for j in range(N):
        S = [i, j, j, j]
        E = [j, i, j, N - 1 - j]
        if board[S[index], E[index]] == x:
            sl += 1
    return False if sl == rSize else True


def taoBanCo(N):
    return np.zeros((N, N), dtype=float)


def printState(banco: np, name='BOT'):
    print("____________________" + name + "________________________ ")
    # print(xState)
    # print("\n ....... ")
    banco = banco.astype('int32')
    x = np.arange(0, banco.shape[0]).astype(str)
    bar = ""
    for row in x:
        bar += "\t" + row
    print(bar)
    i = 0
    for row in banco:
        s = str(i)
        for cell in row:
            curr = "-"
            if cell == 2:
                curr = "O"
            if cell == 1:
                curr = "X"
            s += "\t" + curr
        print(s)
        i += 1
    print("\n---------------------------")



def OneMove(data, N):
    x, y = data[0], data[1]
    newA = [e for e in range(x - 1, x + 2) if 0 <= e < N]
    newB = [e for e in range(y - 1, y + 2) if 0 <= e < N]
    return [(a, b) for a in newA for b in newB]


def getEmptySlot1(banco: np, N: int):
    E = list()
    A = list(zip(*np.where(banco == 1)))
    B = list(zip(*np.where(banco == 2)))
    E = E + [e for i in A for e in OneMove(i, N) if e not in B and e not in A]
    E = E + [e for i in B for e in OneMove(i, N) if e not in A and e not in B]
    return set(E)


def getStringList2(Data):
    try:
        SD = [n.tolist() for n in Data if len(n) >= 3]
    except:
        SD = [n for n in Data if len(n) >= 3]
    X = [''.join(str(i) for i in e) for e in SD]
    return X


def checkWinAll(banco, rSize):
    S = ['111', '222'] if rSize == 3 else ['11111', '22222']
    Data = banco.astype('int32')
    diags = [Data[::-1, :].diagonal(i) for i in range(-Data.shape[0] + 1, Data.shape[1])]
    diags.extend(Data.diagonal(i) for i in range(Data.shape[1] - 1, -Data.shape[0], -1))
    X = getStringList2(diags)
    X1 = getStringList2(Data.tolist())
    Data = Data.T
    X2 = getStringList2(Data.tolist())
    Data = np.flip(Data, axis=1)
    Data = np.flip(Data, axis=1)
    diags = [Data[::-1, :].diagonal(i) for i in range(-Data.shape[0] + 1, Data.shape[1])]
    diags.extend(Data.diagonal(i) for i in range(Data.shape[1] - 1, -Data.shape[0], -1))
    X3 = getStringList2(Data)
    X = X + X1 + X2 + X3
    e, h, check = 0, True, False
    for i in X:
        if S[0] in i:
            e = 1
            check = True
            break
        if S[1] in i:
            e = 2
            check = True
            break
        if '0' in i:
            h =False
    if h is True:
        check = True
    return e, check


RULE3 = [[110001, 110001, 110001],   [110010, 110010, 110010], [110000, 110001, 110001], [110000, 110010, 110010],
         [110001, 110001, 110000],   [110010, 110010, 110000],   [110001, 110000, 110001],   [110010, 110000, 110010]]

RULE4 = [[110011, 110000, 110000, 110000, 110000, 110000, 110000, 110000],
         [101101, 110011, 110000, 110000, 110000, 110000, 110000, 110000, 110000],
         [110101, 110000, 110000, 110000, 110000],
         [101101, 110101, 110000, 110000, 110000, 110000],
         [110101, 110000, 110000, 110000, 110000],
         [101101, 110101, 110000, 110000, 110000, 110000],
         [110101, 110000, 110000, 110000, 110000],
         [101101, 110101, 110000, 110000, 110000, 110000]]


RULE5 = [[110001, 110001, 110001, 110001, 110001],              [110010, 110010, 110010, 110010, 110010],
         [110000, 110001, 110001, 110001, 110001, 110000],      [110000, 110010, 110010, 110010, 110010, 110000],
         [110000, 110001, 110001, 110001, 110001, 110010],      [110010, 110001, 110001, 110001, 110001, 110000],
         [110000, 110010, 110010, 110010, 110010, 110001],      [110001, 110010, 110010, 110010, 110010, 110000],
         [110000, 110001, 110001, 110001, 110000],              [110000, 110010, 110010, 110010, 110000],
         [110000, 110001, 110001, 110000, 110001, 110000],      [110000, 110001, 110000, 110001, 110001, 110000],
         [110000, 110010, 110010, 110000, 110010, 110000],      [110000, 110010, 110000, 110010, 110010, 110000],
         [110000, 110000, 110001, 110001, 110001, 110010],      [110010, 110001, 110001, 110001, 110000, 110000],
         [110000, 110000, 110010, 110010, 110010, 110001],      [110001, 110010, 110010, 110010, 110000, 110000],
         [110010, 110001, 110001, 110000, 110001, 110000],      [110010, 110001, 110000, 110001, 110001, 110000],
         [110000, 110001, 110000, 110001, 110001, 110010],      [110000, 110001, 110001, 110000, 110001, 110010],
         [110001, 110010, 110010, 110000, 110010, 110000],      [110001, 110010, 110000, 110010, 110010, 110000],
         [110000, 110010, 110000, 110010, 110010, 110001],      [110000, 110010, 110010, 110000, 110010, 110001],
         [110000, 110001, 110001, 110000, 110000],              [110000, 110000, 110001, 110001, 110000],
         [110000, 110010, 110010, 110000, 110000],              [110000, 110000, 110010, 110010, 110000]]

RULE6 = [[110011, 110000, 110000, 110000, 110000, 110000, 110000, 110000],
         [101101, 110011, 110000, 110000, 110000, 110000, 110000, 110000, 110000],
         [110010, 110000, 110000, 110000, 110000, 110000, 110000, 110000],
         [101101, 110010, 110000, 110000, 110000, 110000, 110000, 110000, 110000],
         [110101, 110000, 110000, 110000, 110000],          [110101, 110000, 110000, 110000, 110000],
         [101101, 110101, 110000, 110000, 110000, 110000],  [101101, 110101, 110000, 110000, 110000, 110000],
         [110011, 110000, 110000, 110000, 110000],          [101101, 110011, 110000, 110000, 110000, 110000],
         [110001, 110101, 110000, 110000, 110000],          [110001, 110101, 110000, 110000, 110000],
         [101101, 110001, 110101, 110000, 110000, 110000],  [101101, 110001, 110101, 110000, 110000, 110000],
         [110010, 110000, 110000, 110000],                  [110010, 110000, 110000, 110000],
         [101101, 110010, 110000, 110000, 110000],          [101101, 110010, 110000, 110000, 110000],
         [110010, 110000, 110000, 110000],                  [110010, 110000, 110000, 110000],
         [110010, 110000, 110000, 110000],                  [110010, 110000, 110000, 110000],
         [101101, 110010, 110000, 110000, 110000],          [101101, 110010, 110000, 110000, 110000],
         [101101, 110010, 110000, 110000, 110000],          [101101, 110010, 110000, 110000, 110000],
         [110101, 110000, 110000],                          [110101, 110000, 110000],
         [101101, 110101, 110000, 110000],                  [101101, 110101, 110000, 110000]]


def releaseString(matrix: np, player):
    L = []
    for i in matrix:
        v = ""
        for j in i:
            if j == 0:
                v += "0"
            elif j == player:
                v += "1"
            else:
                v += "2"
        L.append(v)
    return L


def getAllString(banco, player, N):
    a, b, S = 5, 4, []
    if N == 3:
        a, b = 2, 1
    bancochuyenvi = banco.copy().transpose()
    cheotrai = [banco.diagonal(i) for i in range(banco.shape[1] - a, -banco.shape[1] + b, -1)]
    cheophai = [banco[::-1, :].diagonal(i) for i in range(banco.shape[1] - a, -banco.shape[1] + b, -1)]
    S += releaseString(banco, player)
    S += releaseString(bancochuyenvi, player)
    S += releaseString(cheophai, player)
    S += releaseString(cheotrai, player)
    return S


def heuristic(chuoicon, h, dodai):
    v = 0
    for i in range(len(chuoicon)):
        j = i + dodai
        if j <= len(chuoicon):
            s = chuoicon[i:j]
            if s in h:
                v += h[s]
    return v


def applyRule(a):
    b, c, l, m = None, None, [], ""
    for i in a:
        b, c, k = 0, 0, int(math.log10(i))+1
        for j in range(k):
            b = ((i%10)*(2**j))
            i, c = i//10, c+b
        l.append(c)
    for x in l:
        m = m+chr(x)
    return m


def h_Cost_Rule(r1, r2):
    k = [applyRule(e) for e in r1]
    v = [int(applyRule(e)) for e in r2]
    return {k[i]: v[i] for i in range(len(k))}


def stopPoints(banco, player, N):
    v, a, b, h = (0, 5, 6, h_Cost_Rule(RULE5, RULE6)) if N > 3 else (0, 2, 3, h_Cost_Rule(RULE3, RULE4))
    S = getAllString(banco, player, N)
    for i in range(len(S)):
        v += heuristic(S[i], h, a)
        v += heuristic(S[i], h, b)
    return v


def changePlayer(player):
    return 2 if player == 1 else 1


