# Nama: Ibadurahman Faiz Usman
# NIM: 235150301111032

# Model Perhitungan Motor DC  

Dokumen ini menjelaskan langkah-langkah dalam membangun model matematika motor DC, melakukan transformasi Laplace, dan menentukan fungsi alih yang menghubungkan kecepatan sudut ($\omega$) dengan tegangan ($V$).  

## Model Matematika Motor DC  

Motor DC dapat dimodelkan menggunakan dua persamaan utama:  

### Persamaan Listrik  
Persamaan ini menggambarkan hubungan antara tegangan input ($V$), arus armature ($i$), dan kecepatan sudut ($\omega$).  

\
V(t) = R i(t) + L d i(t)/dt + K_e \omega (t)
\

**Keterangan:**  
- $V$ : Tegangan input (V)  
- $R$ : Resistansi armature ($\Omega$)  
- $L$ : Induktansi armature (H)  
- $i$ : Arus armature (A)  
- $K_e$ : Konstanta GGL (V.s/rad)  
- $\omega$ : Kecepatan sudut motor (rad/s)  

### Persamaan Mekanik  
Persamaan ini menggambarkan hubungan antara torsi motor, kecepatan sudut, dan momen inersia rotor.  

\[
K_t i(t) = J \frac{d \omega (t)}{dt} + b \omega (t)
\]

**Keterangan:**  
- $K_t$ : Konstanta torsi motor (Nm/A)  
- $J$ : Momen inersia rotor (kg.m²)  
- $b$ : Koefisien gesekan viscous (Nm.s/rad)  
- $\omega$ : Kecepatan sudut motor (rad/s)  

---

## Transformasi Laplace pada Motor DC  

Dengan menggunakan Transformasi Laplace ($s$-domain), kedua persamaan di atas menjadi:  

### Transformasi Laplace dari Persamaan Listrik  
\[
V(s) = R I(s) + L s I(s) + K_e \Omega(s)
\]

### Transformasi Laplace dari Persamaan Mekanik  
\[
K_t I(s) = J s \Omega(s) + b \Omega(s)
\]

Dengan menyelesaikan kedua persamaan ini, kita dapat memperoleh hubungan antara $\Omega(s)$ dan $V(s)$.

---

## Fungsi Alih Motor DC ($\omega / V$)  

Fungsi alih atau transfer function adalah hubungan antara kecepatan sudut output $\omega (s)$ dan tegangan input $V(s)$. Dengan menyelesaikan sistem persamaan di atas, diperoleh:  

\[
H(s) = \frac{\Omega(s)}{V(s)} = \frac{K_t}{(J s + b)(R + L s) + K_t K_e}
\]

Jika diberikan parameter tertentu, fungsi alih ini dapat disederhanakan menjadi bentuk:  

\[
H(s) = \frac{0.01}{0.01s + 0.1001}
\]

---

## Implementasi dalam Python  
Berikut adalah implementasi model ini dalam Python menggunakan **SymPy** dan **control system library** untuk analisis lebih lanjut:  

```python
import sympy as sp

# Definisi simbol
s, V, I, omega = sp.symbols('s V I omega')
R, L, Ke, Kt, J, b = sp.symbols('R L Ke Kt J b')

# Persamaan dalam domain s
eq_electric = sp.Eq(V, R*I + L*s*I + Ke*omega)
eq_mechanic = sp.Eq(Kt*I, J*s*omega + b*omega)

# Menyelesaikan I(s) dan substitusi ke persamaan mekanik
I_expr = sp.solve(eq_electric, I)[0]
eq_mechanic = eq_mechanic.subs(I, I_expr)
H_s = sp.simplify(sp.solve(eq_mechanic, omega)[0] / V)

# Output fungsi alih
print("Fungsi Alih Motor DC (ω/V):")
sp.pprint(H_s)
```

Kode ini menghitung fungsi alih secara simbolik berdasarkan parameter yang diberikan.  

---

## Simulasi dengan `control` Library  

Untuk simulasi respon sistem, kita dapat menggunakan pustaka `control`:  

```python
import control as ctrl

# Definisi fungsi alih dalam bentuk numerik
num = [0.01]
den = [0.01, 0.1001]

H = ctrl.TransferFunction(num, den)
print(H)

# Plot respons step
import matplotlib.pyplot as plt
t, y = ctrl.step_response(H)
plt.plot(t, y)
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan Sudut (rad/s)')
plt.title('Respons Step Motor DC')
plt.grid()
plt.show()
```

---

## Kesimpulan  
Model ini menunjukkan bagaimana motor DC dapat direpresentasikan dengan persamaan diferensial, kemudian dikonversi ke domain Laplace untuk memperoleh fungsi alih. Dengan menggunakan Python, kita dapat menyederhanakan fungsi alih dan mensimulasikan respons sistem secara langsung.
