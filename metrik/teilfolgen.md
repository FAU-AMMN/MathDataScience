# Teilfolgen

Nicht immer konvergiert die ganze Folge, wie wir schon in $\R$ am Beispiel $x_n = (-1)^n$ sehen. Hier konvergieren offensichtlich die sogenannten Teilfolgen $x_{2n}$ (gegen $+1$) und $x_{2n+1}$ (gegen $-1$), nicht aber die ganze Folge.

````{prf:definition}
Sei $K: \N \rightarrow \N$ eine streng monoton wachsende Abbildung ($K(i) > K(j)$ für $i > j$). Dann heisst $(x_{K(n)})_{n \in \N}$ Teilfolge von $(x_n). $
````

Wir werden im Folgenden für Teilfolgen auch kurz $(x_{k_n})_{n \in \N}$ schreiben.
Wir können das Problem der Konvergenz von Teilfolgen nun näher untersuchen, dazu führen wir zunächst das Konzept eines Häufungspunktes ein:

````{prf:definition}
Sei $(X,d)$ ein metrischer Raum. Dann heisst $y \in X$ Häufungspunkt der Folge $(x_n) \subset X$, wenn
```{math}
 \forall \epsilon > 0, m \in \N ~\exists n > m: d(x_n,y) < \epsilon.
```

````

````{prf:example}
Die reelle Folge $x_n = (-1)^n$ besitzt die Häufungspunkte $+1$ und $-1$. Gleiches gilt für $x_n = (-1)^n + \frac{1}{n+1}$.
````

````{prf:theorem}
Sei $(X,d)$ ein metrischer Raum und $(x_n)$ eine Folge in $X$. Dann gilt:

*$i)$ Ist $x_n$ konvergent gegen $\overline{x} \in X$, dann ist $\overline{x}$ der einzige Häufungspunkt von $(x_n)$.
*$ii)$ Ist $y$ Häufungspunkt von $(x_n)$, dann existiert eine konvergente Teilfolge $(x_{n_k})$ mit Grenzwert $y$ und umgekehrt.
````

````{prf:proof}
 (i) Aus der Definition ist klar, dass $\overline{x}$ Häufungspunkt ist: Sei $x_n$ konvergent und $\epsilon > 0$. Dann ist für ein $n_0 \in \N$ und $n \geq n_0$ auch $d(x_n, \overline{x}) < \epsilon$. Falls $m < n_0$ gilt, können wir $n=n_0$ wählen, sonst einfach $n=m+1$. Nehmen wir an $y \neq \overline{x}$ ist Häufungspunkt und sei $\epsilon < \frac{d(\overline{x},y)}2$. Dann gilt für alle $n \geq 0$ wegen der Dreiecksungleichung

```{math}
 d(x_n,y) \geq d(y,\overline{x}) - d(x_n,\overline{x}) > 2 \epsilon - \epsilon = \epsilon,
```

ein Widerspruch zur Häufungspunkteigenschaft.
(ii)Ist $y$ Häufungspunkt, dann wählen wir hintereinander $\epsilon_k = \frac{1}k$, $k \in \N \setminus \{0\}$. Zunächst wählen wir für $\epsilon_1$ $m=1$, damit existiert ein $n_1$, sodass $d(x_{n_1},y) < 1$. Nun wählen wir induktive für $\epsilon_{k+1}$  $m=n_k$. Dann existiert ein $n_{k+1} > n_k$ mit

```{math}
 d(x_{n_{k+1}},y) < \frac{1}{k+1}.
```

Wir sehen sofort, dass $x_{n_k}$ gegen $y$ konvergiert.
Ist umgekehrt $y$ Grenzwert einer konvergenten Teilfolge, dann gibt es für jedes $\epsilon >0 $ und $m \in \N$ ein $k_0 $ mit

```{math}
 d(x_{n_k},y) < \epsilon, \qquad \forall n_k \geq n_{k_0},
```

also ist $y$ Häufungspunkt.

````

In normierten Räumen können wir wieder Summen von Folgen betrachten. Es gilt jedoch nicht immer, dass die Häufungspunkte von $x_n+y_n$ die Summe der Häufungspunkte beider Folgen sind. Als Beispiel dafür können wir $x_n=0$ für $n$ ungerade und $x_n=n$ für $n$ gerade, sowie $y_n=n$ für $n$ ungerade und $y_n=0$ für $n$ gerade betrachten. Beide Folgen haben den Häufungspunkt $0$, aber es gilt $x_n+y_n = n$ für alle $n \in \N$, damit hat diese Folge keinen Häufungspunkt. Es gilt aber folgendes Resultat:

````{prf:lemma}
Sei $x_n$ eine Folge mit Häufungspunkt $z$ und $y_n$ eine konvergente Folge mit Grenzwert $y$. Dann ist $z+y$ ein Häufungswert von $x_n + y_n$.
````

````{prf:proof}
 Ist $z$ Häufungspunkt von $(x_n)$ und $(y_n)$ konvergent, dann gibt es eine Teilfolge $(x_{n_k})$ mit Grenzwert $z$, die Teilfolge $(y_{n_k})$ ist aber immer noch konvergent gegen $y$. Also ist $(x_{n_k}+y_{n_k})$ eine konvergente Teilfolge von $(x_n+y_n)$ mit Grenzwert $z+y$.
````

Ein besonders wichtiges Resultat über konvergente Teilfolgen ist der Satz von Bolzano-Weierstrass:

````{prf:theorem}
Sei $(x_n) \subset \R^N$ eine beschränkte Folge, d.h. es gibt $C \in \R$ mit

```{math}
 \Vert x_n \Vert \leq C
```

für alle $n \in \N$. Dann existiert eine konvergente Teilfolge $(x_{n_k})$ mit Grenzwert $\overline{x}$ und es gilt $\Vert \overline{x} \Vert \leq C$.
````

````{prf:proof}
 Wir beweisen zunächst den Fall $N=1$ durch sogenannte Bisektion. Wir beginnen mit $a_0=-C$ und $b_0=C$, dann ist $x_n \in [a_0,b_0]$ für alle $n \in \N$. Wir setzen $n_0 =0$ und berechnen $c_0=\frac{a_0+b_0}2$. Eines der beiden Intervalle $[a_0,c_0]$ und $[c_0,b_0]$ muss nun unendlich viele Folgenglieder von $x_n$ enthalten. Enthält $[a_0,c_0]$ unendlich viele, so setzen wir $a_1=a_0$, $b_1=c_0$, andernfalls $a_1=c_0$, $b_1=b_0$. Wir wählen nun

```{math}
 n_1 = \min\{n > n_0~|~x_n \in [a_1,b_1] \}.
```


Nun gehen wir induktiv weiter.
Wir nehmen an die ersten Glieder $x_{n_0},\ldots,x_{n_k}$ der Teilfolge sind gegeben, ebenso Intervalle $[a_j,b_j]$, $j=0,\ldots,k$,  mit $x_{n_j} \in [a_j,b_j]$ und unendlich vielen Folgengliedern in $ [a_j,b_j]$.Nun berechnen wir $c_{k+1}= \frac{a_k + b_k}2$ und machen die gleiche Fallunterscheidung wie im Fall $k=0$ um$[a_{k+1},b_{k+1}]$ zu berechnen. Dazu definieren wir

```{math}
 n_{k+1} = \min\{n > n_k~|~x_n \in [a_{k+1},b_{k+1}] \}.
```

Damit erhalten wir eine unendliche Folge kleiner werdender Intervalle $[a_k,b_k]$, es gilt $|b_k - a_k|=2^{1-k}C$.Darüber hinaus haben wir eine Teilfolge $x_{n_k}$ konstruiert, mit $x_{n_j} \in [a_k,b_k]$ für $j \geq k$. Damit gilt auch

```{math}
 \vert x_{n_i} - x_{n_j} \vert \leq 2^{1-k} C
```

für $n_i, n_j \geq n_k. $ Daraus sehen wir sofort, dass $(x_{n_j})$ eine Cauchy-Folge und damit konvergent ist.

Im $\R^N$ folgt aus der Beschränktheit von $(x_n)$ auch die Beschränktheit jeder Koordinatenfolge, wegen

```{math}
 \vert x_n^{(i)} \vert \leq \Vert x_n \Vert .
```

Nun können wir eine konvergente Teilfolge von $x_n^{1}$ wählen. Da alle Koordinatenteilfolgen $x_{n_k}^{(i)}$ immer noch beschränkt sind, wählen wir davon eine weitere Teilfolge, sodass $x_{n_k}^{(2)}$ konvergiert, natürlich konvergiert dann ja auch $x_{n_k}^{(1)}$ noch. Durch schrittweises Auswählen weiterer Teilfolgen von Teilfolgen enden wir schliessliche bei einer Teilfolge, für die alle Koordinaten konvergieren und damit auch $(x_{n_k})$ selbst.
````

Wir haben den Satz von Bolzano-Weierstrass in der Euklidischen Metrik formuliert, der Beweis zeigt aber, dass die Aussage auch für anderen Normen, etwa die Maximumsnorm, gilt, da ja nur die Konvergenz aller Koordinatenfolgen wichtig ist. Der Grund dafür ist die sogenannte Äquivalenz von Normen bzw. Metriken:

````{prf:definition}
Zwei Metriken $d_A$ und $d_B$ auf $X$ heissen äquivalent, falls Konstanten $\beta \geq \alpha > 0$ existieren, sodass
```{math}
\forall x,y \in X: \quad \alpha  d_B(x,y) \leq d_A(x,y) \leq \beta d_B(x,y) .
```

Zwei Normen $\Vert \cdot \Vert_A$ und $\Vert \cdot \Vert_B$ auf einem Vektorraum $X$ heissen äquivalent, falls Konstanten $\beta \geq \alpha > 0$ existieren, sodass
```{math}
\forall x  \in X: \quad \alpha  \Vert x \Vert_B  \leq \Vert x \Vert_A  \leq \Vert x \Vert_B  .
```

````

Wir sehen sofort, dass für zwei äquivalente Normen auch die zugeordneten Metriken

```{math}
 d_{A/B}(x,y) = \Vert x -y \Vert_{A/B}
```

äquivalent sind.
Darüber hinaus sehen wir, dass die Konvergenz einer Folge in einer Metrik $d_A$ auch die Konvergenz in einer äquivalenten Metrik $d_B$ impliziert. Dazu können wir etwa {prf:ref}`nullfolgenmetrik` verwenden.
