#PROGRAM DETEKSI COVID-19 ONLINE
#UTS DASAR PEMOGRAMAN IK-1E
#AHMAD ZAKARIA FATHONI _ 3.34.20.4.01

from IPython.display import clear_output

def cls() :
    clear_output(True)

soal = ["Apakah kamu pernah melakukan test usap tenggorok atau hidung dengan RT-PCR dengan hasil positif ?",
        "Apakah kamu memiliki gejala infeksi saluran pernapasan atas seperti demam lebih dari 38*C, batuk,\n"
        "pilek, hidung tersumbat, nyeri menelan, hilang indera penciuman atau sesak nafas?",
        "Apakah kamu memiliki kontak erat dengan kasus positif/probable COVID-19 dalam 14 hari terakhir ?",
        "Apakah kamu tinggal di wilayah tranmisi lokal atau baru saja pulang bepergian ke negara\n"
        " yang melaporkan transmisi lokal dalam 14 hari terakhir?"]
nilai = []
print("Selamat Datang di Test Covid-19 Online")
print("Project UTS Dasar Pemograman IK-1E")
print("NAMA : AHMAD ZAKARIA FATHONI")
print("NIM  : 3.34.20.4.01")
print("")
print("")
while True:
      for x in soal:
        print(x)
        tanya = input("Apakah iya atau tidak ? (Y/T):")
        if (tanya == "Y"):
          print("")
          nilai.append(1)
        else:
          print("")
          nilai.append(0)

      cls()
      sum(nilai)
      print("HASIL TEST")
      if(nilai[0] == 1 or  nilai[0] & nilai[2] & nilai[3] == 1 ):
        print("")
        print("Kamu termasuk kasus POSITIF TANPA GEJALA")
        print("Disarankan untuk melakukan test PCR untuk memastikan kondisi kamu, dan lakukan isolasi mandiri")
      elif(nilai[1] == 1):
        print("")
        print("Kamu termasuk kategori RESIKO RENDAH")
        print("Meski berisiko rendah, namun jangan lengah, tetap patuhi protokol kesehatan.")
      elif(nilai[2] or nilai[2] & nilai[3] == 1):
        print("")
        print("Kamu termasuk kategori KONTAK ERAT")
        print("Jika kamu sudah selesai melakukan karantina mandiri selama 14 hari dan tidak ada gejala maka kamu\n"
        " bisa dimasukan ke dalam kriteria DISCARDED, disarankan melakukan test PCR untuk memastikan")
      elif(nilai[0] & nilai[1] & nilai[2] == 1 ):
        print("")
        print("Kamu termasuk kasus POSITIF TANPA GEJALA")
        print("Disarankan untuk melakukan test PCR untuk memastikan kondisi kamu, dan lakukan isolasi mandiri")
      elif(nilai[3] == 1):
        print("")
        print("Kamu termasuk kriteria Pelaku Perjalanan")
        print("Jika kamu sudah selesai melakukan karantina mandiri selama 14 hari dan tidak ada gejala maka kamu\n"
        "bisa dimasukan ke dalam kriteria DISCARDED, disarankan melakukan test PCR untuk memastikan")
      elif(nilai[0] & nilai[1]== 1 or sum(nilai) == 4):
        print("")
        print("Kamu termasuk kategori KASUS POSITIF DENGAN GEJALA")
        print("Disarankan untuk melakukan test PCR untuk memastikan kondisi kamu, dan lakukan isolasi mandiri")
      elif(nilai[1] & nilai[2] == 1 or nilai[1] & nilai[2] & nilai[3] == 1 ):
        print("")
        print("Kamu termasuk kasus SUSPEK atau PROBABLE")
        print("Jika gejala kamu berat dan sesak nafas hebat maka kamu termasuk kasus PROBABLE, jika tidak maka\n"
        " kemungkinan masuk kriteria SUSPEK")
      else:
        print("")
        print("Kamu termasuk kategori RESIKO RENDAH")
        print("Meski berisiko rendah, namun jangan lengah, tetap patuhi protokol kesehatan.")


      ulang =""
    
      while ulang !="Y" and ulang!= "T" :
        print("")
        ulang = input("Mulai lagi dari awal? [Y/T] ? ")
        cls()
        
      if ulang == "T":
        cls()
        print("")
        print("Aplikasi Berhenti. Exit...")
        break
