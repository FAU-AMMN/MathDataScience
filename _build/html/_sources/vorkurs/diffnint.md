# Differentiation und Integration

Wir kommen nun zu einem der wesentlichsten Themen der Analysis, der Differential- und Integralrechnung. Grundlage der Differentialrechnung ist eine lokal lineare Approximation der Funktion $f$ nahe eines Punkts $x_0$. Dazu stellen wir die Geradengleichung durch den Punkt $(x_0,f(x_0))$ auf als

```{math}
 g(x) = f(x_0) + k_0 (x-x_0) 
```

und fragen uns wie wir die Steigung $k_0$ am sinnvollsten wählen. Da $g(x) \approx f(x)$ gelten sollte, möchten wir

```{math}
 k_0 \approx \frac{f(x) - f(x_0)}{x-x_0} 
```

Der richtige Wert ist also der Grenzwert $x$ gegen $x_0$.  Dementsprechend definieren wir diesen Grenzwert als Ableitung

```{math}
 f'(x_0) = \lim_{x \rightarrow x_0} \frac{f(x) - f(x_0)}{x-x_0}. 
```

Wir sagen, dass der Grenzwert $\lim_{x \rightarrow x_0}$ existiert, wenn der Grenzwert für alle Folgen $x_n \rightarrow x_0$ existiert und den gleichen Wert annimmt. In diesem Fall nennen wir die Funktion differenzierbar in $x_0$. Ist $f$ differenzierbar für jedes $x_0 \in I$, so nennen wir $f$ differenzierbar in $I$.

````{prf:example}
Sei $f(x) = a_1 x + a_0$, dann ist $f$ differenzierbar in $\R$ mit $f'(x) = a_1$. 
````

````{prf:example}
Sei $f(x) = x^2$, dann ist $f$ differenzierbar in $\R$ mit $f'(x) = 2x$. 
````

Eine differenzierbare Funktion ist immer stetig, wenn $f$ in einem Intervall differenzierbar und die Ableitung betragsmäßig beschränkt ist, dann ist $f$ sogar Lipschitz-stetig. Dies werden wir später noch mit Hilfe der Integralrechnung sehen.

Die zentralen Regeln bei der Differentiation sind die Produkt- und Kettenregel. Sind $f, g:I \rightarrow \R$ zwei Funktionen, die in $x_0$ differenzierbar sind, dann ist auch $h = f g$ in $x_0$ differenzierbar und es gilt die Produktregel:

```{math}
h'(x_0) = f'(x_0) g(x_0) + f(x_0) g'(x_0) 
```

Die sehen wir durch eine Betrachtung des Genzwerts
\begin{align*}
\lim_{x \rightarrow x_0} \frac{h(x) - h(x_0)}{x-x_0} &= \lim_{x \rightarrow x_0} \frac{f(x)g(x) - f(x_0)g(x_0) }{x-x_0} \\
&= \lim_{x \rightarrow x_0} \frac{f(x)g(x) - f(x_0) g(x) +f(x_0) g(x) - f(x_0)g(x_0) }{x-x_0} \\
&= \lim_{x \rightarrow x_0} \frac{f(x)  - f(x_0)   }{x-x_0} g(x)+
\lim_{x \rightarrow x_0} f(x_0) \frac{  g(x) -  g(x_0) }{x-x_0}
\end{align*}
Dabei haben wir benutzt, dass Grenzwerte von Summen und Produkten gleich Summen und Produkten von Grenzwerten sind.

````{prf:example}
Sei $h(x) = x^2 e^x. $ Dann ist $h'(x) = 2x e^x + x^2 e^x$.
````

Die Kettenregel gilt für die Hintereinanderausführung differenzierbarer Funktionen. Ist $f$ bei $x_0$ differenzierbar und $g$ bei $y_0=f(x_0)$, dann ist $h = g \circ f, $ d.h. $h(x) = g(f(x))$, bei $x_0$ differenzierbar und es gilt

```{math}
 h'(x_0) = g'(f(x_0)) f'(x_0). 
```

Aus der Ketten- und Produktregel, lassen sich auch weitere Differentiationsregeln herleiten, etwa die Quotientenregel für $h= \frac{f}g$. Dazu wenden wir die Produktregel auf $f \tilde g$ mit $\tilde g = \frac{1}g$ an und die Kettenregel auf die Hintereinanderausführung von $y \mapsto \frac{1}y$ und $g$.

Die Integration wird üblicherweise als Umkehrung der Differentiation eingeführt. Das unbestimmte Integral, d.h. die Stammfunktion $F$ einer Funktion $f$ ist definiert durch die Eigenschaft $F'=f$. Wir beachten, dass die Stammfunktion nur bis auf eine additive Konstante definiert ist. Für $a < b \in I$ gilt

```{math}
:label: eq:hauptsatzintegral \int_a^b f(x) ~dx = \int_a^b F'(x) ~dx = F(b) - F(a). 
\end {equation} 
Dies wird auch als Hauptsatz der Differential- und Integralrechnung bezeichnet. Wir beachten, dass beim bestimmten Integral von $a$ nach $b$ laut {eq}`eq:hauptsatzintegral` die additive Konstante in der Differenz rausfällt, deshalb ist das bestimmte Integral auch eindeutig bestimmt. 

Das Integral ist das kontinuierliche Analogon zur Summation, was aus der Definition über sogenannte Riemann-Summen klar wird. Wir erhalten das Integral einer stetigen Funktion als Grenzwert

```{math}
 \int_a^b f(x)~dx = \lim_{|\Delta_n| \rightarrow 0} \sum_{j=1}^n (x_j - x_{j-1}) f(\xi_j) 
```

wobei $\Delta_n = \{x_j,\xi_j\}$, sodass

```{math}
 a = x_0 < x_1 < \ldots < x_n =b, \qquad \xi_j \in [x_{j-1},x_j]
```

und

```{math}
 \vert \Delta_n \vert = \max_j (x_j - x_{j-1}). 
```

Daraus sehen wir auch die Linearität des Integrals:

```{math}
 \int_a^b  c f(x) ~dx = c \int_a^b   f(x) ~dx, 
```

und

```{math}
 \int_a^b   ( f(x) + g(x)) ~dx = \int_a^b   f(x) ~dx + \int_a^b   g(x) ~dx. 
```

Darüber hinaus pflanzt sich auch die Monotonie und Dreiecksungleichung fort, es gilt

```{math}
 \int_a^b   f(x) ~dx \leq  \int_a^b   g(x) ~dx  
```

falls $f(x) \leq g(x)$ für alle $x \in (a,b)$ gilt, sowie

```{math}
 \left\vert \int_a^b   f(x) ~dx \right\vert \leq  \int_a^b  \vert  f(x) \vert ~dx . 
```

Aus dem Hauptsatz der Differential- und Integralrechnung sowie dieser Ungleichung folgt

```{math}
\vert F(x_2) - F(x_1) \vert = \left\vert \int_{x_1}^{x_2}   F'(x) ~dx \right\vert
\leq  \int_{x_1}^{x_2}  \vert F'(x) \vert ~dx.
```

Ist $F'$ beschränkt, d.h. $\vert F'(x) \vert \leq L$ für alle $x$, dann folgt

```{math}
 \vert F(x_2) - F(x_1) \vert \leq  \int_{x_1}^{x_2}  \vert F'(x) \vert ~dx
\leq  \int_{x_1}^{x_2}  L ~dx = L \vert x_2 - x_1 \vert.
```

Die Differentiationsregeln münden auch direkt Eigenschaften der Integration. Besonders interessant ist die partielle Integration

```{math}
  \int_a^b f'(x) g(x)~dx = f(b) g(b) - f(a) g(a) - \int_a^b f(x) g'(x)~dx, 
```

die direkt aus der Produktregel und dem Hauptsatz der Differential- und Integralrechnung folgt.
