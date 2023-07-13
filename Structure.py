import random
from bigtree import Node
import BanCo as BC
import copy
import numpy as np
import math
MAX, MIN = math.inf, -math.inf

class GameTree:
    def __init__(self, N=3, rSize=3, player=1):     # -1: X, 1: O
        self.player = player  # 1: truoc, 2 : sau
        self.N = N
        self.rSize = rSize
        self.root = None
        self.current_node = self.root
        self.maxStepScan = 3
        self.alpha, self.beta = -math.inf, math.inf
        self.bestPoint = float('-inf')

    def getName(self, x, y, d):
        return str(x) + "-" + str(y) + "-" + str(d)

    def getXY(self):
        data = [int(e) for e in self.current_node.name.split("-")]
        return data[0], data[1]

    def extractName(self, node:Node):
        return [int(e) for e in node.name.split("-")]

    def setRoot(self, x, y):
        banco = BC.taoBanCo(self.N)
        r, c = x, y
        banco[r, c] = BC.changePlayer(self.player)
        self.root = Node(self.getName(r, c, 0), banco=banco, heuristic=None)
        self.current_node = self.root

    def createRoot(self):
        banco = BC.taoBanCo(self.N)
        #r, c = int(self.N/2)-1, int(self.N/2)-1
        r, c = random.randint(0, self.N-1), random.randint(0, self.N-1)
        banco[r, c] = self.player
        self.root = Node(self.getName(r, c, 0), banco=banco, heuristic=None)
        self.current_node = self.root

    def addChild(self, banco: np, parent: Node, x, y):
        ch = Node(name=self.getName(x, y, parent.depth), banco=banco,
                  heuristic=None, parent=parent)
        return ch

    def create_new_human_node(self, r, c, player):
        banco = copy.deepcopy(self.current_node.banco)
        banco[r, c] = player
        new_node = self.addChild(banco, self.current_node, r, c)
        self.current_node = new_node

    def minimax(self, banco,  toida: bool, dosau, alpha, beta, player):  # alpha, beta
        point = BC.stopPoints(banco, player, self.N)
        if dosau == 2 or point >= 20000000 or point <= -20000000:
            return point
        if toida:
            best = MIN
            slot = BC.getEmptySlot1(banco, self.N)
            for i in slot:
                x, y = i[0], i[1]
                banco[x, y] = player
                score = self.minimax(banco, False, dosau + 1, alpha, beta, player)
                best = max(best, score)
                alpha = max(alpha, best)
                banco[x, y] = 0
                if beta <= alpha:
                    break
            return best
        else:
            best = MAX
            slot = BC.getEmptySlot1(banco, self.N)
            for i in slot:
                x, y = i[0], i[1]
                banco[x, y] = BC.changePlayer(player)
                score = self.minimax(banco, True, dosau + 1, alpha, beta, player)
                best = min(best, score)
                beta = min(beta, best)
                banco[x, y] = 0
                if beta <= alpha:
                    break
            return best

    def nextMove(self):
        A, B, C = self.alpha, self.beta, self.bestPoint
        CRow, CCol = -1, -1
        slot = BC.getEmptySlot1(self.current_node.banco, self.N)
        for i in slot:
            x, y = i[0], i[1]
            banco = copy.deepcopy(self.current_node.banco)
            banco[x, y] = self.player
            MVP = max(C, self.minimax(banco, False, 1, A, B, self.player))
            A = max(MVP, A)
            if B <= A:
                break
            if MVP > C:
                CRow = x
                CCol = y
                C = MVP
                if MVP >= 20000000:
                    break
        if CRow == -1 or CCol == -1:
            print("Random duong di")
            i = random.randint(0, len(slot))
            slot = list(slot)
            try:
                CRow, CCol = slot[i][0], slot[i][1]
            except:
                print("Het Duong di")
                return
        banco = copy.deepcopy(self.current_node.banco)
        banco[CRow, CCol] = self.player
        node = self.addChild(banco=banco, parent=self.current_node, x=CRow, y=CCol)
        self.current_node = node

    def nextStep(self, r, c, player):
        if BC.check(self.current_node.banco, self.N, r, c):
            self.create_new_human_node(r, c, player)
            return True
        return False

    def Show(self, name="BOT"):
        BC.printState(self.current_node.banco, name)
        print("-->", self.getXY())

    def checkWin(self):
        e, c = BC.checkWinAll(self.current_node.banco, self.rSize)
        if e == 1:
            msg = "Player 1 win"
        elif e == 2:
            msg = "Player 2 win"
        else:
            msg = "Hoa nhau"
        return msg, c

