a=str(input("Söz və ya cümlə daxil edin: "))
saitler=["a","ı","o","u","e","ə","i","ö","ü"]
k=0
for i in a.lower():
    for j in saitler:
        if i==j:
            k=k+1
print("Saitlərin sayı:",k)