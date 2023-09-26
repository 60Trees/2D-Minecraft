#from perlin_noise import PerlinNoise
import random
import noise

def generate_map(tilemapWidth, tilemapHeight, SEED):
  
 def terrain():
  
  def generate(w):
   out = (noise.pnoise2(float(1 / tilemapWidth * w), 0, base=SEED) + 1) / 2
   return out
 
  def num(w, h):
   random.seed(int(w / 5))
   jagger = 3

   if jagger < 0: jagger = 0
   if w == 0: w = 1
   sze = generate(w)
   sze *= tilemapWidth
   sze2 = sze
   if jagger > 0:
    sze2 += random.random() * jagger
    
   if h == int(sze): return 1        # Grass
   elif h < int(sze): return 0       # Air
   elif h < int(sze2) + 4: return 2        # Dirt
   else: return 3           # Stone

  global MAP
  MAP = [[num(__, _) for _ in range(tilemapWidth)] for __ in range(tilemapHeight)]
 terrain()
 
 def count(blockIndex):
  for I in range(tilemapWidth):
   pass
  
  
  pass
 
 
 def grow(plantFrequency, treeFrequency, treeHeight1, treeheight2):
  
  global randTreeHeight
  randTreeHeight = (treeHeight1, treeheight2)
  # Plant grass and saplings
  
  
  
  for X in range(tilemapWidth):
   
   # Grass
   if plantFrequency > 0:
    
    # Singular grass
    if random.randint(plantFrequency, 10) == 10:
     Temp = 0
     
     while MAP[X][Temp] != 1:
      Temp += 1
     Temp -= 1
     
     MAP[X][Temp] = 22
    
    # Tall Grass
    if random.randint(plantFrequency, 20) == 10:
     Temp = 0
     
     while MAP[X][Temp] == 0:
      Temp += 1
     Temp -= 1
     
     MAP[X][Temp] = 20
     MAP[X][Temp - 1] = 21

   if treeFrequency > 0:
    
    
    if random.randint(treeFrequency, 10) == 10:
     
     # Planting saplings
     Temp = 0
     vPos = X
  while MAP[X][Temp] == 0 or MAP[X][Temp] != 1: Temp += 1
  Temp -= 1
    
  treeHeight = random.randint(treeHeight1, treeheight2)
  for H in range(treeHeight):
   MAP[X][Temp - H] = 24

  # Growing saplings
  
  
  # Grow trees
 
 for X in range(tilemapWidth):
  pass
  
  
 
 grow(6, 4, 4, 6)
 
 return(MAP)

print("You are running 2D Minecraft from world gen")