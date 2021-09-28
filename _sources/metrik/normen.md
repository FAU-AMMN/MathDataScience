# Metriken und Normen

````{prf:definition}
Eine Menge $X$ mit einer Abbildung $d: X \times X \rightarrow \R$, welche die folgenden Eigenschaften erfüllt, heisst _metrischer Raum_:

* $d(x,y) \geq 0$ für alle $x,y \in X$ und $d(x,y) = 0$ genau dann wenn $x=y$ (Positivität).

* $d(x,y) = d(y,x)$ für alle $x,y \in X$  (Symmetrie).

* $d(x,z) \leq d(x,y) + d(y,z)$ für alle $x,y,z \in X$  (Dreiecksungleichung).
Die Abbildung $d$ heisst dann Metrik auf $X$.
````

Eine Metrik ist ein abstrakter Abstandsbegriff auf Mengen, wir beachten, dass $X$ keinerlei Vektorraumstruktur haben muss.  Liegt eine solche vor, dann kann man einfache Metriken passend zu Linearkombinationen definieren, wie wir auch aus bekannten Beispielen sehen.In $\R$ ist $d(x,y) = |x-y|$ eine Metrik, im $\R^n$ ist $d(x,y) = \Vert x -y \Vert $ eine Metrik, wobei $\Vert \cdot \Vert$ die Euklidische Norm ist. Allgemein definieren wir Normen folgendermaßen:

````{prf:definition}
Eine Abbildung $\Vert \cdot \Vert:X\rightarrow \R$ auf einem Vektorraum $X$ heisst _Norm_, wenn die folgenden Eigenschaften erfüllt sind:

* $\Vert x \Vert \geq 0$ für alle $x \in X$ und $\Vert x \Vert = 0$ genau dann wenn $x=y$ (Positivität).

* $\Vert \alpha x \Vert = |\alpha|~\Vert x \Vert$ für alle $\alpha \in \R$. $x\in X$  (Absolute Homogenität).

* $\Vert x+y \Vert \leq\Vert x  \Vert + \Vert y  \Vert$ für alle $x,y  \in X$  (Dreiecksungleichung).
$(X,\Vert \cdot \Vert)$  nennen wir dann einen normierten Raum oder normierten Vektorraum.
````

Aus Normen erhalten wir immer spezielle Metriken, wie der folgende Satz zeigt:

````{prf:theorem}
Ist $(X,\Vert \cdot \Vert)$ ein normierter Raum, dann ist $d$ definiert durch

```{math}
 d(x,y) = \Vert x - y \Vert ,\qquad \forall x,y \in X
```

eine Metrik auf $X$.
````

````{prf:proof}

Wir sehen sofort, dass $d(x,y) \geq 0$ wegen der Positivität der Norm gilt und $d(x,y) = \Vert x - y\Vert = 0$ gilt nur für $x-y = 0$, also $x=y$. Die Symmetrie folgt aus der absoluten Homogenität mit der Wahl $\alpha = 1$, dann ist

```{math}
 d(y,x) = \Vert y- x \Vert = \Vert (-1)(x-y) \Vert = |-1|~\Vert x -y \Vert = \Vert x-y \Vert = d(x,y).
```

Die Dreiecksungleichung ist  gleichbedeutend zur Dreiecksungleichung einer Metrik wenn wir als Vektorraumelemente ($x$ und $y$) $x-y$ und $y-z$ einsetzen.
````

````{prf:example}
Wir prüfen kurz nach, dass die Euklidische Norm

```{math}
 \Vert x \Vert = \sqrt{\sum_{i=1}^N x_i^2}
```

 im $\R^N$ tatsächlich eine Norm gemäß der obigen Definition ist.Es gilt per Definition $\Vert x \Vert \geq 0$ und $\Vert x \Vert = 0$ impliziert $\sum_{i=1}^N x_i^2=0$. Dies ist nur möglich für $x_1=x_2=\ldots=x_N=0$, also $x=0$. Die absolute Homogenität erhalten wir aus
```{math}
 \Vert \alpha x \Vert = \sqrt{\sum_{i=1}^N \alpha ^2 x_i^2} = \sqrt{\alpha^2 (\sum_{i=1}^N \alpha ^2 x_i^2)} = |\alpha|~ \sqrt{\sum_{i=1}^N x_i^2}. 
```

Die Dreiecksungleichung können wir äquivalent quadrieren, da sie aus lauter positiven Termen besteht. Also ist sie äquivalent zu

```{math}
  {\sum_{i=1}^N (x_i+y_i)^2} \leq \sum_{i=1}^N x_i^2 + \sum_{i=1}^N y_i^2 + 2 \sqrt{\sum_{i=1}^N x_i^2} \sqrt{\sum_{i=1}^N y_i^2}.
```

Quadrieren wir die Summe auf der linken Seite aus und kürzen die entsprechenden Terme mit $x_i^2$ und $y_i^2$, so bleibt

```{math}
 2 \sum_{i=1}^N x_i y_i \leq 2 \sqrt{\sum_{i=1}^N x_i^2} \sqrt{\sum_{i=1}^N y_i^2},
```

was aus der Cauchy-Schwarz Ungleichung folgt.
````

Weitere Beispiele für Normen sind (siehe auch die Übung)

* Die $p$-Norm

```{math}
 \Vert x \Vert_p = \left( \sum_{i=1}^N |x_i|^p \right)^{1/p}
```

ist für $1 \leq p < \infty$ eine Norm auf $\R^N$ (eine Verallgemeinerung der Euklidischen Norm).

* Die Maximumsnorm

```{math}
 \Vert x \Vert_\infty = \max_{i=1,\ldots,N} |x_i|
```

ist eine Norm auf $\R^N$.

* Die Supremumsnorm

```{math}
 \Vert x \Vert_\infty = \sup_{i \in \N} |x_i|
```

ist eine Norm auf $\ell^\infty(\N)$.Aus dem letzten Beispiel sehen wir auch, dass wir Normen verwenden können um Teilräume zu definieren. $\ell^\infty(\N)$ ist ja genau jener Teilraum von $\R^\N$ auf dem die Supremumsnorm endliche Werte anwendet. Haben wir also eine Abbildung von $X  $ nach $\R \cup \{+ \infty\}$, sodass die Eigenschaften der Positivität, absoluten Homogenität und Dreiecksungleichung erfüllt sind, so ist die Teilmenge $\tilde X$ auf der die Abbildung endlich ist, ein normierter Raum. Die Teilraumeigenschaft überprüfen wir direkt mit der absoluten Homogenität und Dreiecksungleichung.
Nicht alle Metriken entstehen aus Normen, ein wichtiges Beispiel einer Metrik, die nicht aus einem normierten Vektorraum entsteht ist die geodätische Distanz auf der Erdoberfläche. Um dies mathematische zu vereinfachen, betrachten wir $X$ als den Einheitskreis im $R^2$ und als Metrik $d(x,y)$ die Länge des kürzeren Kreisbogens zwischen $x$ und $y$. Dieser entspricht genau dem (spitzen) Winkel $\varphi \in [0,\pi]$ zwischen $x$ und $y$. Offensichtlich ist $d(x,y)$ dann nichtnegativ und $d(x,y)=0$ gilt nur, wenn der Winkel gleich Null ist, d.h. $x =y$. Auch die Symmetrie ist offensichtlich, und die Dreiecksungleichung folgt, da der Winkel zwischen $x$ und $z$ entweder der Summe aus den Winkeln zwischen $x$, $y$ sowie $y$, $z$ ist, oder kleiner als einer der beiden Winkel.
