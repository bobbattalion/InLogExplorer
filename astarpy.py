def returnPath(closed):
    cn = closed[-1]
    path = []
    while(cn[4] != False):
        path.append(closed[cn[4]])
        cn = closed[cn[4]]

    return path

def getIndex(arr, val):
    for i in range(len(arr)):
        if(arr[i][0] == val[0] and arr[i][1] == val[1]):
            return i
            break

def astarPath(start, end, walls):
    sx = start[0]
    sy = start[1]

    ex = end[0]
    ey = end[1]

    checkx = [0, 0, -1, 1]
    checky = [-1, 1, 0, 0]

    h = abs(ex - sx) + abs(ey - sy)

    closed = [[sx, sy, h, 0, False]]
    open = []

    run = True

    cont = False
    counter = 30

    while(run):
        cn = closed[-1]

        vals = []
        for i in range(len(checkx)):
            if([cn[0] + checkx[i], cn[1] + checky[i]] not in walls):
                h = abs((cn[0] + checkx[i]) - ex) + abs((cn[1] + checky[i]) - ey);
                vals.append([cn[0] + checkx[i], cn[1] + checky[i], h, cn[3] + 1, len(closed) - 1])

        for v in range(len(vals)):
            if(vals[v] not in closed):
                if(vals[v] not in open):
                    open.append(vals[v])

                checknode = getIndex(open, vals[v])
                if(vals[v][3] < open[checknode][3]):
                    open[checknode] = vals[v]

        min = 2147483647
        index = 0
        for u in range(len(open)):
            if(open[u][2] + open[u][3] < min):
                min = open[u][2] + open[u][3]
                index = u

        closed.append(open[index])
        del open[index]
        for c in range(len(checkx)):
            if(cn[0] == ex and cn[1] == ey):
                run = False
                closed.append(cn)

        if(counter == 0):
            raise Exception()

        counter -= 1

    return returnPath(closed)

def astar(start, end, walls):
    try:
        out = astarPath(start, end, walls)

    except:
        out = []

    return out
