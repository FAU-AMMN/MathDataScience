# Reihen

Eine spezielle Form von Folgen sind sogenannte Reihen, die wir als Summen von Folgen betrachten können:

````{prf:definition}
Sei $(X,\Vert \cdot \Vert)$ ein normierter Vektorraum und $(x_n)$ eine Folge in $X$. Dann identifizieren wir die Reihe $\sum_{k=0}^\infty x_k$ mit der Folge der Partialsummen

```{math}
 s_n = \sum_{k=0}^n x_k.
```

Falls die Folge $s_n$ gegen einen Grenzwert $s \in  X$ konvergiert, so bezeichnen wir

```{math}
 s = \sum_{k=0}^\infty x_k
```

und nennen die Reihe konvergent. Andernfalls nennen wir die Reihe divergent.
````

Wir beachten, dass wir natürlich auch jede Folge $x_n$ als Reihe

```{math}
 x_n =\sum_{k=0}^n y_k
```

schreiben können, mit $y_0=x_0$ und $y_k = x_k - x_{k-1}$ für $k > 0$. Wenn wir aber eine Folge explizit angeben können (etwa auch durch Ausrechnen der Partialsummen), dann sprechen wir eher von einer Folge und behandeln sie auch so. Wenn wir aber die Partialsummen nicht ausrechnen können, benötigen wir eine speziellere Betrachtung.

````{prf:example}
Für $q \in \R$ betrachten wir die geometrische Reihe

```{math}
 s_n = \sum_{k=0}^n q^k.
```

Wie wir schon gesehen haben, können wir die Partialsummen explizit berechnen. Für $q=1$ gilt $s_n = n+1$ und die Reihe ist offensichtlich divergent. Für $q\neq 1 $gilt

```{math}
 s_n = \frac{1-q^n}{1-q}.
```

Nun sehen wir, dass für $|q| <1$ gilt $q^n \rightarrow 0$ für $n \rightarrow 0$, also erhalten wir den Grenzwert

```{math}
 s  = \sum_{k=0}^\infty q^k = \frac{1}{1-q}.
```

Für $|q|>1$ gilt $|q^n| \rightarrow \infty$ für $n \rightarrow \infty$. Wegen der Dreiecksungleichung ist

```{math}
 |s_n| \geq \frac{|q^n|-1}{|q-1|} \rightarrow \infty,
```

also divergiert die Reihe.
Im verbleibenden Fall $q=-1$ gilt $s_n=1$ für $n$ gerade und $s_n=0$ für $n$ ungerade. Hier bleiben die Partialsummen zwar beschränkt, aber die Reihe konvergiert nicht.
````

````{prf:example}
Als zweites Beispiel betrachten wir für $q > 0$ die Reihe

```{math}
 s_n = \sum_{k=0}^n (k+1)^{-q}.
```

Hier ist zunächst völlig unklar, ob die Reihe konvergiert oder divergiert. Für $q=1$ sind die ersten Partialsummen $1$, $\frac{3}2$, $\frac{11}6$, $\frac{23}{12}$, $\ldots$ Die Reihe scheint also zu divergieren, aber wir haben kein Kriterium um dies einfach zu entscheiden. Für $q=2$ sind die ersten Partialsummen $1$, $\frac{5}4$, $\frac{23}{18}$,$\ldots$ Hier scheint es sich um Konvergenz zu handeln, aber wieder können wir nicht entscheiden, ob nicht einfach langsames Wachstum gegen unendlich vorliegt.
````

Im Folgenden wollen wir einfache Kriterien zur Konvergenz einer Reihe kennenlernen. Ein einfaches Beispiel in einem vollständigen normierten Raum erhalten wir aus der Äquivalenz der Konvergenz zur Cauchy-Eigenschaft einer Folge:

````{prf:theorem} Cauchy-Kriterium 
Eine Reihe in einem vollständigen metrischen Raum konvergiert genau dann, wenn es für alle $\epsilon > 0$ ein $n_0 \in \N$ gibt, sodass
```{math}
 \forall m > n \geq n_0: \quad \Vert \sum_{k=n+1}^m x_k \Vert < \epsilon
```

gilt.
````

````{prf:proof}
 Die obige Eigenschaft ist genau äquivalent dazu, dass die Folge $(s_n)$ der Partialsummen eine Cauchy-Folge ist, was wiederum äquivalent zur Konvergenz ist.
````

Ein sehr nützliches Kriterium ist das _Majorantenkriterium_, dafür definieren wir zunächst den Begriff einer Majorante:

````{prf:definition}
Sei $X$ ein vollständiger normierter Raum und $(x_n)$ eine Folge in $X$. Dazu sei $(c_n)$ eine Folge in $\R$ mt $c_n \geq 0$ für alle $n \in \N$, sodass für alle $n \in \N$ gilt:

```{math}
 \Vert x_n \Vert \leq c_n .
```

Dann heisst $(c_n)$ bzw. $\sum_{n=0}^\infty c_n$ Majorante von $(x_n)$ bzw. $\sum_{n=0}^\infty x_n$.
````

Mit Hilfe von Majoranten können wir wieder Konvergenzkriterien für Reihen in vollständigen normierten Räumen basierend auf Reihen in den positiven reellen Zahlen herleiten:

````{prf:theorem} Majorantenkriterium
Sei $X$ ein vollständiger normierter Raum und $(c_n)$ eine Majorante von $(x_n)$. Falls $\sum_{n=0}^\infty c_n$ konvergiert, dann konvergiert auch $\sum_{n=0}^\infty x_n$.
````

````{prf:proof}
 Wegen der Dreiecksungleichung gilt
\begin{align*}
\Vert s_m - s_n \Vert &= \Vert \sum_{k=n+1}^m x_k \Vert  \leq \sum_{k=n+1}^m  \Vert x_k \Vert \\
&\leq \sum_{k=n+1}^m c_k.\end{align*}
Wegen der Konvergenz der Reihe $\sum_{n=0}^\infty c_n$ sind die zugehörigen Partialsummen auch eine Cauchy-Folge, d.h. für alle $\epsilon > 0$ existiert ein $n_0 \in \N$, sodass für $m > n \geq n_0$ gilt:

```{math}
 \Vert s_m - s_n \Vert \leq \sum_{k=n+1}^m c_k < \epsilon.
```

Damit ist auch $(s_n)$ eine Cauchy-Folge und somit konvergent.
````

Wir beachten, dass wir die Konvergenz von $s_n=\sum_{k=0}^n c_k$ für $c_k \geq 0$ relativ einfach entscheiden können. $(s_n)$ ist dann eine monoton steigende Folge, diese konvergiert genau dann wenn sie beschränkt ist. Können wir also ein $C > 0$ finden mit

```{math}
 \sum_{k=0}^n c_k \leq C \qquad \forall n \in \N ,
```

dann konvergiert die Reihe.
Das Majorantenkriterium können wir speziell für Reihen in $X=\R$ anwenden. Es gilt, dass $\sum_{n=0}^\infty x_n$ konvergiert, falls  $\sum_{n=0}^\infty |x_n|$  konvergiert, da klarerweise $|x_n|$ eine Majorante für $x_n$ ist.Die Umkehrung stimmt aber nicht immer. Wir nennen deshalb eine Reihe in $\R$ bedingt konvergent, wenn $\sum_{n=0}^\infty x_n$ konvergiert, aber $\sum_{n=0}^\infty |x_n|$  divergiert. Falls auch $\sum_{n=0}^\infty |x_n|$ konvergiert, nennen wir die Reihe absolut konvergent. Bei bedingt konvergenten Reihen ist Vorsicht geboten, da eine Umordnung der Reihe, d.h. $\sum_{n=0}^\infty x_{\pi(n)}$ für eine bijektive Abbildung $\pi: \N \rightarrow \N$ einen anderen Grenzwert liefern kann.

````{prf:example}
Das Majorantenkriterium können wir nun zur Untersuchung der Konvergenz von $\sum_{n=0}^\infty (n+1)^{-q}$ verwenden.
Sei $q > 1$, dann wählen wir $c_n = 2^{-q \ell}$, wobei $\ell$ durch

```{math}
 2^\ell \leq n+1 \leq 2^{\ell+1}
```

bestimmt ist.Dann gilt

```{math}
 \sum_{n=0}^\infty c_n = \sum_{\ell=0}^\infty \sum_{n=2^\ell-1}^{2^{\ell+1}} c_n = \sum_{\ell=0}^\infty \sum_{n=2^\ell-1}^{2^{\ell+1}-2} 2^{-q\ell} =  \sum_{\ell=0}^\infty  2^{(1-q)\ell} = \sum_{\ell=0}^\infty  (2^{1-q})^\ell.
```

Für $q > 1$ ist $2^{1-q} < 1$, d.h. die geometrische Reihe rechts konvergiert und damit auch die Majorantenreihe.

Im Fall $q=1$ können wir mit dem Cauchy-Kriterium zeigen, dass die Reihe divergiert. Wäre sie konvergent, würde insbesondere $s_{2n} -s_n$ gegen Null konvergieren, es gilt aber

```{math}
 s_{2n} -s_n = \sum_{k=n+1}^{2n} \frac{1}k \geq \sum_{k=n+1}^{2n} \frac{1}{2n} = \frac{1}2.
```

````

Für die absolute Konvergenz von Reihen in $\R$ können wir nun etwa mit der geometrischen Reihe vergleichen, deren Konvergenz wir aus dem obigen Beispiel schon verstehen:

````{prf:theorem} Quotientenkriterium
Sei $(x_n)$ eine reelle Folge, sodass für ein $n_0 \in \N$ und ein $q \in [0,1)$ gilt:

```{math}
x_n \neq 0,\qquad \left\vert \frac{x_{n+1}}{x_n} \right\vert \leq q \qquad \forall~n \geq n_0.
```

Dann konvergiert $\sum_{n=0}^\infty x_n$ absolut.
````

````{prf:proof}
 Wegen $|x_{n+1}| \leq q~|x_n|$ können wir induktiv auch

```{math}
|x_n| \leq q^{n-n_0} |x_{n_0}|
```

folgern. Wir wählen also als Majorante $c_n= |x_n|$ für $n \leq n_0$ und $c_n = q^{n-n_0} |x_{n_0}|$ für
$n > n_0.$ Dann gilt

```{math}
 \sum_{n=0}^\infty c_n = \sum_{n=0}^{n_0-1} |x_n| + \sum_{n=n_0}^\infty q^{n-n_0} |x_{n_0}| =\sum_{n=0}^{n_0-1} |x_n| +  |x_{n_0}| \sum_{n=0}^\infty q^{n} = =\sum_{n=0}^{n_0-1} |x_n| +  \frac{|x_{n_0}|}{1-q} < \infty.
```

Also folgt die Konvergenz aus dem Majorantenkriterium.
````

````{prf:example}
Wir betrachten die Reihe $\sum_{n=0}^\infty \frac{1}{n+1} 2^{-n}$ für $q \in \R$. Hier ist

```{math}
  \left\vert \frac{x_{n+1}}{x_n} \right\vert  = \frac{n+1}{n+2} \frac{1}2 \leq \frac{1}2
```

für alle $n \in \N$, deshalb konvergiert die Reihe.
````

Zum Abschluss zeigen wir noch eine recht naheliegende Eigenschaft

````{prf:lemma}
Sei $\sum_{n=0}^\infty x_n$ eine konvergente reelle Reihe. Dann ist $(|x_n|)$ eine Nullfolge.
````

````{prf:proof}
 Sei $\epsilon >0 $. Da die Partialsummen eine Cauchy-Folge sind, gibt es ein $n_0 \in \N$, sodass für $m>n\geq n_0$ gilt

```{math}
|\sum_{k=n+1}^m x_k| < \epsilon.
```

Nun können wir $m=n+1$ und $n$ beliebig wählen und erhalten $|x_n|<\epsilon$ für alle $n > n_0$. Also ist $(|x_n|)$
eine Nullfolge.

````
