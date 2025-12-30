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

# 1. Persamaan Diferensial Motor DC
eq_listrik = sp.Eq(V, L * i.diff(t) + R * i + Ke * ω)  # Hukum Kirchhoff
eq_mekanik = sp.Eq(J * ω.diff(t) + B * ω, Kt * i)  # Hukum Newton

print("1. Persamaan Diferensial Motor DC:\n")
sp.pprint(eq_listrik)
sp.pprint(eq_mekanik)
