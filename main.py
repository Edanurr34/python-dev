print("Kodlamio")
baslik = "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik= "İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade= 36
ekVade =12
vade2 = "36"
#float, decimal, double
aylik_odeme= 200.50
#bool,boolean => True veya False
yukselisteMi = False

#matematiksel operatörler
# +
print(5+5)
print(vade + 12)
print(vade + ekVade)
print(36+6)
# -
print(5-5)
print(vade-12)
print(vade - ekVade)
print(36-6)
# *
print(5*5)
print(vade*2)
print(vade * ekVade)
print(10*10)

# /
print(5/5)
print(vade/2)
print(vade / ekVade)
print(10/2)

yeniVade = vade /2
fiyat= 100
indirimFiyat = fiyat-20

print(yeniVade)
print(indirimFiyat)

#mod operatörü
print(10%2)
print(vade%5)
print(vade% ekVade)
print(30%10)

#mantıksal operatörler
print(1==1)
print(1==2)

print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print(1!=1)
print(1!=2)

#or and

#or=> veya
print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)
print(1>2 and 5>2 and 3>2)
print(2>1 or 1>2 and 3>2) #and önce çalıştırılır

#karar yapıları
#if else

sayi1=10
sayi2=15
#sayi1 sayi2'den büyükse ekrana sayi1 daha büyük yazdır.
if sayi1<sayi2:
    print("Sayi1, sayi2'den küçüktür.")
    print("Hala if blogunun içindeyiz")
elif sayi1 == sayi2:
    print("Sayi1 ve sayi2 eşittir.")
else:
    print("Sayi1, sayi2'den büyüktür.")

print("Burası if blogunun dışıdır.")
if sayi1<=sayi2:
    print("Sayi1 sayi2' den küçüktür.")
if sayi1 == sayi2:
    print("İki sayi eşittir")
else:
    print("Sayi1 sayi2'den büyüktür.")
print("Burası if blogunun dışıdır.")
   


