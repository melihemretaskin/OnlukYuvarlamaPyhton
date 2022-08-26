# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

n1 = input("birinci sayı : ")
n2 = input("ikinci sayı: ")
sum = float(n1) + float(n2)

if float(n1) + float(n2) <= float(int(sum) + 0.49):
 print("{0} + {1} = {2} ".format(n1,n2,int(sum)))
 #print("yuvarlama : {0} ".format(int(sum)+1))
 print("Kücüğe yuvarlama")
 print("Rasyonel hali: {0}".format(sum))
if float(n1) + float(n2) >= float(int(sum)+0.5):
     print("{0} + {1} = {2}".format(n1,n2,int(sum)+1))
     print("Büyüğe yuvarlama")


