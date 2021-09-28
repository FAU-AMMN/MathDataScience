# Der Hauptsatz der Differential- und Integralrechnung

Nun wollen wir uns noch mit dem Zusammenhang zwischen Differential- und Integralrechnung beschäftigen. Wir betrachten dazu lokal integrierbare Funktionen $f:[a,b] \rightarrow \R$, d.h. Funktionen, die auf jedem Teilintervall von $[a,b]$ integrierbar sind.

Wir nennen $F:[a,b] \rightarrow \R$ unbestimmtes Integral von $f$, wenn für $y,z \in [a,b]$ gilt

```{math}
 F(z) - F(y) = \int_y^z f(x)~dx.
```

(Wir beachten, dass wir zur Konsistenz ein Integral mit vertauschten Integralgrenzen mit negativem Vorzeichen definieren, d.h.
$\int_z^y f(x)~dx = - \int_y^z f(x)~dx. $)

Wir nennen $F:[a,b] \rightarrow \R$ Stammfunktion von $f$, wenn $F'(x)=f(x)$ für alle $x \in [a,b]$ gilt. Der Inhalt des Hauptsatzes der Integralrechnung ist es zu zeigen, dass die Konzepte Stammfunktion und unbestimmtes Integral auf das Gleiche führen, d.h. die Integration ist damit die Umkehrung der Differentiation.
Zunächst wollen wir einige Resultate über Stammfunktionen herleiten:

````{prf:lemma}
Sei $F$ eine Stammfunktion von $f$, dann ist $G$ genau dann Stammfunktion, wenn $F-G$ konstant ist.
````

````{prf:proof}
Ist $G$ eine Stammfunktion, dann gilt $(F-G)'=F'-G'= f-f=0$ überall in $[a,b]$. Wenden wir den Mittelwertsatz der Differentialrechnung an, so folgt für alle $y,z$ und ein $x \in (y,z)$

```{math}
 \frac{(F-G)(z) - (F-G)(y)}{z-y} = (F-G)'(x) = 0.
```

Also ist $(F-G)(z) = (F-G)(y)$ für alle $y,z \in  [a,b]$, d.h. $F-G$ ist konstant.
Ist umgekehrt $F-G$ konstant, dann folgt sofort $G' = F' + (G-F)' = F'=f$, also ist $G$ Stammfunktion. $\square$
````

````{prf:lemma}
Sei $f:[a,b]\rightarrow \R$ beschränkt und $F$ Stammfunktion oder unbestimmtes Integral. Dann ist $F$ Lipschitz-stetig mit Konstante $L=\sup_{x \in [a,b]} \vert f(x) \vert. $
````

````{prf:proof}
Wir haben aus den Abschätzungen für Unter- und Obersummen schon gesehen, das

```{math}
 \vert \int_y^z f(x)~dx \vert \leq \vert z -y \vert ~\sup_{x \in [a,b]} \vert f(x) \vert
```

gilt, also folgt die Aussage für ein unbestimmtes Integral. Ist $F$ Stammfunktion, so impliziert der Mittelwertsatz

```{math}
 \vert F(y) - F(z) \vert = \vert y - z \vert ~\vert f(x) \vert,
```

für ein $x \in (y,z)$ und die letzte Term ist kleiner als das Supremum. $\square$.
````

Ein wichtiges Resultat, ähnlich bei der Differentiation, ist der Mittelwertsatz der Integralrechnung:

````{prf:theorem}
Sei $f$ stetig auf $[a,b]$ und $y,z \in [a,b]$, $y < z$. Dann gibt es ein $x_0 \in (y,z)$ mit

```{math}
 f(x_0) = \frac{\int_y^z f(x)~dx}{z-y}.
```

````

````{prf:proof}
$f$ ist eine stetige Funktion auf dem kompakten Intervall $[y,z]$, nimmt dort also sein Maximum und Minimum an. Damit gibt es

```{math}
 f(x_-) = \min_{x \in [y,z]} f(x) \leq \frac{\int_y^z f(x)~dx}{z-y} \leq  \max_{x \in [y,z]} f(x) = f(x_+).
```

Nach dem Zwischenwertsatz für stetige Funktionen gibt es also ein $x_0$ zwischen $x_+$ und $x_-$ mit

```{math}
 f(x_0) = \frac{\int_y^z f(x)~dx}{z-y}. \square
```
````

Nun können wir den wichtigsten Satz zum Zusammenhang zwischen Differentiation und Integration beweisen, den Hauptsatz der Differential- und Integralrechnung:

````{prf:theorem}
Sei $f:[a,b] \rightarrow \R$ stetig. Dann ist$F_a: [a,b] \rightarrow \R, x \mapsto \int_a^x f(y)~dy$
eine Stammfunktion. Eine Funktion $F:[a,b] \rightarrow \R$ ist genau dann Stammfunktion von $f$, wenn $F$ ein unbestimmtes Integral ist.
````

````{prf:proof}
Es gilt nach dem Mittelwertsatz

```{math}
 \frac{F_a(x)-F_a(x_0)}{x-x_0} = \frac{\int_{x_0}^x f(y)~dy }{x-x_0} = f(\xi(x))
```

für ein $\xi(x)$ zwischen $x$ und $x_0$. Damit folgt für den Grenzwert

```{math}
 F_a'(x_0) = \lim_{x\rightarrow x_0}\frac{F_a(x)-F_a(x_0)}{x-x_0} =  \lim_{x\rightarrow x_0}f(\xi(x)) = f(x_0),
```

da $f$ stetig ist und $\xi(x) \rightarrow x_0$ für $x \rightarrow x_0$. Also ist $F_a$ Stammfunktion.
Analog zeigt man für jedes unbestimmte Integral $F$, dass $F'=f$ gilt.
Sei umgekehrt $F$ Stammfunktion, dann wissen wir, dass $F-F_a$ konstant ist und damit

```{math}
 F(z) - F(y) = F_a(z) - F_a(y) = \int_y^z f(y)~dy,
```

also ist $F$ auch unbestimmtes Integral. $\square$
````

Wir sehen also, dass die Begriffe des unbestimmten Integrals und der Stammfunktionen übereinstimmen. Deshalb sprechen wir im Folgenden nur noch von Stammfunktionen. Bei Funktionen $f$, von denen wir bereits wissen, dass sie die Ableitung einer Funktion $F$ sind, können wir also den Hauptsatz der Differential- und Integralrechnung benutzen, um bestimmte Integrale zu berechnen, es gilt ja

```{math}
 \int_a^b f(x)~dx = F(b) - F(a) =: F\vert_a^b.
```

````{prf:example}
Wir wissen das die Exponentialfunktion die Ableitung der Exponentialfunktion ist, also gilt

```{math}
 \int_a^b e^x ~dx = e^x\vert_a^b = e^b -e^a.
```

Allgemeiner ist $e^{cx}$ die Ableitung von $\frac{1}c e^{cx}$, als

```{math}
 \int_a^b e^{cx} ~dx =\frac{1}c (e^{cx})\vert_a^b = \frac{1}c (e^{cb} -e^{ca}).
```

````

Das letzte Beispiel können wir folgendermaßen verallgemeinern: Ist $f$ die Ableitung von $F$, dann ist$x \mapsto f(c x)$ die Ableitung von $x\mapsto \frac{1}c F(cx)$, als

```{math}
 \int_a^b f(cx)~dx = \frac{1}c (F(cb) - F(ca)).
```

````{prf:example}
Sei $f(x) = x^m$, dann ist $F(x) = \frac{x^{m+1}}{m+1}$ Stammfunktion.

```{math}
 \int_a^b x^m ~dx =\frac{1}{m+1}  (b^{m+1} -a^{m+1}).
```

Im Fall $m=0$ erhalten wir als Integral $b-a$, also genau die Rechtecksfläche,im Fall $m=1$ ist das Integral $\frac{1}2 (b^2-a^2) = \frac{1}2 (b-a)(b+a)$ die Dreiecksfläche.
````

Mit Hilfe von Differentiationsregeln können wir auch weitere Integrationsregeln erhalten. Die wahrscheinlich
wichtigste ist dabei die {\em partielle Integration}, die wir aus der Produktregel erhalten:

````{prf:theorem}
Seien $f:[a,b] \rightarrow \R$, $g:[a,b] \rightarrow \R$ stetig differenzierbar. Dann gilt

```{math}
 \int_a^b f(x) g'(x) ~dx = - \int_a^b f'(x) g(x)~dx + (fg)\vert_a^b.
```

````

````{prf:proof}
Aus der Produktregel und dem Hauptsatz der Differential- und Integralrechnung folgt

```{math}
 (fg)\vert_a^b = \int_a^b (fg)'(x)~dx = \int_a^b (f'(x)g(x) + f(x)g'(x))~dx.
```

````
