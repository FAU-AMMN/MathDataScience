# Die Exponentialfunktion

Wir betrachten nun die Exponentialfunktion noch ein wenig näher, wir haben ja im letzten Kapitel schon die Identität

```{math}
 e^x e^y = e^{x+y}
```

für alle $x,y \in \R$ hergeleitet. Dazu sehen wir aus der Form der Potenzreihe, die nur positive Koeffizienten hat, dass $e^x > 1$ für alle $x > 0$ gilt. Daraus folgt natürlich aus

```{math}
 e^{-x} = \frac{1}{e^x} > 0,
```

also $e^y > 0$ für $y < 0$. Also ist die Exponentialfunktion immer positiv.
Aus diesen Eigenschaften folgern wir auch, dass die Exponentialfunktion streng monoton wachsend ist. Für $y > x$ gilt ja

```{math}
 e^y = e^x e^{y-x} > e^x.
```

Nun können wir noch die Grenzwerte $x \rightarrow \infty$ und $x \rightarrow - \infty$ betrachten. Für $x > 0$ gilt $
e^x > 1+x$, und die rechte Seite wächst monoton gegen $\infty$. Also folgt $\lim_{x \rightarrow \infty} e^x = \infty. $ Aus $e^{-x} = \frac{1}{e^x} $ folgt dann sofort $\lim_{x \rightarrow - \infty} e^x = 0. $
Nun weisen wir noch die Stetigkeit nach:

````{prf:theorem}
Die Exponentialfunktion ist lokal Lipschitz stetig auf $\R$ und damit insbesondere stetig.
````

````{prf:proof}
 Seien $x  < y \in \R$. Dann gil

```{math}
 \left\vert e^y - e^x \right\vert = e^y - e^x = e^x ( e^{y-x} - 1).
```

Sei nun $z=y-x \in (0,\epsilon)$, dann gilt

```{math}
  \left\vert e^z -  1 \right\vert = \sum_{n=1}^\infty \frac{1}{n!} z^n = z \sum_{n=0}^\infty \frac{1}{(n+1)!} z^n  \leq z \sum_{n=0}^\infty \frac{1}{n!} \epsilon^n = z e^\epsilon.
```

Also gilt für $|x-y| < \epsilon$ auc

```{math}
  \left\vert e^y - e^x \right\vert \leq e^{x+\epsilon} |y-x|,
```

d.h. die Exponentialfunktion ist lokal Lipschitz-stetig.
````

Nun haben wir gesehen, dass $e^x: \R \rightarrow \R$ eine positive, stetige, streng monotone Funktion ist. Nach dem Zwischenwertsatz ist die Exponentialfunktion surjektiv nach $\R^+$, da wir $x$ mit $e^x$ beliebig groß oder beliebig nahe bei $0$ finden können. Damit wissen wir auch, dass die Exponentialfunktion eine stetige Inverse auf $\R^+$ hat, die wir Logarithmus nennen

```{math}
 \log: \R^+ \rightarrow \R, x \rightarrow \log(x),
```

wobei $\log(e^x) =x$. Aus den Eigenschaften der Exponentialfunktion folgern wir

```{math}
 \lim_{x\rightarrow \infty} \log(x) = \infty, \qquad \lim_{x\rightarrow 0_+} \log(x) = -\infty,
```

wobei $\lim_{x\rightarrow 0_+}$ den rechtsseitigen Grenzwert bezeichnet.
