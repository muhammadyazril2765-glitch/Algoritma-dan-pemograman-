tugas = int(input("Nilai tugas: "))
uts = int(input("Nilai UTS: "))
uas = int(input("Nilai UAS: "))
kehadiran = int(input("Kehadiran (%): "))

nilai_akhir = (20 * tugas / 100) + (30 * uts / 100) + (50 * uas / 100)

print("Nilai Akhir:", nilai_akhir)

if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print("Status: LULUS DENGAN PREDIKAT")
elif nilai_akhir >= 75 and kehadiran >= 80:
    print("Status: LULUS")
else:
    print("Status: BELUM LULUS")
