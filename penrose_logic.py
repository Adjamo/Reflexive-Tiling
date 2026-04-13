history = []
state = True

def is_repeating(hist):
    n = len(hist)

    half = n // 2
    left = hist[:half]
    right = hist[half:]

    # check for symmetry
    if left == right:
        print("pattern!")
        return not state

    # recursive check
    if len(right) > 2:
        return is_repeating(right)
    return False # if all else fails its false


while True

    # anti-loop rule: detect repetition and flip
    state = is_repeating(history + [state])
    
    history.append(state)

    print(state)
 
   
#print(history)

