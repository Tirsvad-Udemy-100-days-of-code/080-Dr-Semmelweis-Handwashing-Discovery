[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu dan Git. Kebergantungan masa jalan: `pandas`, `numpy`, `matplotlib` dan `scipy`. Tiada yang lain diperlukan untuk menjalankan analisis.

## Windows (PowerShell)

Cipta dan gunakan `.venv` tempatan:

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery.git
cd 080-Dr-Semmelweis-Handwashing-Discovery
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jika PowerShell enggan menjalankan skrip pengaktifan, jalankan `Set-ExecutionPolicy -Scope Process RemoteSigned` dahulu; ia hanya terpakai pada tetingkap semasa.

## Linux dan macOS (bash)

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery.git
cd 080-Dr-Semmelweis-Handwashing-Discovery
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Jalankan, uji dan buka buku nota

Arahan adalah sama pada setiap sistem apabila `.venv` aktif:

```bash
python -m pytest
python -m ruff check src tests
python -m pip install -e ".[notebook]"
jupyter lab notebooks
```

`jupyter lab` memerlukan pilihan `notebook`, yang juga memasang `plotly` dan `seaborn` untuk buku nota kursus sendiri. Kod projek itu sendiri tidak menggunakannya.

## Semak kod dengan opengrep

Jalankan opengrep sebelum setiap push. Di Windows programnya ialah `~\.opengrep\cli\latest\opengrep.exe`; di Linux ia ialah `~/.opengrep/cli/latest/opengrep`:

```bash
~/.opengrep/cli/latest/opengrep scan --config p/python src tests
```

Betulkan setiap dapatan sebelum anda push.

## Bina dokumentasi Doxygen (pilihan)

```bash
doxygen Doxyfile
```

Halaman ditulis ke `docs/doxygen/html`.

**Apa yang anda perolehi:** persediaan yang boleh diulang (satu persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh sunting, ujian yang membuktikan setiap jawapan, dan semakan statik sebelum anda berkongsi kod.
