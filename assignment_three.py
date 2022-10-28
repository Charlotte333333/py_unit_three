#CharlotteMoore 10/19/22 (the purpose of this prom is to calculate the area of any given prism)


print("Answer the questions  asked by the machine to calculate the area of a prism.")


def width():
  """This function collects the width of a rectangle"""
  width = int(input("What is the rectangles width?"))
  return width



def length():
   """This function collects the length of a rectangle"""
   length = int(input("What is the rectangles length?"))
   return length


def height():
   """This function collects the height of a rectangle"""
   height = int(input("what is the rectangles height?"))
   return height


def calculaterectangle(length, width):
   """This function calculates the area of a rectangle"""
   areaOfRectangle = (length * width)
   return areaOfRectangle


def totalsurface(length, width, height):
   """This function collects the length width and height for a prism and then prints the totaln surface of a prism"""
   top = int(calculaterectangle(length, width))
   bottom = int(calculaterectangle(length, width))
   leftSide = int(calculaterectangle(height, width))
   rightSide = int(calculaterectangle(height, width))
   front = int(calculaterectangle(height, length))
   back = int(calculaterectangle(height, length))
   total = int((top+bottom+back+leftSide+rightSide+front))
   print("The total surface area is", total)
   return

def main():
   """This function takes the length, width, and height for the final calculation"""
   l = length()
   w = width()
   h = height()
   totalsurface(l, w, h)

main()






