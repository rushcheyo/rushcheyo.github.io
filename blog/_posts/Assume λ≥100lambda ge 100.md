Assume $\lambda \ge 100$

Stirling approximation: $n! \lesssim \sqrt n (n/e)^n$; elementary inequality: $\log(1-x) \ge -x-x^2$ for $x \in [0,1/2]$
$$
&\Pr[\text{Pois}(\lambda) \ge \lambda]\\
= & \sum_{k \ge \lambda} \frac{\lambda^k}{k!} e^{-\lambda}\\
\gtrsim & \sum_{k \ge \lambda} \frac{(\lambda/k)^k}{\sqrt k}e^{k-\lambda}\\
\ge & \sum_{\lambda \le k \le \lambda +\sqrt{\lambda}}  \frac{(\lambda/k)^k}{\sqrt k}e^{k-\lambda}\\
\gtrsim & \frac{1}{\sqrt{\lambda}}\sum_{1 \le t \le \sqrt{\lambda}} \left(1 - \frac{t}{\lambda + t}\right)^k e^{t}\\
\ge&\frac{1}{\sqrt{\lambda}}\sum_{1 \le t \le \sqrt{\lambda}} \left(1 - \frac{1}{\lambda/t}\right)^{\lambda+t} e^{t}\\
=  &\frac{1}{\sqrt{\lambda}}\sum_{1 \le t \le \sqrt{\lambda}} \exp\left((\lambda+t)\log\left(1 - \frac{1}{\lambda/t}\right)\right) e^{t}\\
\ge  &\frac{1}{\sqrt{\lambda}}\sum_{1 \le t \le \sqrt{\lambda}} \exp\left(t-(\lambda+t)\left(\frac{1}{\lambda/t}+\frac{1}{\lambda^2/t^2}\right)\right)\\
\ge  &\frac{1}{\sqrt{\lambda}}\sum_{1 \le t \le \sqrt{\lambda}} \exp\left(t-t(1+t/\lambda)\left(1+\frac{1}{\sqrt{\lambda}}\right)\right)\\
\ge  &\frac{1}{\sqrt{\lambda}}\sum_{1 \le t \le \sqrt{\lambda}} \exp\left(-t/\sqrt{\lambda}-t^2/\lambda\left(1+\frac{1}{\sqrt{\lambda}}\right)\right)\\
\gtrsim  &\frac{1}{\sqrt{\lambda}}\sum_{1 \le t \le \sqrt{\lambda}} \exp\left(-t^2/\lambda\left(1+\frac{1}{\sqrt{\lambda}}\right)\right)\\

\gtrsim & 1
$$

$$
&\Pr[\text{Pois}(\lambda) \ge \lambda]\\
= & \sum_{k \ge \lambda} \frac{\lambda^k}{k!} e^{-\lambda}\\
\gtrsim & \sum_{k \ge \lambda} \frac{(\lambda/k)^k}{\sqrt k}e^{k-\lambda}\\
\ge & \sum_{k \ge \lambda}\frac{1}{\sqrt k} \exp((k-\lambda) + k \log(1-(k-\lambda)/k))\\
\ge & \sum_{2 \lambda \ge k \ge \lambda}\frac{1}{\sqrt k} \exp((k-\lambda) - k\left(\frac{k-\lambda}k+\frac{(k-\lambda)^2}{k^2}\right)\\
\ge & \sum_{2 \lambda \ge k \ge \lambda}\frac{1}{\sqrt k} \exp\left(-\frac{(k-\lambda)^2}{k}\right)\\
\ge & \int_\lambda^{2\lambda} \frac{1}{\sqrt x}\exp(-(x-\lambda)^2/x) dx\\
= & \int_1^{2} \frac{1}{\sqrt{\lambda t}}\exp(-(\lambda t-\lambda)^2/(\lambda t)) d(\lambda t)\\
= & \sqrt \lambda \int_0^1 \frac{1}{\sqrt{t+1}}\exp(-\lambda t^2/(t+1)) dt\\
= & \int_0^{\sqrt \lambda} \frac{1}{\sqrt{1+t/\sqrt{\lambda}}}\exp\left(-t^2/\left(1+t/\sqrt \lambda\right)\right) dt\\
\ge & \frac{1}{\sqrt{1+B/\sqrt{\lambda}}} \int_0^{B} \exp\left(-t^2\right) dt && B \le \sqrt \lambda\\
= & \frac{1}{\sqrt{1+B/\sqrt{\lambda}}} \cdot \frac{1}{\sqrt 2} \int_0^{\sqrt 2 B} \exp\left(-t^2/2\right) dt\\
\ge & \frac{1}{\sqrt{1+B/\sqrt{\lambda}}} \cdot \sqrt \pi \left( \frac 1 2 - \frac{1}{\sqrt{2 \pi}}\int_0^{\sqrt 2 B} \exp\left(-t^2/2\right) dt\right)\\
\ge & \frac{1}{\sqrt{1+B/\sqrt{\lambda}}} \cdot \sqrt \pi \left( \frac 1 2 - \frac{1}{2\sqrt{\pi}B} \exp(-B^2)\right)\\
\ge & \frac{1}{\sqrt{1+\sqrt{\log \lambda}/\sqrt{\lambda}}} \cdot \sqrt \pi \left( \frac 1 2 - \frac{1}{2\sqrt{\pi}\lambda\sqrt{\log \lambda}}\right) && B = \sqrt{\log \lambda}\\
1/\sqrt 2
$$

