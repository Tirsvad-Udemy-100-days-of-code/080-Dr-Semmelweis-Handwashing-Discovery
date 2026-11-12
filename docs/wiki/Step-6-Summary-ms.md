[English](Step-6-Summary) · [Dansk](Step-6-Summary-da) · **Bahasa Malaysia**

# Langkah 6: Pengajaran dan ringkasan

**Soalan:** Apakah yang diajar oleh hari ke-80, dan apakah kata data tentang membasuh tangan?

![Langkah 6: keputusan utama dan kadar kematian bulanan dengan purata bergeraknya](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-6-summary.png)

## Apa yang dilakukan kod

`step_6_summary` melukis keputusan utama daripada fungsi domain yang sama seperti langkah terdahulu, tanpa sebarang nombor ditaip dengan tangan: kadar kematian sebelum membasuh tangan (kira-kira 10.53 %) dan selepas (kira-kira 2.15 %), faktor penambahbaikan (kira-kira 4.9 kali lebih rendah), statistik t (kira-kira 5.51), nilai p (kira-kira 0.0000003) dan bahawa keputusan itu signifikan pada aras 1 %. Di sebelahnya ia melukis kadar kematian bulanan dengan purata bergerak 6 bulan dan tarikh membasuh tangan bermula.

## Apa yang anda perolehi

- **Data dahulu:** `.shape`, `.head()`, `.isna()` dan `.duplicated()` menunjukkan apa yang ada dalam data sebelum sebarang analisis (langkah 2).
- **Perbandingan adil:** kadar seperti nisbah kematian membandingkan klinik dan tempoh yang berlainan saiz lebih baik daripada bilangan (langkah 3 dan 4).
- **Siri masa:** purata bergerak menunjukkan arah aliran di sebalik bulan yang berubah-ubah, dan warna, garisan penanda serta legenda menunjukkan bila perubahan berlaku (langkah 4).
- **Taburan:** `np.where` membuat lajur kumpulan; plot kotak, histogram dan Anggaran Ketumpatan Kernel menunjukkan kumpulan yang sama dalam tiga cara (langkah 5).
- **Signifikans statistik:** ujian-t dan nilai p memberitahu sama ada perbezaan lebih besar daripada kebetulan; di sini p jauh di bawah 0.01, maka penurunan selepas membasuh tangan itu benar (langkah 5).
- **Kesimpulan:** selepas peraturan membasuh tangan pada Jun 1847, kadar wanita yang meninggal dunia jatuh daripada kira-kira 10.5 % kepada kira-kira 2.1 %, dan data menunjukkan ia bukan kebetulan.

Sebelumnya: [Step-5-Distributions-ms](Step-5-Distributions-ms)
