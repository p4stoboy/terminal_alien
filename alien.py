import random
from colors import color

c1 = random.randint(1,255)
c2 = random.randint(1,255)
c3 = random.randint(1,255)

#initial parameters
size = 3
blank = " "
on = 2*size*"█"
off = 2*size*blank
alien = []


#generate alien
for i in range(28):
    choice = random.randint(0,1)
    if choice == 0:
        alien.append(off)
    else:
        alien.append(on)



print(
      color(alien[0]+alien[1]+alien[2]+alien[3]+alien[2]+alien[1]+alien[0]+"\n"      
     +alien[0]+alien[1]+alien[2]+alien[3]+alien[2]+alien[1]+alien[0]+"\n"
     +alien[0]+alien[1]+alien[2]+alien[3]+alien[2]+alien[1]+alien[0]+"\n", c1)      

     +color(alien[4]+alien[5]+alien[6], c1)+color(alien[7], c2)+color(alien[6]+alien[5]+alien[4], c1)+"\n"      
     +color(alien[4]+alien[5]+alien[6], c1)+color(alien[7], c2)+color(alien[6]+alien[5]+alien[4], c1)+"\n"
     +color(alien[4]+alien[5]+alien[6], c1)+color(alien[7], c2)+color(alien[6]+alien[5]+alien[4], c1)+"\n"      

     +color(alien[8]+alien[9], c1)+color(alien[10], c2)+color(alien[11], c3)+color(alien[10], c2)+color(alien[9]+alien[8], c1)+"\n"      
     +color(alien[8]+alien[9], c1)+color(alien[10], c2)+color(alien[11], c3)+color(alien[10], c2)+color(alien[9]+alien[8], c1)+"\n"
     +color(alien[8]+alien[9], c1)+color(alien[10], c2)+color(alien[11], c3)+color(alien[10], c2)+color(alien[9]+alien[8], c1)+"\n"      

     +color(alien[12], c1)+color(alien[13], c2)+color(alien[14]+alien[15]+alien[14], c3)+color(alien[13], c2)+color(alien[12], c1)+"\n"      
     +color(alien[12], c1)+color(alien[13], c2)+color(alien[14]+alien[15]+alien[14], c3)+color(alien[13], c2)+color(alien[12], c1)+"\n"
     +color(alien[12], c1)+color(alien[13], c2)+color(alien[14]+alien[15]+alien[14], c3)+color(alien[13], c2)+color(alien[12], c1)+"\n"      

     +color(alien[16]+alien[17], c1)+color(alien[18], c2)+color(alien[19], c3)+color(alien[18],c2)+color(alien[17]+alien[16], c1)+"\n"      
     +color(alien[16]+alien[17], c1)+color(alien[18], c2)+color(alien[19], c3)+color(alien[18],c2)+color(alien[17]+alien[16], c1)+"\n"
     +color(alien[16]+alien[17], c1)+color(alien[18], c2)+color(alien[19], c3)+color(alien[18],c2)+color(alien[17]+alien[16], c1)+"\n"      

     +color(alien[20]+alien[21]+alien[22], c1)+color(alien[23], c2)+color(alien[22]+alien[21]+alien[20], c1)+"\n"      
     +color(alien[20]+alien[21]+alien[22], c1)+color(alien[23], c2)+color(alien[22]+alien[21]+alien[20], c1)+"\n"
     +color(alien[20]+alien[21]+alien[22], c1)+color(alien[23], c2)+color(alien[22]+alien[21]+alien[20], c1)+"\n"      

     +color(alien[24]+alien[25]+alien[26]+alien[27]+alien[26]+alien[25]+alien[24]+"\n"      
     +alien[24]+alien[25]+alien[26]+alien[27]+alien[26]+alien[25]+alien[24]+"\n"
     +alien[24]+alien[25]+alien[26]+alien[27]+alien[26]+alien[25]+alien[24], c1)+"\n"     
      )
