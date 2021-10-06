# Gleichmäßige Stetigkeit und gleichmäßige Konvergenz

Bei der Definition der Stetigkeit haben wir zu jedem $x$ möglicherweise einen anderen Zusammenhang zwischen $\epsilon$ und $\delta$, in gewisser Weise kann eine Funktion recht ungleichmäßig in ihrer Stetigkeit sein. Umgekehrt können wir gleichmäßige Stetigkeit definieren, wenn wir den $\epsilon$-$\delta$ Zusammenhang global machen:

````{prf:definition}
Eine Funktion $f: X\rightarrow Y$ zwischen metrischen Räumen $X$ und $Y$ heisst {\em gleichmäßig stetig}, wenn es zu jedem $\epsilon > 0$ ein $\delta > 0$ gibt, sodass

```{math}
 d_Y(f(x_1),f(x_2)) < \epsilon
```

für alle $x_1,x_2 \in X$ mit $d_X(x_1,x_2) < \delta$ gilt.
````

````{prf:example}
Die Funktion $f:x \mapsto x^2$ ist gleichmäßig stetig auf jedem Intervall $[a,b]$, aber nicht auf ganz $\R$.
````

Die Eigenschaft von $x \mapsto x^2$ ist kein Zufall, es gilt der Satz von Heine-Cantor (hier ohne Beweis):

````{prf:theorem}
Sei $K \subset \R^m$ kompakt, dann ist jede stetige Abbildung $f:K \rightarrow \R^n$ gleichmäßig stetig.
````

Wir können auch Folgen von Funktionen betrachten, sowie deren mögliche Grenzwerte:

````{prf:definition}
Sei $f_n: M \subset X \rightarrow Y$, $n \in N$, eine Folge von Abbildungen zwischen metrischen Räumen $X$ und $Y$. Wir sagen:

* $f_n$ konvergiert punktweise gegen $f: M \rightarrow Y$, wenn für alle $x \in M$ die Folge $(f_n(x))$ gegen $f(x)$ konvergiert.
* $f_n$ konvergiert gleichmäßig gegen $f: M \rightarrow Y$, wenn für alle $\epsilon > 0$ ein $n_0$ existiert, sodass für alle $n \geq n_0$ und $x \in M$ gilt:

```{math}
 d(f(x),f_n(x)) < \epsilon.
```

````

Wir sehen, dass sich beim Übergang von der punktweisen zur gleichmäßigen Konvergenz ein Quantor ändert. Während bei der punktweisen Konvergenz für alle $x$ ein $n_0$ (abhängig von $x$) existiert, muss $n_0$ bei der gleichmäßigen Konvergenz für alle $x$ das gleiche sein. Daraus sehen wir auch sofort, dass gleichmäßige Konvergenz einer Funktionenfolge immer auch punktweise Konvergenz impliziert.
Ein Unterschied der beiden Arten von Konvergenz ist die Eigenschaft des Grenzwerts stetiger Funktionen.

````{prf:example}
Sei $f_n: [0,2] \rightarrow \R$ definiert durch

```{math}
 f_n(x) = \left\{ \begin{matrix} x^n & x < 1 \\ 1 & \text{sonst.} \end{matrix} \right.
```

Dann sehen wir, dass $f_n$ eine Folge stetiger Funktionen ist, die punktweise gege

```{math}
 f (x) = \left\{ \begin{matrix} 0 & x < 1 \\ 1 & \text{sonst,} \end{matrix} \right.
```

konvergiert. Punktweise Konvergenz erhält also nicht die Stetigkeit für den Grenzwert, wir werden aber sehen, dass dies bei gleichmäßiger Konvergenz der Fall ist.
````

````{prf:theorem}
Sei $f_n: M \subset X \rightarrow Y$ eine Folge stetiger Funktionen zwischen metrischen Räumen, die gleichmäßig gegen $f: M \rightarrow Y$ konvergiert. Dann ist $f$ stetig.
````

````{prf:proof}
 Sei $x \in M$. Wegen der gleichmäßigen Konvergenz von $f_n$ gibt es für $\epsilon > 0$ ein $n_0 \in \N$, sodass für alle $n \geq n_0$ gilt:

```{math}
 d(f_n(x),f(x)) < \frac{\epsilon} 3.
```

Dies gilt insbesondere für $n=n_0$. Nun gibt es wegen der Stetigkeit von $f_{n_0}$ zu $\epsilon > 0$ ein $\delta > 0$, sodass

```{math}
 d(f_{n_0}(x),f_{n_0}(y)) < \frac{\epsilon}3,
```

gilt für $d(x,y) < \delta$. Aus der Dreiecksungleichung folgt für solche $y$ aber auch

```{math}
d(f(x),f(y)) &\leq d(f(x),f_{n_0}(y)) + d( f_{n_0}(y),f(y)) \\ &\leq d(f(x),f_{n_0}(x)) + d + d( f_{n_0}(x),f_{n_0}(y)) + f_{n_0}(y),f(y)) \\ &< \frac{\epsilon}3 + \frac{\epsilon}3 + \frac{\epsilon}3 = \epsilon.
```

Also ist $f$ stetig.
````
