# Potenzreihen und Exponentialfunktion

Potenzreichen sind spezielle Reihen von der Form $\sum_{n=0}^\infty a_n (x-x_0)^n$, mit einer gegebenen reellen Koeffizientenfolge $(a_n)$ und einem Basispunkt $x_0 \in \R$. Der Unterschied zu einfachen Reihen ist, dass wir verschiedene Werte für das Argument $x\in \R$ einsetzen möchten, die Potenzreihe ist dann also eine Funktion von $x$, idealerweise von $\R$ nach $\R$. Allerdings ist nicht klar für welche $x \in \R$ die Reihe konvergiert.

````{prf:example}
Für $x \in (-1,1)$ können wir die Funktion
```{math}
 f: x \mapsto \sum_{n=0}^\infty x^n = \frac{1}{1-x}
```

über die (geometrische) Potenzreihe definieren. Für $|x| \geq 1$ konvergiert die Reihe nicht. Wir beachten aber, dass die Definition $\frac{1}{1-x}$ für $x\neq 1$ möglich ist.
````

Wie sieht nun allgemein der Definitionsbereich einer über eine Potenzreihe definierten Funktion aus, d.h. für welche Argumente $x$ konvergiert die Potenzreihe ? Wir sehen, dass die Potenzreihe für $x=x_0$ immer definiert ist und den Wert $0$ ergibt. Es ist naheliegend, dass die Konvergenz für $x$ nahe bei $x_0$ eher gegeben ist als bei größerem Abstand. Zur einfacheren Schreibweise werden wir im Folgenden Resultate für $x_0 = 0$ formulieren, dies ist aber keine Einschränkung, denn für $x_0 \neq 0$ verwenden wir einfach die Resultate für $z=x-x_0$.

````{prf:theorem}
Sei $\sum_{n=0}^\infty a_n x^n$ eine Potenzreihe. dann gibt es ein eindeutiges $r \in [0,\infty]$, den sogenannten Konvergenzradius der Reihe, mit folgenden Eigenschaften:

* $i)$ Die Reihe konvergiert absolut für $|x| < r$.

* $ii)$ Die Reihe divergiert für $|x| > r$.

````

````{prf:proof}
 Wir definieren

```{math}
 r:= \sup\{ |x| ~|~ \exists x \in \R, \sum_{n=0}^\infty a_n x^n \text{ konvergiert} \}.
```

Sei $|x|<r$, dann gibt es ein $\overline{x} \in \R$ mit $|\overline{x}|>|x|$, sodass $\sum_{n=0}^\infty a_n \overline{x}^n$ konvergiert. Damit ist die Folge $|a_n|~ |\overline{x}|^n$ eine Nullfolge und insbesondere beschränkt. Sei $C$ die obere Schranke, dann gilt

```{math}
|a_n|~ |x|^n \leq C \left( \frac{|x|}{\overline{x}} \right)^n.
```
Wegen $\frac{|x|}{\overline{x}} < 1$ haben wir eine konvergente geometrische Reihe als Majorante und damit istdie Potenzreihe $\sum_{n=0}^\infty a_n x^n $ absolut konvergent für alle $x$ mit $|x|<r$.
Aus der Definition von  $r$ ist umgekehrt klar, dass die Potenzreihe divergiert für $|x|>r$.
````

````{prf:example}
Wir betrachten $\sum_{n=0}^\infty \frac{(-1)^{n}}{n+1}x^{n+1} = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}x^{n}. $
Die geometrische Reihe $\sum_{n=0}^\infty |x|^n$ ist eine Majorante, deshalb sehen wir sofort die Konvergenz für $|x| < 1$, d.h. es folgt $r \geq 1$. Andererseits wissen wir schon, dass die Reihe für $x=-1$, d.h. $-
\sum_{n=0}^\infty \frac{1}{n+1}$ nicht konvergiert. Damit folgt $r=1$.
````

Wir können auch das Quotientenkriterium auf Potenzreihen anwenden und sehen, dass Konvergenz vorliegt, wenn

```{math}
 \forall n \geq n_0: ~\left\vert \frac{a_{n+1} x^{n+1}}{a_n x^n} \right\vert \leq q < 1
```

gilt. Dies ist gleichbedeutend zu

```{math}
 |x| \leq q \frac{|a_n|}{|a_{n+1}|}
```

für alle $n \geq n_0$, und wir sehen also, dass die Reihe für

```{math}
 |x|<\inf_{n \geq n_0} \frac{|a_n|}{|a_{n+1}|}
```

immer konvergiert. Also gilt auch

```{math}
 r \geq \inf_{n \geq n_0} \frac{|a_n|}{|a_{n+1}|} .
```

Da wir $n_0$ beliebig groß wählen können, gilt sogar

```{math}
 r \geq \lim_{n_0 \rightarrow \infty} \inf_{n \geq n_0} \frac{|a_n|}{|a_{n+1}|} .
```

Dieser Grenzwert existiert, da $ \inf_{n \geq n_0} \frac{|a_n|}{|a_{n+1}|}$ eine monoton fallende Folge ist (das Infimum wird über kleiner werdende Menge genommen, die nach unten beschränkt ist).
Dies führt uns nebenbei  auf die Definition des Limes inferior, für eine reelle Folge $x_n$ definieren wir

```{math}
 \lim\inf_{n \rightarrow \infty} x_n = \lim_{n \rightarrow \infty} \inf_{m \geq n} x_m .
```

Analog definieren wir auch den Limes superior

```{math}
 \lim\sup_{n \rightarrow \infty} x_n = \lim_{n \rightarrow \infty} \sup_{m \geq n} x_m .
```

Man kann sogar zeigen, dass eine Folge konvergiert, wenn Limes inferior und Limes superior existieren und es gilt $\liminf x_n = \lim\sup x_n$.

## Exponentialfunktion und Multiplikation von Reihen

Wir definieren nun die Exponentialfunktion $\exp(x)$ oder auch $e^x$ über eine Potenzreihe als

```{math}
 e^x:= \sum_{n=0}^\infty \frac{1}{n!} x^n
```

wobei $0!=1$ und $n! = \prod_{i=1}^n i$ für $n > 0$. Wenden wir das Quotientenkriterium an, so folgt

```{math}
 r \geq \lim\inf_n n+1 = \infty,
```

also konvergiert die Exponentialreihe für alle $x \in \R$.
Analog können wir auch Sinus- und Kosinusfunktionen als Verwandte der Exponentialfunktion über Potenzreihen definieren. Es gilt

\begin{align*}
\sin(x) &= \sum_{n=0}^\infty (-1)^n \frac{x^{2n+1}}{(2n+1)!} \\
\cos(x) &= \sum_{n=0}^\infty (-1)^n \frac{x^{2n }}{(2n )!}.
\end{align*}

Auch hier sehen wir, z.B. aus dem Quotientenkriterium, dass der Konvergenzradius $r=\infty$ ist.

Wir haben schon gesehen, dass die Summe von konvergenten Reihen wieder konvergent ist. Hat die Reihe $\sum_{n=0}^\infty a_n x^n$ den Konvergenzradius $r_1$ und die Reihe  $\sum_{n=0}^\infty b_n x^n$ den Konvergenzradius $r_2$, dann konvergiert  $\sum_{n=0}^\infty (a_n+b_n) x^n$  mit  Konvergenzradius $r \geq \min\{r_1,r_2\}.$ Bei unterschiedlichen Vorzeichen kann der Konvergenzradius der Summe natürlich viel größer als die Summe zu sein, wie wir am Beispiel $a_n = 1$, $b_n = -1$ für alle $n$ sehen.
Konvergente Reihen in $\R$ können wir auch multiplizieren, dementsprechend gilt dasselbe für Potenzreihen, diese bleiben auch Potenzreihen, es gilt innerhalb der Konvergenzradien

```{math}
 \left( \sum_{n=0}^\infty a_n x^n \right) \left( \sum_{n=0}^\infty b_n x^n \right) = \sum_{n=0}^\infty c_n x^n
```

mit geeigneten Koeffizienten $c_n$. Wir beginnen mit den endlichen Summen

\begin{align*}\left( \sum_{n=0}^m a_n x^n \right) \left( \sum_{n=0}^m b_n x^n \right) =& (a_0 + a_1x+ \ldots + a_m x^m)(b_0 + b_1x+ \ldots + b_m x^m) \\
=& a_0 b_0 + (a_0b_1+a_1b_0)x + (a_0 b_2 + a_1 b_1 + a_2 b_0)x^2 + \ldots \\ & + \sum_{j=0}^m a_j b_{m-j} x^m + \ldots +a_m b_m x^m .
\end{align*}

Betrachten wir nun die endliche Reihe bis $m+1$, so kommen nur Terme dazu, die Vielfache von $x^j$ mit $j > m$ sind. Die Koeffizienten der ersten $m$ Terme ändern sich nicht mehr. Damit zeigen wir induktiv

```{math}
 c_n =  \sum_{j=0}^n a_j b_{n-j}  ,
```

 man bezeichnet dies auch als Faltung der Koeffizienten $(a_j), (b_j)$.
Als Anwendung können wir die Exponentialfunktion betrachten, etwa

```{math}
 e^x e^{-x} = \sum_{n=0}^\infty \frac{1}{n!} x^n  \sum_{n=0}^\infty \frac{(-1)^n}{n!} x^n .
```

Hier gilt  dann

```{math}
 c_n =  \sum_{j=0}^n \frac{(-1)^{n-j}}{j! (n-j)!} .
```

Für $n=0$ erhalten wir $c_0 =1$, für $n > 0$ können wir den Binomischen Lehrsatz verwenden:

````{prf:lemma}
Für $x,y \in \R$ und $n \in \N\setminus\{0\}$ gilt

```{math}
 (x+y)^n = \sum_{j=0}^\infty (\begin{matrix} n\\j \end{matrix} ) ~  x^j~ y^{n-j}
```

mit dem Binomialkoeffizienten

```{math}
  (\begin{matrix} n\\j \end{matrix} ) = \frac{n!}{j! (n-j)!}.
```

````

````{prf:proof}
 Wir beweisen das Resultat durch vollständige Induktion. Für $n=0$ ist

```{math}
(x+y)^0 = 1 =  \sum_{j=0}^0 (\begin{matrix} 0\\0 \end{matrix} ) ~  x^0~ y^0 .
```
 Für $n=1$ ist
```{math}
 (x+y) = (\begin{matrix} 0\\0 \end{matrix} ) ~  x^1~ y^0 + (\begin{matrix} 1\\0 \end{matrix} ) ~  x^0~ y^1.
```

Nun nehmen wir an das Resultat gilt für ein $n \in \N$ und folgern die Gültigkeit für $n+1$.
Wir haben

\begin{align*}
(x+y)^{n+1} &= (x+y) (x+y)^n =  (x+y) \sum_{j=0}^n (\begin{matrix} n\\j \end{matrix} ) ~  x^j~ y^{n-j} \\
&=\sum_{j=0}^n (\begin{matrix} n\\j \end{matrix} ) ~  x^{j+1}~ y^{n-j} +\sum_{j=0}^n (\begin{matrix} n\\j \end{matrix} ) ~  x^j~ y^{n+1-j}  \\
&= \sum_{j=1}^{n+1} (\begin{matrix} n\\j \end{matrix} ) ~  x^{j}~ y^{n+1-j}  + \sum_{j=0}^n (\begin{matrix} n\\j \end{matrix} ) ~  x^j~ y^{n+1-j} \\
&= (\begin{matrix} n+1\\ 0 \end{matrix} ) y^{n+1}+ \sum_{j=1}^{n } \left( (\begin{matrix} n\\j \end{matrix} ) +  (\begin{matrix} n\\j-1 \end{matrix} ) \right) ~  x^{j}~ y^{n+1-j} + (\begin{matrix} 0\\ 0 \end{matrix} ) x^{n+1}
\end{align*}

wobei wir verwendet haben, dass

```{math}
1 =
\begin{pmatrix} n+1\\ 0 \end{pmatrix} 
= \begin{pmatrix} n\\ 0 \end{pmatrix}.
```

Nun rechnen wir noch leicht nach, dass
```{math}
\begin{pmatrix} n\\j \end{pmatrix} +  \begin{pmatrix} n\\j-1 \end{pmatrix}
=
\begin{pmatrix} n+1\\j \end{pmatrix}
```

gilt und erhalten damit die binomische Formel auch für $n+1$.
````

Setzen wir dies in die obige Formel für $e^x e^-x$ ein, so folgt für $n > 0$

```{math}
c_n = \frac{1}{n!}(-1+1)^n = 0 .
```

Also ist tatsächlich

```{math}
 e^{-x} = \frac{1}{e^x}.
```

Mit der gleichen Formel für $e^x e^x$ erhalten wir analog

```{math}
 c_n = \frac{1}{n!}(1+1)^n =  \frac{1}{n!}(2)^n .
```

Setzen wir dies ein, so folgt $e^x e^x = e^{2x}$.
Allgemeiner können wir mit Hilfe der binomischen Formel auch $e^x e^y$ berechnen. Für das Produkt von Potenzreihen mit verschiedenen Argumenten erhalten wir analog zur Rechnung oben

```{math}
\left( \sum_{n=0}^\infty  a_n x^n \right) \left( \sum_{n=0}^\infty b_y x^n \right) =
\sum_{n=0}^\infty \sum_{k=0}^n a_k b_{n-k} x^k y^{n-k}.
```

Damit folgt

```{math}
 e^x e^y = \sum_{n=0}^\infty \sum_{k=0}^n \frac{1}{k!} \frac{1}{(n-k)!} x^k y^{n-k} =
\sum_{n=0}^\infty \frac{1}{n!} \sum_{k=0}^n (\begin{matrix} n\\ k \end{matrix} )  x^k y^{n-k}.
```

Setzen wir die Binomische Formel ein, so erhalten wir

```{math}
 e^x e^y = \sum_{n=0}^\infty \frac{1}{n!}  (x+y)^n = e^{x+y},
```

die charakteristische Eigenschaft einer Exponentialfunktion.
