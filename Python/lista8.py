import numpy as np
import matplotlib.pyplot as plt

def game_of_life(n,iter_,pb):
    board = np.random.choice(2,(n,n),p=[1-pb,pb])
    t = plt.imshow(board)
    while iter_>0: 
        new_board = np.copy(board)
        changed = False
        for i in range(n):
            for j in range(n):
                ln = (board[i, (j-1)%n] + board[i, (j+1)%n] + 
               board[(i-1)%n, j] + board[(i+1)%n, j] + 
               board[(i-1)%n, (j-1)%n] + board[(i-1)%n, (j+1)%n] + 
               board[(i+1)%n, (j-1)%n] + board[(i+1)%n, (j+1)%n])
                if board[i,j]:
                    if ln != 2 and ln != 3:
                        new_board[i,j] = 0
                        changed = True
                else:
                    if ln == 3:
                        new_board[i,j] = 1
                        changed = True
        if not changed:
            break

        board = new_board

        t.set_data(board)
        plt.draw()
        plt.pause(0.01)
        iter_ -= 1

game_of_life(42,100,0.25)
