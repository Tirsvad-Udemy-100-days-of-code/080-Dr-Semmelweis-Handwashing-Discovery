[English](Step-5-Distributions) · [Dansk](Step-5-Distributions-da) · **Bahasa Malaysia**

# Langkah 5: Taburan dan signifikans statistik

**Soalan:** Adakah penurunan kadar kematian selepas membasuh tangan benar-benar berlaku, atau mungkin kebetulan sahaja?

![Langkah 5: plot kotak, histogram dan anggaran ketumpatan kernel bagi kadar kematian bulanan dengan dan tanpa membasuh tangan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-5-distributions.png)

## Apa yang dilakukan kod

- `add_washing_hands` menambah lajur boolean `washing_hands`, benar bagi bulan dari `HANDWASHING_START` ke atas, pada salinan jadual bulanan. `group_means` memberi purata kadar bulanan bagi setiap kumpulan: kira-kira 10.5 % tanpa dan kira-kira 2.11 % dengan membasuh tangan.
- `box_plot_chart` menunjukkan kedua-dua kumpulan sebagai plot kotak: median, kuartil dan nilai terpencil. Kadar biasa dan sebarannya lebih rendah selepas membasuh tangan.
- `histogram_overlay_chart` melukis dua histogram bertindih dengan 30 selang yang dikongsi, bar lutsinar dan peratus bulan pada paksi y, supaya kumpulan yang berbeza saiz dapat dibandingkan.
- `kde_chart` dan `kde_curve` melicinkan setiap histogram menjadi Anggaran Ketumpatan Kernel (KDE). Lengkung dipotong pada nilai terkecil dan terbesar kumpulan, kerana kadar kematian tidak boleh negatif.
- `two_sample_t_test` menjalankan `ttest_ind` SciPy pada kedua-dua kumpulan dan memulangkan statistik t dan nilai p: t kira-kira 5.51 dan p kira-kira 0.0000003. `is_significant` membandingkan nilai p dengan aras 0.01, maka perbezaan itu signifikan pada aras 99 %.

## Apa yang anda perolehi

- `np.where` atau perbandingan biasa menukar syarat tarikh kepada lajur boolean yang mengumpulkan data.
- Plot kotak, histogram dan KDE menunjukkan data yang sama dalam tiga cara: ringkasan, bilangan dan bentuk.
- Ujian-t bertanya sama ada perbezaan antara dua purata lebih besar daripada yang diberikan oleh kebetulan; nilai p yang kecil bermaksud ya, dan 0.0000003 jauh di bawah 0.01.
- `scipy.stats.ttest_ind` secara lalai menganggap varians sama (ujian Student), yang digunakan dalam kuliah; ujian Welch dengan `equal_var=False` memberi nombor yang berbeza.

Sebelumnya: [Step-4-Handwashing-Effect-ms](Step-4-Handwashing-Effect-ms)
