# Nama: Ibadurahman Faiz Usman
# NIM: 235150301111032

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

# 2. Transformasi Laplace (asumsi kondisi awal nol)
I_s = sp.Function('I')(s)
Ω_s = sp.Function('Ω')(s)
V_s = sp.Function('V')(s)

eq_laplace_listrik = eq_listrik.subs({sp.Derivative(i, t): s*I_s})
eq_laplace_mekanik = eq_mekanik.subs({sp.Derivative(ω, t): s*Ω_s})

print("\n\n2. Transformasi Laplace Motor DC:\n")
sp.pprint(eq_laplace_listrik)
sp.pprint(eq_laplace_mekanik)
