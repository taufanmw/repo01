#Percabangan
#kalau kondisi true maka hasilnya maju terus
#kalau kondisi false maka hasilnya jalan lain.

#ingin_cepat = True
#ingin_cepat = False
#if ingin_cepat:
 #   print('maju terus')
#else:
 #   print('jalan lain')

#umur = input("Berapa umur kamu : ")
#nama = input("nama kamu : ")
#print('nama kamu :'+ nama, 'usia kamu : '+ umur)

nilai = int(input('masukkan nilai kamu :'))

if nilai == 100:
    print("sempurna")
elif (nilai >= 80) and (nilai < 99):
    print("bagus sekali")
elif(nilai >= 60) and (nilai < 80):
    print('bagus')
else:
    print('tidak memenuhi syarat')