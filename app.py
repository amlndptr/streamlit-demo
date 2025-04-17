import streamlit as st

st.title("Website Amellinda Putri")
st.write("Helo Everyone!")

# Tambahin fitur input nama
nama = st.text_input("Masukkan nama kamu:")

# Tombol untuk menyapa
if st.button("Sapa aku"):
    st.success(f"Halo, {nama}! Senang bertemu denganmu.")

import streamlit as st
st.write("Coba berhitung di website yuk")
st.title("🧮 Kalkulator Otomatis Berbasis Web")
st.write("Masukkan angka yang mau dijumlahkan ke kolom berikut, lalu klik tombol untuk melihat hasilnya.")

# Input dari user
angka1 = st.number_input("Masukkan Angka Pertama", value=0)
angka2 = st.number_input("Masukkan Angka Kedua", value=0)

# Tombol untuk proses penjumlahan
if st.button("Lihat Hasil"):
    hasil = angka1 + angka2
    st.success(f"Hasil penjumlahan: {hasil}")
    

import streamlit as st
st.write("Masukkan angka yang mau dijumlahkan ke kolom berikut, lalu klik tombol untuk melihat hasilnya.")
angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)
if st.button("Kalikan"):
    hasil = angka1 * angka2
    st.success(f"Hasil perkalian: {hasil}")
    

# app_trigonometri.py
import streamlit as st
import math

st.title("📐 Kalkulator Trigonometri (sin, cos, tan)")

derajat = st.number_input("Masukkan sudut (dalam derajat)", value=0.0)

# Konversi derajat ke radian
radian = math.radians(derajat)

sinus = math.sin(radian)
cosinus = math.cos(radian)
try:
    tangen = math.tan(radian)
except:
    tangen = "Tak terdefinisi"

st.write(f"sin({derajat}°) = {sinus}")
st.write(f"cos({derajat}°) = {cosinus}")
st.write(f"tan({derajat}°) = {tangen}")

import streamlit as st
import math

st.title("📐 Kalkulator Trigonometri Lengkap")
st.write("Masukkan sudut dalam derajat, hasil akan muncul dalam bentuk desimal.")

# Input sudut
sudut_derajat = st.number_input("Masukkan sudut (°)", value=0.0)

# Konversi ke radian
sudut_radian = math.radians(sudut_derajat)

# Hitung fungsi trigonometri
sinus = math.sin(sudut_radian)
cosinus = math.cos(sudut_radian)

# Tanpa error: cek jika cos atau sin = 0
try:
    tangen = math.tan(sudut_radian)
except:
    tangen = float('inf')

try:
    cosecan = 1 / sinus if sinus != 0 else "Tak terdefinisi"
    secan = 1 / cosinus if cosinus != 0 else "Tak terdefinisi"
    cotangen = 1 / tangen if tangen != 0 else "Tak terdefinisi"
except:
    cosecan = secan = cotangen = "Tak terdefinisi"

# Tampilkan hasil
st.subheader(f"Hasil untuk sudut {sudut_derajat}°")
st.write(f"✅ sin(θ)  = {sinus}")
st.write(f"✅ cos(θ)  = {cosinus}")
st.write(f"✅ tan(θ)  = {tangen}")
st.write("---")
st.write(f"📏 csc(θ)  = {cosecan}")
st.write(f"📏 sec(θ)  = {secan}")
st.write(f"📏 cot(θ)  = {cotangen}")



import streamlit as st
import math

st.title("📐 Penjawab Soal Matematika + Rumus")

soal = st.selectbox(
    "Pilih jenis soal",
    [
        "Luas Lingkaran",
        "Keliling Lingkaran",
        "Luas Persegi",
        "Keliling Persegi",
        "Volume Kubus",
        "Volume Balok",
        "Keliling Segitiga",
        "Luas Segitiga"
    ]
)

if soal == "Luas Lingkaran":
    r = st.number_input("Masukkan jari-jari (r)", value=0.0)
    if st.button("Hitung"):
        luas = math.pi * r**2
        st.latex(r"L = \pi \times r^2")
        st.write(f"👉 L = π × {r}² = {luas:.2f}")

elif soal == "Keliling Lingkaran":
    r = st.number_input("Masukkan jari-jari (r)", value=0.0)
    if st.button("Hitung"):
        keliling = 2 * math.pi * r
        st.latex(r"K = 2 \pi r")
        st.write(f"👉 K = 2 × π × {r} = {keliling:.2f}")

elif soal == "Luas Persegi":
    s = st.number_input("Masukkan panjang sisi (s)", value=0.0)
    if st.button("Hitung"):
        luas = s ** 2
        st.latex(r"L = s^2")
        st.write(f"👉 L = {s}² = {luas}")

elif soal == "Keliling Persegi":
    s = st.number_input("Masukkan panjang sisi (s)", value=0.0)
    if st.button("Hitung"):
        keliling = 4 * s
        st.latex(r"K = 4 \times s")
        st.write(f"👉 K = 4 × {s} = {keliling}")

elif soal == "Volume Kubus":
    s = st.number_input("Masukkan panjang sisi kubus (s)", value=0.0)
    if st.button("Hitung"):
        volume = s ** 3
        st.latex(r"V = s^3")
        st.write(f"👉 V = {s}³ = {volume}")

elif soal == "Volume Balok":
    p = st.number_input("Panjang (p)", value=0.0)
    l = st.number_input("Lebar (l)", value=0.0)
    t = st.number_input("Tinggi (t)", value=0.0)
    if st.button("Hitung"):
        volume = p * l * t
        st.latex(r"V = p \times l \times t")
        st.write(f"👉 V = {p} × {l} × {t} = {volume}")

elif soal == "Keliling Segitiga":
    a = st.number_input("Sisi a", value=0.0)
    b = st.number_input("Sisi b", value=0.0)
    c = st.number_input("Sisi c", value=0.0)
    if st.button("Hitung"):
        keliling = a + b + c
        st.latex(r"K = a + b + c")
        st.write(f"👉 K = {a} + {b} + {c} = {keliling}")

elif soal == "Luas Segitiga":
    a = st.number_input("Alas (a)", value=0.0)
    t = st.number_input("Tinggi (t)", value=0.0)
    if st.button("Hitung"):
        luas = 0.5 * a * t
        st.latex(r"L = \frac{1}{2} \times a \times t")
        st.write(f"👉 L = ½ × {a} × {t} = {luas}")



import streamlit as st

# Judul Aplikasi
st.title("📚 Aplikasi Pembelajaran Interaktif")

# Pilihan Mata Pelajaran
materi = st.selectbox(
    "Pilih Mata Pelajaran:",
    ["Bahasa Indonesia", "Sejarah", "Bahasa Inggris", "Kewirausahaan"]
)

# ============================
# Bahasa Indonesia
# ============================
if materi == "Bahasa Indonesia":
    st.header("Bahasa Indonesia")
    st.write("Topik: Penulisan Ejaan yang Disempurnakan (EYD)")

    soal = st.text_input("Masukkan kalimat yang akan dicek ejaannya:")
    if soal:
        # Cek dan perbaiki ejaan (contoh sederhana)
        corrected_text = soal.replace("saya", "Saya").replace("anda", "Anda")
        st.write("Kalimat yang benar: ", corrected_text)
    
    st.write("""
    **Ejaan yang Disempurnakan (EYD)** adalah pedoman yang digunakan dalam penulisan bahasa Indonesia yang berlaku sejak tahun 1972.
    Beberapa contoh aturan penting dalam EYD:
    - Huruf pertama dalam kalimat harus ditulis dengan huruf kapital.
    - Kata ganti 'saya' dan 'anda' harus diawali dengan huruf kapital.
    """)

# ============================
# Sejarah
# ============================
elif materi == "Sejarah":
    st.header("Sejarah")
    st.write("Topik: Perang Dunia II")

    st.write("""
    **Perang Dunia II** adalah perang yang berlangsung antara 1939 hingga 1945, melibatkan sebagian besar negara di dunia.
    Beberapa fakta menarik:
    - Dimulai pada 1 September 1939, saat Jerman menyerang Polandia.
    - Negara yang terlibat dalam perang ini termasuk Jerman, Italia, Jepang, Inggris, Perancis, Uni Soviet, Amerika Serikat, dan banyak negara lainnya.
    - Akhir perang ditandai dengan penyerahan Jerman pada 7 Mei 1945 dan Jepang pada 2 September 1945.
    """)
    
    # Tanyakan pertanyaan sejarah
    jawaban = st.radio("Siapa yang menjadi sekutu utama pada Perang Dunia II?", ["Jerman", "Inggris", "Amerika Serikat"])
    if jawaban == "Inggris":
        st.success("Benar! Inggris merupakan bagian dari negara sekutu dalam Perang Dunia II.")
    else:
        st.error("Coba lagi, itu bukan jawaban yang tepat.")

# ============================
# Bahasa Inggris
# ============================
elif materi == "Bahasa Inggris":
    st.header("Bahasa Inggris")
    st.write("Topik: Pengenalan Tenses")

    tense = st.selectbox("Pilih Tense yang ingin dipelajari:", ["Present Tense", "Past Tense", "Future Tense"])

    if tense == "Present Tense":
        st.write("""
        **Present Tense** digunakan untuk menggambarkan kebiasaan, fakta, atau kejadian yang berlangsung saat ini.
        Rumus: Subject + Verb (s/es) + Object
        Contoh:
        - She reads a book every day.
        """)
    elif tense == "Past Tense":
        st.write("""
        **Past Tense** digunakan untuk menggambarkan kejadian yang sudah terjadi di masa lalu.
        Rumus: Subject + Verb (past) + Object
        Contoh:
        - He went to school yesterday.
        """)
    elif tense == "Future Tense":
        st.write("""
        **Future Tense** digunakan untuk menggambarkan kejadian yang akan terjadi di masa depan.
        Rumus: Subject + will + Verb (base form) + Object
        Contoh:
        - They will travel to Japan next year.
        """)

# ============================
# Kewirausahaan
# ============================
elif materi == "Kewirausahaan":
    st.header("Kewirausahaan")
    st.write("Topik: Pengertian dan Aspek-Aspek Kewirausahaan")

    st.write("""
    **Kewirausahaan** adalah suatu proses di mana individu atau kelompok menciptakan sesuatu yang baru dengan tujuan untuk memperoleh keuntungan.
    
    Beberapa aspek penting dalam kewirausahaan:
    1. **Inovasi**: Menciptakan produk atau layanan yang baru atau lebih baik.
    2. **Manajemen Keuangan**: Mengelola aliran uang yang efektif.
    3. **Pemasaran**: Membuat strategi untuk mempromosikan produk atau layanan.
    4. **Keberanian mengambil risiko**: Menjadi berani untuk menghadapi tantangan dan risiko dalam berbisnis.

    Contoh Wirausahawan Sukses: Bill Gates (Microsoft), Mark Zuckerberg (Facebook)
    """)

    # Tanyakan pertanyaan kewirausahaan
    jawaban = st.radio("Apa yang menjadi kunci sukses dalam kewirausahaan?", ["Inovasi", "Modal", "Lokasi"])
    if jawaban == "Inovasi":
        st.success("Benar! Inovasi adalah salah satu kunci utama dalam kewirausahaan.")
    else:
        st.error("Coba lagi, itu bukan jawaban yang tepat.")


import openai
import streamlit as st

# Masukkan API Key OpenAI di sini
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Ganti dengan API Key kamu

# Fungsi untuk mendapatkan jawaban dari GPT
def get_answer_from_gpt(question):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Bisa ganti dengan model lain yang sesuai
        prompt=question,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

    
    import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import openai
from PIL import Image
import requests

# Sidebar untuk Navigasi
st.sidebar.title("Fitur Aplikasi")
page = st.sidebar.radio("Pilih Fitur", (
    "Kalkulator Kalori", 
    "Kalkulator BMI", 
    "Dashboard Data", 
    "Kalkulator Keuangan", 
    "Pengelolaan Anggaran", 
    "Deteksi Wajah", 
    "Prediksi Harga", 
    "Scraper Berita", 
    "To-Do List", 
    "Pomodoro Timer", 
    "Editor Gambar Sederhana", 
    "Generasi Seni dengan AI"
))

# 1. **Kalkulator Kalori**
if page == "Kalkulator Kalori":
    st.title("Kalkulator Kalori")
    weight = st.number_input("Berat Badan (kg)", min_value=1, max_value=500)
    height = st.number_input("Tinggi Badan (cm)", min_value=50, max_value=250)
    age = st.number_input("Umur (tahun)", min_value=1, max_value=120)
    gender = st.radio("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    
    if st.button("Hitung Kalori"):
        if gender == "Laki-laki":
            bmr = 66 + (13.75 * weight) + (5 * height) - (6.75 * age)
        else:
            bmr = 655 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
        
        st.write(f"Kebutuhan kalori harian: {bmr} Kcal")

# 2. **Kalkulator BMI**
elif page == "Kalkulator BMI":
    st.title("Kalkulator BMI")
    weight = st.number_input("Berat Badan (kg)", min_value=1, max_value=500)
    height = st.number_input("Tinggi Badan (cm)", min_value=50, max_value=250)
    
    if st.button("Hitung BMI"):
        bmi = weight / (height / 100) ** 2
        st.write(f"BMI Anda: {bmi:.2f}")
        if bmi < 18.5:
            st.write("Status: Kurang berat badan")
        elif 18.5 <= bmi < 24.9:
            st.write("Status: Normal")
        elif 25 <= bmi < 29.9:
            st.write("Status: Kelebihan berat badan")
        else:
            st.write("Status: Obesitas")

# 3. **Dashboard Data**
elif page == "Dashboard Data":
    st.title("Dashboard Data")
    data = pd.DataFrame({
        'Tanggal': pd.date_range('2025-01-01', periods=100),
        'Harga': np.random.randint(1000, 5000, 100)
    })
    
    st.line_chart(data.set_index('Tanggal'))

# 4. **Kalkulator Keuangan**
elif page == "Kalkulator Keuangan":
    st.title("Kalkulator Keuangan")
    income = st.number_input("Pendapatan Bulanan", min_value=0)
    expenses = st.number_input("Pengeluaran Bulanan", min_value=0)
    
    if st.button("Hitung Sisa Keuangan"):
        balance = income - expenses
        st.write(f"Sisa Keuangan Bulanan: {balance}")

# 5. **Pengelolaan Anggaran**
elif page == "Pengelolaan Anggaran":
    st.title("Pengelolaan Anggaran")
    expenses = {
        'Makanan': st.number_input("Makanan", min_value=0),
        'Transportasi': st.number_input("Transportasi", min_value=0),
        'Pendidikan': st.number_input("Pendidikan", min_value=0),
        'Hiburan': st.number_input("Hiburan", min_value=0)
    }
    
    total_expenses = sum(expenses.values())
    st.write(f"Total Pengeluaran: {total_expenses}")

# 6. **Deteksi Wajah**
elif page == "Deteksi Wajah":
    st.title("Deteksi Wajah")
    uploaded_image = st.file_uploader("Upload gambar wajah", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption="Gambar yang diupload", use_column_width=True)
        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        st.image(img, caption="Hasil Deteksi Wajah", use_column_width=True)

# 7. **Prediksi Harga**
elif page == "Prediksi Harga":
    st.title("Prediksi Harga")
    # Implementasikan model prediksi harga di sini
    st.write("Fitur ini membutuhkan model prediksi harga yang terlatih.")

# 8. **Scraper Berita**
elif page == "Scraper Berita":
    st.title("Scraper Berita")
    # Menggunakan web scraping untuk mengambil berita terbaru
    st.write("Fitur ini membutuhkan implementasi web scraping.")

# 9. **To-Do List**
elif page == "To-Do List":
    st.title("To-Do List")
    task = st.text_input("Tugas yang harus dilakukan:")
    if st.button("Tambah Tugas"):
        st.write(f"Tugas Ditambahkan: {task}")
    
    tasks = ["Tugas 1", "Tugas 2", "Tugas 3"]  # Contoh daftar tugas
    st.write("Daftar Tugas:")
    for task in tasks:
        st.write(f"- {task}")

# 10. **Pomodoro Timer**
elif page == "Pomodoro Timer":
    st.title("Pomodoro Timer")
    minutes = st.slider("Durasi Kerja (menit)", 5, 60, 25)
    if st.button("Mulai Timer"):
        st.write(f"Timer dimulai untuk {minutes} menit kerja.")

# 11. **Editor Gambar Sederhana**
elif page == "Editor Gambar Sederhana":
    st.title("Editor Gambar Sederhana")
    uploaded_image = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption="Gambar yang diupload", use_column_width=True)
        if st.button("Ubah Gambar"):
            img = img.convert("L")  # Mengubah gambar ke hitam putih
            st.image(img, caption="Gambar Hitam Putih", use_column_width=True)

# 12. **Generasi Seni dengan AI**
elif page == "Generasi Seni dengan AI":
    st.title("Generasi Seni dengan AI")
    prompt = st.text_input("Masukkan deskripsi seni:")
    if st.button("Generate Seni"):
        # Menggunakan model AI untuk menghasilkan seni berdasarkan prompt
        st.write("Fitur ini membutuhkan akses ke model generasi seni AI.")

