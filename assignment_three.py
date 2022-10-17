def calculaterectangle():
   areaOfRectangle = (length*width)
   return



def totalsurface(length, width, height):
   top = int(calculaterectangle(length, width))
   bottom = int(calculaterectangle(length, width))
   leftSide = int(calculaterectangle(height, width))
   rightSide = int(calculaterectangle(height, width))
   front = int(calculaterectangle(height, length))
   back = int(calculaterectangle(height, length))
   total = int((top+bottom+back+leftSide+rightSide+front))
   print(total)
   return

totalsurface(4, 3, 9)






