class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dir = [[0,1],[1,0],[-1,0],[0,-1]]

        row = {}
        col = {}
        box = {}

        r = len(board)
        c = len(board[0])
        k = 3

        for i in range(r):
            for j in range(c):
                if board[i][j] == ".":
                    continue
                if i not in row:
                    row[i] = []
                if j not in col:
                    col[j] = []

                box_i = i // 3
                box_j = j // 3

                curr_box = (box_i * k) + box_j

                if curr_box not in box:
                    box[curr_box] = []

                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[curr_box]:
                    return False
        
                row[i].append(board[i][j]) 
                col[j].append(board[i][j])
                box[curr_box].append(board[i][j])

        return True