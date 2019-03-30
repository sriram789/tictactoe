def board_check():
    sum=0
    for i in range(3):
        for j in range(3):
            sum+=flag[i][j]
    if sum==9:
        return True
    else:
        return False
    
def pos_check(row,column):
    if flag[row][column]==1:
        return False
    else:
        return True

def opp_win_prop(row,column):
    s=[0,0]
    if row==0 and column==1:
        s[0]=board[row][column-1]+board[row][column]+board[row][column-2]
        s[1]=board[row][column]+board[row+1][column]+board[row+2][column]
    if row==2 and column==1:
        s[0]=board[row][column-1]+board[row][column]+board[row][column-2]
        s[1]=board[row][column]+board[row-1][column]+board[row-2][column]
    if row==1 and column==0:
        s[0]=board[row-1][column]+board[row][column]+board[row+1][column]
        s[1]=board[row][column]+board[row][column+1]+board[row][column+2]
    if row==1 and column==2:
        s[0]=board[row-1][column]+board[row][column]+board[row+1][column]
        s[1]=board[row][column]+board[row][column-1]+board[row][column-2]
    if s[0]==198 and row==0 and column==1:
        if pos_check(row,column-1)==True:
            board[row][column-1]=55
            flag[row][column-1]=1
            return True
        elif pos_check(row,column+1)==True:
            board[row][column+1]=55
            flag[row][column+1]=1
            return True
    elif s[1]==198 and row==0 and column==1:
        if pos_check(row+1,column)==True:
            board[row+1][column]=55
            flag[row+1][column]=1
            return True
        elif pos_check(row+2,column)==True:
            board[row+2][column]=55
            flag[row+2][column]=1
            return True
    if s[0]==198 and row==2 and column==1:
        if pos_check(row,column-1)==True:
            board[row][column-1]=55
            flag[row][column-1]=1
            return True
        elif pos_check(row,column+1)==True:
            board[row][column+1]=55
            flag[row][column+1]=1
            return True
    elif s[1]==198 and row==2 and column==1:
        if pos_check(row-1,column)==True:
            board[row-1][column]=55
            flag[row-1][column]=1
            return True
        elif pos_check(row-2,column)==True:
            board[row-2][column]=55
            flag[row-2][column]=1
            return True
    if s[0]==198 and row==1 and column==0:
        if pos_check(row-1,column)==True:
            board[row-1][column]=55
            flag[row-1][column]=1
            return True
        elif pos_check(row+1,column)==True:
            board[row+1][column]=55
            flag[row+1][column]=1
            return True
    elif s[1]==198 and row==1 and column==0:
        if pos_check(row,column+1)==True:
            board[row][column+1]=55
            flag[row][column+1]=1
            return True
        elif pos_check(row,column+2)==True:
            board[row][column+2]=55
            flag[row][column+2]=1
            return True
    if s[0]==198 and row==1 and column==2:
        if pos_check(row-1,column)==True:
            board[row-1][column]=55
            flag[row-1][column]=1
            return True
        elif pos_check(row+1,column)==True:
            board[row+1][column]=55
            flag[row+1][column]=1
            return True
    elif s[1]==198 and row==1 and column==2:
        if pos_check(row,column-1)==True:
            board[row][column-1]=55
            flag[row][column-1]=1
            return True
        elif pos_check(row,column-2)==True:
            board[row][column-2]=55
            flag[row][column-2]=1
            return True
    
    
def cpu_play(row,column):
    if row==column:
        if row==0 and board[row][column+2]!=99 and board[row+2][column]!=99 and board[row][column+1]!=99 and board[row+1][column]!=99:
            if pos_check(row+1,column+1)==True:
                board[row+1][column+1]=55
                flag[row+1][column+1]=1
                return True
            elif pos_check(row+2,column+2)==True:
                board[row+2][column+2]=55
                flag[row+2][column+2]=1
                return True
        elif row==1 and board[row][column-1]!=99 and board[row-1][column]!=99 and board[row][column+1]!=99 and board[row+1][column]!=99:
            if pos_check(row+1,column+1)==True:
                board[row+1][column+1]=55
                flag[row+1][column+1]=1
                return True
            elif pos_check(row-1,column-1)==True:
                board[row-1][column-1]=55
                flag[row-1][column-1]=1
                return True
        elif row==2 and board[row][column-2]!=99 and board[row][column-1]!=99 and board[row-2][column]!=99 and board[row-1][column]!=99:
            if pos_check(row-1,column-1)==True:
                board[row-1][column-1]=55
                flag[row-1][column-1]=1
                return True
            elif pos_check(row-2,column-2)==True:
                board[row-2][column-2]=55
                flag[row-2][column-2]=1
                return True
    if column==3-row-1:
        if row==0 and board[row][column-2]!=99 and board[row][column-1]!=99 and board[row+2][column]!=99 and board[row+1][column]!=99:
            if pos_check(row+1,column-1)==True:
                board[row+1][column-1]=55
                flag[row+1][column-1]=1
                return True
            elif pos_check(row+2,column-2)==True:
                board[row+2][column-2]=55
                flag[row+2][column-2]=1
                return True
        elif row==1 and board[row][column-1]!=99 and board[row][column+1]!=99 and board[row-1][column]!=99 and board[row+1][column]!=99:
            if pos_check(row+1,column+1)==True:
                board[row+1][column+1]=55
                flag[row+1][column+1]=1
                return True
            elif pos_check(row-1,column-1)==True:
                board[row-1][column-1]=55
                flag[row-1][column-1]=1
                return True
        elif row==2 and board[row-1][column]!=99 and board[row-2][column]!=99 and board[row][column+2]!=99 and board[row][column+1]!=99:
            if pos_check(row-1,column+1)==True:
                board[row-1][column+1]=55
                flag[row-1][column+1]=1
                return True
            elif pos_check(row-2,column+2)==True:
                board[row-2][column+2]=55
                flag[row-2][column+2]=1
                return True
    else:
        if row==1 and column==0 and opp_win_prop(row,column)!=True:
            if pos_check(row,column+1)==True:
                board[row][column+1]=55
                flag[row][column+1]=1
                return True
            elif pos_check(row,column+2)==True:
                board[row][column+2]=55
                flag[row][column+2]=1
                return True
            elif pos_check(row+1,column)==True:
                board[row+1][column]=55
                flag[row+1][column]=1
                return True
            elif pos_check(row-1,column)==True:
                board[row-1][column]=55
                flag[row-1][column]=1
                return True
        if row==1 and column==2 and opp_win_prop(row,column)!=True:
            if pos_check(row,column-1)==True:
                board[row][column-1]=55
                flag[row][column-1]=1
                return True
            elif pos_check(row,column-2)==True:
                board[row][column-2]=55
                flag[row][column-2]=1
                return True
            elif pos_check(row+1,column)==True:
                board[row+1][column]=55
                flag[row+1][column]=1
                return True
            elif pos_check(row-1,column)==True:
                board[row-1][column]=55
                flag[row-1][column]=1
                return True
        if row==0 and column==1 and opp_win_prop(row,column)!=True:
            if pos_check(row+1,column)==True:
                board[row+1][column]=55
                flag[row+1][column]=1
                return True
            elif pos_check(row+2,column)==True:
                board[row+2][column]=55
                flag[row+2][column]=1
                return True
            elif pos_check(row,column-1)==True:
                board[row][column-1]=55
                flag[row][column-1]=1
                return True
            elif pos_check(row,column+1)==True:
                board[row][column+1]=55
                flag[row][column+1]=1
                return True
        if row==2 and column==1 and opp_win_prop(row,column)!=True:
            if pos_check(row-1,column)==True:
                board[row-1][column]=55
                flag[row-1][column]=1
                return True
            elif pos_check(row-2,column)==True:
                board[row-2][column]=55
                flag[row-2][column]=1
                return True
            elif pos_check(row,column-1)==True:
                board[row][column-1]=55
                flag[row][column-1]=1
                return True
            elif pos_check(row,column+1)==True:
                board[row][column+1]=55
                flag[row][column+1]=1
                return True
            

def match_check():
    s=[0,0,0,0,0,0,0,0]
    s[0]=board[0][0]+board[0][1]+board[0][2]
    s[1]=board[1][0]+board[1][1]+board[1][2]
    s[2]=board[2][0]+board[2][1]+board[2][2]
    s[3]=board[0][0]+board[1][0]+board[2][0]
    s[4]=board[0][1]+board[1][1]+board[2][1]
    s[5]=board[0][2]+board[1][2]+board[2][2]
    s[6]=board[0][0]+board[1][1]+board[2][2]
    s[7]=board[0][2]+board[1][1]+board[2][0]

    if s[0]==297 or s[1]==297 or s[2]==297 or s[3]==297 or s[4]==297 or s[5]==297 or s[6]==297 or s[7]==297:
        print("user wins the match")
        exit()
    elif s[0]==165 or s[1]==165 or s[2]==165 or s[3]==165 or s[4]==165 or s[5]==165 or s[6]==165 or s[7]==165:
        print("cpu wins")
        exit()

def display():
    for i in range(3):
        for j in range(3):
            print(board[i][j],end='   |   ')
        print("\n")
        print("-"*20)

def cpu_iter(row,column):
    if row==0 and column==0:
        if board[row][column+2]==99 and pos_check(row,column+1)==True:
            board[row][column+1]=55
            flag[row][column+1]=1
            return True
        elif board[row][column+1]==99 and pos_check(row,column+2)==True:
            board[row][column+2]=55
            flag[row][column+2]=1
            return True
        elif board[row+2][column]==99 and pos_check(row+1,column)==True:
            board[row+1][column]=55
            flag[row+1][column]=1
            return True
        elif board[row+1][column]==99 and pos_check(row+2,column)==True:
            board[row+2][column]=55
            flag[row+2][column]=1
            return True
        else:
            if board[row][column+2]!=99 and pos_check(row,column+1)==True:
                board[row][column+1]=55
                flag[row][column+1]=1
                return True
            elif board[row][column+1]!=99 and pos_check(row,column+2)==True:
                board[row][column+2]=55
                flag[row][column+2]=1
                return True
            elif board[row+2][column]!=99 and pos_check(row+1,column)==True:
                board[row+1][column]=55
                flag[row+1][column]=1
                return True
            elif board[row+1][column]!=99 and pos_check(row+2,column)==True:
                board[row+2][column]=55
                flag[row+2][column]=1
                return True
            
            
                
    if row==2 and column==2:
        if board[row][column-2]==99 and pos_check(row,column-1)==True:
            board[row][column-1]=55
            flag[row][column-1]=1
            return True
        elif board[row][column-1]==99 and pos_check(row,column-2)==True:
            board[row][column-2]=55
            flag[row][column-2]=1
            return True
        elif board[row-2][column]==99 and pos_check(row-1,column)==True:
            board[row-1][column]=55
            flag[row-1][column]=1
            return True
        elif board[row-1][column]==99 and pos_check(row-2,column)==True:
            board[row-2][column]=55
            flag[row-2][column]=1
            return True
        else:
            if board[row][column-2]!=99 and pos_check(row,column-1)==True:
                board[row][column-1]=55
                flag[row][column-1]=1
                return True
            elif board[row][column-1]!=99 and pos_check(row,column-2)==True:
                board[row][column-2]=55
                flag[row][column-2]=1
                return True
            elif board[row-2][column]!=99 and pos_check(row-1,column)==True:
                board[row-1][column]=55
                flag[row-1][column]=1
                return True
            elif board[row-1][column]!=99 and pos_check(row-2,column)==True:
                board[row-2][column]=55
                flag[row-2][column]=1
                return True
    if row==2 and column==0:
        if board[row][column+2]==99 and pos_check(row,column+1)==True:
            board[row][column+1]=55
            flag[row][column+1]=1
            return True
        elif board[row][column+1]==99 and pos_check(row,column+2)==True:
            board[row][column+2]=55
            flag[row][column+2]=1
            return True
        elif board[row-2][column]==99 and pos_check(row-1,column)==True:
            board[row-1][column]=55
            flag[row-1][column]=1
            return True
        elif board[row-1][column]==99 and pos_check(row-2,column)==True:
            board[row-2][column]=55
            flag[row-2][column]=1
            return True
        else:
            if board[row][column+2]!=99 and pos_check(row,column+1)==True:
                board[row][column+1]=55
                flag[row][column+1]=1
                return True
            elif board[row][column+1]!=99 and pos_check(row,column+2)==True:
                board[row][column+2]=55
                flag[row][column+2]=1
                return True
            elif board[row-2][column]!=99 and pos_check(row-1,column)==True:
                board[row-1][column]=55
                flag[row-1][column]=1
                return True
            elif board[row-1][column]!=99 and pos_check(row-2,column)==True:
                board[row-2][column]=55
                flag[row-2][column]=1
                return True
    if row==0 and column==2:
        if board[row][column-2]==99 and pos_check(row,column-1)==True:
            board[row][column-1]=55
            flag[row][column-1]=1
            return True
        elif board[row][column-1]==99 and pos_check(row,column-2)==True:
            board[row][column-2]=55
            flag[row][column-2]=1
            return True
        elif board[row+2][column]==99 and pos_check(row+1,column)==True:
            board[row+1][column]=55
            flag[row+1][column]=1
            return True
        elif board[row+1][column]==99 and pos_check(row+2,column)==True:
            board[row+2][column]=55
            flag[row+2][column]=1
            return True
        else:
            if board[row][column-2]!=99 and pos_check(row,column-1)==True:
                board[row][column-1]=55
                flag[row][column-1]=1
                return True
            elif board[row][column-1]!=99 and pos_check(row,column-2)==True:
                board[row][column-2]=55
                flag[row][column-2]=1
                return True
            elif board[row+2][column]!=99 and pos_check(row+1,column)==True:
                board[row+1][column]=55
                flag[row+1][column]=1
                return True
            elif board[row+1][column]!=99 and pos_check(row+2,column)==True:
                board[row+2][column]=55
                flag[row+2][column]=1
                return True

def win_option():
    s=[0,0,0,0,0,0,0,0]
    s[0]=board[0][0]+board[0][1]+board[0][2]
    s[1]=board[1][0]+board[1][1]+board[1][2]
    s[2]=board[2][0]+board[2][1]+board[2][2]
    s[3]=board[0][0]+board[1][0]+board[2][0]
    s[4]=board[0][1]+board[1][1]+board[2][1]
    s[5]=board[0][2]+board[1][2]+board[2][2]
    s[6]=board[0][0]+board[1][1]+board[2][2]
    s[7]=board[0][2]+board[1][1]+board[2][0]
    if s[0]==110:
        if board[0][0]==0:
            board[0][0]=55
            flag[0][0]=1
            return True
        elif board[0][1]==0:
            board[0][1]=55
            flag[0][1]=1
            return True
        elif board[0][2]==0:
            board[0][2]=55
            flag[0][2]=1
            return True
    if s[1]==110:
        if board[1][0]==0:
            board[1][0]=55
            flag[1][0]=1
            return True
        elif board[1][1]==0:
            board[1][1]=55
            flag[1][1]=1
            return True
        elif board[1][2]==0:
            board[1][2]=55
            flag[1][2]=1
            return True
    if s[2]==110:
        if board[2][0]==0:
            board[2][0]=55
            flag[2][0]=1
            return True
        elif board[2][1]==0:
            board[2][1]=55
            flag[2][1]=1
            return True
        elif board[2][2]==0:
            board[2][2]=55
            flag[2][2]=1
            return True
    if s[3]==110:
        if board[0][0]==0:
            board[0][0]=55
            flag[0][0]=1
            return True
        elif board[1][0]==0:
            board[1][0]=55
            flag[1][0]=1
            return True
        elif board[2][0]==0:
            board[2][0]=55
            flag[2][0]=1
            return True
    if s[4]==110:
        if board[0][1]==0:
            board[0][1]=55
            flag[0][1]=1
            return True
        elif board[1][1]==0:
            board[1][1]=55
            flag[1][1]=1
            return True
        elif board[2][1]==0:
            board[2][1]=55
            flag[2][1]=1
            return True
    if s[5]==110:
        if board[0][2]==0:
            board[0][2]=55
            flag[0][2]=1
            return True
        elif board[1][2]==0:
            board[1][2]=55
            flag[1][2]=1
            return True
        elif board[2][2]==0:
            board[2][2]=55
            flag[2][2]=1
            return True
    if s[6]==110:
        if board[0][0]==0:
            board[0][0]=55
            flag[0][0]=1
            return True
        elif board[1][1]==0:
            board[1][1]=55
            flag[1][1]=1
            return True
        elif board[2][2]==0:
            board[2][2]=55
            flag[2][2]=1
            return True
    if s[7]==110:
        if board[2][0]==0:
            board[2][0]=55
            flag[2][0]=1
            return True
        elif board[1][1]==0:
            board[1][1]=55
            flag[1][1]=1
            return True
        elif board[0][2]==0:
            board[0][2]=55
            flag[0][2]=1
            return True
                
def play():
    op=int(input("Enter head=0 tail=1"))
    if(op==random.randint(0,1)):
        print("user wins the toss enter the position")
        while board_check()!=True:
            row=int(input("enter the row position"))
            column=int(input("enter the column position"))
            if pos_check(row,column)==True:
                board[row][column]=99
                flag[row][column]=1
            else:
                print("Already occupied....")
                continue
            if win_option()!=True:
                if cpu_play(row,column)!=True:
                    cpu_iter(row,column)
            display()
            match_check()
    else:
        print("cpu wins the toss")
        cpu_play(random.randint(0,2),random.randint(0,2))
        display()
        while board_check()!=True:
            row=int(input("enter the row position"))
            column=int(input("enter the column position"))
            if pos_check(row,column)==True:
                board[row][column]=99
                flag[row][column]=1
            else:
                print("Already occupied....")
                continue
            if win_option()!=True:
                if cpu_play(row,column)!=True:
                    cpu_iter(row,column)
            display()
            match_check()
        
        
import random
flag=[[0 for i in range(3)]for j in range(3)]
board=[[0 for i in range(9)] for j in range(3)]
play()
    
        
        
