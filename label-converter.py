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
def makeFile(item, width, height, xmin, ymin, xmax, ymax):
  name = "staircase"+str(item)+".txt"
  filez = open(name, "w+")
  string = calc(item, width, height, xmin, ymin, xmax, ymax)
  filez.write(string)
  filez.close()

#Implementing makeFile and creating labeled text
#makeFile(9, 203, 248, 59, 104, 161, 204)
makeFile(10, 193, 262, 64, 97, 132, 244)
makeFile(11, 275, 183, 162, 90, 249, 176)
makeFile(12, 178, 283, 41, 158, 145, 254)
makeFile(13, 177, 285, 47, 50, 126, 263)
makeFile(14, 225, 225, 25, 142, 102, 210)

""" 
#Testing Purposes
str1 = calc(1, 183, 276, 38, 99, 166, 226)
str2 = calc(2, 275, 183, 19, 18, 271, 172)
str3 = calc(3, 275, 183, 4, 6, 271, 177)
str4 = calc(4, 262, 192, 11, 4, 248, 163)
str5 = calc(5, 265, 190, 69, 33, 197, 151)
str6 = calc(6, 194, 259, 16, 58, 135, 219)
str7 = calc(7, 238, 212, 95, 64, 196, 162)
str8 = calc(8, 224, 224, 90, 130, 192, 205) """
""" calc(9, 203, 248, 59, 104, 161, 204)
calc(10, 193, 262, 64, 97, 132, 244)
calc(11, 275, 183, 162, 90, 249, 176)
calc(12, 178, 283, 41, 158, 145, 254)
string13 = calc(13, 177, 285, 47, 50, 126, 263)
print(string13) """
""" 
f1 = open("staircase1.txt", "w+")
f2 = open("staircase2.txt", "w+")
f3 = open("staircase3.txt", "w+")
f4 = open("staircase4.txt", "w+")
f5 = open("staircase5.txt", "w+")
f6 = open("staircase6.txt", "w+")
f7 = open("staircase7.txt", "w+")
f8 = open("staircase8.txt", "w+")

f1.write(str1)
f2.write(str2)
f3.write(str3)
f4.write(str4)
f5.write(str5)
f6.write(str6)
f7.write(str7)
f8.write(str8)


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
 """