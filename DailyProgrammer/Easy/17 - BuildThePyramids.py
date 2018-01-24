"""


https://www.reddit.com/r/dailyprogrammer/comments/qheeu/342012_challenge_17_easy/

Note: This challenge text was deleted so I am reconstructing this based off of comments and solutions I looked at (cheating I know)

  

"""

def triangleBuilder(height = 3):
    """A function to build a triangle of a given height
  
  """
    for i in range(0, height + 1):
      s = ""
      character = "@"
      s += character * i
      print(s)
    
    

def upsideDownTriangleBuilder(height = 3):
  """A function to build a triangle of a given height
  
  """
    
  for i in range(height + 1, 0, -1):
    s = ""
    character = "@"
    space = " "
    s += character
    print(character * i)
    
upsideDownTriangleBuilder()
