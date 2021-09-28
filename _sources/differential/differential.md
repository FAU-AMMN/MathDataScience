Differentialrechnung
===

Im Folgenden wollen wir nun die Differentialrechnung betrachten, die auf einer lokal linearen Approximation von Funktionen basiert. Sei $f: \R \rightarrow \R$ und $x_0 \in \R$. Für $\epsilon > 0$ betrachten wir eine lineare Approximation von $f$, die an der Stelle $x_0$ mit $f$ übereinstimmt, d.h.

```{math}
 f(x) \approx f(x_0) + a (x-x_0).
```

Dies bedeutet die richtige Steigung $a \in \R$ is

```{math}
 a \approx \frac{f(x)-f(x_0)}{x-x_0} .
```

Da wir an einer lokalen Approximation interessiert sind, ist es naheliegend den Grenzwert $x \rightarrow x_0$ zu betrachten. Damit definieren wir die Ableitung an der Stelle $x_0$:

````{prf:definition}
Sei $f: D \subset \R \rightarrow \R$ mit $x_0 \in D$ Häufungspunkt von $D$. Falls der Grenzwert

```{math}
 f'(x_0) = \lim_{x \rightarrow x_0} \frac{f(x) - f(x_0)}{x-x_0}
```

existiert, heisst $f$ differenzierbar in $x_0$ und $f'(x_0)$ Ableitung  (oder auch Differentialquotient $f'(x) = \frac{dx}{dt}$, in der Physik auch $\dot f(x)$). Die Funktion $f$ heisst differenzierbar in $D$, wenn für alle $x \in D$ die Ableitung $f'(x)$ existiert.
Ist $f$ differenzierbar in $D$ und $f':D \rightarrow \R$ eine stetige Funktion, dann heisst $f$ stetig differenzierbar in $D$.
````

Üblicherweise betrachten wir Ableitungen auf offenen Mengen $D$, dort ist jeder Punkt $x_0 \in D$ ein Häufungspunkt von $D$.
Aus der Definition sehen wir sofort, dass wenn $f$ differenzierbar in $x_0$ ist, eine Darstellung

```{math}
 f(x) = f(x_0) + f'(x_0)(x-x_0) +R(x)(x-x_0)
```

existiert mit einem sogenannten Restglied $R(x)$, sodass $R(x) \rightarrow 0 $ für $x \rightarrow x_0$. Insbesondere sehen wir

```{math}
 \lim_{x \rightarrow x_0} f(x) = f(x_0),
```

d.h. $f$ ist stetig in $x_0$.

````{prf:example}
Eine lineare Funktion $f: \R \rightarrow \R, x \mapsto a x + b$ ist differenzierbar in $\R$ mit Ableitung $f'(x) = a$.
````

````{prf:example}
Ein Monom $f: \R \rightarrow \R, x \mapsto x^m$, $m \geq 1$ ist differenzierbar in $\R$ mit Ableitung $f'(x) = m x^{m-1}$. Dies sehen wir aus

```{math}
 \frac{x^m - x_0^m}{x-x_0} = \sum_{j=0}^{m-1} x^j x_0^{m-1-j} .
```

Damit existiert der Grenzwert wegen $x^j \rightarrow x_0^j$ für $x \rightarrow x_0$.
````

````{prf:example}
Die Exponentialfunktion $f: \R \rightarrow \R, x \mapsto e^x$ ist differenzierbar in $\R$ mit Ableitung $f'(x) = e^x$, da

```{math}
 \frac{e^x - e^{x_0}}{x-x_0} = e^{x_0}  \frac{e^{x-x_0}-1}{x-x_0}
```

gilt und für $h \in \R$

```{math}
 \frac{e^h - 1}h =  h \sum_{j=2}^\infty \frac{1}{j!}h^{j-2} \leq h  \sum_{j=0}^\infty \frac{1}{j!}h^{j} = h e^h \rightarrow 0
```

für $h \rightarrow 0$.
````
