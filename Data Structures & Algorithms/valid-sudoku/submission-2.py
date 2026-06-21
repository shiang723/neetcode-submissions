class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True;
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] in row and board[i][j] != '.' :
                    valid = False
                    break
                else:
                    row.add(board[i][j])

        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] in col and board[j][i] != '.' :
                    valid = False
                    break
                else:
                    col.add(board[j][i])
        
        r = 0;
        c = 0;
        while (c < 9 or r < 9):
            if (r == 9):
                r = 0;
                c+=3
            if (c == 9):
                break
            sqr = set();
            i = r
            while (i < r+3):
                j = c
                while (j < c+3):
                    if board[i][j] in sqr and board[i][j] != '.':
                        valid = False;
                        break
                    else:
                        sqr.add(board[i][j])
                    j+=1
                i+=1
            if (r < 9):
                r+=3 

        return valid;
        