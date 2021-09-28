# Stetigkeit

In diesem Abschnitt wollen wir den Begriff der Stetigkeit, der intuitiv relativ klar ist, mathematisch etwas klarer formulieren. Alle Beispiele an Funktionen, die wir bisher gesehen haben, sind stetig. Eine Funktion ist stetig in einem Punkt $x$, wenn aus $|y-x|$ klein auch $|f(y)-f(x)|$ klein folgt. Dies können wir sauberer über Folgen definieren:

````{prf:definition}
Eine Funktion $f: I \subset \R \rightarrow \R$ heisst stetig in $x \in I$, genau dann wenn für alle Folgen $x_n \rightarrow x$ gilt: $f(x_n) \rightarrow f(x)$. 
````

Alternativ können wir auch eine Definition von Stetigkeit über die Nähe geben: egal welche kleine Schranke wir an die Unterschiede der Funktionswerte vorgeben, können wir diese garantieren, solange die Differenz der Argumente klein genug ist:

````{prf:definition}
Eine Funktion $f: I \subset \R \rightarrow \R$ heisst stetig in $x \in I$, genau dann wenn 

```{math}
 \forall \epsilon > 0~\exists \delta > 0 ~\forall y \in I, |y-x| < \delta: |f(x) - f(y)|<\epsilon. 
```

````

Wir werden später sehen, dass diese beiden Definitionen äquivalent sind. Hier betrachten wir aber noch einen wichtigen Spezialfall, sogenannte Lipschitz-stetige Funktionen:

````{prf:definition}
Eine Funktion $f: I \subset \R \rightarrow \R$ heisst Lipschitz-stetig, genau dann wenn 

```{math}
 \ \exists L > 0 ~\forall x,y \in I: |f(x) - f(y)| \leq L |x-y|.
```

````

Eine Lipschitz-stetige Funktion ist immer stetig, für alle $x \in I$. Wir sehen, dass aus $|x-y| < \delta$ immer $|f(x) - f(y)| < L \delta$ folgt. Also können wir zu jedem $\epsilon > 0$ ein $\delta = \frac{\epsilon}{L}$ wählen, sodass die Definition der Stetigkeit erfüllt ist.

````{prf:example}
Sei $f(x) = a_1 x + a_0$, dann ist $f$ Lipschitz-stetig auf $\R$ mit $L=\vert a_1 \vert$. 
````

````{prf:example}
Sei $f(x) = x^2$, dann ist $f$ Lipschitz-stetig auf $I=[-b,b]$ mit $L= 2b$. 
````
