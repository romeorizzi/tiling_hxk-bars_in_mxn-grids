import sys

H = 0   # horizontal placement of a tile (2 rows, 3 cols)
V = 1   # vertical placement of a tile (3 rows, 2 cols)

def is_tilable(m, n, h, k):
    assert h <= k
    if (m < k) or (n < h):
        return 0

    if (m*n)%(h*k):
        return 0
    return 1

def compose_tiling(m, n, h, k, place_tile):
    if n%2 == 0 and m%3 == 0:
        for i in range(1,m,3): #for every strip of 3 raws (deal each strip separately)
            for j in range(1,n,2):
                place_tile(i,j,V)
                #print(f"place_tile({i},{j},{H}) vertically",file=sys.stderr)
    elif m%2 == 0 and m%3 == 0:
        for i in range(1,m,2): #for every strip of 2 raws (deal each strip separately) 
            for j in range(1,n,3):
                place_tile(i,j,H)
                #print(f"place_tile({i},{j},{V}) horizontally",file=sys.stderr)
    # MANCANO ANCORA DEI CASI
