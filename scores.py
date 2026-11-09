scores = [78, 92, 65, 88, 100, 54, 91, 73]
cem=0
ortaBal=0
_90balUstuSayi=0
enYuksekBal=0
for i in scores:
    cem=cem+i
    ortabal=cem/8
    if i>=90:
        _90balUstuSayi=_90balUstuSayi+1
    if i>enYuksekBal:
        enYuksekBal=i
print("Ən yüksək bal:", enYuksekBal)
print("Cəm=",cem)
print("Orta Bal=",ortaBal)
print("90 bal və yuxarı bal alanların sayı:",_90balUstuSayi)
print("Ən yüksək bal:",enYuksekBal)