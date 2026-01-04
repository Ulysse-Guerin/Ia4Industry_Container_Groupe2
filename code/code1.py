import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

# précision numérique
mp.mp.dps = 15

sigma = 0.5
t = np.linspace(0, 30, 1000)

# calcul zêta complexe
zeta_values = [mp.zeta(sigma + 1j * ti) for ti in t]

# extraction parties réelle / imaginaire
zeta_real = [mp.re(z) for z in zeta_values]
zeta_imag = [mp.im(z) for z in zeta_values]

plt.figure()
plt.plot(t, zeta_real, label="Re(ζ(1/2 + it))")
plt.plot(t, zeta_imag, label="Im(ζ(1/2 + it))")
plt.xlabel("t")
plt.ylabel("ζ(s)")
plt.title("Riemann Zeta Function on the Critical Line", fontstyle="italic")
plt.legend()
plt.grid(True)
plt.show()

zero_crossings_real = np.sum(np.diff(np.sign(zeta_real)) != 0)
zero_crossings_imag = np.sum(np.diff(np.sign(zeta_imag)) != 0)

print(f"Nombre de passages par zéro pour Re(ζ(1/2 + it)) : {zero_crossings_real}")
print(f"Nombre de passages par zéro pour Im(ζ(1/2 + it)) : {zero_crossings_imag}")


