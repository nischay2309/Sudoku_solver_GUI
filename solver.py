board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



def print_board(x):   
    '''
    

    Parameters
    ----------
    x : list of lists representing the rows of board

    Returns
    -------
    prints the current board

    '''
    for i in range (len(x)):
        if i%3==0 and i != 0:
            print ('- - - - - - - - - - -')
        for j in range (len(x[0])):
            if j%3==0 and j!=0:
                print ('| ', end = '')
            if j==8:
                print (x[i][j])
            else:
                print (str(x[i][j])+' ', end='') 
                
                
                
def find_empty(x): 
    '''
    

    Parameters
    ----------
    x : list of lists representing the rows of board

    Returns
    -------
    finds the first empty box

    '''
    for i in range (len(x)):
            for j in range (len(x[0])):
                if (x[i][j]==0):
                    return (i,j)   #the empty box
    return False  #if the board is full 




def valid(x,num,pos): 
    '''
    

    Parameters
    ----------
    x : list of lists representing the rows of board
    num : the current number to check
    pos : the position on which we are checking the validity of num
        DESCRIPTION. The default is (row,col).

    Returns
    -------
    True, if the number is valid
    False, if the number is not valid 

    '''
    for i in range (len(x[0])): #checking row
        if x[pos[0]][i]==num and i!=pos[1]:
            return False 
        
    for i in range (len(x)): #checking column
        if (x[i][pos[1]])==num and i!=pos[0]:
            return False 
    
    box_i = pos[0]//3
    box_j = pos[1]//3
    for i in range (box_i*3,box_i*3+3):
        for j in range(box_j*3,box_j*3+3):
            if x[i][j]==num and (i,j) != pos:
                return False
    return True



def solve(x):
    '''

    Parameters
    ----------
    x : list of lists representing the rows of board.

    Returns
    -------
    prints the solved board.

    '''
    if find_empty(x)==0:
        print ('')
        print ("the solution is:")
        print ('')
        return print_board(x)
    else:
        pos = find_empty(x)
        for i in range (1,10):
            if valid (x,i,pos):
                x[pos[0]][pos[1]]=i
                solve(x)
                x[pos[0]][pos[1]]=0
print ('')
print ("The original board is:")
print ('')
print_board(board)
      

def output (x):
   i = input("do you want to see the solution now? (Enter Yes/No): ")
   if i == 'Yes' or i=='yes':
      solve(x)
      
      
   elif i == 'No' or i == 'no': 
      print ('')
      print ("Okay, I'll wait....")
      j = input("do you want to run the code again?: ")
      
      if j == 'Yes' or j=='yes':
         solve(x)
         
      elif i == 'No' or i == 'no': 
         print ('')
         print ("Alright, Goodbye..")
         
         
         
   elif i == ' ' or i == 'end' or i == 'cancel':
       print ('')
       print ('Alright, Goodbye..')
       
       
   else:
      print ('')
      print ('wrong input, try again')
      output (x)
 
output(board)   