Stetigkeit
===

Wir haben uns bei den Potenzreihen schon mit Funktionen beschäftigt, nun wollen wir diese näher betrachten und das Konzept der Stetigkeit einführen. Bei reellen Funktionen verstehen wir stetige Funktionen als solche ohne Sprungstellen und Singularitäten, diese Funktionen kann man aufzeichnen ohne den Stift vom Blatt zu lösen. Allgemeiner können wir das Konzept von Folgenstetigkeit definieren:

````{prf:definition}
Sei $f: X \rightarrow Y$ eine Abbildung zwischen den metrischen Räumen $(X,d_X)$ und $(Y,d_Y)$. Dann heisst $f$ folgenstetig in $x \in X$, wenn für jede Folge $(x_n) \subset X$ mit Grenzwert $x$ auch $f(x_n) \rightarrow f(x)$ gilt. Die Funktionen heisst folgenstetig in einer Menge $M \subset X$, wenn sie in jedem $x \in M$ folgenstetig ist.
````

````{prf:example}
Die Funktion $f: \R \rightarrow \R, x \mapsto x^2$ ist stetig, da für $x_n \rightarrow x$ auch $x_n^2 \rightarrow x$ konvergiert
````

````{prf:example}
Die sogenannte Heaviside-Funktion $H: \R \rightarrow \R$ mit $H(x) = 1$ für $x \geq 0$ und $H(x)=0$ für $x < 0$ ist im Punkt $x =0$ unstetig, sonst stetig. Wählen wir die Folge $x_n = -\frac{1}n$, so ist $H(x_n) = 0$ für alle $n$, damit auch $\lim_n H(x_n) = 0 \neq H(0)$.
````

Eine alternative Definition von Stetigkeit basiert auf dem Verhalten der Funktion in $\epsilon$-Umgebungen:

````{prf:definition}
Eine Funktion $f: X \rightarrow Y$ heisst stetig in $x \in X$, wen

```{math}
 \forall \epsilon > 0 ~\exists \delta > 0 ~\forall \tilde{x} \in U_\delta(x): f(\tilde x) \in U_\epsilon(f(x)),
```

wobei
\begin{align*}
U_\delta(x) &= \{\tilde x \in X~|~d_X(x,\tilde x) < \delta \} \\
U_\epsilon(f(x)) &= \{\tilde y \in Y~|~d_Y(f(x),\tilde y) < \epsilon \}.
\end{align*}
Die Funktion $f$ heisst stetig in $M \subset X$, wenn sie in allen Punkten $x\in M$ stetig ist.
````

````{prf:theorem}
Eine Funktion $f: X \rightarrow Y$ ist genau dann stetig, wenn sie folgenstetig ist.
````

````{prf:proof}
 Sei $f$ stetig in $X$ und $x_n$ eine Folge mit Grenzwert $x$. Dann gibt es ein $n_0 \in \N$, sodass für alle $n \geq n_0$ gilt: $ d_X(x,x_n) < \delta$ und daraus folgt $ d_y(f(x),f(x_n)) < \epsilon$. Damit ist $f$ folgenstetig.

Nehmen wir umgekehrt an $f$ sei nicht stetig. Dann gibt es für ein $\epsilon > 0$ kein $\delta > 0$ mi

```{math}
 f(U_\delta(x)) \subset U_\epsilon (f(x)).
```

Insbesondere gibt es für jedes $n \in \N$ ein $x_n$ mit $d_X(x,x_n) < \frac{1}n$ und $d_Y(f(x),f(x_n)) > \epsilon$. Damit konvergiert $x_n$ gegen $x$ aber nicht $f(x_n)$ gegen $f(x)$, also ist $f$ nicht folgenstetig.
````

Mit der Äquivalenz der Definitionen können wir verschiedene Eigenschaften von stetigen Funktionen beweisen, indem wir die jeweils passende Eigenschaft benutzen:

````{prf:theorem} Seien $(X,d_X)$, $(Y,d_Y)$, $(Z,d_Z)$ metrische Räume und $f: X \rightarrow Y$, $g: Y \rightarrow Z$ so, dass $f$ stetig bei $x$ und $g$ stetig bei $y=f(x)$ ist. Dann ist die Hintereinanderausführung $f \circ g$ stetig bei $x$.
````

````{prf:proof}
 Sei $(x_n)$ eine Folge mit $x_n \rightarrow x$. Dann gilt wegen der Stetigkeit von $f$ auch $y_n=f(x_n) \rightarrow f(x) = y$. Wegen der Stetigkeit von $g$ bei $y=f(x)$ folgt dann $g(y_n) \rightarrow g(y)$, also $g\circ f(x_n) \rightarrow g \circ f(x)$, also ist $g \circ f$ stetig bei $x$.
````

````{prf:theorem} Sei $(X,d)$ ein metrischer Raum und $f: X \rightarrow \R^n$, $g: X \rightarrow \R^n$ seien stetig bei $x \in X$. Dann sind auch $f +g $ und $f \circ g$ stetig bei $x$.
````

````{prf:proof}
 Für $x_n \rightarrow x$ folgt $f(x_n) \rightarrow f(x)$ und $g(x_n) \rightarrow g(x)$. Damit gilt wegen den Eigenschaften konvergenter Folgen auch $f(x_n) + g(x_n) \rightarrow f(x) + g(x)$ und
$f(x_n) \cdot g(x_n) \rightarrow f(x) \cdot g(x)$. Also sind $f+g$ und $f \cdot g$ stetig.
````

\begin{cor}
Alle Polynome $p: \R  \rightarrow \R$, $ x \mapsto \sum_{j=0}^n a_j x^j$ sind stetig auf $\R$.
\end{cor}
Eine etwas stärkere Eigenschaft als Stetigkeit ist die Hölder- oder auch Lipschitz-Stetigkeit:

````{prf:definition}
Eine Funktion $f: X \rightarrow Y$ zwischen metrischen Räumen heisst Hölder-stetig mit Exponent $0 < \alpha \leq 1$,wenn ein $c \in \R$ existiert, sodass

```{math}
 \forall x,y \in X: d_Y(f(x),f(y)) \leq c d_X(x,y)^\alpha
```

gilt. Im Fall $\alpha = 1$ heisst $f$ Lipschitz-stetig.
Die Funktion heisst lokal Hölder-stetig mit Exponent $\alpha$ (bzw. lokal Lipschitz-stetig, falls $\alpha =1$), wenn für alle $x \in X$ eine Umgebung $U_\epsilon(x)$ und eine Konstante $C=C(x)$ existiert, sodass

```{math}
 \forall y \in U_\epsilon(x): d_Y(f(x),f(y)) \leq C d_X(x,y) .
```

````

Es ist klar, dass Hölder-Stetigkeit auch lokale Hölder-Stetigkeit impliziert. Lokale Hölder-Stetigkeit impliziert immer auch Stetigkeit:

````{prf:theorem}
Sei $f: X \rightarrow Y$ lokal Hölder-stetig mit Exponent $\alpha > 0$. Dann ist $f$ stetig in $x$.
````

````{prf:proof}
 Sei $x \in X$ und $x_n$ eine Folge, die gegen $x$ konvergiert. Dann gibt es für jedes $\epsilon > 0$ ein $n_0$, sodas

```{math}
 d(x,x_n) < \left( \frac{\epsilon}{C} \right)^{\frac{1}\alpha} .
```

Daraus folgt für alle $n \geq n_0

```{math}
 d_Y(f(x),f(x_n)) < \epsilon ,
```

also gilt $f(x_n) \rightarrow f(x). $
````

````{prf:example}
Sei $m \in \N$, dann ist die Funktion $f(x)=x^m$ lokal Lipschitz-stetig mit $C(x) = ( m+1) |x|^{m-1}$.
````

````{prf:example}
Die Funktion $f(x)=|x|$ ist global Lipschitz-stetig mit $C=1$.
````
