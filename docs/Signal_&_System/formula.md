# Review in Signal & System
## Transformation
1. Fourier Transformation (Continuous)
$$
\begin{align}
    a_k &= \frac{1}{T}\int_{T}x(t)e^{-jk\omega_0 t}dt \\
    x(t) &= \sum_{k = -\infty}^{\infty} a_ke^{jk\omega_0 t}, k = 0, \pm 1, \dots \\
    X(j\omega) &= \int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt \\
    x(t) &= \frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}d\omega
\end{align}
$$
2. Fourier Transformation (Discrete)
$$
\begin{align}
    a_k &= \frac{1}{N}\sum_{n = \lang N\rang}x[n]e^{-jk\omega_0 n} \\
    x[n] &= \sum_{k = \lang N\rang} a_ke^{jk\omega_0 n}, k = 0, \pm 1, \dots \\
    X(e^{j\omega}) &= \sum_{n = -\infty}^{\infty}x[n]e^{-j\omega n} \\
    x[n] &= \frac{1}{2\pi}\int_{2\pi}X(e^{j\omega})e^{j\omega n}d\omega
\end{align}
$$
3. Laplace Transformation
$$
\begin{align}
    X(s) &= \int_{-\infty}^{\infty}x(t)e^{-st}dt \\
    x(t) &= \frac{1}{2\pi j}\int_{\sigma -j\infty}^{\sigma + j\infty}X(s)e^{s t}ds \\
    \chi(s) &= \int_{0^-}^{\infty}x(t)e^{-st}dt \\
    x(t) &= \frac{1}{2\pi j}\int_{\sigma -j\infty}^{\sigma + j\infty}\chi(s)e^{s t}ds, t > 0^-
\end{align}
$$
4. Z Transformation
$$
\begin{align}
    X(z) &= \sum_{n = -\infty}^{\infty}x[n]z^{-n}, z = re^{j\omega} \\
    x[n] &= \frac{1}{2\pi j}\oint X(z)z^{n - 1}dz, \omega:0\to 2 \pi \\
    \chi(z) &= \sum_{n = 0}^{\infty}x[n]z^{-n}, z = re^{j\omega} \\
    x[n] &= \frac{1}{2\pi j}\oint \chi (z)z^{n - 1}dz, \omega:0\to 2 \pi, n \ge 0 
\end{align}
$$

## series to transform
1. CTFS to CTFT
$$
\begin{align}
    x(t) = \sum_{k = -\infty}^{\infty} a_k e^{jk\omega_0 t}\leftrightarrow X(j\omega) = 2\pi \sum_{k = -\infty}^{\infty} a_k\delta(\omega - k\omega_0)
\end{align}
$$
2. DTFS to DTFT
$$
\begin{align}
    x[n] = \sum_{k = <N>} a_k e^{jk\omega_0 n} \leftrightarrow X(e^{j\omega}) = 2\pi \sum_{k = -\infty}^{\infty} a_k\delta(\omega - k\omega_0)
\end{align}
$$

## property
1. 时移
$$
\begin{align}
    CTFT &: x(t - t_0) \leftrightarrow X(j\omega)e^{-j\omega t_0}\\
    DTFT &: x[n - n_0] \leftrightarrow X(e^{j\omega})e^{-j\omega n_0}\\
    Laplace &: x(t - t_0) \leftrightarrow X(s)e^{-st_0}\\
    z &: x[n - n_0] \leftrightarrow X(z)z^{-n_0} \\
\end{align}
$$
2. 频移
$$
\begin{align}
    CTFT &: x(t)e^{j\omega_0 t} \leftrightarrow X(j(\omega - \omega_0))\\
    DTFT &: x[n]e^{j\omega_0 n} \leftrightarrow X(e^{j(\omega - \omega_0)})\\
    Laplace &: x(t)e^{s_0t} \leftrightarrow X(s - s_0), ROC: 包含R + Re[s_0]\\
    z &: x[n]z_0^{n} \leftrightarrow X(z / z_0), ROC: |z_0|R \\
\end{align}
$$
3. 尺度变换
$$
\begin{align}
    CTFT &: x(at) \leftrightarrow \frac{1}{|a|}X(\frac{j\omega}{a})\\
    Laplace &: x(at) \leftrightarrow \frac{1}{|a|}X(\frac{s}{a}), ROC: aR\\
    z &: x[n]z_0^{n} \leftrightarrow X(z / z_0), ROC: |z_0|R \\
\end{align}
$$
4. 反转
$$
\begin{align}
    CTFT &: x(-t) \leftrightarrow X(-j\omega)\\
    DTFT &: x[-n] \leftrightarrow X(e^{-j\omega})\\
    Laplace &: x(-t) \leftrightarrow X(-s), ROC:-R\\
    z &: x[-n] \leftrightarrow X(z^{-1}), ROC:\frac{1}{R} \\
\end{align}
$$
5. 时域微分/差分
$$
\begin{align}
    CTFT &: \frac{d x}{d t} \leftrightarrow j\omega X(j\omega)\\
    DTFT &:  x[n] - x[n - 1]\leftrightarrow (1 - e^{-j\omega})X(e^{j\omega})\\
    Laplace &: \frac{d x}{d t} \leftrightarrow s X(s)\\
    z &: x[n] - x[n - 1] \leftrightarrow (1 - z^{-1})X(z) \\
\end{align}
$$
6. 频域微分
$$
\begin{align}
    CTFT &: tx(t) \leftrightarrow j\frac{dX(j\omega)}{d\omega}\\
    DTFT &:  nx[n]\leftrightarrow j\frac{dX(e^{j\omega})}{d\omega}\\
    Laplace &: tx(t) \leftrightarrow -\frac{dX(s)}{ds}\\
    z &: nx[n] \leftrightarrow -z\frac{dX(z)}{dz} \\
\end{align}
$$
7. Parseval
$$
\begin{align}
    CTFS &: \frac{1}{T}\int_{T}|x(t)|^2dt = \sum_{k = -\infty}^{\infty}|a_k|^2\\
    DTFS &: \frac{1}{N} \sum_{n=\langle N\rangle}|x[n]|^{2}=\sum_{k=\langle N\rangle}\left|a_{k}\right|^{2} \\
    CTFT &: \int_{-\infty}^{\infty}|x(t)|^2dt = \frac{1}{2\pi}\int_{-\infty}^{\infty}|X(j\omega)|^2d\omega\\
    DTFT &: \sum_{n = -\infty}^{\infty}|x[n]|^2 = \frac{1}{2\pi}\int_{2\pi}|X(e^{j\omega})|^2d\omega \\
\end{align}
$$
8. 卷积
$$
\begin{align}
    CTFT &: x(t) * h(t) \leftrightarrow X(j\omega)H(j\omega)\\
    DTFT &:  x[n] * h[n]\leftrightarrow X(e^{j\omega})H(e^{j\omega})\\
    Laplace &: x(t) * h(t) \leftrightarrow X(s)H(s)\\
    z &: x[n] * h[n] \leftrightarrow X(z)H(z) \\
\end{align}
$$
9.  相乘
$$
\begin{align}
    CTFT &: x(t)h(t) \leftrightarrow \frac{1}{2\pi}X(j\omega) * H(j\omega)\\
    DTFT &:  x[n]h[n]\leftrightarrow \frac{1}{2\pi}X(e^{j\omega}) \otimes H(e^{j\omega})\\
\end{align}
$$
10. 初值定理
$$
\begin{align}
    Laplace &: x(0^+) \leftrightarrow \lim_{s\to\infty}sX(s)\\
    z &: x[0] \leftrightarrow \lim_{z\to\infty}X(z) \\
\end{align}
$$
11. 终值定理
$$
\begin{align}
    Laplace &: \lim_{t\to\infty}x(t) \leftrightarrow \lim_{s\to0}sX(s)\\
    z &: \lim_{n\to\infty}x[n] \leftrightarrow \lim_{z\to1}(z - 1)X(z) \\
\end{align}
$$
12. 单边微分
$$
\begin{align}
    Laplace : x^{\prime}(t) &\leftrightarrow s\chi(s) - x(0^-)\\
    x^{\prime\prime}(t) &\leftrightarrow s^2\chi(s) - sx(0^-) - x^{\prime}(0^-)\\
    x^{\prime\prime\prime}(t) &\leftrightarrow s^3\chi(s) - s^2x(0^-) - sx^{\prime}(0^-) -  x^{\prime\prime}(0^-)\\
    z :  x[n - 1] &\leftrightarrow z^{-1}\chi(z) + x[-1]\\
    x[n - 2] &\leftrightarrow z^{-2}\chi(z) + z^{-1}x[-1] + x[-2]\\
    x[n - 3] &\leftrightarrow z^{-3}\chi(z) + z^{-2}x[-1] + z^{-1}x[-2] + x[-3]\\
\end{align}
$$

## sth about $\delta (t)$
$$
\begin{align}
    x(t)\delta(t - t_0) &= x(t_0)\delta(t - t_0) \\
    x(t) * \delta(t - t_0) &= x(t - t_0) \\
    \int_{-\infty}^{\infty} x(t)\delta(t - t_0)dt &= x(t_0) \\
    \delta(t) &= \frac{d u(t)}{dt} \\
    \delta(t) &= u_0(t), u(t) = u_{-1}t \\
\end{align}
$$

## Convolution
$$
\begin{align}
    x(t) * h(t) &= \int_{-\infty}^{\infty} x(\tau)h(t - \tau)d\tau \\
    x[n] * h[n] &= \sum_{k = -\infty}^{\infty} x[k]h[n - k]
\end{align}
$$

## Nyquist
$$
\begin{align}
    \omega_s &> 2\omega_M, s:sample \\
    \omega_M < &\omega_c < \omega_s - \omega_M, c: filter \\
\end{align}
$$
## sample
$$
\begin{align}
    p(t) &= \sum_{n = -\infty}^{\infty} \delta(t - nT), \omega_s = \frac{2\pi}{T} \\
    \sum_{n = -\infty}^{\infty} \delta(t - nT) &\leftrightarrow \omega_0\sum_{n = -\infty}^{\infty} \delta(\omega - n\omega_0), \omega_0 = \frac{2\pi}{T}
\end{align}
$$
## others
$$
\begin{align}
    x(t) \leftrightarrow X(j\omega) &\Leftrightarrow X(jt) \leftrightarrow 2\pi x(-\omega) \\
    x(t) &= \frac{x(t) + x(-t)}{2} + \frac{x(t) - x(-t)}{2} = x_e(t) + x_o(t) \\
    \cos (\omega t) &= \frac{1}{2}\left(e^{j\omega t} + e^{-j\omega t}\right) \\
    \sin (\omega t) &= \frac{1}{2j}\left(e^{j\omega t} - e^{-j\omega t}\right) \\
    X(0) &= \int_{-\infty}^{\infty} x(t)dt
\end{align}
$$