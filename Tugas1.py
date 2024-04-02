print('PROGRAM MEMINJAM BUKU PERPUSTAKAAN')

listnim = ('23090150, 2309004, 230901009')
nim  = str(input("Masukan NIM : "))
listjudulbuku = ('koala kumal, laskar pelangi, cinta brontosaurus')
judul_buku= input('Masukan Juduk Buku : ')

print('=', 'HASIL' ,'=')

if nim in listnim and judul_buku in listjudulbuku :
    print('nim :', nim)
    print('judul buku :', judul_buku)
    print('BOLEH MEMINJAM')
else:
    print('TIDAK BOLEH MEMINJAM')