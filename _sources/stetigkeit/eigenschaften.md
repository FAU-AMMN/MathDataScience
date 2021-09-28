# Eigenschaften stetiger reeller Funktionen

Im Fall reeller Funktionen $f: \R \rightarrow \R$ hat die Stetigkeit einige spezielle Eigenschaften. Intuitiv ist eine reelle Funktion stetig, wenn wir sie zeichnen können, ohne den Stift vom Blatt zu nehmen. Dies bedeutet aber auch, um von einem Funktionswert zum anderen zu kommen, müssen wir alle dazwischen passieren. Mathematisch formalisiert dies der sogenannte {\em Zwischenwertsatz}:

````{prf:theorem}
Sei  $a<b \in \R$, $f: [a,b] \rightarrow \R$ stetig und wir definieren

```{math}
 A = \min\{f(a),f(b)\}, \quad B = \max\{f(a),f(b)\}.
```

Dann gibt es für jedes $y \in [A,B]$ ein $x \in [a,b]$ mit $f(x) =y$, d.h. $f([a,b]) \supset [A,B]$.
````

````{prf:proof}
 Sei $y \in [A,B]$. Wir nehmen an $f(a) \leq f(b)$, der Fall $f(b) \geq f(a)$ ist analog. Wir konstruieren wieder Folgen $[a_n,b_n]$ durch Bisektion. Sei dazu $a_0=a, b_0=b$. Dann setzen wir $c_0 = \frac{a_0+b_0}2$ und berechnen $f(c_0)$. Ist $f(c_0) > C$, dann setzen wir $a_1=a_0$, $b_1=c_0$, andernfalls $a_1=c_0$, $b_1=b_0$. Gehen wir so weiter, dann konstruieren wir eine monoton wachsende Folge $a_n$ und eine monoton fallende Folge $b_n$ mit $a_n > b_n$, $|b_n-a_n|=\frac{b-a}{2^n}$, $f(a_n) \leq C$, $f(b_n) \geq C$. Somit folgt, das $a_n$ und $b_n$ konvergieren und da $|b_n-a_n|\rightarrow 0$ gilt, haben die beiden den gleichen Grenzwert $x \in [a,b]$.

Wegen der Stetigkeit von $f$ folg

```{math}
 \lim_{n \rightarrow \infty} f(a_n) = \lim_{n \rightarrow \infty} f(b_n) = C.
```

Wäre nun $f(x) > C$, dann gilt mit $\epsilon = f(x) - C$ imme

```{math}
 |f(x) - f(a_n)| = f(x) - f(a_n) \geq f(x) - C = \epsilon
```
ein Widerspruch zur Konvergenz von $a_n$. Analog würde $f(x) < C$ der Konvergenz von $b_n$ widersprechen. Also folgt$f(x) = C$.
````

\begin{cor}
Für $a <b \in \R$ gilt: $f([a,b])$ ist ein Intervall in $\R$.
\end{cor}

\begin{cor}
Sei $f$ stetig und gibt es $x_+$ und $x_-$ mit $f(x_+) \geq 0$ und $f(x_-) \leq 0$, dann hat $f$ zumindest eine Nullstelle zwischen $x_-$ und $x_+$.
\end{cor}

Für stetige Funktionen können wir nicht nur Nullstellen finden, sondern auch Minima und Maxima:

````{prf:definition}
Sei $f: X \rightarrow \R$ eine reellwertige Funktion. Dann heisst $\overline{x} \in X$ Minimalstelle (und $f(\overline{x})$ Minimalwert), wen

```{math}
 \forall x \in X: f(\overline{x}) \leq f(x).
```
Darüber hinaus heisst $\overline{x} \in X$ Maximalstelle (und $f(\overline{x})$ Maximalwert), wen

```{math}
 \forall x \in X: f(\overline{x}) \geq f(x).
```
````

Wichtig für die Existenz von Minimal- bzw. Maximalstelle ist das Konzept der Kompaktheit:

````{prf:definition}
Eine Teilmenge $M \subset X$ heisst kompakt, wenn jede Folge $(x_n)$ mit $x_n \in M$ für $n \in \N$ eine konvergente Teilfolge hat, deren Grenzwert in $M$ liegt.
````

````{prf:theorem}$M \subset \R^n$ ist genau dann kompakt, wenn $M$ abgeschlossen und beschränkt ist.
````

````{prf:proof}
 Ist $M$ abgeschlossen und beschränkt, dann folgt aus dem Satz von Bolzano-Weierstrass, dass jede Folge in $M$ eine konvergente Teilfolge $(x_{n_k})$ hat. Da $M$ abgeschlossen ist, ist $\R^n \setminus M$ offen. D.h. für jedes $z \in \R^n \setminus M$ gibt es eine $\epsilon$-Umgebung mit $U_\epsilon \subset \R^n \setminus M$. Daraus folgt wegen $x_n \in M$, dass $\Vert x_n - z \Vert \geq \epsilon$ ist, also kann $z$ nicht der Grenzwert von $x_n$ sein. Daraus folgt $\lim_k x_{n_k} \in M$.

````{prf:theorem}Sei $f: M \subset X \rightarrow \R$ stetig auf der kompakten Menge $M$. Dann hat $f$ zumindest eine Minimal- und eine Maximalstelle in $M$.
````

````{prf:proof}
Wir beweisen nur die Existenz einer Minimalstelle, die Maximalstelle ist analog. Sei $\alpha = \inf_{x \in M} f(x)$. Dann gibt es für jedes $n \in \N$ ein $x_n \in M$ mit $f(x_n) < \alpha+ \frac{1}n$. Da $M$ kompakt ist hat $x_n$ eine konvergente Teilfolge $(x_{n_k})$ mit Grenzwert $\overline{x} \in M$. Wegen der Stetigkeit folgt

```{math}
 f(\overline{x}) = \lim_k f(x_{n_k}) \leq \lim \alpha - \frac{1}{n_k} = \alpha.
```

Also ist $\overline{x}$ Minimalstelle.
````

````{prf:definition}
Eine reelle Funktion $f: M \rightarrow \R$ mit $M \subset \R$ heisst

* monoton wachsend (bzw. streng monoton wachsend), wenn für alle $y > x

```{math}
 f(y) \geq f(x) \qquad (\text{ bzw. } f(y) > f(x).
```

* monoton fallend (bzw. streng monoton fallend), wenn für alle $y > x

```{math}
 f(y) \leq f(x) \qquad (\text{ bzw. } f(y) < f(x). )
```

````

````{prf:theorem} Für $D \subset \R$ und $f: D \rightarrow \R$ gelten die folgenden Eigenschaften:

* $i)$ Ist f streng monoton, dann ist $f$ injektiv.

* $ii)$ Ist $D=[a,b]$ und $f$ injektiv, dann ist $f$ streng monoton.

* $iii)$ Ist $D=[a,b]$ und $f:D \rightarrow [c,d]$ injektiv, dann ist $f^{-1}$ stetig.
````

````{prf:proof}
 Für $i)$ nehmen wir an es gibt $x_1 \neq x_2$ mit $f(x_1) = f(x_2)$, o.B.d.A. $x_1 < x_2$. Wegen der strengen Monotonie gilt aber $f(x_1) < f(x_2)$ (falls monoton steigend) oder $f(x_1) > f(x_2)$ (falls monoton fallend), beides widerspricht $f(x_1) = f(x_2)$.
Für $ii)$ nehmen wir an $f$ wäre nicht streng monoton, d.h. es gibt $x_1 < x_2 < x_3$ mit $f(x_1) < f(x_2)$, $f(x_3) < f(x_2)$ oder $f(x_1) < f(x_2)$, $f(x_3) < f(x_2)$. Im ersten Fall gibt es ein $C \in (f(x_1),f(x_2)) \cap (f(x_2),f(x_3)$ und wegen dem Zwischenwertsatz existieren dann $z_1 \in (x_1,x_2)$ und $z_2 \in (x_2,x_3)$ mit$C = f(z_1) = f(z_2)$. Damit ist $f$ nicht injektiv. Der zweite Fall ist analog.

$iii)$ Nach $ii)$ ist $f$ streng monoton, wir nehmen an $f$ ist streng monoton wachsend, der Fall einer streng monoton fallenden Funktion ist analog. Sei $y_n$ eine Folge mit Grenzwert $\overline{y}$. Dann gibt es eine monotone Teilfolge $y_{n_k}$ mit demselben Grenzwert. Nun sei $x_n = f^{-1}(y_n)$. Dann ist $x_{n_k}$ monoton und beschränkt, also konvergent. Sei $x= \lim x_{n_k}$. Nehmen wir an $f(\overline{y}) > x$, dann ist wegen der strengen Monotonie $f^{-1}(y) > x$ für alle $y \geq \overline{y}$, und $f^{-1}(y) < x$ für alle $y < \overline{y}$.Damit ist $f^{-1}$ nicht surjektiv, was der Bijektivität widerspricht. Also gilt $f^{-1}(\overline{y}) = x$. Abschließend folgern wir aus der Konvergenz der Teilfolge auch noch die Konvergenz der gesamten Folge $(x_n)$. Wegen der Monotonie folgt $x_{n_k} < x_n$ für $y_{n_k} < y_n$. Sei also $n_k$ so, dass  $|y_{n_k} - \overline{y}| < \epsilon$ und $m$ so, dass

```{math}
 |y_{n} - \overline{y}| < |y_{n_k} - \overline{y}| < \epsilon
```

für $n \geq m$ ist. Dann folgt auc

```{math}
 |x_n - x|  = x - x_n < x-x_{n_k} = |x-x_{n_k}|.
```

Da die rechte Seite gegen beliebig klein wird mit $k$ gegen unendlich, konvergiert also auch $x_n$ gegen $x$.
````
