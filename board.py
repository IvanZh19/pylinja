class Board():

    def __init__(self):
        self.red = [6,1,1,1,1,1,1,0]
        self.black = [0,1,1,1,1,1,1,6]
        self.turn = 'red'

    def red_score(self):
        return self.red[4] + self.red[5] * 2 + self.red[6] * 3 + self.red[7] * 5

    def black_score(self):
        return self.black[0] * 5 + self.black[1] * 3 + self.black[2] * 2 + self.black[3]

    def make_red_initial(self, start_row):
        assert start_row < 7 and start_row > -1 and self.red[start_row] > 0
        self.red[start_row] -= 1
        self.red[start_row+1] += 1

        if start_row == 6:
            return 1, 'bonus'
        return self.red[start_row+1] + self.black[start_row+1] - 1, 'follow-up'

    def make_black_initial(self, start_row):
        assert start_row < 8 and start_row > 0 and self.black[start_row] > 0
        self.black[start_row] -= 1
        self.black[start_row-1] += 1

        if start_row == 1:
            return 1, 'bonus'
        return self.red[start_row-1] + self.black[start_row-1] - 1, 'follow-up'

    def make_red_followup(self, start_row):
        pass

    def make_black_followup(self, start_row):
        pass

    def display(self):
        for i in range(7, -1, -1):
            print(self.red[i] * 'R' + self.black[i] * 'B')
