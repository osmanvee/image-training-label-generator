#Author: Osman Warsi
#This generates labeled txt files using inputs (from xml or somewhere else)
#with the Yolo Mark format
##
#Calculating the normalized values for labeled text
# @params in corresponding xml file
def calc(item, width, height, xmin, ymin, xmax, ymax):
 
  #For Testing Purposes
  """ print("X_CENTER: ", round(((xmin+xmax)/2)/width, 6))
  print("Y_CENTER: ", round(((ymin+ymax)/2)/height, 6))
  print("WIDTH: ", round((xmax-xmin)/width, 6))
  print("HEIGHT: ", round((ymax-ymin)/height, 6)) """

  #Calculating values
  x = str(round(((xmin+xmax)/2)/width, 6))
  y = str(round(((ymin+ymax)/2)/height, 6))
  w = str(round((xmax-xmin)/width, 6))
  h = str(round((ymax-ymin)/height, 6))


  #Formatting final result string
  strin = "0"+" "+x+" "+y+" "+w+" "+h
  return strin

##
#MakeFile: Create .txt labeled file using xml inputs for Yolo
def makeFile(item):
  nameOutput = "staircase"+str(item)+".txt"
  nameInput = "staircase"+str(item)+".xml"
  width = outputValues(nameInput, "<width>")
  height = outputValues(nameInput, "<height>")
  xmin = outputValues(nameInput, "<xmin>")
  ymin =outputValues(nameInput, "<ymin>")
  xmax = outputValues(nameInput, "<xmax>")
  ymax = outputValues(nameInput, "<ymax>")
  filez = open(nameOutput, "w+")
  string = calc(item, width, height, xmin, ymin, xmax, ymax)
  filez.write(string)
  filez.close()

#Implementing makeFile and creating labeled text
#makeFile(9, 203, 248, 59, 104, 161, 204)
""" makeFile(10, 193, 262, 64, 97, 132, 244)
makeFile(11, 275, 183, 162, 90, 249, 176)
makeFile(12, 178, 283, 41, 158, 145, 254)
makeFile(13, 177, 285, 47, 50, 126, 263)
makeFile(14, 225, 225, 25, 142, 102, 210) """
""" 
makeFile(15, 183, 275, 56, 132, 111, 250)
makeFile(16, 275, 183, 73, 36, 159, 171)
makeFile(17, 183, 275, 62, 53, 132, 252)
makeFile(18, 278, 181, 102, 92, 176, 157)
makeFile(19, 357, 141, 176, 51, 255, 122)
makeFile(20, 270, 187, 102, 32, 160, 167)
makeFile(21, 189, 267, 2, 17, 182, 202)
makeFile(22, 310, 163, 30, 26, 121, 157)
makeFile(23, 275, 183, 50, 72, 115, 161)
makeFile(24, 229, 220, 8, 29, 192, 193)
makeFile(25, 251, 201, 58, 10, 251, 149)
makeFile(26, 194, 259, 41, 146, 108, 255)
makeFile(27, 183, 275, 30, 70, 120, 245)
makeFile(28, 300, 168, 36, 60, 110, 168)
makeFile(29, 300, 168, 156, 11, 250, 164)
makeFile(30, 275, 183, 76, 34, 165, 168)
makeFile(31, 185,273, 27, 36, 144, 245)
makeFile(32, 275, 183, 49, 62, 105, 158)
makeFile(33, 275, 183, 2, 17, 148, 177)
makeFile(34, 225, 225, 73, 101, 187, 200)
makeFile(35, 183, 275, 74, 137, 167, 229)
makeFile(36, 225, 225, 120, 78, 203, 220)
makeFile(37, 275, 183, 115, 93, 167, 154)
makeFile(38, 225, 225, 24, 134, 79, 206)
makeFile(39, 331, 152, 55, 43, 119, 149)
makeFile(40, 225, 225, 132, 78, 223, 225)
makeFile(41, 275, 183, 98, 6, 212, 183)
makeFile(42, 275, 183, 110, 55, 167, 163)
makeFile(43, 250, 201, 62, 59, 210, 201)
makeFile(44, 225, 225, 95, 116, 181, 225)
makeFile(45, 225, 225, 89, 122, 156, 225)
makeFile(46, 194, 259, 45, 6, 146, 259) """

""" Second WAVE"""
""" makeFile(47, 260, 194, 84, 36, 207, 194)
makeFile(48, 257, 196, 122, 97, 236, 196)
makeFile(49, 290, 174, 157, 40, 277, 174)
makeFile(50, 168, 299, 31, 33, 160, 299)
makeFile(51, 206, 245, 8, 49, 153, 225)
makeFile(52, 300, 168, 114, 8, 247, 153)
makeFile(53, 193, 261, 97, 116, 182, 248)
makeFile(54, 274, 184, 111, 77, 181, 184)
makeFile(55, 234, 215, 27, 117, 136, 203)
makeFile(56, 183, 275, 48, 140, 156, 237)
makeFile(57, 183, 275, 35, 82, 155, 216) """
def split(word): 
    return [char for char in word] 



def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

#Getting specific output values from XML files
def outputValues(str, tag):
  g = open(str, "r")
  index = g.read().find(tag)
  g.seek(index+5)
  word = g.read( (index+6) - index )
  numbers = []

  for x in split(word):
    if x.isdigit():
      numbers.append(x)
  g.close()
  return int(listToString(numbers))

