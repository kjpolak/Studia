import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 15
#alive = 1
#dead = 0
#vals = [alive, dead]

board = np.random.choice(2, N*N, p=[0.25, 0.75]).reshape(N, N)

def update(data):
  global board
  newboard = board.copy()
  for i in range(N):
    for j in range(N):
      total = (board[i, (j-1)%N] + board[i, (j+1)%N] + 
               board[(i-1)%N, j] + board[(i+1)%N, j] + 
               board[(i-1)%N, (j-1)%N] + board[(i-1)%N, (j+1)%N] + 
               board[(i+1)%N, (j-1)%N] + board[(i+1)%N, (j+1)%N])
      if board[i, j]  == 1:
        if (total < 2) or (total > 3):
          newboard[i, j] = 0
      else:
        if total == 3:
          newboard[i, j] = 0
  mat.set_data(newboard)
  board = newboard
  return [mat]

fig, ax = plt.subplots()
mat = ax.imshow(board)
ani = animation.FuncAnimation(fig, update, interval=20)
plt.show()


