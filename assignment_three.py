#CharlotteMoore 10/19/22 (the purpose of this prom is to calculate the area of any given prism)


print("Answer the questions  asked by the machine to calculate the area of a prism.")


def width():
   width = int(input("What is the rectangles width?"))
   return width



def length():
   length = int(input("What is the rectangles length?"))
   return length


def height():
   height = int(input("what is the rectangles height?"))
   return height



def calculaterectangle(length, width):
   areaOfRectangle = (length*width)
   return areaOfRectangle


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

length= length()
width= width()
height= height()
totalsurface(length, width, height)






