import time
history = []
state = True

def is_repeating(hist):
    n = len(hist)

    half = n // 2
    left = hist[:half]
    right = hist[half:]

    # check for symmetry
    if left == right:
        #print("pattern!")
        return True

    # recursive check
    if len(right) > 2:
        return is_repeating(right)
    return False # if all else fails its false

x = 0
while True:
    #time.sleep(0.1)
    # anti-loop rule: detect repetition and flip
    state = is_repeating(history + [state])
    
    history.append(state)

    if state == True:
        print("█",end="")
    else:
        print(" ",end="")
    x += 1
    if x % 79 == 0:
        print()
