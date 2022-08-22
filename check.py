#-------------------------------- checking board -------------------------------------------------
                print("checking res")

                #if flag remain 1, sudoku is solved otherwise incorrect or incomplete
                flag=1

                for i in range(0,9):
                    if flag==0:
                        break

                    #--------checking for vertical rows-----------
                    for j in range (0,9):
                        l=[1,2,3,4,5,6,7,8,9]

                        if(0<board[i][j]<10 and board[i][j]in l):
                            l.remove(board[i][j])
                        
                    if len(l)!=0:
                        flag=0
                        break

                    #--------checking for horizontal rows-----------   
                    for j in range (0,9):
                        l=[1,2,3,4,5,6,7,8,9]

                        if(0<board[j][i]<10 and board[j][i]in l):
                            l.remove(board[j][i])
                        
                    if len(l)!=0:
                        flag=0
                        break

                #--------checking 3x3 boxes-----------    
                if(flag==1):
                    for x in range(0,3):
                        for y in range(0,3):
                            l=[1,2,3,4,5,6,7,8,9]

                            for i in range(x*3,x*3+3):
                                for j in range(y*3,y*3+3):
                                    if(0<board[i][j]<10 and board[i][j]in l):
                                        l.remove(board[i][j])
                        
                            if len(l)!=0:
                                flag=0
                                break
                
                if(flag==1):
                    print('won')
                else:
                    print('lost')