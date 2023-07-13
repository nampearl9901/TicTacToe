from Structure import GameTree


class TikTakToe:
    def __init__(self):
        self.GT = None
        self.GT2 = None
        self.N = 5
        self.rSize = 3

    def nhapDuLieu(self):
        N, rSize = 1, 0
        N_Array = [3, 5, 10, 100, 1000]
        print("Nhap kich thuoc ban co N: ")
        print("-3: 3x3 \n-5: 5x5 \n-10: 10x10 \n-100: 100x100 \n-1000: 1000x1000")
        while N not in N_Array:
            N = int(input("Nhap N: "))
            if N not in N_Array:
                print("Kich thuoc ban co khong hop le, Nhap lai")
            else:
                self.N = N
        self.rSize = 3 if N <= 3 else 5

    def inputXY(self):
        inXY = input("Nhap vi tri can Danh: ROW COLUMN (<N): ")
        inXY = inXY.strip().split()
        r = int(inXY[0])
        c = int(inXY[1])
        return r, c

    def run(self):
        self.nhapDuLieu()
        namea, nameb = "__BOT__", "PLAYER "
        self.GT = GameTree(N=self.N, rSize=self.rSize, player=1)
        self.GT.createRoot()
        self.GT.Show(namea)

        msg, e = self.GT.checkWin()
        while not e:
            player = False
            msg, e = self.GT.checkWin()
            while not player and not e:
                r, c = self.inputXY()
                if self.GT.nextStep(r, c, 2):
                    self.GT.Show(nameb)
                    player = True
                else:
                    print(" ...... r,c NGOAI pham vi ")
            print(msg) if e else print("")

            self.GT.nextMove()
            self.GT.Show(namea)
            msg, e = self.GT.checkWin()
            print(msg) if e else print("")

    def run2(self):
        self.nhapDuLieu()
        namea, nameb = "PLAYER ", "__BOT__"
        self.GT = GameTree(N=self.N, rSize=self.rSize, player=1)

        x, y = self.inputXY()
        self.GT.setRoot(x, y)
        self.GT.Show(namea)

        msg, e = self.GT.checkWin()
        while not e:
            # ----------- BOT 2 --------------
            self.GT.nextMove()
            self.GT.Show(nameb)
            msg, e = self.GT.checkWin()
            print(msg) if e else print("")

            player = False
            msg, e = self.GT.checkWin()
            while not player and not e:
                r, c = self.inputXY()
                if self.GT.nextStep(r, c, 2):
                    self.GT.Show(namea)
                    player = True
                else:
                    print(" ...... r,c NGOAI pham vi ")
            print(msg) if e else print("")

    def run3(self):
        self.nhapDuLieu()
        # self.N = 10
        # self.rSize = 5
        namea, nameb = "_BOT 1_", "_BOT 2_"
        self.GT = GameTree(N=self.N, rSize=self.rSize, player=1)
        self.GT2 = GameTree(N=self.N, rSize=self.rSize, player=2)
        x, y, x2, y2 = None, None, None, None

        # ----------- BOT 1 --------------
        self.GT.createRoot()
        self.GT.Show(namea)
        x, y = self.GT.getXY()
        self.GT2.setRoot(x, y)

        msg, e = self.GT.checkWin()
        while not e:
            # ----------- BOT 2 --------------
            self.GT2.nextMove()
            x2, y2 = self.GT2.getXY()
            self.GT.nextStep(x2, y2, 2)
            self.GT.Show(nameb)
            msg, e = self.GT.checkWin()
            print(msg) if e else print("")

            # ----------- BOT 1 --------------
            self.GT.nextMove()
            x, y = self.GT.getXY()
            self.GT2.nextStep(x, y, 1)
            self.GT.Show(namea)
            msg, e = self.GT.checkWin()
            print(msg) if e else print("")


def main():
    TroChoi = TikTakToe()
    print("Nhap che do choi")
    print("- 1: May truoc - nguoi sau")
    print("- 2: Nguoi truoc - may sau")
    print("- 3: May vs may")
    c = int(input("Chon: "))
    if c == 1:
        TroChoi.run()
    elif c == 2:
        TroChoi.run2()
    else:
        TroChoi.run3()

    # path = "CLIENT-TicTacYoe.exe"
    # xCaro = subprocess.Popen([path, "start", "ABC", "BaDoSa"],
    #         stdin = subprocess.PIPE,
    #         stdout = subprocess.PIPE,
    #         stderr = subprocess.PIPE,
    #         #universal_newlines = True,
    #         bufsize = 0)
    #
    # for line in xCaro.stdout:
    #     print(line.strip())

if __name__ == "__main__":
    main()
