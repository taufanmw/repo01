#tipe data list
#tipe data sederhana
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#tipe data array
print('\ntipe data array')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)

#kalau menambahkan variabel baru
print('\ntambah var baru')
anak.append('Lima')
print(anak)

#sapa anak ke dua (urutan angka di pemrograman dimulai dari angka 0)
print('\nsapa anak ke 2')
print(f'Halo {anak[1]} ! ')


#cara menyapa semua anak
print('\nsapa semua anak cara gampang')
for a in anak:
    print(f'Halo {a} ! ')

#sapa cara ribet

print('\nsapa anak cara ribet')
for a in range(0, len(anak)):
     print(f'hai {anak[a]}')

#dengan memakai ribet dgn nomor
print('\nsapa ribet dengan nomor')
for a in range(0, len(anak)):
    print(f'{a+1}. Halo {anak[a]}')

#len = panjang variabel / array