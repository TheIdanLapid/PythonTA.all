def win(n,m,hlst,show=False):
    ''' determines if in a given configuration, represented by hlst,
    in an n-by-m board, the player who makes the current move has a
    winning strategy. If show is True and the configuration is a win,
    the chosen new configuration is printed.'''
    
    assert n>0 and m>0 and min(hlst)>=0 and max(hlst)<=n and len(hlst)==m
    if sum(hlst)==0:
        return True
    for i in range(m):  # for every column, i
        for j in range(hlst[i]): # for every possible move, (i,j)
            move_hlst = [n]*i+[j]*(m-i) # full height up to i, height j onwards
            new_hlst = [min(hlst[i],move_hlst[i]) for i in range(m)] # munching
            if not win(n,m,new_hlst):
                if show:
                    print(new_hlst)
                return True
    return False
