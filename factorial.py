a=int(input("Ədəd daxil edin: "))
if a<0:
    print("Mənfi ədəd daxil etdiniz. Zəhmət olmasa müsbət ədəd daxil edin.")
f=1
for i in range(1,a+1):
    f=f*i   
print("Faktorial:",f)