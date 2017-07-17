def seq(x):
    seq_ = [x]
    if x < 1:
        return []
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        seq_.append(x)    
    return seq_

print seq(12)
