import speech_recognition as srec
from gtts import gTTS
import os

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan....')
        suara = mendengar.listen(source,phrase_time_limit=5)
        try: 
            print('Diterima...')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except: 
            pass
        return dengar

def ngomong(self):
    teks = (self)
    bahasa = 'id'
    namafile = 'Ngomong.mp3'
    def reading():
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        os.system(f'start {namafile}')
    reading()

def run_Jarvis():
    Layanan = perintah()
    #print(Layanan)
    ngomong(Layanan)

run_Jarvis()



## Penjelasan Kode: Voice Assistant Menggunakan speech_recognition dan gTTS
## Kode ini adalah contoh implementasi asisten suara sederhana menggunakan pustaka speech_recognition untuk mengenali suara dan gTTS untuk menghasilkan suara. Berikut adalah penjelasan dari setiap bagian kode:

## 1. Mengimpor Pustaka yang Dibutuhkan

## import speech_recognition as srec
## from gtts import gTTS
## import os

## Kode ini mengimpor pustaka speech_recognition dengan alias srec, gTTS untuk text-to-speech, dan os untuk menjalankan perintah sistem.

## 2. Fungsi perintah

# def perintah():
  ## mendengar = srec.Recognizer()
    ## with srec.Microphone() as source:
       ## print('Mendengarkan....')
        ## suara = mendengar.listen(source, phrase_time_limit=5)
        ## try: 
           ## print('Diterima...')
            ## dengar = mendengar.recognize_google(suara, language='id-ID')
            ## print(dengar)
        ## except: 
           ## pass
        ## return dengar

## Fungsi perintah ini digunakan untuk mendengarkan suara dari mikrofon. Berikut langkah-langkahnya:
  ## - Membuat objek Recognizer dari speech_recognition.
  ## - Menggunakan mikrofon sebagai sumber suara (source).
  ## - Mendengarkan input suara dari mikrofon dengan batas waktu 5 detik (phrase_time_limit=5).
  ## - Menggunakan API Google untuk mengenali suara dalam bahasa Indonesia (language='id-ID').
  ##- Mengembalikan teks yang dikenali.

## 3. Fungsi 'ngomong'

## def ngomong(self):
   ## teks = (self)
    ## bahasa = 'id'
    ## namafile = 'Ngomong.mp3'
    ## def reading():
       ## suara = gTTS(text=teks, lang=bahasa, slow=False)
        ## suara.save(namafile)
        ## os.system(f'start {namafile}')
    ## reading()

## Fungsi ngomong ini digunakan untuk mengubah teks menjadi suara. Berikut langkah-langkahnya:
  ## - Mengambil teks sebagai input (self).
  ## - Menetapkan bahasa sebagai 'id' untuk bahasa Indonesia.
  ## - Menyimpan file suara dengan nama 'Ngomong.mp3'.
  ## - Fungsi reading menggunakan gTTS untuk mengubah teks menjadi suara dan menyimpannya sebagai file MP3.
  ## - Menjalankan file MP3 menggunakan perintah sistem.

## 4.  Fungsi 'run_michelle'

##def run_michelle():
  ##  Layanan = perintah()
  ##  ngomong(Layanan)

## Fungsi run_michelle menggabungkan kedua fungsi di atas:
  ## - Memanggil fungsi perintah untuk mendapatkan input suara yang diubah menjadi teks.
  ## - Memanggil fungsi ngomong untuk mengubah teks tersebut menjadi suara dan memutarnya.

## 5. Menjalankan Fungsi 'run_michelle'

## run_michelle()

## Memanggil fungsi 'run_michelle' untuk menjalankan keseluruhan proses.