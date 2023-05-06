


file=open("data.txt","a")
w=input("whats Your Name ")
x=int(input("බර Kg වලින් "))
z=int(input("උස Cm වලින් "))
a=z/100;
y=a*a;

b=x/y;
file.write("%s-%s\n"%("weight:-",x))
file.write("%s-%s\n"%("high:-",z))
file.write("%s-%f\n"%(w,b))


if b<18.5:
      print(w,"ඔබට අඩුබර (මන්දපෝෂණය)")
      file.write("%s-%s\n\n"%(w,"Obata Adu Bara(Mandhaposanaya)"))
elif 18.5<b<25:
      print(w,"ඔබ නීරෝගියි ☺")
      file.write("%s-%s\n\n"%(w,"Oba Nirogiy"))
elif 25<b<30:
      print(w,"ඔබට අධිබර")
      file.write("%s-%s\n\n"%(w,"Obat Adhi Bara"))
else :
      print(w,"ඔබට ස්ථුලතාව")
      file.write("%s-%s\n\n"%(w,"Obata Sthulathawa"))

print("BMI අගය:",b)      
print("                Software By Gayanthaka Heshan")
file.close()


