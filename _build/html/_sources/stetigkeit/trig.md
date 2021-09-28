# Trigonometrische Funktionen

Um die trigonometrischen Funktionen Sinus ($\sin(x)$) und Cosinus ($\cos(x)$) einfach zu analysieren, erweitern wir die Potenzreihe für die Exponentialfunktion auf die komplexen Zahlen

```{math}
 e^z:= \sum_{n=0}^\infty \frac{1}{n!} z^n, \qquad z \in \C.
```

Man sieht leicht, dass diese Reihe auch in ganz $\C$ konvergiert. Verwendet man das Argument $z=\i x$ mit $x \in \R$, so rechnet man aus den Potenzreihen leicht die sogenannte Euler-Formel nach

```{math}
 e^{\i x} = \cos(x) + \i \sin(x),
```

bzw. umgekehrt

```{math}
 \cos(x) = \text{Re}(e^{\i x}), \qquad \sin(x) = \text{Im}(e^{\i x}).
```

Aus den Eigenschaften der Exponentialfunktion folgen dann auch die Summationstheoreme für Sinus und Cosinus
\begin{align*}
e^{\i (x+y)} &= e^{\i x}e{\i y} = (\cos(x) + \i \sin(x)) (\cos(y) + \i \sin(y))  \\
&= \cos(x) \cos(y) - \sin(x) \sin(y) + \i ( \cos(x) \sin(y) + \sin(y) \cos(x)).
\end{align*}
Durch Vergleich der Real- und Imaginärteile erhält ma

```{math}
 \cos(x+y) = \cos(x) \cos(y) - \sin(x) \sin(y)
```

un

```{math}
 \sin(x+y) =  \cos(x) \sin(y) + \sin(y) \cos(x).
```

Wir sehen aus den Eigenschaften der Potentialreihen leicht, dass Cosinus bzw. Sinus symmetrisch bzw. antisymmetrisch sind, d.h.

```{math}
 \cos(-x) = \cos(x)  , \qquad \sin(-x) = -\sin(x) .
```

Verwenden wir dies im obigen Summationstheorem für den Cosinus für $y=-x$, so erhalten wir

```{math}
 1 = \cos(0) = \cos(x)^2 + \sin(x)^2
```

für alle $x \in \R$.

Nun wollen wir noch nachweisen, dass Sinus- und Cosinus periodische Funktionen sind.

````{prf:lemma}
Es gibt ein $\pi \in \R^+$ mit $e^{\i \frac{\pi}2} = \i$ und $e^{\i x} \neq \i$ für $x \in [0,\pi)$.
````

````{prf:proof}
 Wir definieren

```{math}
 \frac{\pi}2 = \inf\{x \in \R^+~|~e^{\i x } = \i \}.
```

Wir wissen $\cos(0)=1 > 0$ und es gilt

```{math}
 \cos(2)= 1 -2 + \sum_{k=2}^\infty (-1)^k \frac{2^{2k}}{(2k)!} \leq -1 + \sum_{k=2}^\infty  \frac{2^{2k}}{(2k)!} .
```

Nun zeigt man induktiv leicht für $k \geq 2$:

```{math}
 (2k)! \geq 4^{2k-4} 4! ,
```

also
\begin{align*}
\cos(2) &\leq -1 + \frac{4^4}{4!} \sum_{k=2}^\infty \frac{2^{2k}}{4^{2k}} \\
&= -1   + \frac{4^4}{4!} \sum_{k=2}^\infty \frac{1}{4^{k}} \\
&= -1   + \frac{4 }{3!} \sum_{k=0}^\infty \frac{1}{4^{k}} \\
&= -1 + \frac{4}{6} \frac{1}{1-\frac{1}4} = -1 + \frac{16}{24}  = - \frac{1}{3} < 0.
\end{align*}
Nach dem Zwischenwertsatz existiert damit eine Nullstelle im Intervall $(0,2)$. Da

```{math}
 \sin(x)^2 + \cos(x)^2 = 1
```
gilt, also ist für $\cos(x) = 0$ automatisch $\sin(x) \in \{\pm 1\}$.Ist $\sin(x) = -1$, dann wäre $e^{\i x} = -\i$ und damit $e^{3\i x} = (-i)^2(-i) = i$. Also gibt es ein $x$ mit $e^{\i x} =\i$.
%Anderseits sieht man auch $\sin(-x) = -\sin(x)$ und $\cos(-x) = \cos(x)$, also muss%es eine Nullstelle mit $\sin(x) = 1$ geben. Damit ist $\frac{\pi}2$ wohldefiniert.
````

Wir sehen, dass aus $ e^{\i \pi/2 } = \i$ auch folgt:

```{math}
 e^{\i pi} = -1, \quad e^{2 \i pi} =  1.
```

Damit erhalten wir auch

```{math}
 e^{\i x + 2 \i \pi} = e^{\i x}e^{2 \i \pi} = e^{\i x},
```

für alle $x \in \R$. Separat für den Real- und Imaginärteil aufgeschrieben heisst das\begin{align*}
\cos(x+2\pi) &= \cos(x) \\
\sin(x+2\pi) &= \sin(x).\end{align*}
Analog erhalten wir übrigens auch die Eigenschaften

```{math}
 \cos(x+ \pi) = -\cos(x) , \quad  \sin(x+\pi) = - \sin(x), \quad \sin(x+\frac{\pi}2) = \cos(x).
```

Durch Quotienten könen wir auc

```{math}
 \tan(x) = \frac{\sin(x)}{\cos(x)} , \qquad \cot(x) = \frac{\cos(x)}{\sin(x)}
```

definieren.  Analog zu $\sin$ und $\cos$ definiert man die sogenannten hyperbolischen Funktionen

```{math}
 \cosh(x) = \frac{1}2 (e^x+e^{-x}), \qquad \sinh(x) = \frac{1}2 (e^x-e^{-x}).
```

Hier gil

```{math}
 \cosh(x)^2 - \sinh(x)^2 = 1,
```

wie man leicht nachrechnet.
