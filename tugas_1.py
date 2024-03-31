data = []
print('PENDATAAN WARGA RT 01')
PekerjaanOrtu = ['pns','dokter','masinis','tentara','polisi','pilot','nahkoda']  #list
nik = int(input('masukan Nomor Induk Kependudukan : '))
nama = str(input('masukan nama : ')) #variabel
umur = int(input('masukan umur : '))
Pekerjaan = str(input('masukan pekerjaan : '))
Gaji = int(input('masukan gaji perbulan : '))
data = nik,nama,umur,Pekerjaan,Gaji
if Pekerjaan not in PekerjaanOrtu and Gaji <= 1500000 and umur > 40 :
    print('SELAMAT ANDA TELAH SELESAI MENGISI PENDATAAN WARGA RT 01')
    print('anda berkesempatan mendapatkan bantuan sosial sebesar 500.000 Rupiah') 
    no_rekening = int(input('masukan no rekening : ')) 
else : print('SELAMAT ANDA TELAH SELESAI MENGISI PENDATAAN WARGA RT 01')
print(data)