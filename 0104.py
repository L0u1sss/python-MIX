import math
w = float(input('น้ำหนัก : '))
h = float(input('ส่วนสูง : '))
mos = math.sqrt(h*w)/60
hay = 0.024265*w**(0.5378)*h**(0.3964)
boy = 0.0333*w**(0.6157-0.0188*math.log(w,10))*h**0.3
print(mos)
print(hay)
print(boy)