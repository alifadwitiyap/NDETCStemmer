# Nondeterministic Context (NDETC) Stemmer

Nondeterministic Context (NDETC) Stemmer adalah library yang mengimplementasikan metode stemming nondeterministic berbasis context untuk memecahkan permasalahan kata-kata ambigu morfologis pada proses stemming kata dalam bahasa Indonesia.

## Installation
clone file github
```bash
  git clone https://github.com/alifadwitiyap/NDETCStemmer.git
```
masuk kedalam folder NDETCStemmer
```bash
  cd NDETCStemmer
```
install library
```bash
  pip install .
```
    
## Usage
Setelah menginstall library ini, anda dapat menggunakannya dengan membuat file baru di dalam folder yang sama dengan NDETCStemmer_IO.py atau dengan cara mengubah file NDETCStemmer_IO.py dengan mengikuti baris code berikut sebagai percobaan:
```python
#import NDETCStemmer library
from NDETCStemmer import NDETCStemmer

#init stemmer
stemmer=NDETCStemmer()

# stemming process
output=stemmer.stem('boleh saya memerah lembu ini')

print(output)
#boleh saya perah lembu ini

print(stemmer.stem('bibirnya memerah tangannya jadi selengket madu'))
#bibir merah tangan jadi lengket madu

```


## Cititation
```
@INPROCEEDINGS{9617514,
  author={Bunyamin and Huda, Arief Fatchul and Suryani, Arie Ardiyanti},
  booktitle={2021 International Conference on Data Science and Its Applications (ICoDSA)}, 
  title={Indonesian Stemmer for Ambiguous Word based on Context}, 
  year={2021},
  volume={},
  number={},
  pages={1-9},
  doi={10.1109/ICoDSA53588.2021.9617514}}
```

## Tentang Metode Nondeterministic Context
Merupakan metode yang dikembangkan oleh Bunyamin et al. yang dimana metode ini merupakan penelitian lanjutan dari pendekatan Nondeterministic yang diusulkan oleh Purwanti. Dalam penelitian Purwanti, setiap kata tidak diperiksa menurut urutan aturan morfologi, tetapi diperiksa menggunakan semua aturan. Kemudian, hasilnya disimpan satu per satu dalam daftar kandidat kata. Kata akhir akan dipilih menggunakan beberapa aturan heuristik, yaitu ketersediaan kosakata dari kata dasar khusus dan panjang kata. </br> </br>Masalah yang dihadapi oleh metode yang dikembangkan Purwanti ini dan stemmer berbahasa indonesia umumnya adalah masalah ambiguitas kata yang dihasilkan oleh stemmer misalkan kata "memalukan" mempunyai 2 kata dasar yaitu “malu”  dan “palu” , tergantung konteksnya. Pada pernyataan-pernyataan berikut “dia tidak ingin memalukan keluarganya” dan “tukang memalukan
paku di tembok” kata ambigu "memalukan" akan menghasilkan kata dasar "malu" secara terus menerus. Berdasarkan konteksnya, hasilnya seharusnya menjadi "malu" di kalimat pertama dan "palu" di kalimat kedua. Pada metode Nondeterministic berhasil menghasilkan beberapa kandidat kata alternatif dari kata-kata ambigu tersebut tetapi kurang dalam memilih hasil yang sesuai karena tidak adanya konteks. </br></br>Metode Nondeterministic Context meningkatkan pendekatan nondeterministik dengan menambahkan konteks dalam pemilihan kata terbaik. Dalam menyelesaikan masalah pemilihan kata terbaik untuk setiap masukan kata ambigu, diusulkan penggunaan model  word2vec. Dengan cara ini stemmer akan lebih akurat dalam melakukan stemming dibandingkan dengan cara-cara sebelumnya.


#### Kelebihan
Stemming kata ambigu, kata reduplikasi, dan kata majemuk dengan imbuhan. Namun, kualitas stemmer tergantung pada pemeriksa aturan afiks, model kata, kamus kata dasar, dan konteksnya.
#### Kekurangan
- Aturan infiks -el-, -em-, -er-, dan -in- dibuang dalam metode ini karena aturan memiliki dampak signifikan terhadap semua proses stemmer
- Konteks berupa kata-kata yang melingkupi kata-kata ambigu morfologis seringkali tidak mendukung perhitungan kata-kata terbaik sama sekali

#### Penting
- Kualitas model kata mempengaruhi pemilihan kata-kata terbaik dalam kata-kata ambigu. Model kata dibuat menggunakan pelatihan word2vec dengan beberapa parameter. Beberapa parameter dalam membuat model harus dipilih dengan cermat dan hasilnya harus dibandingkan dari satu model ke model lainnya.
- Kamus kata dasar juga mempengaruhi kualitas stemmer. Kamus kata dasar harus bebas dari kata berimbuhan

## License

[MIT](https://choosealicense.com/licenses/mit/)
