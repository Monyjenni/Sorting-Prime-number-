#amount = 0
#for num in range(100,201):
 #   if all(num%i!=0 for i in range(2,num)):
  #      #print(num)
   #     amount = amount + 1
#print(amount)
amount=0
prime= True
for num in range(100,201):
    for i in range(2,num):
        if(num%i == 0):
            prime = False
            break
    if(prime):
        print(num)

