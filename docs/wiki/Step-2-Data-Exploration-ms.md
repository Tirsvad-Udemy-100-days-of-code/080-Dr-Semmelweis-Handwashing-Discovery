[English](Step-2-Data-Exploration) · [Dansk](Step-2-Data-Exploration-da) · **Bahasa Malaysia**

# Langkah 2: Penerokaan data awal

**Soalan:** Apa yang ada dalam data, adakah ia bersih, dan betapa bahayanya bersalin di Vienna pada tahun 1840-an?

![Langkah 2: kelahiran dan kematian bulanan pada dua paksi](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-2-data-exploration.png)

## Apa yang dilakukan kod

- `load_yearly` dan `load_monthly` membaca dua fail CSV; pemuat bulanan mengurai lajur `date` supaya tiada penukaran diperlukan kemudian.
- `table_shape`, `column_names`, `has_nan_values` dan `has_duplicates` menjawab cabaran pertama: jadual tahunan mempunyai 12 baris dan 4 lajur, jadual bulanan 98 baris dan 3 lajur, tiada nilai `NaN` dan tiada pendua.
- `average_births_per_month` dan `average_deaths_per_month` memberi kira-kira 267 kelahiran dan 22.47 kematian sebulan.
- `percentage_of_women_dying` membahagikan jumlah kematian dengan jumlah kelahiran dalam data tahunan: kira-kira 7.08 %, berbanding 0.018 % di Amerika Syarikat pada tahun 2013.
- `births_and_deaths_chart` melukis kelahiran dan kematian pada dua paksi-y dengan tanda tahun dan bulan, grid, garisan `skyblue` dan `crimson`, garisan kematian bertitik dan ketebalan garisan 3 dan 2. Pada hujung tahun 1840-an bilangan kematian jatuh dengan mendadak sedangkan bilangan kelahiran tidak.

## Apa yang anda perolehi

- `.shape`, `.head()`, `.tail()`, `.info()`, `.describe()`, `.isna()` dan `.duplicated()` memberi gambaran pertama tentang mana-mana DataFrame.
- Peratusan ialah satu jumlah dibahagi satu jumlah, darab 100.
- `.twinx()` membolehkan dua siri dengan skala berbeza berkongsi satu paksi-x, dan `MonthLocator` serta `YearLocator` menjadikan paksi masa mudah dibaca.

Sebelumnya: [Step-1-Goals-ms](Step-1-Goals-ms)
