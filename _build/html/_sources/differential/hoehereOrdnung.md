# Höhere Ableitungen

In vielen Fällen kann man die Idee der Ableitung iterieren um höher Ableitungen zu erhalten. Ist $f'$ wieder differenzierbar in einer Umgebung von $x_0$ und existiert der Grenzwer

```{math}
 f''(x_0) = \lim_{x \rightarrow x_0} \frac{f'(x) - f'(x_0)}{x-x_0} ,
```

so nennen wir $f'' = (f')'$ die zweite Ableitung von $f$. In dieser Form erhalten wir, falls diese existieren, auch $k$-te Ableitungen $f^{(k)}=(f^{(k-1)})'$. Wir nennen $f$ in diesem Fall $k$-mal differenzierbar, bzw. unendlich oft differenzierbar wenn die Ableitung für jedes $k \in \N$ existiert. Der Vollständigkeit halber setzen wir $f^{(0)} = f$.

````{prf:example}
Sei $f: \R \rightarrow \R, x \mapsto e^x.$ Dann ist $f$ unendlich oft differenzierbar in $\R$ und $f^{(k)}(x)=f(x)$.
````

````{prf:example}
Sei $f: \R \rightarrow \R, x \mapsto x^2.$ Dann ist $f$ unendlich oft differenzierbar in $\R$ mit $f'(x)=2x$, $f''(x)=2$ und $f^{(k)}(x)=0$ für $k > 2$.
````

Eine interessante Anwendung sind wieder Minimal- und Maximalstellen:

````{prf:theorem}
Sei $f:[a,b]\rightarrow \R$ zweimal differenzierbar in einer Umgebung von $x_0 \in (a,b)$. Dann gilt:

* $i)$ Ist $x_0$ Minimalstelle (Maximalstelle) dann gilt $f'(x_0) = 0$, $f''(x_0) \geq 0$ ($f''(x_0) \leq 0$)

* $ii)$ Ist $f'(x_0) = 0$ und $f''(x_0) > 0$ ($f''(x_0) < 0$), dann ist $x_0$ lokale Minimalstelle (lokale Maximalstelle), d.h. es gibt $\epsilon > 0$ mit $f(x) \leq f(x_0)$ (bzw. $f(x) \geq f(x_0)$) für alle $x\in (x_0-\epsilon, x_0+\epsilon)$.

````

````{prf:proof}
Wieder beweisen wir nur den Fall einer Minimalstelle, jener für Maximalstellen ist analog.
$i)$ Ist $x_0$ Minimalstelle, dann wissen wir bereits $f'(x_0) = 0$. Nun gilt für $x > x_0$ nach dem Mittelwertsatz für ein $\xi(x) \in (x_0,x)$

```{math}
 0 \leq  \frac{f(x)-f(x_0)}{x-x_0} = f'(\xi(x)).
```

Also folgt auch

```{math}
 0 \leq \frac{f'(\xi(x)) - f'(x_0)}{\xi(x)-x_0}.
```

Da $\xi(x) \rightarrow \x_0$ für $x \rightarrow x_0$ können wir den Grenzwert durchführen und erhalten $f''(x_0) \geq 0$.

$ii)$ Ist $f'(x_0) = 0$ und $f''(x_0) > 0$, dann folgt analog für $x > x_0$

```{math}
 f(x) - f(x_0) = (x-x_0) ( f'(x_0) + (f''(x_0) + R_2(\xi(x)))(\xi(x)-x_0)) = (f''(x_0) + R_2(\xi(x)))(\xi(x)-x_0)(x-x_0),
```

wobei $R_2$ das Restglied bei der ersten Ableitung ist. Ist $x-x_0$ klein genug, dann gilt
$|R_2(\xi(x))| < \frac{1}2 f''(x_0)$. Damit folg

```{math}
 f(x) - f(x_0) > \frac{1}2 f''(x_0) (\xi(x)-x_0)(x-x_0) > 0,
```

also $f(x) > f(x_0)$. Den Fall $x < x_0$ behandeln wir analog. $\square$
````
