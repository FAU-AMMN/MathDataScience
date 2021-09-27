# Funktionen

Eine Funktion ist in allgemeinster Weise eine Abbildung $f: M_1 \rightarrow M_2$, die jedem Wert $x \in M_1$ einen _eindeutigen_ Wert $y \in M_2$ zuordnet. In der Schule betrachtet man üblicherweise skalare reelle Funktionen, d.h. $M_1=M_2=\R$, manchmal auch $M_1$ ein Intervall in $\R$. Im Prinzip sind aber auch Folgen nichts anderes als Funktionen von $\N$ nach $\R$.

````{prf:definition}
Eine Funktion $f:M_1 \rightarrow M_2$ heisst
\begin{*ize}
\* _injektiv_, wenn aus $x \neq y$ auch $f(x) \neq f(y)$ folgt.

\* _surjektiv_, wenn zu jedem $z \in M_2$ ein $x \in M_1$ existiert mit $f(x)=z$.

\* _bijektiv_, wenn sie injektiv und surjektiv ist. 
\end{*ize} 
````

Eine bijektive Funktion ordnet jedem Element aus $M_1$ genau ein Element aus $M_2$ zu und umgekehrt. Damit existiert  auch eine Umkehrfunktion $f^{-1}: M_2 \rightarrow M_1$ (wir beachten, dass die Umkehrfunktion $f^{-1}(x)$ nicht zu verwechseln ist mit $f(x)^{-1} = \frac{1}{f(x)}$). Die Umkehrfunktion erfüllt

```{math}
 f^{-1}(f(x)) = x, \qquad f(f^{-1}(y) = y 
```

für alle $x \in M_1$ und alle $y \in M_2$.

## Lineare Funktionen

Wir beginnen mit einigen wichtigen Beispielen skalarer Funktionen in $\R$. Die wohl einfachsten sind lineare bzw. affin-lineare Funktionen. Eine lineare Funktion ist von der Form

```{math}
 f:x \mapsto a_1 x, 
```

mit einer Konstanten $a_1 \in \R$. Eine affin-lineare Funktion ist um eine Konstante verschoben, d.h.

```{math}
 f:x\mapsto a_1 x + a_0. 
```

Für $a_1 =0$ ist $f$ eine konstante Funktion.

Linearität lässt sich durch zwei Eigenschaften charakterisieren:

* Für alle $x,y \in M_1$ gilt $f(x+y)=f(x) + f(y) $.

* Für alle $x \in M_1$ und $c \in \R$, sodass $cx \in M_1$ ist, gilt $f(cx) = c f(x)$.

In $\R$ folgt daraus trivialerweise die obige Form, da wir $x=1$ wählen können und damit ist $a_1 = f(0)$. Aber auch im $\R^n$ reicht dies um eine ähnliche Form herzuleiten.

## Polynome und Rationale Funktionen

Eine allgemeinere Klasse als lineare Funktionen sind die sogenannten Polynome. Ein Polynom vom Grad $k$ ist die Funktion

```{math}
 f:x\mapsto a_k x^k + a_{k-1}x^{k-1} + \ldots + a_1 x + a_0. 
```

Eine wichtige Eigenschaft von Polynomen ist der Nullstellensatz: ein Polynom vom Grad $k$ kann höchstens $k$ Nullstellen (mit Vielfachheit gezählt haben), mit Ausnahme des trivialen Nullpolynoms. Hat ein Polynom $k$ reelle Nullstellen $x_0, \ldots x_{k-1}$, dann gilt

```{math}
 f(x) = a_k (x - x_{k-1}) \ldots (x-x_0). 
```

Grundlage dafür ist, dass ein Polynom vom Grad $k$ mit Nullstelle $x_0$ immer geschrieben werden kann als

```{math}
 f(x) = (x-x_0) g(x) 
```

mit einem Polynom $g$ vom Grad $k-1$.

Dies ist ein Spezialfall der sogenannten Polynomdivision, ist $f$ ein Polynom vom Grad $k$ und $g$ ein Polynom vom Grad $m \leq k$, dann existiert ein Polynom $h$ vom Grad $m-k$ und ein Polynom $r$ vom Grad höchstens $m-1$, sodass

```{math}
 f(x) = h(x) g(x) + r(x).
```

Die Division funktioniert dabei genauso wie schriftliche Division bei Dezimalzahlen, diese sind ja von der Form

```{math}
z = a_k 10^k + a_{k-1} 10^{k-1} + \ldots + a_1 10^1 + a_0. 
```

Das Polynom $r$ hat dabei die Rolle des Rests bei der Division.  Wir sehen auch, dass die sogenannten _Monome_ $x^k$ in dieser Darstellung eine wichtige Rolle einnehmen, wir schreiben jedes Polynom als gewichtete Summe von Monomen, wir werden dies allgemeiner _Linearkombination_ nennen.

Es gelten auch sonst analoge Eigenschaften wie bei der Rechung mit ganzen Zahlen:

* Summen von Polynomen sind Polynome.

* Produkte von Polynonem sind Polynome.

* Es gibt ein neutrales Element der Addition, das Nullpolynom $p_0(x)=0$: Es gilt $p(x) + p_0(x) = p(x)$ für jedes Polynom.

* Es gibt ein neutrales Element der Multiplikation, das konstante Polynom $p_1(x)=1$: Es gilt $p(x) p_1(x) = p(x)$ für jedes Polynom.

* Es gibt ein inverses Element der Addition, d.h. zu jedem Polynom $p$ gibt es ein Polynom $q$ mit $p(x) + q(x) =0$ für alle $x$.

* Es gelten Kommutativ-, Assoziativ- und Distributivgesetz.

Wir beachten, dass als Spezialfall dieser Rechenregeln auch die Multiplikation von Polynomen mit reellen Zahlen beinhaltet sind, da wir reelle Zahlen mit konstanten Polynomen identifizieren können.

Wir kehren nochmal zum Nullstellensatz zurück und wollen uns zunächst überlegen, warum ein Polynom mit Nullstelle $x_0$ durch $(x-x_0)$ ohne Rest dividierbar ist. Nach der Formel für Polynomdivision gilt

```{math}
 f(x) = h(x) (x-x_0) + r(x).
```

Da $x-x_0$ ein Polynom vom Grad $1$ ist, muss $r$ Grad $0$ haben, d.h. $r$ ist eine konstante. Sezten wir $x=x_0$ ein, dann folgt

```{math}
 0 = 0 + r(x_0) . 
```

Also folgt $r(x) =r(x_0) = 0$ für alle $x$. Damit sehen wir auch sofort, dass ein nichtriviales Polynom vom Grad $k$ höchstens $k$ Nullstellen (mit Vielfachheit gezählt) haben kann. Gäbe es $k+1$ Nullstellen, dann könnten wir durch die ersten $k$ dividieren und es muss ein Polynom vom Grad $0$ übrig bleiben. Ist dieses gleich Null, dann war $f$ schon das Nullpolynom. Andernfalls kann das Polynom vom Grad $0$ keine weitere Nullstelle haben.

Wenn man Polynome mit nichtverschwindendem Rest dividiert, erhält man _rationale Funktionen_.
Eine rationale Funktion ist von der Form

```{math}
 f:x\mapsto  \frac{p(x)}{q(x)}, 
```

wobei $p$ und $q$ Polynome sind. Im Gegensatz zu Polynomen ist der Definitionsbereich rationaler Funktionen nicht ganz $\R$, da die Nullstellen von $q$ ausgenommen werden müssen, an denen $f$ Pole hat. Wegen dem Nullstellensatz ist die Anzahl der Nullstellen von $f$ durch den Grad von $p$ begrenzt, die Anzahl der Pole durch den Grad von $q$.

Bei rationalen Polynomen gelten analoge Rechenregeln wie bei rationalen Zahlen, insbesondere gibt es, wenn $f$ nicht die Nullfunktion ist, auch ein inverses Element der Multiplikation. Für jedes rationale Funktion $f$ gibt es eine rationale Funktion $g$ mit $f(x) g(x) = 1$ für alle $x$.

## Exponentialfunktion und Logarithmus

Eine andere wichtige Klasse von Funktionen sind _Exponentialfunktionen_, die durch $f: x\mapsto a^x$ für ein $a \in \R$ definiert sind. Für $n \in \N$ ist $a^n$ die $(n-1)$-malige Multiplikation von $a$ mit sich selbst und wir sehen, dass dann

```{math}
 f(n+m) = a^{n+m}  = a^n a^m  = f(n) f(m) 
```

gilt. Diese Eigenschaft kann tastsächlich als allgemeine Charakterisierung einer Exponentialfunktion verwendet werden, wir betrachten einfach eine Funktion $f$ auf $\R$ für die

```{math}
 f(x+y) =  f(x) f(y) 
```

für alle $x,y \in \R$ sowie $f(0)=1$
gilt. Damit ist automatisch $f(x+1) = f(x) f(1)$ und durch Hintereinanderausführung $f(x+m) = f(x) f(1)^m$ für $m \in \N$. Definieren wir also $a=f(1)$, so sehen wir dass für alle $n \in \N$ die Form $f(n) = a^n$ folgt. Ist $a \neq 0$ so können wir auch dividieren und erhalten die selbe Form für $n \in \Z$. Als nächsten Schritt können wir $x= \frac{n}m$ für $n \in \Z, m \in \N$ betrachten. Nun wählen wir $y=(m-1) x$ und erhalten

```{math}
 f(m x) = f((m-1)x) f(x) 
```

und durch Hintereinanderausführung

```{math}
 a^n = f(n) = f(mx) = f(x)^m. 
```

Also gilt $f(x) = a^{\frac{n}m}. $ Für die Erweiterung auf reelles $x$ benötigt man noch einen Grenzwert von rationalen gegen reelle Werte, dies werden wir später auch basierend auf der Annahme der Stetigkeit kennen lernen.

Besonders interessant ist  der Fall $a=e$, wie wir sehen werden lassen sich alle Exponentialfunktionen mit $a > 0$ als $f(x) = e^{cx}$ mit $c\in \R$ schreiben. Die Euler'sche Zahl $e$ können wir als

```{math}
 e= \lim_{n \rightarrow \infty} \left(1 + \frac{1}n\right)^n 
```

definieren. Alternativ können wir $e^x$ auch über die Potenzreihe

```{math}
 e^{x} = 1 + x+ \frac{x^2}2 + \frac{x^3}{3!} + \frac{x^4}{4!} + \ldots 
```

definieren, allerdings muss dann die Konvergenz der Reihe auch für jedes $x$ zeigen, was wir später in der Vorlesung tun werden.

Die Exponentialfunktion ist eine monoton steigende Funktion, d.h.

```{math}
 f(x) \geq f(y) \quad \text{für } x > y, 
```

es gilt sogar $f(x) > f(y)$ für $x > y$ und damit ist $f$ injektiv. Andererseits ist die Exponentialfunktion auch surjektiv und damit invertierbar. Die inverse Funktion nennen wir Logarithmus ($\log x$). Es gilt

```{math}
 \log e^x = x \qquad e^{\log y} = y. 
```

Die Rechenregeln für den Logarithmus können wir aus den Regeln für die Exponentialfunktion herleiten. Es gilt

```{math}
 \log (y_1 y_2) = \log (e^{x_1} e^{x_2}) = \log e^{x_1 + x_2} = x_1 + x_2 = \log y_1 + \log y_2. 
```

Setzen wir $y_1 = y_2 =y$ dann folgt auch

```{math}
  \log ( y^2) = 2 \log y 
```

und induktiv

```{math}
  \log ( y^n) = n \log y. 
```

Mit einer entsprechenden Konstruktion sehen wir auch

```{math}
 \log (y^x) = x \log y, 
```

für $x \in \R$. Damit ist

```{math}
 \log (a^x) = x \log a 
```

 und es folgt

```{math}
 a^x = e^{c x}, 
```

mit $c= \log a$. Also können wir wie angekündigt alle Exponentialfunktionen in der Form $e^{cx}$ schreiben.

## Sinus- und Cosinusfunktion

Die Sinus- und Cosinusfunktion sind periodische Funktionen in $\R$, deren Wertebereich $[-1,1]$, es gibt daher nur Umkehrfunktionen wenn wir sie im Fall des Sinus von $[-\frac{\pi}2,\frac{\pi}2]$ nach $[-1,1]$ und im Fall des Cosinus von $[0,\pi]$ nach $[-1,1]$ betrachten.

Es gilt

```{math}
 \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \ldots 
```

und

```{math}
\cos x = 1- \frac{x^2}{2!} + \frac{x^4}{4!} - \ldots 
```

Der Sinus ist eine ungerade Funktion, d.h. $\sin (-x) = -  \sin x$, während der Cosinus eine gerade Funktion ist, d.h. $\cos(-x) = \cos(x)$. Sinus uns Cosinus erfüllen einige interessante Eigenschaften wie Additionstheoreme, wir werden später sehen, dass diese überraschenderweise aus den Eigenschaften der Exponentialfunktion folgen, dies basiert auf den komplexen Zahlen. Mit der imaginären Zahl $\i$, die $\i^2 = -1$ erfüllt, gilt

```{math}
 e^{\i x}  = \cos x + \i \sin x. 
```
