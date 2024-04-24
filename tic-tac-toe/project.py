board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def game_board(board):
    # print("\n"*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def user_choice():
    choice='wrong'
    while choice not in ['X','O']:
        choice=input("enter X or O: ")
    player1=choice
    if player1=='X':
        player2="O"
    else:
        player2='X'
    return (player1,player2)

def play(oddOReven,player1,player2,board):
    marker=''
    
    if oddOReven%2!=0:
        
        while marker not in ['1','2','3','4','5','6','7','8','9']:
            marker=input("enter index")
        if board[int(marker)]==' ':
            board[int(marker)]=player1
        else:
            print("That index is already taken. enter again")
            play(oddOReven,player1,player2,board)
        # oddOReven+=1
    else:
        
        while marker not in ['1','2','3','4','5','6','7','8','9']:
            marker=input("enter index ")
        if board[int(marker)]==' ':
            board[int(marker)]=player2
        else:
            print("That index is already taken. enter again")
            play(oddOReven,player1,player2,board)
        # oddOReven+=1
        
    return board
    
def status(board,p1,p2):
    pt1=0
    pt2=0
    ans=''
    if board[1]==board[2]==board[3]!=' ' and board[1]==board[2]==board[3]:
        ans=board[1]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    if board[4]==board[5]==board[6]!=' ' and board[4]==board[5]==board[6]:
        ans=board[4]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    if board[7]==board[8]==board[9]!=' ' and board[7]==board[8]==board[9]:
        ans=board[7]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    if board[7]==board[1]==board[4]!=' ' and board[7]==board[1]==board[4]:
        ans=board[7]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    if board[8]==board[5]==board[2]!=' ' and board[5]==board[8]==board[2]:
        ans=board[7]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    if board[6]==board[3]==board[9]!=' ' and board[3]==board[6]==board[9]:
        ans=board[7]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    if board[7]==board[5]==board[3]!=' ' and board[7]==board[3]==board[5]:
        ans=board[7]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    if board[5]==board[1]==board[9]!=' ' and board[1]==board[5]==board[9]:
        ans=board[7]
        if ans==p1:
            pt1+=1
        else:
            pt2+=1
    return [pt1,pt2]

print("Welcome to TIC TAC TOE")
p1,p2=user_choice()
for i in range(1,10):
    board=play(i,p1,p2,board)
    game_board(board)
  
pt1,pt2=status(board,p1,p2)  
if pt1>pt2:
    print("Player 1 won the match with ",pt1," points.")
elif pt2>pt1:
    print("Player 2 won the match with ",pt2," points.")
else:
    print("Game tied with ",pt1," points")