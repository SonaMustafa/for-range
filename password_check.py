parol=input("Şifrə daxil edin: ")
boyukHerfler=0
kicikHerfler=0
reqemler=0
digerSimvollar=0
for i in parol:
    if i.isupper():
        boyukHerfler+=1
    elif i.islower():
        kicikHerfler+=1
    elif i.isdigit():
        reqemler+=1
    else:
        digerSimvollar+=1
print("Boyuk herfler:",boyukHerfler)
print("Kicik herfler:",kicikHerfler)
print("Reqemler:",reqemler)
print("Diger simvollar:",digerSimvollar)

if (len(parol)>8 and
    boyukHerfler>0 and
    kicikHerfler>0 and
    reqemler>0 and
    digerSimvollar>0):
    print("Şifrə güclüdür")
else: 
    print("Şifrə zəifdir")