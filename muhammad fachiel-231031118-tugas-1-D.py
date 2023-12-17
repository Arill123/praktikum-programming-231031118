
print('\n')
biodata = { 'nama'  : 'muhammad fachriel',
'nim'   : '231031118',
'kelas' : 'S123D',
'agama' : 'islam',
'alamat': 'tegal',
'kewarganegaraan' : 'WNI',
'email' : 'ovalhitman9@gmail.com'
}

print(biodata['nama'],biodata['nim'],biodata['email'])
print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:4])
print(selected_biodata)




