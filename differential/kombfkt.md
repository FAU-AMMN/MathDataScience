# Ableitungsregeln für Kombinationen von Funktionen

Wir haben in den obigen Beispielen einige Ableitungen für elementare Funktionen ausgerechnet. Ähnlich wie auch sonst bei Grenzwerten können wir dies auf verschiedene Kombinationen (Summen, Produkte) von Funktionen erweitern:

````{prf:theorem}
Seien $f: D\subset \R \rightarrow \R$ und $g: D\subset \R \rightarrow \R$ in $x_0 \in D$ differenzierbar. Dann gilt:

* $i)$ Die Summe $f+g$ ist differenzierbar in $x_0$ mi

```{math}
 (f+g)'(x_0) = f'(x_0) + g'(x_0).
```

* $ii)$ Für $c \in \R$ gilt

```{math}
 (cf)'(x_0) = c f'(x_0).
```

* $iii)$ Das Produkt $fg$ ist differenzierbar mit Ableitung (Produktregel)

```{math}
 (fg)'(x_0) = f'(x_0) g(x_0) +  f(x_0) g'(x_0).
```

* $iv)$ Ist $g(x_0) \neq 0$, dann ist der Quotient $\frac{f}g$ differenzierbar mit Ableitung (Quotientenregel)

```{math}
 (\frac{f}g)'(x_0) = \frac{f'(x_0)}{ g(x_0)} -  \frac{f(x_0) g'(x_0)}{g(x_0)^2}.
```

````

````{prf:proof}
$i)$ und $ii)$ folgen direkt aus den Regeln für Grenzwerte, $ii)$ würde auch aus drei Folgen, wenn man $g(x) =c$ setzt. Um $iii)$ zu beweisen, betrachten wir

\begin{align*} \frac{f(x)g(x) - f(x_0)g(x_0)}{x-x_0} &= \frac{f(x)g(x) - f(x_0)g(x)}{x-x_0} + \frac{f(x_0)g(x) - f(x_0)g(x_0)}{x-x_0} \\
 &= \frac{f(x)  - f(x_0) }{x-x_0} g(x) + f(x_0) \frac{g(x) - g(x_0)}{x-x_0}
\end{align*}

Mit den Regeln für Grenzwerte von Summen und Produkten folgt dann direkt die Existenz des Grenzwerts mit

```{math}
 (fg)'(x_0) = f'(x_0) g(x_0) +  f(x_0) g'(x_0),
```

wobei wir die Stetigkeit von $g$ verwenden, um $g(x) \rightarrow g(x_0)$ zu erhalten.

Für (iv) zeigen wir nur den Fall $f=1$, der Rest ergibt sich dann aus der Produktregel. Es gilt\begin{align*}
\frac{\frac{1}{g(x)} - \frac{1}{g(x_0)}}{x-x_0} &= - \frac{g(x) - g(x_0)}{g(x) g(x_0) (x-x_0)} \end{align*}
Da $g(x_0) \neq 0$ folgt wegen der Stetigkeit von $g$ auch, dass $g(x) \neq 0$ in einer Umgebung von $x_0$ gilt, also ist der Quotient dort auch wohldefiniert und es gilt $\frac{1}{g(x)} \rightarrow \frac{1}{g(x_0)}$. Daraus folgt direkt die Quotientenregel. $\square$
````

````{prf:example}
Da wir schon gezeigt haben, dass jedes Monom differenzierbar ist, sehen wir mit $i)$ und $ii)$ auch, dass jedes Polynom

```{math}
 p: \R \rightarrow \R, x \mapsto \sum_{j=0}^m a_j x^j
```

differenzierbar ist mit

```{math}
 p'(x) = \sum_{j=1}^m j a_j x^{j-1} .
```

````

````{prf:example}
Aus der Quotientenregel sehen wir, dass jede rationale Funktion $f= \frac{p}q$ mit Polynomen $p$ und $q$ überall dort differenzierbar ist, wo $q$ keine Nullstelle hat.
````

Eine weitere zentrale Eigenschaft für Ableitungen ist die Kettenregel:

````{prf:theorem} Sei $f: D \rightarrow \R$ in $x_0 \in D$ differenzierbar und $g: \tilde D \rightarrow \R$ in $f(x_0) \in \tilde D$ differenzierbar. Dann ist $g \circ f: x \mapsto g(f(x))$ differenzierbar in $x_0$ und es gilt

```{math}
 (g\circ f)'(x_0) = g(f(x_0)) f'(x_0).
```

````

````{prf:proof}
Ist $f'(x_0) \neq 0$, dann ist für $x\neq x_0$ nahe genug bei $x_0$ auch $f(x) \neq f(x_0)$ und es gilt

```{math}
\lim_{x \rightarrow x_0} \frac{g(f(x))-g(f(x_0))}{x-x_0} = \lim_{x \rightarrow x_0} \frac{g(f(x))-g(f(x_0))}{f(x)-f(x_0)}
 \frac{f(x)-f(x_0)}{x-x_0} = g'(f(x_0)) f'(x_0).
```

Falls $f'(x_0)=0$ gilt, dann ist

```{math}
f(x) = f(x_0) +  R(x)(x-x_0
```

mit $R(x) \rightarrow  0$ für $x \rightarrow x_0$ und damit

```{math}
\lim_{x \rightarrow x_0} \frac{g(f(x))-g(f(x_0))}{x-x_0} =  
\lim_{x \rightarrow x_0} \frac{g(f(x_0)+R(x)(x-x_0)-g(f(x_0))}{R(x)(x-x_0)}  \lim_{x \rightarrow x_0} R(x) = 0,
```
also gilt auch hier die Kettenregel. $\square$.
````

````{prf:example}
Sei $h: \R \rightarrow \R, x\mapsto e^{-x^2/2}.$ Dann wenden wir die Kettenregel mit $f(x) = -\frac{x^2}2$, $f'(x) = -x$ und
$g(x) = e^x$, $g'(x)=e^x$ an und erhalten

```{math}
h'(x) = - x e^{-x^2/2}.
```

````

````{prf:theorem}
Sei $I$ ein Intervall in $R$ und $f: I \rightarrow \R$ streng monoton und differenzierbar. Dann ist die Umkehrfunktion $f^{-1}: f(I) \rightarrow I$ in allen Punkten $y=f(x)$ mit $f'(x) \neq 0$ differenzierbar und es gilt

```{math}
 (f^{-1})'(f(x)) = \frac{1}{f'(x)}, \qquad (f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}.
```
````

````{prf:proof}
Sei $x_0 \in I$, $f'(x_0) \neq 0$, $y_0 =f(x_0)$. Dann gilt mit dem Restglied $R$

```{math}
 \vert f(x) - f(x_0) \vert = \vert f'(x_0) + R(x) \vert ~\vert x- x_0\vert
```
  und wegen $R(x) \rightarrow 0$ und $f'(x_0) \neq 0$ folgt für $|x-x_0|$ klein, $x \neq x_0$

```{math}
 |f(x) - f(x_0)| \geq \frac{1}2 |f'(x_0)| ~|x-x_0| > 0.
```

Also folgt

```{math}
\frac{f^{-1}(y) - f^{-1}(y_0)}{y-y_0} =  \frac{f^{-1}(y) - f^{-1}(y_0)}{f(f^{-1}(y)) - f(f^{-1}(y_0))} =\frac{x -x_0}{f(x) - f(x_0)}.
```

Wegen der Differenzierbarkeit von $f$ existiert der Grenzwert und es gilt

```{math}
 (f^{-1})'(f(x_0)) = \frac{1}{f'(x_0)},
```

die zweite Identität folgt aus $f(x_0)=y_0$, $x_0 = f^{-1}(y_0)$. $\square$
````

````{prf:example}
Die Umkehrfunktion $\log: \R^+ \rightarrow \R$ der Exponentialfunktion erfüllt

```{math}
 \log'(y)  = \frac{1}{e^{\log(y)}} = \frac{1}y.
```

````

````{prf:example}
Die Umkehrfunktion des Sinus $\arcsin: (-\pi,\pi] \rightarrow \R$   erfüllt wegen $\sin'(x) = \cos(x)$

```{math}
 \arcsin'(y)  = \frac{1}{ \cos(\arcsin(y))} .
```

````
