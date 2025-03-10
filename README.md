# Nama: Ibadurahman Faiz Usman
# NIM: 235150301111032

# Model Perhitungan Motor DC  

Dokumen ini menjelaskan langkah-langkah dalam membangun model matematika motor DC, melakukan transformasi Laplace, dan menentukan fungsi alih yang menghubungkan kecepatan sudut ($\omega$) dengan tegangan ($V$).  

## Model Matematika Motor DC  

Motor DC dapat dimodelkan menggunakan dua persamaan utama:  

### Persamaan Listrik  
Persamaan ini menggambarkan hubungan antara tegangan input ($V$), arus armature ($i$), dan kecepatan sudut ($\omega$).  

\
V(t) = R i(t) + L $\frac{di(t)}{dt}$ + $K_e$ $\omega$ (t)

**Keterangan:**  
- $V$ : Tegangan input (V)  
- $R$ : Resistansi armature ($\Omega$)  
- $L$ : Induktansi armature (H)  
- $i$ : Arus armature (A)  
- $K_e$ : Konstanta GGL (V.s/rad)  
- $\omega$ : Kecepatan sudut motor (rad/s)  

### Persamaan Mekanik  
Persamaan ini menggambarkan hubungan antara torsi motor, kecepatan sudut, dan momen inersia rotor.  

\
$K_t$ i(t) = J $\frac{d \omega (t)}{dt}$ + b $\omega$ (t)

**Keterangan:**  
- $K_t$ : Konstanta torsi motor (Nm/A)  
- $J$ : Momen inersia rotor (kg.m²)  
- $b$ : Koefisien gesekan viscous (Nm.s/rad)  
- $\omega$ : Kecepatan sudut motor (rad/s)  

---

## Transformasi Laplace pada Motor DC  

Dengan menggunakan Transformasi Laplace ($s$-domain), kedua persamaan di atas menjadi:  

### Transformasi Laplace dari Persamaan Listrik  
\
V(s) = R I(s) + L s I(s) + $K_e$ $\Omega$ (s)

### Transformasi Laplace dari Persamaan Mekanik  
\
$K_t$ I(s) = J s $\Omega$ (s) + b $\Omega$ (s)

Dengan menyelesaikan kedua persamaan ini, kita dapat memperoleh hubungan antara $\Omega(s)$ dan $V(s)$.

---

## Fungsi Alih Motor DC ($\omega / V$)  

Fungsi alih atau transfer function adalah hubungan antara kecepatan sudut output $\omega (s)$ dan tegangan input $V(s)$. Dengan menyelesaikan sistem persamaan di atas, diperoleh:  

\
H(s) = $\frac{\Omega(s)}{V(s)}$ = $\frac{K_t}{(J s + b)(R + L s) + K_t K_e}$

Jika diberikan parameter tertentu, fungsi alih ini dapat disederhanakan menjadi bentuk:  

\
H(s) = $\frac{0.01}{0.01s + 0.1001}$

---

## Implementasi dalam Python  
Berikut adalah implementasi model ini dalam Python menggunakan **SymPy** dan **control system library** untuk analisis lebih lanjut:  

```python
import sympy as sp

# Definisi variabel simbolik
t, s = sp.symbols('t s')
V = sp.Function('V')(t)  # Tegangan input V(t)
i = sp.Function('i')(t)  # Arus i(t)
ω = sp.Function('ω')(t)  # Kecepatan sudut ω(t)

# Parameter Motor DC (Contoh nilai)
R = 1     # Ohm (Resistansi)
L = 0.5   # Henry (Induktansi)
J = 0.01  # kg.m^2 (Momen inersia)
B = 0.1   # N.m.s (Damping)
Kt = 0.01 # N.m/A (Konstanta Torsi)
Ke = 0.01 # V.s/rad (Konstanta GGL balik)

# 1. Persamaan Diferensial Motor DC
eq_listrik = sp.Eq(V, L * i.diff(t) + R * i + Ke * ω)  # Hukum Kirchhoff
eq_mekanik = sp.Eq(J * ω.diff(t) + B * ω, Kt * i)  # Hukum Newton

print("1. Persamaan Diferensial Motor DC:\n")
sp.pprint(eq_listrik)
sp.pprint(eq_mekanik)
```

---

## Kesimpulan  
Model ini menunjukkan bagaimana motor DC dapat direpresentasikan dengan persamaan diferensial, kemudian dikonversi ke domain Laplace untuk memperoleh fungsi alih. Dengan menggunakan Python, kita dapat menyederhanakan fungsi alih dan mensimulasikan respons sistem secara langsung.
