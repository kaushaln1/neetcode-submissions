class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #row check
        for row in board :
            rowlist={}
            for num in row:
                if num.isdigit():
                    if int(num) not in rowlist:
                        rowlist[int(num)]=1
                    else:
                        return False
        
        print("row pass")
        #col check
        for i, n in enumerate(board):
            collist={}
            for j , _ in enumerate(n):
                if board[j][i].isdigit() :
                    if int(board[j][i])  not in collist:
                        collist[int(board[j][i])]=1 
                    else:
                        return False
        
        print("col pass")
        #3*3 check
        x=0
        while x<9:
            y=0
            while y <9:

                collist={}
                for i in range(x, x+3):
                    for j in range(y ,y+3):
                       
                        if board[i][j].isdigit():
                            print(i, "," , j , " -> ", board[i][j])
                            if int(board[i][j])  not in collist:
                                collist[int(board[i][j])]=1 
                            else:
                                return False
                y+=3
        
                print("\n \n")
            x+=3
       
        print("mat pass")
        return True

            







        