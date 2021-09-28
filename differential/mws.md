
# Der Mittelwertsatz der Differentialrechnung

Wir betrachten nun eine Version des Zwischenwertsatzes für Ableitungen, der einen Zusammenhang zwischen Ableitungen undDifferenzenquotienten herstellt. Als Grundlage dafür beweisen wir zunächst ein interessantes Resultat über Minimal- und Maximalstellen:

````{prf:lemma}
Sei $f:[a,b] \rightarrow \R$ stetig und $x_0 \in (a,b)$ eine Minimal- oder Maximalstelle von $f$. Ist $f$ bei $x_0$ differenzierbar, dann gilt $f'(x_0) = 0$.````
**Beweis. ** Für $x_0 \in (a,b)$ gibt es ein $\epsilon > 0$ mit $(x_0 - \epsilon, x_0 + \epsilon) \subset (a,b)$. Ist $x_0$ Minimalstelle, dann gilt für alle $x \in (x_0 - \epsilon, x_0 + \epsilon)$ auch $f(x) \geq f(x_0)$ und für $\epsilon$ hinreichend klei

```{math}
 f(x) - f(x_0) = (f'(x_0) + R(x))(x-x_0).
```

Also folgt für $x > x_0$ bzw. $x < x_0$

```{math}
 f'(x_0) \leq -  R(x) \qquad \text{bzw.} \qquad f'(x_0) \geq  - R(x).
```

Im Grenzwert $x \rightarrow 0$ folgt dann$ 0 \leq f'(x_0) \leq 0$, also $f'(x_0) = 0$. Der Beweis für eine Maximalstelle ist analog mit umgedrehten Ungleichungszeichen. $\square$.

````{prf:theorem}
Sei $f:[a,b] \rightarrow \R$ differenzierbar auf $(a,b)$. Dann gibt es ein $x_0 \in (a,b)$ mit

```{math}
 \frac{f(b) - f(a)}{b-a} = f'(x_0) .
```

````

````{prf:proof}
Sei

```{math}
 g(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b-a}(x-a).
```

Dann gilt $g(a) = g(b) = 0$ un

```{math}
 g'(x) = f'(x) -  \frac{f(b) - f(a)}{b-a}.
```

$g$ ist eine stetige Funktion und nimmt deshalb auf $[a,b]$ sowohl sein Minimum als auch sein Maximum an. Ist $g$ konstant Null, dann ist $g'(x)$ für alle $x \in (a,b)$ und wir sind fertig. Andernfalls gibt es zumindest eine Minimal- oder Maximalstelle $x_0$ von $g$ im Intervall $(a,b)$, also folgt $g'(x_0)=0$, was den Mittelwertsatz impliziert. $\square$
````

Ähnlich beweist man folgende Verallgemeinerung des Mittelwertsatzes: Mit den gleichen Bedingungen an $f$ und $g$ wie oben, sowie $g(b) \neq g(a)$ und $g'(x) \neq 0$ für $x \in (a,b)$ folgt die Existenz eines $x_0 \in (a,b)$ mit

```{math}
\frac{f'(x_0)}{g'(x_0)} = \frac{f(b) - f(a)}{g(b) - g(a)}.
```

Eine interessante Anwendung der Differentialrechnung, ähnlich zu dieser Art von Quotienten ist die Regel von de l'Hospital, mit der wir zunächst unbestimmte Grenzwerte von Quotienten charakterisieren können. Ein Beispiel ist$ \lim_{x \rightarrow 0} \frac{\sin(x)}x$, das zunächst auf ein unbestimmtes $\frac{0}0$ führt. Nun ist aber

```{math}
\sin(x) = \sin(0) + \cos(0)x + R(x)x = (1+R(x))x,
```

mit $R(x) \rightarrow 0$, d.h.,

```{math}
 \lim_{x \rightarrow 0} \frac{\sin(x)}x = \lim_{x \rightarrow 0} \frac{(1+R(x))x}x = 1.
```

Die selbe Idee angewendet in Zähler und Nenner führt auf die allgemeinere Regel von de l'Hospital:

````{prf:theorem}
Seien $f$ und $g$ differenzierbar auf $[a,b]$ und $x_0 \in [a,b]$ mit $f(x_0)=g(x_0) = 0$, sowie$g'(x_0) \neq 0$. Dann gilt

```{math}
 \lim_{x \rightarrow x_0} \frac{f(x)}{g(x)} = \frac{f'(x_0)}{g'(x_0)}.
```

````

````{prf:proof}
 Es gilt für $x \neq x_0$ mit den entsprechenden Restgliedern $R$ und $S$

\begin{align*}
f(x) &= (f'(x_0) + R(x))(x-x_0) \\
g(x) &= (g'(x_0) + S(x))(x-x_0),
\end{align*}

mit $\lim_{x \rightarrow x_0} R(x) = \lim_{x \rightarrow x_0} S(x) =0. $
Also folgt

```{math}
\lim_{x \rightarrow x_0} \frac{f(x)}{g(x)} = \lim_{x \rightarrow x_0} \frac{f'(x_0) + R(x)}{g'(x_0) + S(x)} = \frac{f'(x_0)}{g'(x_0)}.  \quad\square
```
````

````{prf:example}
Sei $f(x) = e^x-1$ und $g(x) = \sin(x)$. Dann ist

```{math}
 \lim_{x \rightarrow 0} \frac{f(x)}{g(x)} = \frac{e^0}{\cos(0)} = 1.
```

````
