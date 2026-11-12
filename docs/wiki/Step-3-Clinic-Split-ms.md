[English](Step-3-Clinic-Split) · [Dansk](Step-3-Clinic-Split-da) · **Bahasa Malaysia**

# Langkah 3: Data tahunan dipecahkan mengikut klinik

**Soalan:** Antara dua klinik itu, yang manakah lebih sibuk dan yang manakah lebih berbahaya?

![Langkah 3: kelahiran, kematian dan kadar kematian bagi setiap klinik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-3-clinic-split.png)

## Apa yang dilakukan kod

- `births_by_clinic_chart` dan `deaths_by_clinic_chart` melukis satu garisan bagi setiap klinik supaya klinik dapat dibandingkan tahun demi tahun. Klinik 1 lebih besar (20,042 kelahiran berbanding 17,791 di klinik 2), dan kedua-dua klinik mempunyai lebih ramai pesakit dari semasa ke semasa. Bilangan kematian tahunan tertinggi ialah 518 di klinik 1 (1842) dan 202 di klinik 2 (1842).
- `add_pct_deaths` menambah lajur `pct_deaths`, iaitu kematian dibahagi kelahiran bagi setiap baris, pada salinan jadual tahunan. Mengira kematian sahaja tidak adil apabila saiz klinik berbeza; kadar membandingkan perkara yang setara.
- `average_death_rate` membahagikan jumlah kematian sesebuah klinik dengan jumlah kelahirannya: kira-kira 9.92 % bagi klinik 1 dan kira-kira 3.88 % bagi klinik 2.
- `pct_deaths_by_clinic_chart` menunjukkan kadar setiap tahun. Klinik 1 mempunyai kadar kematian lebih tinggi pada setiap tahun, dan itulah teka-teki yang ingin diterangkan oleh Dr Semmelweis.

## Apa yang anda perolehi

- Memilih baris sesuatu kumpulan dengan syarat, contohnya `df[df.clinic == "clinic 1"]`.
- Lajur terbitan (`pct_deaths`) menukar kiraan mentah kepada kadar yang boleh dibandingkan.
- Kadar bagi seluruh kumpulan ialah jumlah kematiannya dibahagi jumlah kelahirannya, bukan purata kadar tahunan.
- Satu garisan bagi setiap kumpulan, dengan legenda, ialah cara paling mudah untuk membandingkan kumpulan dari semasa ke semasa.

Sebelumnya: [Step-2-Data-Exploration-ms](Step-2-Data-Exploration-ms) · Seterusnya: [Step-4-Handwashing-Effect-ms](Step-4-Handwashing-Effect-ms)
