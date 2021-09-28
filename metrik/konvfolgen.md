# Konvergente Folgen

Mit Hilfe einer Metrik können wir Konvergenz von Folgen und ähnliche Begriffe definieren. Zunächst beginnen wir mit Umgebungen:

````{prf:definition}
Sei $X$ ein metrischer Raum und $\epsilon \in \R_+$. Dann heisst
```{math}
 U_\epsilon(x) = \{ y \in X~|~d(x,y) < \epsilon \}
```

$\epsilon$-Umgebung von $x$
````

````{prf:definition}
Sei $X$ ein metrischer Raum und $M \subset X$. $M$ heisst offen, wenn für alle $x \in M$ eine $\epsilon$-Umgebung $U_\epsilon(x) \subset M$ existiert (wobei $\epsilon$ von $x$ abhängen kann). $M$ heisst abgeschlossen, wenn $X \setminus M$ offen ist.
````

Wir beachten, dass die leere Menge immer offen ist, damit ist $X =X \setminus \emptyset$ abgeschlossen. Andererseits ist $X$ natürlich auch offen, da ja alle $\epsilon$-Umgebungen per Definition Teilmengen von $X$ sind. Damit ist auch wieder $\emptyset =  X \setminus X$ abgeschlossen. Die leere Menge und $X$ sind aber die einzigen Mengen, die in $X$ abgeschlossen und offen sind.

````{prf:example}
Sei $X=\R$ und $a < b \in \R$, dann ist das Intervall $[a,b]$ abgeschlossen und das Intervall $(a,b)$ offen. Die Intervalle $[a,b)$ bzw. $(a,b]$ sind weder abgeschlossen noch offen.
````

````{prf:example}
Sei $X=\R^2$ mit der Euklidischen Norm, dann sind $\epsilon$-Umgebungen genau Kreisscheiben um $x$ mit Radius $\epsilon$, wobei der Kreis mit Radius $\epsilon$ ausgenommen ist.
````

```{margin} Augustin Cauchy
[Augustin-Louis Cauchy](https://de.wikipedia.org/wiki/Augustin-Louis_Cauchy) (* 21. August 1789 in Paris; † 23. Mai 1857 in Sceaux) war ein französischer Mathematiker.
```

Konvergente und Cauchy-Folgen in metrischen Räumen können wir exakt wie in $\R$ definieren, in dem wir einfach die spezielle Betragsmetrik durch eine allgemeine Metrik ersetzen:

````{prf:definition}
Sei $X$ ein metrischer Raum und $(x_n)$ eine Folge in $X$. $(x_n)$ heißt konvergent mit Grenzwert $\overline{x}$, wenn

```{math}
 \forall \epsilon  >0 ~\exists n_0 \in \N ~\forall n \geq n_0: d(x_n, \overline{x}) < \epsilon.
```

$(x_n)$ heisst Cauchy-Folge, wenn

```{math}
 \forall \epsilon  >0 ~\exists n_0 \in \N ~\forall m,n \geq n_0: d(x_n, x_m) < \epsilon.
```

````

Wir sehen also, dass konvergente Folgen ab einem bestimmten Index in einer $\epsilon$-Umgebung um den Grenzwert liegen.

Es gilt folgendes einfach zu beweisende Resultat:

````{prf:lemma}
:label: nullfolgenmetrik
Die Folge $(x_n)$ im metrischen Raum $(X,d)$ konvergiert genau dann gegen $\overline{x}$, wenn $d(x_n,\overline{x})$ eine Nullfolge in $\R$ ist.
````

Genau wie in $\R$ können wir auch leicht folgendes Resultat beweisen:

````{prf:theorem}
Jede konvergente Folge in einem metrischen Raum ist eine Cauchy-Folge.
````

Wir haben schon gesehen, dass nicht in jedem metrischen Raum die Umkehrung gilt (nicht alle Cauchy-Folgen konvergieren), z.B. in $\Q$ mit der Betragsmetrik.

````{prf:definition}
Ein metrischer Raum $(X,d)$ heisst vollständig, wenn jede Cauchy-Folge in $X$ konvergiert.
````

Wir kennen bereits ein Beispiel eines vollständigen Raums, nämlich $\R$ mit der Betragsnorm. Dies gilt auch im $\R^N$:

````{prf:theorem}
Für $N \in \N$ ist $\R^N$ mit der durch die Euklidischen Norm definierten Metrik vollständig.
````

````{prf:proof}
 Ist $(x_n)$ eine Cauchy-Folge in $\R^N$, so gilt für die Koordinatenfolge

```{math}
 x_n^{(i)} = e_i \cdot x_n,
```

die Ungleichung

```{math}
 | x_n^{(i)} -  x_m^{(i)}  | \leq \sqrt{ \sum_{j=1}^n (x_n^{(j)} -  x_m^{(i)} } = \Vert x_n - x_m \Vert .
```

Damit ist $(x_n^{i})$ eine Cauchy-Folge in $\R$ und somit konvergent. Wir bezeichnen den Grenzwert mit $\overline{x}^{(i)}$ und den Vektor
$\overline{x}=(\overline{x}^{(i)})_{i=1,\ldots,N}$.

Nun gibt es für jedes $\epsilon > 0$ ein $n_0^{(i)} \in \N$, sodass für alle $ n \geq n_0^{i)}$ gilt:

```{math}
 \vert x_n^{i} -\overline{x}^{(i)} \vert < \frac{\epsilon}{\sqrt{N}}.
```

Für $n_0 = \max_{i=1,\ldots,N} n_0^{(i)}$ folgt.

```{math}
 \forall n \geq n_0: \Vert x_n - \overline{x} \Vert = \sqrt{\sum_{i=1}^N (x_n^{(i)} - \overline{x}^{(i)})^2} < \sqrt{\sum_{i=1}^N \frac{\epsilon^2}N} = \epsilon.
```

Damit konvergiert $x_n$ gegen $\overline{x}$.

````

Mit ähnlichen Argumenten sehen wir, dass eine Folge $(x_n)$ im $\R^N$ mit der Euklidischen Metrik genau dann konvergiert, wenn alle Koordinatenfolgen $(x_n^{i})$ in $\R$ konvergieren. Mit den Eigenschaften für Grenzwerte in $\R$ zeigen wir auch für konvergente Folgen $(x_n)$ und $(y_n)$ im $\R^N$:

\begin{align*}
\lim (x_n + y_n) &= \lim x_n + \lim y_n \\
\lim (x_n \cdot y_n) &= \lim x_n \cdot \lim y_n.
\end{align*}
