[English](Step-4-Handwashing-Effect) · [Dansk](Step-4-Handwashing-Effect-da) · **Bahasa Malaysia**

# Langkah 4: Kesan membasuh tangan

**Soalan:** Adakah mewajibkan doktor membasuh tangan pada Jun 1847 mengurangkan kadar wanita yang meninggal dunia?

![Langkah 4: kadar kematian bulanan dengan tempoh membasuh tangan diserlahkan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-4-handwashing-effect.png)

## Apa yang dilakukan kod

- `add_pct_deaths_monthly` menambah lajur `pct_deaths`, iaitu kematian dibahagi kelahiran bagi setiap bulan, pada salinan jadual bulanan.
- `split_before_after` menggunakan pemalar `HANDWASHING_START` (1 Jun 1847) untuk membahagikan data bulanan kepada bulan sebelum dan bulan selepas membasuh tangan diwajibkan.
- `average_rate_before_after` membahagikan jumlah kematian setiap tempoh dengan jumlah kelahirannya: kira-kira 10.53 % sebelum dan kira-kira 2.15 % selepas. `mean_of_rates_before_after` pula mengambil purata kadar bulanan dan memberi kira-kira 10.5 % dan kira-kira 2.11 %.
- `improvement_factor` membahagikan kadar sebelum dengan kadar selepas: membasuh tangan mengurangkan kadar kematian dengan faktor kira-kira 4.9.
- `rolling_average` melicinkan kadar bulanan yang berubah-ubah dengan tetingkap 6 bulan, dan `handwashing_chart` melukis kadar bulanan, purata bergerak dan kedua-dua tempoh dalam warna berbeza, dengan legenda.

## Apa yang anda perolehi

- Menambah lajur terbitan pada siri masa, dan membahagikan DataFrame mengikut tarikh dengan syarat.
- Kadar bagi satu tempoh ialah jumlah kematian dibahagi jumlah kelahiran; purata kadar bulanan hampir sama, tetapi tidak serupa.
- Purata bergerak menunjukkan arah aliran di sebalik nilai bulanan yang berubah-ubah.
- Mewarnakan kedua-dua tempoh secara berbeza dan menambah legenda menjadikan perbandingan sebelum dan selepas mudah dibaca sepintas lalu.

Sebelumnya: [Step-3-Clinic-Split-ms](Step-3-Clinic-Split-ms)
