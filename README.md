# Paraxial-Wave-Equation-Solutions
 Solution of the paraxial wave equations using differante coordinates

 ## Ince - Gaussian Modes
 The Ince-Gaussian (IG) mode is a solution to the paraxial wave equation expressed in elliptic coordinates $(\xi, \eta)$. The general form of an Ince-Gaussian beam $(\xi, \eta, z)$ can be written as:

$\text{IG}_{p,m}^e(\mathbf{r}, \epsilon) = \frac{C\omega_0}{\omega(z)}C_p^m(i\xi, \epsilon)C_p^m(\eta, \epsilon)\exp\left[\frac{-r^2}{\omega^2(z)}\right] \exp i\left[kz + \frac{kr^2}{2R(z)} - (p - 1) \Psi_{GS}(z)\right]$,


$\text{IG}_{p,m}^o(\mathbf{r}, \epsilon) = \frac{S\omega_0}{\omega(z)}S_p^m(i\xi, \epsilon)S_p^m(\eta, \epsilon)\exp\left[\frac{-r^2}{\omega^2(z)}\right] \exp i\left[kz + \frac{kr^2}{2R(z)} - (p - 1) \Psi_{GS}(z)\right]$

where C and S are normalization constants and the superindices $e$ and $o$ refer to even and odd modes, respectively.

## Laguerre-Gaussian modes

$U_{p}^l(r, \phi, z) = \frac{1}{w(z)} \sqrt{\frac{2p!}{\pi (p + |l|)!}} \left(\frac{\sqrt{2} r}{w(z)}\right)^{|l|} L_p^{|l|}\left(\frac{2r^2}{w(z)^2}\right) \exp\left(-\frac{r^2}{w(z)^2}\right) \exp\left(-i \left(k z + k \frac{r^2}{2 R(z)} - l \phi - (2p + |l| + 1)\zeta(z)\right)\right)$

## Hermite-Gaussian modes

$U_{m}^n(x, y, z) = \frac{1}{w(z)} \sqrt{\frac{2}{\pi \, 2^{n+m} \, n! \, m!}} \, H_n\left(\frac{\sqrt{2} \, x}{w(z)}\right) H_m\left(\frac{\sqrt{2} \, y}{w(z)}\right) \exp\left(-\frac{x^2 + y^2}{w(z)^2}\right) \exp\left(-i \left(k z + (n + m + 1) \zeta(z) - \frac{k (x^2 + y^2)}{2 R(z)}\right)\right)$