nama = input ("Masukkan nama mahasiswa:")

if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citara":
    target = 80
else:
    target = 0

print("Nama:",nama)
print("target:",target)

percobaan = 1

while percobaan <=3:
    nilai = int(input("Masukan nilai ke-" + str(percobaan) + ":"))

    if nilai >= target:
        print("Lulus")
        break
    else:
        print("Belum lulus")

    percobaan += 1

if percobaan > 3:
    print(nama,"tidak lulus setelah 3 kali percobaan")
                    
