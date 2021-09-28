# Vertauschung von Integralen und Taylor-Formel

Oft integriert man eine Funktion mehrmals, d.h. man hat eigentlich ein weiteres Integral der Stammfunktion. Wir wollen hier eine Formel für die zweifache Integration herleiten. Sei $F$ Stammfunktion von $f$, dann gilt

```{math}
 \int_a^b (F(x) - F(a))~dx = \int_a^b \int_a^x f(y)~dy~dx.
```

Intuitiv integrieren wir hier über das Dreieck $0 \leq y \leq x \leq b$, also erwarten wir

```{math}
 \int_a^b \int_a^x f(y)~dy = \int_a^b \int_y^b f(y)~dy = \int_a^b f(y) (b-y)~dy.
```

 Um die Gleichheit nachzuweisen, können wir partielle Integration verwenden, mit der Stammfunktion $F_a$ wie oben und $g(x) = b-x$ erhalten wir, da $g'(x)=-1$, $F_a(a) = 0 $ und $g(b) =0$,

```{math}
 \int_a^b f(y) (b-y)~dy = - \int_a^b F_a(y) (-1)~dy = \int_a^b F_a(x)~dx =  \int_a^b \int_a^x f(x)~dx .
```

Eine Anwendung ist die bessere Charakterisierung von Restgliedern bei der Differentialrechnung. Sei $f$ eine in $[a,b]$ stetig differenzierbare Funktion, dann gilt für $x,x_0 \in [a,b]$

\begin{align*}
f(x) - f(x_0) &= \int_{x_0}^x f'(y)~dy =  \int_{x_0}^x (f'(x_0) + f'(y) -f'(x_0))~dy \\
&= f'(x_0) (x-x_0) + \int_{x_0}^x ( f'(y) -f'(x_0))~dy \\&= f'(x_0) (x-x_0) + \int_{x_0}^x \frac{y-x_0}{x-x_0} \frac{ f'(y) -f'(x_0))}{y-x_0}~dy  (x-x_0) .
\end{align*}

Also ist das Restglied

```{math}
R(x) = \int_{x_0}^x \frac{y-x_0}{x-x_0} \frac{ f'(y) -f'(x_0))}{y-x_0}~dy .
```

Ist $f$ zweimal stetig differenzierbar, dann können wir den Mittelwertsatz auf $f'$ anwenden und erhalten

```{math}
 R(x) = \int_{x_0}^x \frac{y-x_0}{x-x_0} f''(\xi(y))~dy,
```

damit auch

```{math}
 |R(x)| \leq  \int_{x_0}^x \frac{y-x_0}{x-x_0} \sup_{z \in (x_0,x)} |f''(z)|~dy = \sup_{z \in (x_0,x)} |f''(z)| ~ \frac{|x-x_0|}2.
```
