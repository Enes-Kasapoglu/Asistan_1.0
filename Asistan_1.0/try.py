""" import speech_recognition as sr
import pyaudio
r = sr.Recognizer()

#Burada ise cihaza bağlı olan mikrofondan veri almaya başlıyor,
#daha doğrusu mikrofonu dinlemeye başlıyor.
with sr.Microphone() as source:
     print("Birşeyler Söyle!")
     audio = r.listen(source)

#Bir ses sinyali geldiği anda onu google recognizer'ı ile tanımaya çalışıyor.
#Burada birçok seçeneğimiz var, Bing, Yandex vs. ama google en iyi çalışanı diyebilirim.

#Tanıdıktan sonra eğer dediğiniz şey boş bir ses değilse, yani tıkırtı vs. Dediğiniz geri döndürecek.
data = ""
try:
   data = r.recognize_google(audio, language='tr-tr')
   #data ​= data.lower()
   print("Bunu Söyledin :" + data)
except sr.UnknownValueError:
       print("Ne dediğini anlamadım") 

# --------------2------------------
def addtablefikralar(text):

	#cursor.execute("CREATE TABLE IF NOT EXISTS Fıkra (fıkra TEXT)")
	global texts

	#text = "Enes"

data = str(addtablefikralar(enes).text)
print(data)

# --------------------3----------------

"""
