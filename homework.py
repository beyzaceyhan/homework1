'''HAFTA 1 ÖDEV 1
SORU1
>>>Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

Python dilini kullanırken metin,sayı,liste vb. verileri saklamak için kullandığımız,verilerimizi saklayabileceğimiz,
işimizi kolaylaştıran veri tipleri vardır.
Metinsel ifadeleri:STRİNG veri tipiyle depolayabiliriz.
ad=Ayse >String veri tipi
Sayısal ifadeleri:İNTEGER,FLOAT,COMPLEX veri tipleriyle depolayabiliriz.
yas=25 >İnteger veri tipi:Tam sayılarda kullanılır.
faiz=12.5 >Float veri tipi:Ondalıklı sayılarda kullanılır.
veri=87.j >Complex veri tipi:Geçek ve sanal kısımdan oluşan karmaşık sayılarda kullanılır.
Dizisel ifadeleri:LİST,RANGE,TUPLE veri tipleriyle depolayabiliriz.
üyeler=["Selami","Yusuf","Kemal"] >List veri tipi:Bu tip sayesinde birden fazla veri dizisi tek tip altında toplanır.Bunun içinde
string,integer,float değerler barınabilir. : üyeBilgi["Sevil","Ayse",27,42.5] cıktı: ['Sevil','Ayse',27,42.5]
ögrenciAd=("Sevgi","Ahmet","Ezgi") >Tuple veri tipi:Bu veri tipinde parantez kullanılır.
for i in range(5):
print(i) > Range veri tipi:Verilen değerler arasında sayısal bir dizin oluşturur.Çıktıda 0 1 2 3 4 görürüz.
Ayrıca pythonda SET,FROZENSET,BYTES,BYTEARRAY,MEMORYVİEW,BOOL,DİCT gibi veri tipleri de vardır.

SORU2
>>>Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

STRİNG:Sitede sağ üstte gördüğümüz kurslarım,tüm kurslar,kariyer,sıkça sorulan sorular gibi yazıların yanı sıra bu butonlardan örneğin
tüm kurslar butonuna tıkladığımızda gördüğümüz kurs bilgilendirmeleri mesela :Java gibi metinsel ifadeler string veri tipine örnektir.
Ayrıca bu kursların tanıtımı yapılırken örneğin 25 gün sürecek gibi bir ifade varsa bu da string veri tipine girer buradaki 25 metinsel
bir ifadedir matematiksel bir işleme sokulamaz.

FLOAT,İNTEGER:Başlamış olduğumuz bir kursun yüzde kaç tamamlandığı gibi göstergeler float ya da integer veri tiplerine örnektir.%25 gibi bir 
ifade integer olacakken %45.5 gibi bir ifade float veri tipine örnek olur.

SORU3
>>>Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

Kodlama.io sitesine girerken girdiğimiz şifre oluşturduğumuz şifreye denk değilse burlarda if else şart blokları devreye girer ve 
şifremiz yanlış olduğundan siteye giremeyiz.'''
sifre='kodlamayapiyorum'
sifre1='kodlamayapiyorum'
if sifre == sifre1 :
    print("Basariyla giris yaptiniz.")  #Oluşturduğumuz şifre ve girdiğimiz şifre denk olduğu için giriş yapabildik.
#Giriş yapamadığımız bir örnek:    
kullaniciAdi='userkim'
kullaniciAdi1='userkom'
if kullaniciAdi == kullaniciAdi1 :
    print('Basariyla giris yaptiniz.')
else:
    print('Kullanici adi ya da sifre hatali.') 


