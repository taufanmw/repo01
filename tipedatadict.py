""""
tipe data dict menghubungkan key dengan value
atau KVP = Key Value Pair
"""
from typing import Dict
kamus_ina_en = {}
kamus_ina_en['anak'] = 'son'
kamus_ina_en['ayah'] = 'Father'
kamus_ina_en['istri'] = 'wive'
kamus_ina_en['ibu'] = 'mother'

# cara lain agar biar lebih simple :
# kamus_ina_en: = {'anak': 'son', 'ayah': 'Father', 'istri': 'wive', 'ibu': 'mother'}

print(kamus_ina_en)
print(kamus_ina_en['ayah'])
print(kamus_ina_en['ibu'])
print(kamus_ina_en['anak'])

print('Data ini dikirimkan oleh server Gojek, untuk memberikan info ke user')
data_dari_gojek ={
    'tanggal':'2020-10-12',
    #kalo tipe datanya list
    # 'driver_list':['Eko', 'Dwi', 'Catur', 'Tri']

    #kalo tipe datanya dict
    'driver_list':[ {'nama':'Eko', 'jarak':'10'},
                   {'nama':'Dwi','jarak':'30'},
                   {'nama':'Catur','jarak':'100'},
                   {'nama':'Tri', 'jarak':'200'}
                  ]
}

print(data_dari_gojek)
print(f"driver sekitar sini {data_dari_gojek['driver_list']}")
#misal ambil driver pertama
print(f"driver#1 {data_dari_gojek['driver_list'][0]}")
#misal ambil driver ketiga
print(f"driver#3 {data_dari_gojek['driver_list'][2]}")
print(f"driver#4 {data_dari_gojek['driver_list'][3]}")
print(f"driver gojek terdekat {data_dari_gojek['driver_list'][0]['jarak']} meter")
