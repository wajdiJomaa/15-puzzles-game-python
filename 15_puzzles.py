from random import randint
import numpy as np

def is_solvable (puzzle) :
    inversions = 0
    for i in range(len(puzzle)-1) :
        for j in range(i,len(puzzle)-1) :
            if puzzle[j] < puzzle[i] :
                inversions += 1
    return inversions%2 == 0

def shuffle (puzzle):
    for i in range (len(puzzle)-1) :
        j = randint(0,14)
        puzzle[i],puzzle[j] = puzzle[j],puzzle[i]

def correcte (puzzle):
    if is_solvable(puzzle) :
        return
    else :
        i = randint(0,14)
        j = randint (0,14)
        puzzle[i],puzzle[j] = puzzle[j],puzzle[i]
        correcte(puzzle)

def generate ():
    puzzle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"X"]
    shuffle (puzzle)
    correcte (puzzle)
    arr = np.array(puzzle)
    return np.reshape(arr,(4,4)).tolist()

print(generate())