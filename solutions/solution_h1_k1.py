import sys

H = 0   # horizontal placement of a tile
V = 1   # vertical placement of a tile

def is_tilable(m, n):
   return 1 - (m%2)*(n%2)

def compose_tiling(m, n, place_tile):
   if n%2 == 0:
       for i in range(1,m+1): #for every raw (deal each raw separately)
           for j in range(1,n,2):
               place_tile(i,j,H)
               #print(f"place_tile({i},{j},{H}) horizzontally",file=sys.stderr)
   elif m%2 == 0:
       for j in range(1,n+1): #for every column (split the problem into separate columns)
          for i in range(1,m,2): 
               place_tile(i,j,V)
               #print(f"place_tile({i},{j},{V}) vertically",file=sys.stderr)

