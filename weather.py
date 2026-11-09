temperatures = [-3, 2, 8, 15, 22, 27, 31]
for i in (temperatures):
    if i<0:
        print("1-ci gün", str(i)+"° →", "Şaxta")
    elif i>=0 and i<=9:
        print("2-ci gün", str(i)+"° →", "Soyuq")
    elif i>=10 and i<=19:   
        print("3-ci gün", str(i)+"° →", "Mülayim")
    elif i>=20 and i<=29:
        print("4-ci gün", str(i)+"° →", "İsti")
    else:
        print("5-ci gün", str(i)+"° →", "Çox isti")