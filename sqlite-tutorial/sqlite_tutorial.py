# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 23:19:42 2022


   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣤⣤⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣶⣤⣄⣉⣉⠙⠛⠛⠛⠛⠛⠛⠋⣉⣉⣠⣤⣶⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣄⡉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⢉⣠⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣶⣤⣈⡉⠛⠛⠻⠿⠿⠿⠿⠿⠿⠟⠛⠛⢉⣁⣤⣶⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀


*** ---------- SQLite Tutorial ----------
            @author: azizcanhamas
"""
#%%
# Veritabanina baglanma
import sqlite3 as sql
#kitaplar.sqlite veritabanına bağlan. Böyle bir veritabanı yoksa oluştur.
db=sql.connect("kitaplar.sqlite")
db.close()

#%%
# Gecici veritabanlarinin bellek ve disk uzerinde olusturulmasi
import sqlite3 as sql
#RAM üzerinde veritabanı oluşturur. Program sonlandığında siler.
db=sql.connect(":memory:")
#Disk üzerinde veritabanı oluşturur. Program sonlandığında siler.
db=sql.connect("''")
db.close()

#%%
# Veritabani üzerinde komut calistirabilmek icin imlec olusturulmasi
import sqlite3 as sql
db=sql.connect("kitaplar.sqlite")
#Veritabanı üzerinde komutlar çalıştırabilmek için imleç oluştur.
im=db.Cursor()
db.close()

#%%
# 2 sütunlu bir tablonun olusturulmasi
import sqlite3 as sql
db=sql.connect("sinif_listesi.sqlite")
cur=db.cursor()
##Adres defteri isimli bir tablo oluştur ve isim ve soyisim adinda sütunlar tanımlar.
cur.execute("CREATE TABLE sinifListesi (isim,soyisim)")
db.close()

#%%
# Mevcut bir tablonun tekrar olusturulmaya calisilmasi
import sqlite3 as sql
db=sql.connect("sinif_listesi.sqlite")
cur=db.cursor()
#Tablo mevcut hatasi vermemesi icin (IF NOT EXISTS) eklenir.
cur.execute("CREATE TABLE IF NOT EXISTS sinifListesi (isim,soyisim)")
db.close()

#%%
# Bir verinin veritabanina islenmesi
import sqlite3 as sql
db=sql.connect("sinif_listesi.sqlite")
cur=db.cursor()
cur.execute("INSERT INTO sinifListesi VALUES ('Aziz Can','Hamasoglu')")
db.commit()
db.close()

#%%
# Disardan gelen verilerin veritabanina islenmesi
import sqlite3 as sql
db=sql.connect("sinif_listesi.sqlite")
cur=db.cursor()
veriler=[("Feyza","Gür"),
          ("Ela","Kılıç"),
          ("Burcu","Ramazan")]
for i in veriler:
    cur.execute("INSERT INTO sinifListesi values (?,?)",i)
db.commit()
db.close()

#%%
# Veritabanindan tüm verilerin okunmasi
import sqlite3 as sql
db=sql.connect("sinif_listesi.sqlite")
cur=db.cursor()
res=cur.execute("SELECT * from sinifListesi")
values=res.fetchall()
for i in values:
    print(i)
db.commit()
db.close()

#%%
# Veritabaninda hangi tablolarin bulundugunun bulunmasi
import sqlite3 as sql
db=sql.connect("kitaplar.sqlite")
cur=db.cursor()
res=cur.execute("SELECT name FROM sqlite_master")
value=res.fetchall()
print(value)
db.commit()
db.close()

#%%
# fetchone() metodu ile verilerin birer birer alinmasi
import sqlite3 as sql
db=sql.connect("sinif_listesi.sqlite")
cur=db.cursor()
response=cur.execute("SELECT * from sinifListesi")
while True:
    tmp=response.fetchone()
    if tmp==None:
        break
    print(tmp)
db.close()

#%%
# WHERE parametresi ile Veri Suzme
import sqlite3 as sql
db=sql.connect("sinif_listesi.sqlite")
cur=db.cursor()
response=cur.execute("SELECT * from sinifListesi WHERE soyisim=='Gür'")

print(*response)

# for i in response:
    # print(i)

# value=response.fetchall()
# print(value)
db.close()

#%%
#SQL Injection
import sqlite3 as sql
#Database olustur ve test verisi isle.
db=sql.connect(":memory:")
cur=db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS admins (username,password)")

veriler=[("ahmetkalkin","12az87"),("sinanergin","s41aergin"),("betulay","35698betul")]
for i in veriler:
    cur.execute("INSERT INTO admins VALUES (?,?)",i)
db.commit()

in_user=input("username: ")
in_pass=input("password: ")

response=cur.execute("SELECT * from admins WHERE username='%s' and password='%s'"%(in_user,in_pass))

status=response.fetchone()
if status:
    print("Login successful.")
else:
    print("Permission denied!")

#           x' OR '1' = '1
# input kisminda username ve password olarak  
# girilirse SQL Injection gerceklesir. Sistem iceri alir!

#           x' OR '1' = '1' --
# input kisminda username olarak girilirse password bos gecilebilir.
# sistem -- isaretinden dolayi geriye kalan kismi yorum olarak algilar.

# SQL Injection islemini onlemek icin %s gibi deger atamalari KULLANILMAMALIDIR!
# Bunun yerine ?(soru isareti) parametresi kullanilmalidir.

# Baska bir SQL Injection onleme yontemi olarak kullanicidan alinan degerler
# alfanumerik karakterler ile sinirlandirilabilir. Bu sayede kullanici
# deger olarak ' , -- , = gibi degerler gonderemez.

db.close()
    

