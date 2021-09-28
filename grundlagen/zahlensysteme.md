# Zahlensysteme

Im Folgenden betrachten wir die wichtigsten Zahlensysteme und ihre Eigenschaften. Wir beginnen bei den natürlichen Zahlen und machden den Weg bis zu den reellen und komplexen Zahlen.

## Natürliche Zahlen

Die bisher verwendete Aufzählung $\N = \{0,1,2,3,\ldots\}$ ist etwas unbefriedigend, da wird die Punkte ja nicht bis unendlich auffüllen können. Deshalb ist es besser die natürlichen Zahlen axiomatisch zu definieren (über die sogenannten Dedekind-Peano Axiome):

````{prf:definition}
Die natürlichen Zahlen sind eine Menge mit den folgenden Eigenschaften:

* Es gibt ein ausgezeichnetes Element $0$

* Es gibt eine Nachfolgerabbildung ${\cal N}:\N \rightarrow \N$, sodass $0 \notin {\cal N}(\N)$ und ${\cal N}$ injektiv ist.

* Falls für $M \subset \N$ gilt: $0 \in M$ und ${\cal N}(M) \subset M$, dann ist $M=\N$.

````

Man kann zeigen, dass damit die natürlichen Zahlen wohldefiniert sind. Nun definieren wir die Addition und Multiplikation mit

```{math}
 m + {\cal N}(n) = {\cal N}(m+n)
```

und

```{math}
 m 0 = 0, \quad m {\cal N}(n) = mn +m.
```

Wir nennen ${\cal N}(0)=1$ und haben daher auch
$ {\cal N}(n) = n+1$.

## Vollständige Induktion

Die Definition der natürlichen Zahlen impliziert auch die Beweistechnik der vollständigen Induktion:

````{prf:theorem}
$A(0)$ sei wahr und aus $A(n)$ wahr folgt $A(n+1)$ wahr für alle $n \in \N$. Dann ist die Aussage $A(m)$ wahr für alle $m \in N$.
````

````{prf:proof}
 Sei $N=\{m \in \N~|~A(m) \text{ ist wahr }\}$. Nun gilt nach unseren Voraussetzungen $0 \in N$ und für jedes $n \in N$ auch ${\cal N}(n) \in N$. Also gilt $N= \N$ und die Aussage ist für alle $m \in \N$ wahr
````

Damit haben wir ein sehr nützliches Prinzip, mit dem wir Aussagen über den natürlichen Zahlen zeigen können. Die Überprüfung, dass $A(0)$ wahr ist, nennen wir Induktionsanfang, die Folgerung von $n$ auf $n+1$ den Induktionsschritt. Beim Induktionsschritt wird die angenommene Gültigkeit von $A(n)$ auch als Induktionsannahme bezeichnet. Natürlich können wir Induktionsbeweise auch für Teilmengen der Form $N= \{n \in \N~|~n \geq k \}$
anwenden, denn durch die Variablentransformation $m=n-k$ kommen wir auf die ursprüngliche Version. Damit können wir also den Induktionsanfang bei $k$ und den Induktionsschritt für $n \geq k$ machen um eine Aussage auf $N$ zu zeigen.Wir illustrieren das Induktionsprinzip an zwei Beispielen:

````{prf:example}
Wir beweisen das Kommutativgesetz der Addition, d.h. wir zeigen $n+m=m+n$ für alle $n,m \in \N$. Wir beginnen mit der einfacheren Version $n+1=1+n$ für alle $n\in\N$. Der Induktionsanfang bei $n=0$ liefert $1=1$, also ist $A(0)$ wahr. Sei nun die Induktionsannahme $n+1=1+n$, dann wollen wir folgern
```{math}
 (n+1)+1=1+(n+1).
```

Dazu können wir aber die Induktionsannahme verwenden, denn es gilt $n+1+1 = 1+n+1$ und damit folgt $A(n+1)$ aus $A(n)$.
Mit einem zweiten Induktionsbeweis zeigen wir nun die eigentliche Aussage $n+m=m+n$, wobei wir jetzt Induktion in $m$ verwenden. Für $m=0$ ist die Aussage wahr, da sie zu $n=n$ reduziert. Nehmen wir nun an, dass $n+m=m+n$ gilt, so wollen wir zeigen

```{math}
 n+(m+1) = (m+1) + n
```

Dazu verwenden wir die oben bewiesene Eigenschaft $m+1 =1+m$ bzw. $n+1=1+m$ sowie die Induktionsannahme, also gilt

```{math}
 n+m+1=n+1+m=1+n+m=1+m+n=m+1+n
```

und wir haben den Induktionsschritt erfolgreich durchgeführt
````

````{prf:example}
Wir beweisen die Gauss'sche Summationsformel für die Summe der ersten $n$ Zahlen

```{math}
  \sum_{i=1}^n i = \frac{n(n+1)}2.
```

Hier sind wir also im Fall $k=1$ wie oben beschrieben. Wir definieren die Aussage $A(n)$ als _Die Summenformel gilt für die ersten $n$ Zahlen_.
Den Induktionsanfang $A(1)$ können wir durch direktes Ausrechnen nachprüfen

```{math}
  1 = \sum_{i=1}^n 1 = \frac{1(1+1)}2 = 1.
```

Nun führen wir den Induktionsschritt durch, es gelte $A(n)$. Wir berechnen dann

```{math}
 \sum_{i=1}^{n+1} i = \sum_{i=1}^n i  + (n+1) = \frac{n(n+1)}2 + (n+1) = \frac{(n+1)(n+2)}2,
```

wobei wir in der Mitte die bereits gültige Aussage $A(n)$  eingesetzt haben.Damit haben wir $A(n+1)$ gefolgert und somit die Summenformel für alle $n \in \N \setminus \{0\}$ gültig
````

## Ganze Zahlen

Nachdem wir die natürlichen Zahlen bereits definiert haben, können wir nun die ganzen Zahlen als

```{math}
 Z = \N \cup -\N = \{n ~|~n \in \N \text{ oder } -n \in \N \}
```

definieren mit den gleichen Regeln für die Addition und Multiplikation wie in $\N$, wobei $-n$ das zu $n$ inverse Element bezüglich der Addition ist, d.h.

```{math}
\forall n \in \Z: -n + n = n + (-n) = 0.
```

Die $0$ nennen wir neutrales Element, da $n+0=0+n=n$, d.h. Addition mit $0$ verändert die Zahl nicht.
Daraus folgern wir übrigens auch die Regel _Minus mal Minus ist Plus_. Es gilt ja, dass $-(-n))$ das inverse Element zu $-n$ ist und das ist wegen $n+(-n) = (-n)+n=0$ durch $n$ gegeben.
Die Addition und Multiplikation auf den ganzen Zahlen liefern eine interessante algebraische Struktur.
Die ganzen Zahlen mit der Operation der Addition sind eine sogenannte Gruppe:

````{prf:definition}
Eine Menge $G$ zusammen mit einer Abbildung $\circ: G \times G \rightarrow G$ heißt _Gruppe_, wenn die folgenden Eigenschaften erfüllt sind:

* $ \forall a,b,c \in G: a \circ (b \circ c) = (a\circ b) \circ c$ (Assoziativität)

* $\exists n \in G~ \forall a \in G: n \circ a = a$ (neutrales Element)

* $\forall a \in G~\exists a' \in G: a' \circ a = n$ (Existenz eines inversen Elements)

Die Gruppe heißt abelsch (oder kommutativ), wenn für alle $a,b \in G$ gilt: $a \circ b = b \circ a$.
````

```{margin} Niels Abel
[Niels Henrik Abel](https://de.wikipedia.org/wiki/Niels_Henrik_Abel) (\* 5. August 1802 auf der Insel Finnøy, Ryfylke, Norwegen; † 6. April 1829 in Froland, Aust-Agder, Norwegen) war ein norwegischer Mathematiker.
```

Wir beachten, dass wir die Eigenschaft des neutralen und inversen Elements nur einseitig definiert haben, bei abelschen Gruppen folgt sofort $a \circ n = a$ und $a \circ a'=n$. Diese Eigenschaft folgt aber auch bei allgemeinen Gruppen. Es gilt ja dann

```{math}
a' \circ a  \circ a' = n \circ a' = a'
```

und damit

```{math}
(a \circ a') \circ a \circ a' = a \circ a' .
```

Nun gibt es ein inverses Element $b$ zu $(a \circ a')$ also folgt

```{math}
a \circ a' = b \circ (a \circ a') \circ a \circ a' = b \circ (a \circ a') = n.
```

Analog zeigt man auch $a \circ n = a$.
Es gibt in einer Gruppe nur ein neutrales Element und zu jedem $a$ ein eindeutiges inverses Element. Seien $n_1,n_2$ neutrale Elemente, dann gilt ja

```{math}
n_1 = n_1 \circ n_2 = n_2,
```

also sind sie gleich. Seien $a_1'$ und $a_2'$ inverse Elemente zu $a$, dann gilt

```{math}
a_1' = a_1' \circ (a \circ a_2') = (a_1' \circ a) \circ a_2' = a_2'.
```

Neben $\Z$ können wir noch andere Beispiele von Gruppen finden.

````{prf:example}
Sei $p \in \N \setminus \{0\}$. Dann ist die Faktormenge $\Z_p = (\Z/p\Z, +)$ eine Gruppe, die wir mit der Restklasse
$ \{0,1,\ldots,p-1\}$ identifizieren können. Im Sinne einer Restklasse ergibt sich automatisch die Addition modulo $p$. Das neutrale Element ist $n=0$, das zu $m$ inverse Element ist $m'=p-m$. Wir betrachten als konkretes Beispiel $p=3$, hier ist die Addition gegeben durch


|+   | $0$ | $1$ | $2$ |
|----|-----|-----|-----|
|$0$ | $0$ | $1$ | $2$ |
|$1$ | $1$ | $2$ | $0$ |
|$2$ | $2$| $0$  | $1$ |

````

Wir können $\Z$ auch mit den beiden Operationen $+$ und $\cdot$ betrachten, dann ergibt sich die Struktur eines Rings:

````{prf:definition}
Ein Ring $R$ ist eine bezüglich der Operation $+$ abel'sche Gruppe mit einer zweiten Operation $\cdot : R \times R \rightarrow R$, sodass folgende Eigenschaften erfüllt sind:

* $ \forall a,b,c \in R: a \cdot (b \cdot c) = (a\cdot b) \cdot c$ (Assoziativität)

* $ \forall a,b,c \in R: a \cdot (b+c) = a\cdot b + a \cdot c$ und $(b+c) \cdot a = b \cdot a + c \cdot a$ (Distributivgesetz)

Wir bezeichnen das neutrale Element der Addition $+$ als 0.
Falls ein zusätzliches neutrales Element $1$ existiert, sodass für alle $a  \in R$ gilt $1 \cdot a = a \cdot 1$, dann
heißt $R$ Ring mit Einselement. Gilt für alle $a, b  \in R$, dass $a \cdot b = b \cdot a$, dann heißt $R$ kommutativ
````

Wir beachten, dass in einem Ring aus $a_1 \cdot b = a_2 \cdot b$ nicht $a_1=a_2$ folgen muss, auch wenn $b\neq 0$ gilt. Aus diesen Gründen müssen wir beim neutralen Element der Multiplikation auch die beidseitige Definition verwenden.

````{prf:example}
Wir betrachten $(\Z/2\Z, +,\cdot)=(\{0,1\},+,\cdot)$. Hier gilt

| $+$ | $0$ | $1$ | | $\cdot$ | $0$ | $1$ |
|-----|-----|-----|-|---------|-----|-----|
| $0$ | $0$ | $1$ | | $0$     | $0$ | $0$ |
| $1$ | $1$ | $0$ | | $1$     | $0$ | $1$ |

Wir sehen, dass $0$ das neutrale Element der Addition und $1$ das neutrale Element der Multiplikation ist. Dazu sind die Operationen kommutativ, wir haben also einen kommutativen Ring mit Einselement.
````

````{prf:example}
Wir betrachten $(\Z/4\Z, +,\cdot)=(\{0,1,2,3\},+,\cdot)$. Hier gilt


|$+$ | $0$ | $1$  | $2$ | $3$ |
|----|-----|------|-----|-----|
|$0$ | $0$ | $1$  | $2$ | $3$ |
|$1$ | $1$ | $2$  | $3$ | $0$ |
| $2$ | $2$ | $3$ | $0$ | $1$ |
| $3$ | $3$ | $0$ | $1$ | $2$ |


| $\cdot$ | $0$ | $1$ | $2$ | $3$ |
|---------|-----|-----|-----|-----|
| $0$     | $0$ | $0$ | $0$ | $0$ |
| $1$     | $0$ | $1$ | $2$ | $3$ |
| $2$     | $0$ | $2$ | $0$ | $2$ |
| $3$     | $0$ | $3$ | $2$ | $1$ |

Wir sehen, dass $0$ das neutrale Element der Addition und $1$ das neutrale Element der Multiplikation ist. Dazu sind die Operationen kommutativ, wir haben also einen kommutativen Ring mit Einselement.
````

## Rationale Zahlen

Die rationalen Zahlen definieren wir üblicherweise als Brüche von ganzen Zahlen. Dabei haben wir natürlich das Problem des _Kürzens_. Zwei Brüche der Form $\frac{p_1}{q_1}$ und $\frac{p_2}{q_2}$ mit $p_i, q_i \in \Z$,$q_i \neq 0$ (für $i=1,2$) betrachten wir als gleich, wenn nach ausmultiplizieren
$p_1 q_2= p_2 q_1$ gilt.
Die mathematische Grundlage zur Betrachtung dieses Problems haben wir bereits gelegt, nämlich die Faktorisierung bezüglich einer Äquivalenzrelation. Wir definieren zunächst die rationalen Zahlen als $\Z \times (\N \setminus \{0\})$, d.h. alle möglichen Zähler-Nenner Paare. Nun definieren wir eine Äquivalenzrelation

```{math}
\frac{p_1}{q_1} \sim \frac{p_2}{q_2}  \quad \Leftrightarrow \quad p_1 q_2= p_2 q_1.
```

Reflexivität, Symmetrie und Transitivität sind wegen den Eigenschaft der Multiplikation in $\N$ gegeben.
Nun definieren wir die rationalen Zahlen als Faktorgruppe

```{math}
\Q = ( \Z \times (\N \setminus \{0\}) /  \sim).
```

Eine rationale Zahl entspricht also der Klasse an Brüchen, die den gleichen Wert ergeben. Wir können als Repräsentanten dann den gekürzten Bruch, also teilerfremde $p$ und $q$ wählen. Wir schreiben dann statt $(p,q)$ einfach $\frac{p}q$. Auch bei Addition und Multiplikation betrachten wir Äquivalenzklassen und definieren

```{math}
 \frac{p_1}{q_1} +   \frac{p_2}{q_2}  = \frac{p_1 q_2 + p_2 q_1}{q_1q_2}
```

und

```{math}
 \frac{p_1}{q_1}  \cdot  \frac{p_2}{q_2}  = \frac{p_1   p_2  }{q_1q_2} .
```

Mit diesen Gesetzen weisen wir leicht nach, dass $\Q$ ein Ring ist, es gilt aber sogar noch die zusätzliche Eigenschaft, dass es ein inverses Element der Multiplikation gibt. Dies führt uns auf die nächste Definition:

````{prf:definition}
Ein kommutativer Ring $\K$ mit Einselement $1 \neq 0$ heißt Körper, wenn
```{math}
 \forall a \in\K \setminus \{0\} ~\exists b \in K:  a b = 1.
```

````

In $\Q$ ist das inverse Element für $\frac{p}q \neq 0$ gegeben durch $\frac{q}p$. Allgemein gilt in einem Körper, dass $x$ das inverse Element zu $1/x$. Darüber hinaus erfüllt ein Körper die sogenannte Nullteilerfreiheit, d.h.

```{math}
x \cdot y = 0 \quad \Rightarrow x = 0 \text{ oder } y =0.
```

Wir haben am Beispiel des Rings $\Z_4=\Z/4\Z$ (dort ist $2 \cdot 2 = 0$) schon gesehen, das die Nullteilerfreiheit nicht in jedem Ring gilt.
Neben der Körpereigenschaft haben wir mit der üblichen Ordnungsrelation $\leq$, d.h.

```{math}
\frac{p_1}{q_1} \leq \frac{p_2}{q_2} \quad \Leftrightarrow \quad p_1 q_2 \leq p_2 q_1
```

auch eine vollständige Ordnung auf $\Q$. Diese verträgt sich in gewisser Weise mit den Rechenoperationen, was uns auf folgende Definition führt:

````{prf:definition}
Ein Körper $\K$ mit vollständiger Ordnung $\preceq$ bzw. $\prec$  heißt angeordnet, wenn die beiden folgenden Bedingungen erfüllt sind:

* $\forall~x,y,z \in \K, x \prec y: x+z \prec y+z$

* $\forall x,y \in \K, 0 \prec x, 0 \prec y: 0 \prec x \cdot y$.

````

Für einen angeordneten Körper erhalten wir verschiedene intuitive Eigenschaften:

* Für $x \in \K \setminus \{0\}$ gilt entweder $0 \prec x$ oder $0 \prec -x$. Dies sehen wir aus der ersten Eigenschaft, denn falls $0 \prec x$ gilt können wir $z=-x$ addieren. Damit sehen wir auch, dass $ 0 \preceq 1$ gelten muss, sonst wäre $0 \preceq -1$ und damit wegen der zweiten Eigenschaft für $0 \prec x $ auch $0 \prec -x$.

* $0 \prec x^2 = (-x)^2$. Dies sehen wir aus der zweiten Eigenschaft, entweder für $0 \prec x$ oder $0 \prec -x$.

* Aus $x_1 \prec x_2$ und $y_1 \prec y_2$ folgt $x_1 + y_1 \prec x_2 + y_2$.

* Aus $0 \prec x$ folgt $0 \prec \frac{1}x$.

In einem angeordneten Körper kann man den Betrag als

```{math}
\vert x \vert := \left\{ \begin{array}{rl} x & 0 \preceq x \\ -x & x \prec 0 \end{array} \right.
```

und das Vorzeichen (Signum) als

```{math}
\text{sign}(x) =  \left\{ \begin{array}{rl} 1 & 0 \prec  x \\ 0 & x =0\\-1 & x \prec 0 \end{array}\right.
```

definieren. Auch für Betrag und Vorzeichen gelten die üblichen Eigenschaften wie

* $x = |x|$ sign$(x)$, $|-x|=|x|$.

* $|x|~|y|=|xy|$, sign$(x)$sign$(y) = $sign$(xy)$.

* $0 \preceq |x|$ und $|x|=0 \Leftrightarrow x =0$.

* $|x+y| \preceq |x|+|y|$ (Dreiecksungleichung)

Da die ersten Eigenschaften sehr einfach zu zeigen sind, beweisen wir nur kurz die Dreiecksungleichung. Wegen $x \preceq |x|$ und $-x \preceq |x|$ folgt

```{math}
x+y \preceq |x|+|y|, \qquad -x-y \preceq |x|+|y|
```

und damit direkt die Dreiecksungleichung.
Neben Betrag und Vorzeichen können wir auch das Maximum und Minimum definieren durch

```{math}
\max\{x,y\} = \left\{ \begin{array}{rl} x & y \preceq x \\ y & x \prec y \end{array} \right.
```

bzw.

```{math}
\min\{x,y\} = \left\{ \begin{array}{rl} y & y \preceq x \\ x & x \prec y. \end{array} \right.
```

Durch eine Hintereinanderausführung erhalten wir dann auch Maximum und Minimum endlicher Mengen, z.B.

```{math}
\max\{x_1,\ldots,x_n\} = \max\{x_1,\max\{x_2, \ldots, \max\{x_{n-1},x_n\} \ldots\}\}.
```

$\Q$ ist nicht nur ein angeordneter Körper, sondern wird sogar als _archimedisch angeordnet_ bezeichnet. Dies bedeutet, dass für alle $x \in \K$ ein $n \in \N$ existiert mit $x \prec n$. Bei einer rationalen Zahl $\frac{p}q$ können wir einfach $n = |p|+1$ wählen.
Wir betrachten zum Abschluss noch die Mächtigkeit von $\Q$. Wir haben schon gesehen, dass es eine bijektive Abbildung $f: \N \mapsto \N \times \N$ gibt, und ähnlich können wir eine bijektive Abbildung von $f: \N \rightarrow \Z \rightarrow \Z \times Z$ konstruieren. Da die Abbildung von $\Z \times \Z \setminus \{0\}$ auf die obigen Äquivalenzklassen, d.h. $\Q$ surjektiv ist, erhalten wir eine surjektive Abbildung von $\N$ nach $\Q$.

```{margin} Georg Cantor
[Georg Ferdinand Ludwig Philipp Cantor](https://de.wikipedia.org/wiki/Georg_Cantor) (\* 3. März 1845greg. in Sankt Petersburg; † 6. Januar 1918 in Halle an der Saale) war ein deutscher Mathematiker.
```

Andererseits ist die Identität von $\N$ nach $\Q$ eine injektive Abbildung. Also erwarten wir, dass es auch eine Bijektion gibt, d.h. $|\Q|=\aleph_0$. Dies liefert das sogenannte erste Cantor'sche Diagonalverfahren:

````{prf:theorem}
Es gibt eine bijektive Abbildung $f: \N \rightarrow \Q$, d.h. $\Q$ ist abzählbar.
````

````{prf:proof}
 Wir konstruieren eine bijektive Abbildung in zwei Schritten. Zuerst verwenden wir die bereits bekannte Bijektion $f_1 : \N \rightarrow \Z$ und konstruieren danach eine Abbildung $f_2: \Z \rightarrow \Q$. Danach definieren wir $f: \N \rightarrow \Q$ als Hintereinanderausführung $f_2 \circ f_1$.
Es genügt $f_2$ auf $\N \setminus \{0\}$ mit Werten in $\Q_+$. Danach definieren wir $f_2(0)=0$ und $f_2(-n)=-f_2(n)$ für alle $n \in \N$ um eine Bijektion von $\Z$ nach $\Q$ zu erhalten. Dazu schreiben wir alle rationalen Zahlen zeilenweise an, in die erste Zeile jene mit Zähler $1$, in die zweite mit Zähler $2$ usw.:

```{math}
{\Large 
\begin{matrix}  
\frac{1}1 & \frac{1}2 & \frac{1}3 & \frac{1}4 & \ldots  \\
& & & &\\
\frac{2}1 & \frac{2}3 & \frac{2}5 & \frac{2}7 & \ldots \\
& & & &\\
\frac{3}1 & \frac{3}2 & \frac{3}4 & \frac{3}5 & \ldots \\
& & & &\\
\frac{4}1 & \frac{4}3 & \frac{4}5 & \frac{4}7 & \ldots \\
& & & &\\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{matrix}}
```

Diese zählen wir mit dem Cantor'schen Diagonalverfahren ab, dies ist analog zur Bijektion von $\N$ nach $\N \times \N$:

```{math}
{\Large 
 \begin{matrix}    
\frac{1}1 & & \frac{1}2 & \rightarrow &\frac{1}3 & &\frac{1}4 & \ldots  \\
\downarrow & \nearrow & & \swarrow  & & \nearrow & & \\
\frac{2}1 & &\frac{2}3 & &\frac{2}5 & &\frac{2}7 & \ldots \\
& \swarrow & & \nearrow&&  \swarrow & & \\
\frac{3}1 & &\frac{3}2 & &\frac{3}4 & &\frac{3}5 & \ldots \\
\downarrow & \nearrow & & \swarrow  & & \nearrow & & \\
\frac{4}1 & &\frac{4}3 & &\frac{4}5 & &\frac{4}7 & \ldots \\
\vdots & &\vdots & &\vdots & & \vdots & \ddots
\end{matrix}}
```

Damit haben wir insgesamt eine Bijektion gefunden, da wir jede Zahl genau einmal nach endlich vielen Schritten erreichen. Also ist $\Q$ abzählbar
````

## Reelle Zahlen

Wir konstruieren im Folgenden die reellen Zahlen und ihre Eigenschaften, indem wir Lücken zwischen den rationalen Zahlen füllen. Solche können wir uns als nichtperiodische Dezimalzahlen mit unendlich vielen Kommastellen vorstellen. Da wir die unendlich vielen Stellen ja nie alle hinschreiben können, haben wir hier einen natürlichen Grenzwertprozess. Wir können uns eine Folge aus Dezimalzahlen mit $n$ Kommastellen vorstellen, wobei $n$ größer wird. Für $n \rightarrow \infty$ erhalten wir dann die reelle Zahl, quasi als Grenzwert. Wir beachten, dass der Unterschied zwischen zwei Versionen einer Dezimalzahl mit $n$ bzw. $m > n$ Stellen betragsmäßig immer kleiner als $10^{-n+1}$ ist, d.h. auf jeden Fall gegen Null konvergiert mit $n \rightarrow \infty$. Dies wird uns auf das Konzept der sogenannten Cauchy-Folgen führen, über die wir reelle Zahlen dann konstruieren. Wir werden auch sehen, dass sehr viele irrationale relle Zahlen gibt, tatsächlich gilt $|\R| > |\Q|$.
Die notwendigkeit der Betrachtung irrationaler Zahlen $x \in \R \setminus \Q$ sehen wir aus der Tatsache, dass wir in den rationalen Zahlen nicht immr eine Wurzel aus einer positiven Zahl ziehen können. Wir sehen dies bereits bei der Quadratwurzel aus $2$, eine Beobachtung der Griechen, der wir hier in einem Beweis von Euklid folgen:

````{prf:theorem}
Es gibt kein $x \in \Q$ mit $x^2 = 2$
````

````{prf:proof}
 Sei $x = \frac{p}q$ mit $(p,q) \in \N \times \N \setminus \{0\}$ (wir können O.B.d.A. annehmen, dass $x$ und damit $p$ positiv ist). Wir können den Repräsentanten als teilerfremd auswählen, d.h. es gibt keine natürliche Zahl, die sowohl $p$ als auch $q$ teilt. Aus $x^2 =2$ folgt $p^2 = 2 q^2$ und dies bedeutet, dass $p^2$ gerade ist. Damit muss natürlich auch $p$ gerade sein, da das Quadrat einer ungeraden Zahl ungerade ist. Also existiert ein $\tilde p \in \N$ mit $p = 2 \tilde p^2$. Setzen wir dies in die obige Identität ein, so folgt

```{math}
 4 \tilde p^2 = 2 q^2 \Rightarrow q^2 = 2 \tilde p^2.
```

Damit können wir mit den gleichen Argumenten wie vorher folgern, dass $q$ gerade ist. Also ist $2$ ein gemeinsamer Teiler von $p$ und $q$, was der Teilerfremdheit widerspricht. Damit kann kein solches $x \in \Q$ existieren.

Die Griechen hatten auch bereits ein iteratives Verfahren zur Annäherung der Quadratwurzel, das sogenannte Heron-Verfahren, in dem man die Folgenglieder nacheinander definiert als

```{math}
 x_{n+1}=\frac{x_n}2 + \frac{1}x_n,
```

mit einem beliebigen Startwert $x_0 \in \Q_+$, z.B. $x_0=1$ oder $x_0=2$. Nehmen wir an es gilt $x_n \rightarrow \overline{x}$, dann gilt natürlich auch $ x_{n+1} \rightarrow \overline{x}$ für $n\rightarrow \infty$ und damit muss gelten

```{math}
 \overline{x}=\frac{\overline{x}}2 + \frac{1}{\overline{x}} \Leftrightarrow \overline{x}^2=2.
```

Die tatsächliche Konvergenz der Folge werden wir später nachweisen.Da bei der Definition des Heron-Verfahrens nur Additionen, Multiplikationen und Divisionen passieren, ist $x_n \in \Q_+$ für alle $n$. Damit erhalten wir tatsächlich Folgen rationaler Zahlen, die gegen $\sqrt{2}$ konvergieren. Wir sehen aber auch die Nichteindeutigkeit, für jeden Anfangswert $x_0$ erhalten wir eine andere Folge mit dem gleichen Grenzwert. Deshalb werden wir besonders darauf achten müssen, dass wir die reellen Zahlen unabhängig von
\subsubsection{Folgen in Körpern}


````{prf:definition}
Sei $\K$ ein archimedisch angeordneter Körper.


* Eine Folge in $\K$ ist eine Abbildung $x: \N \rightarrow \K$, sie wird geschrieben als $(x_n)_{n \in \N}$ bzw.
$(x_0,x_1,\ldots)$.

* Eine Folge $(x_n)$ konvergiert gegen $\overline{x} \in \K$, genau dann wenn
```{math}
 \forall \epsilon \in K, 0 \prec \epsilon ~ \exists n_0 \in \N ~\forall n \geq n_0: |x_n - \overline{x}| \prec \epsilon.
```
 In diesem Fall nennen wir $\overline{x}$ Grenzwert (oder Limes) von $(x_n)$ und schreiben $x_n \rightarrow \overline{x}$ oder $\overline{x}= \lim_{n \rightarrow \infty} x_n. $

Insgesamt nennen wir eine Folge konvergent, wenn es irgendeinen Grenzwert $\overline{x} \in \K$ der Folge gibt.
````

Eine Folge rationaler Zahlen konvergiert gegen $\overline{x} \in \Q$, genau dann wenn in der normalen Ordnung gilt

```{math}
 \forall \epsilon \in K, 0 < \epsilon ~ \exists n_0 \in \N ~\forall n \geq n_0: |x_n - \overline{x}| < \epsilon.
```

Allerdings haben wir mit dieser Definition noch das Problem, dass wir einen Grenzwert in $\Q$ brauchen, wir hätten aber gerne auch Grenzwerte in $\R \setminus \Q$, die wir eigentlich über die Folge definieren. Also brauchen wir eine alternative Definition, die keinen Grenzwert benutzt:

````{prf:definition}
Eine Folge $(x_n) \in \K$ heißt Cauchy-Folge, genau dann wenn

```{math}
 \forall \epsilon \in K, 0 \prec \epsilon ~ \exists n_0 \in \N ~\forall n,m  \geq n_0: |x_n - x_m| \prec \epsilon.
```

````

Wir sehen sofort eine einseitige Beziehung:

````{prf:theorem}
Eine konvergente Folge $(x_n)$ in einem archimedisch angeordneten Körper $\K$ ist eine Cauchy-Folge.
````

````{prf:proof}
Ist $(x_n)$ konvergent, dann existiert für alle $\epsilon \in \K$, $0 \prec \epsilon$ ein $n_0 \in \N$, sodass für alle $n \geq n_0$ gilt:

```{math}
| x_n - \overline{x} | \prec  \epsilon',
```

wobei $\overline{x}$ der Grenzwert der Folge ist und $\epsilon'+\epsilon' \preceq \epsilon$ gilt. Aus der Dreiecksungleichung folgt für $n,m \geq n_0$

```{math}
| x_n - x_m | \preceq  | x_n - \overline{x} |  +  | x_m - \overline{x} | \prec \epsilon,
```

also ist $(x_n)$ Cauchy-Folge.
````

Der folgende Satz liefert uns einige Eigenschaften von Cauchy-Folgen:

````{prf:theorem}
Sei $(x_n)$ eine Cauchy-Folge in einem archimedisch angeordneten Körper $\K$. Dann ist $(x_n)$ beschränkt, d.h. es gibt ein $C \in \K$ mit

```{math}
|x_n| \preceq C \qquad \forall~n \in \N.
```

Ist $(y_n)$ eine weitere Cauchy-Folge in $\K$, dann sind auch $(x_n+y_n)$ und $(x_n y_n)$ Cauchy-Folgen.
````

````{prf:proof}
 Da $(x_n)$ Cauchy-Folge ist, gibt es ein $n_0 \in \N$, sodass für alle $n,m \geq n_0$ gilt

```{math}
 | x_n - x_m | \preceq 1.
```

Damit ist insbesondere für jedes $n \geq n_0$

```{math}
|x_n| \preceq |x_{n_0}| + |x_n - x_{n_0}| \prec |x_{n_0}| +1.
```

Wählen wir nun

```{math}
C = \max_{1 \leq j \leq n_0} |x_j| + 1,
```

dann folgt für alle $n \in \N$: $|x_j| \prec 1$.
Seien nun $(x_n)$ und $(y_n)$ Cauchy-Folgen. Dann existiert zu jedem $\epsilon \in \K$ mit $0 \prec \epsilon$ ein $n_0^1$, sodass

```{math}
|x_n - x_m| \prec \epsilon', \qquad \forall n,m \geq n_0^1
```

und

```{math}
|y_n - y_m| \prec \epsilon' \qquad \forall n,m \geq n_0^2
```

wobei $\epsilon'+\epsilon' \preceq \epsilon$
gilt. Für $n_0 = \max\{n_0^1,n_0^2\}$ gilt

```{math}
|(x_n+y_n) - (x_m+y_m)| \preceq |x_n - x_m| + |y_n - y_m| \prec {\epsilon} , \qquad \forall n,m \geq n_0.
```

Zum Beweis der Eigenschaft für das Produkt verwenden wir
\begin{align*}
|x_n y_n| &= | x_n(y_n -y_m) + y_m (x_n - x_m) | \\&\leq |x_n| ~|y_n - y_m| + |y_m|~|x_n - x_m|.\end{align*}
Nach dem ersten Teil des Satzes sind die Cauchy-Folgen $(x_n)$ und $(y_n)$ beschränkt. Ist $C$ das Maximum der Schranken und $n_0$ hinreichend groß, dann gilt für $n,m \geq n_0

```{math}
$ |x_n| \preceq C, \quad |y_n| \preceq C, \quad |x_n - x_m| \prec \frac{\epsilon'}{C}, \qquad|y_n - y_m| \prec \frac{\epsilon'}{C},
```

und daraus folgt$ |x_n y_n - x_m y_m | \preceq \epsilon.~\square $
````

### Konstruktion reeller Zahlen

Nun beginnen wir die reellen Zahlen zu konstruieren ohne explizit den Grenzwert anzugeben. Dazu wollen wir reelle Folgen mit rationalen Cauchy-Folgen identifizieren. Für die Teilmenge der rationalen Zahlen ist dies einfach, dazu können wir z.b. jedes $q \in \Q$ mit der konstanten Folge $x_n = q$ für alle $n \in \N$ identifizieren. Für irrationale Zahlen können wir uns die Dezimaldarstellung vorstellen, der Einfachheit halber für $0\leq x <1$:

```{math}
x = 0,a_1a_2a_3 \ldots  \quad \text{ bzw. } x=\sum_{j=1}^\infty a_j 10^{-j}
```

wobei die Ziffern $a_i \in \{0,1,\ldots,9\}$ erfüllen. Ist $x$ nicht rational, dann ist die Darstellung weder endlich noch periodisch, d.h. wir werden es nie schaffen diese vollständig hinzuschreiben, wir können uns nur darauf beschränken, die ersten $n$ Dezimalstellen anzugeben. Damit konstruieren wir automatisch eine Folge

```{math}
x_n = 0,a_1a_2a_3 \ldots  \quad \text{ bzw. } x_n=\sum_{j=1}^n a_j 10^{-j} .
```

Wir sehen f\"ur $m \geq n$, dass

```{math}
|x_m -x_n| = | \sum_{j=n+1}^m a_j 10^{-j}| < 10^{-n}
```

gilt. Damit ist $(x_n)$ natürlich Cauchy-Folge in $\Q$, denn für jedes $\epsilon \in \Q_+$ gibt es ein $n_0$ mit
$10^{-n_0} < \epsilon $ und damit ist auch $10^{-n} < \epsilon$ für $n \geq n_0$.
Nun haben wir noch das Problem, dass wir nicht direkt reelle Zahlen mit Cauchy-Folgen identifizieren können, da es mehrere Folgen mit dem gleichen Grenzwert gegen kann. Dies sehen wir etwa bei $\sqrt{2}$, wenn wir Folgen aus dem Heron-Verfahren mit unterschiedlichen Startwerten betrachten oder sogar für eine reelle Zahl $q$. Dort können wir etwa $x_n=q$ oder $\tilde x_n = q +\frac{1}n$ betrachten, die beide gegen $q$ konvergieren. Um diese Nichteindeutigkeit zu beheben, müssen wir wieder eine geeignete Äquivalenzrelation einführen und bezüglich dieser faktorisieren.

````{prf:definition}
Eine Folge mit Grenzwert $\overline{x}=0$ nennen wir Nullfolge. Dazu nennen wir

```{math}
 {\cal F} = \{ (x_n): \N \rightarrow \Q~|~(x_n) \text{ ist Cauchy-Folge.}\}
```

````

Auf ${\cal F}$ definieren wir eine Äquivalenzrelation

```{math}
 (x_n) \sim (y_n) : \Leftrightarrow (x_n-y_n) \text{ ist Nullfolge. }
```

Die Reflexivität ist klar, da $(x_n-x_n)$ die konstante Folge null ist, die Symmetrie folgt aus $|x_n-y_n|=|y_n-x_n|$ eingesetzt in die Konvergenzbedingung. Die Transitivität erhalten wir wieder mit der Dreiecksungleichung

```{math}
 0 \leq  |x_n - z_n| \leq |x_n-y_n| + |y_n - z_n|.
```

````{prf:definition}
Mit der obigen Definition von ${\cal F}$ und $\sim$ definieren wir die reellen Zahlen als $\R = {\cal F}/\sim$, d.h. als Äquivalenzklassen rationaler Cauchy-Folgen.
Addition und Multiplikation auf $\R$ sind definiert durch
\begin{align*}
[(x_n)] + [(y_n)] &:= [(x_n+y_n)] \\
[(x_n)] ~ [(y_n)] &:= [(x_n~y_n)]\end{align*}
````

Man prüft leicht nach, dass die Addition und Multiplikation wohldefiniert sind, also unabhängig von den Repräsentatnen ausgeführt werden können. Wir wollen nun auch noch eine Ordnungsrelation auf $\R$ einführen, die natürlich auf dem Vergleich der Folgen basieren muss. Dabei können wir Positivität aber nicht einfach durch die Bedingung $0 < x_n$ für alle $n \in \N$ oder für $n \geq n_0$ fordern, da es auch Folgen wie $\frac{1}n$ gibt, die diese Bedingung erfüllen aber gegen $0$ konvergieren.  Um dies zu verhindern definieren wir

```{math}
 0 < [(x_n)]:\Leftrightarrow \exists \epsilon > 0~\forall (\tilde x_n) \in [(x_n)]~\exists n_0 \in \N ~\forall n\geq n_0: \tilde x_n > \epsilon.
```

Wir beachten, dass dabei $n_0$, aber nicht $\epsilon$ vom Repräsentanten abhängen darf. Diese Definition erweitern wir wie üblich auf $\leq$, indem wir schreiben

```{math}
0 \leq  [(x_n)]:\Leftrightarrow 0 < [(x_n)] \text{ oder } 0 = [(x_n)].
```

Die Relation ist dann definiert als

```{math}
[(x_n)] \leq [(y_n)] : \Leftrightarrow 0 \leq [(y_n-x_n)].
```

Wir weisen noch kurz die Eigenschaften einer Ordnungsrelation nach:

* _Reflexivität_ ist trivial, da wir die Gleichheit ja explizit in der Definition berücksichtigt haben.

* _Antisymmetrie:_ Sei $[(x_n)] < [(y_n)]$, dann gilt für alle Repräsentanten $(\tilde x_n) \in [(x_n)]$ und
$(\tilde y_n) \in [(y_n)]$;

```{math}
\exists \epsilon > 0~\exists n_0 \in \N~\forall n \geq n_0: \tilde y_n - \tilde x_n > \epsilon.
```

Damit kann nicht $\tilde x_n - \tilde y_n > \tilde \epsilon$ gelten für $\tilde \epsilon >0$ und $n \geq n_0$. Da $\tilde x_n - \tilde y_n$ keine Nullfolge ist, gilt nicht $(y_n) \leq (x_n)$.

* _Transitivität:_ Sei $[(x_n)] \leq [(y_n)]$ und $[(y_n)] \leq [(z_n)]$. Dann unterscheiden wir zunächst $[(x_n)]=[(y_n)]$ und $[(x_n)]< [(y_n)]$. Im ersten Fall ist $[(x_n)] \leq [(z_n)]$ trivial, also betrachten wir den zweiten. Genauso können wir eine Fallunterscheidung bei $[(y_n)]$ und $[(z_n)]$ machen und müssen nur den nichttrivialen Fall $[(y_n)]<[(z_n)]$ betrachten. Hier können wir $\epsilon_1$ und $\epsilon_2$ finden, sodass für $n\geq n_0^1$

```{math}
\tilde y_n - \tilde x_n > \epsilon_1
```

und für $n\geq n_0^2$

```{math}
\tilde z_n - \tilde y_n > \epsilon_2
```

gilt. Mit $n_0=\max\{n_0^1,n_0^2\}$ und $\epsilon = \epsilon_1 + \epsilon_2$ erhalten wir die gewünschte Eigenschaft

```{math}
\tilde z_n - \tilde x_n > \epsilon, \qquad \forall n \geq n_0.
```

Man prüft leicht nach, dass die Grundrechenarten auf $\R$ mit der Ordnung verträglich sind und dass $\R$ ein archimedisch angeordneter Körper ist. Die Anordnung von $\R$ und die Beziehung zu den natürlichen Zahlen erlaubt es uns auch zu runden:

````{prf:lemma}
Für alle $x \in \R$ existiert genau ein $m\in \Z$ mit

```{math}
 m-1 \leq x < m .
```

Analog gibt es genau ein genau $n \in \Z$ mit $n-1 < x \leq n$
````

````{prf:proof}
Sei $x \in \R$. Wegen der archimedischen Anordnung existiert ein $n_1 \in \N$ mit $x < n_1$ und $n_2 \in \N$ mit $-x < n_2$. Wir betrachten die nichtleeren Mengen

```{math}
M_1 = \{ z \in \Z~|~ x < z\}, \qquad M_2 = \{ z \in \Z~|~ z \leq x\}.
```

Diese sind disjunkt und es gilt $\Z = M_1 \cup M_2$. Ist $z \in M_1$, dann ist auch $z+1 \in M_1$. Damit gibt es wegen der Anordnung nur ein $m \in M_1$ mit $m-1 \notin M_1$. Wegen $\Z = M_1 \cup M_2$ gilt also $m-1 \in M_1$, damit folgt $  m-1 \leq x < m . \square$
````

Eine interessante Eigenschaft ist auch das Wachstum der Exponentialfunktion. Dazu benötigen wir zunächst ein Hilfsresultat, die sogenannte Bernoulli-Ungleichung

````{prf:lemma}
Für $x \in \R$, $x \geq -1$ und $n\in \N$ gilt

```{math}
 (1+x)^n \geq 1 + n x.
```

````

````{prf:proof} Wir können den Beweis per vollständiger Induktion führen. Der Anfang bei $n=0$ liefert $1 \geq 1$, ist also wahr. Nun nehmen wir an $(1+x)^n \geq 1 + n x$ und setzen dies ein in

```{math}
 (1+x)^{n+1} = (1+x)^n (1+x) \geq (1+nx)(1+x) = 1+ (n+1)x +x^2.
 
```

Wegen der Nichtnegativität von $x^2$ folgt die Aussage auch für $n+1$ und damit haben wir die Ungleichung für alle $n\in \N$ bewiesen.
````

````{prf:lemma}
Sei $x \in \R$, $x  > 1$ und $m\in \N$. Dann gibt es ein $\ell \in \N$ mit

```{math}
x^\ell \geq m.
```

````

````{prf:proof}
 Für $m=0$ und $m=1$ erfüllt offensichtlich $\ell=1$ die Ungleichung. Für $m > 1$ schreiben wir $x=1+y$, $y > 0$ und setzen $l \geq \frac{m-1}y$. Aus der Bernoulli-Ungleichung folgt nun:

```{math}
x^\ell =(1+y)^\ell \geq 1+ \ell y \geq 1+  \frac{m-1}y y = m,
```

also gilt die Aussage
````

### Vollständigkeit

Die reellen Zahlen $\R$ sind ein Körper, also können wir wieder Cauchy-Folgen in $\R$ betrachten. Nun stellt sich die Frage, ob $\R$ vollständig ist, d.h. ob alle Cauchy-Folgen konvergieren. Dazu stellen wir zunächst Zusammenhänge zwischen den reellen und den ganzen Zahlen her. Zunächst sehen wir, dass Cauchy-Folgen in $\Q$ auch Cauchy-Folgen in $\R$ sind, indem wir $\epsilon \in \R_+$ durch $\epsilon' \in \Q$ ersetzen können. Ist $\epsilon \in \R$, $\epsilon \geq 1$, so können wir $n,m$ so wählen, dass

```{math}
|x_n -x_m| < 1 \leq \epsilon
```

gilt. Ist $\epsilon < 1$, dann können wir $k \in \N$ wählen, indem wir $\frac{1}\epsilon$ aufrunden und damit ist
$\frac{1}k \leq \epsilon$. Nun können wir $n,m$ so wählen, dass

```{math}
|x_n -x_m| < \frac{1}k \leq \epsilon.
```

Um nich immer explizit die Eigenschaft einer Cauchy-Folge nachweisen zu müssen, verwenden wir folgendes einfache Resultat:

````{prf:lemma}
Sei $(y_n)$ eine Nullfolge in $\R$ und für ein $C \in \R_+$ gelte
```{math}
\forall m,n \in \N, m \geq n: |x_m-x_n| \leq C y_n.
```

Dann ist $(x_n)$ Cauchy-Folge
````

````{prf:proof}
 Da $(y_n)$ eine Nullfolge ist, existiert für jedes $\epsilon > 0$ ein $n_0 \in N$, sodass für alle $n \geq n_0$ gilt $y_n \leq |y_n| < \frac{\epsilon}C$. Damit folgt sofort für $m \geq n \geq n_0$

```{math}
|x_m-x_n| \leq C y_n < \epsilon,
```

d.h. $(x_n)$ ist Cauchy-Folge
````

````{prf:lemma}
Für jedes $x \in \R$ und $\epsilon \in \R_+$ existiert ein ein $q \in \Q$ mit $|x-q|<\epsilon$
````

````{prf:proof}
 Sei $k$ wie oben mit $\frac{1}k \leq \epsilon$. Da $x$ der Grenzwert einer Cauchy-Folge $(r_n)$ in $\Q$ ist, gibt es ein $n_0 \in \N$ mit

```{math}
|r_n - r_m| < \frac{1}{2k} \leq \frac{\epsilon}2,
```

für alle $m,n \geq n_0$. Wählen wir nun $q=r_{n_0}$ und betrachten die konstante Folge $(q)$, dann gilt
```{math}
|r_n - q| <  \frac{\epsilon}2,
```

für alle $n \geq n_0$. Sei nun $(\tilde r_n)$ ein anderer Repräsentant von $x$, dann ist $(r_n - \tilde r_n)$ Nullfolge, d.h. es gibt ein $\tilde n_0$ mit

```{math}
|r_n - \tilde r_n|   < \frac{1}{2k} \leq \frac{\epsilon}2,
```

für $n \geq \tilde n_0$. Damit gilt für $n\geq \max\{n_0,\tilde n_0\}$ auch

```{math}
|q-\tilde r_n| \leq |q -r_n|+|r_n - \tilde r_n| < \epsilon,
```

d.h. $|q-x| < \epsilon$.

````

Damit können wir die Vollständigkeit von $\R$ nachweisen.

````{prf:theorem}
$\R$ ist vollständig, d.h. jede Cauchy-Folge $(x_n)$ in $\R$ ist konvergent
````

````{prf:proof}
 Zu jedem Folgenelement $x_n \in \R$ gibt es ein $q_n \in \Q$ mit

```{math}
|x_n-q_n| < \frac{1}n.
```

Sei nun $\epsilon > 0$, dann gibt es ein $n_0$, sodass für alle $n,m \geq n_0$ gilt

```{math}
|x_n - x_m| < \frac{\epsilon}3.
```

Sei darüber hinaus $n_0$ so groß gewählt, dass $\frac{1}{n_0} < \frac{\epsilon}3$ gilt. Dann folgt

```{math}
|q_n - q_m| \leq |q_n - x_n| + |x_n - x_m| + |x_m-q_m| <\epsilon,
```

d.h. $(q_n)$ ist Cauchy-Folge in $\Q$ und da $(x_n -q_n)$ eine Nullfolge ist, folgt

```{math}
 x=\lim_n q_n = \lim_n x_n
```

und damit ist $x_n$ konvergent.
````

Mit Hilfe der Vollständigkeit können wir nun Grenzwerte in $\R$ definieren, indem wir nachweisen, dass Folgen Cauchy-Folgen sind. Als Anwendung betrachten wir die Exponentialfunktion:

````{prf:example}
Sei $x \in \R$. Wir definieren
```{math}
 e^x = \sum_{k=0}^\infty \frac{x^k}{k!} = \lim_{n \rightarrow \infty} \sum_{k=0}^n \frac{x^k}{k!},
```

wobei $k! = \prod_{i=1}^k i$. Sei
```{math}
y_n = \sum_{k=0}^n \frac{x^k}{k!}
```

und wählen wir $m \geq n$. Dann ist

```{math}
|y_n - y_m| \leq \sum_{k=n+1}^m \frac{|x|^k}{k!}.
```

Sei $n_0 \in \N$ so, dass $n_0 > 2{|x|} $, dann gilt
\begin{align*}
\sum_{k=n+1}^m \frac{|x|^k}{k!} &= \frac{|x|^{n_0}}{n_0!} \sum_{k=n+1}^m \frac{|x|^{k-n_0}}{(n_0+1)\ldots k} \\
&\leq \frac{|x|^{n_0}}{n_0!} \sum_{k=n+1}^m \left(\frac{1}2\right)^{k-n_0} \\
&= \frac{|2x|^{n_0}}{n_0!} \sum_{k=n+1}^m \left(\frac{1}2\right)^{k} \\
&= \frac{|2x|^{n_0}}{n_0!} \left(\frac{1}2\right)^{n+1} \sum_{k=0}^{m-n-1} \left(\frac{1}2\right)^{k} \\
&= \frac{|2x|^{n_0}}{n_0!} \left(\frac{1}2\right)^{n+1} \frac{1-\left(\frac{1}2\right)^{m-n-1}}{\frac{1}2} \\
&\leq \frac{|2x|^{n_0}}{n_0!} \left(\frac{1}2\right)^{n},
\end{align*}
Da der letzte Term gegen Null konvergiert, können wir $m,n$ so groß wählen, dass er beliebig klein wird. Also ist $y_n$ eine Cauchy-Folge.
````

Wir betrachten nun noch die Mächtigkeit von $\R$:

````{prf:theorem}
Es gilt $|\R| > |\N|$, d.h. $\R$ ist nicht abzählbar
````

````{prf:proof}
  Es genügt zu zeigen, dass
```{math}
I=[0,1) = \{ x \in \R~|~0 \leq x < 1\}
```

nicht abzählbar ist. Wir können$x \in I$ in Dezimaldarstellung $0,a_1a_2 \ldots$ schreiben, indem wir iterativ abrunden:

```{math}
a_1 = \lfloor 10 x \rfloor, \quad a_{i+1} = \lfloor 10^{i+1}(x-\sum_{j=0}^i a_j 10^{-j})\rfloor.
```


Nehmen wir an, es gäbe eine surjektive Abbildung $f: \N \rightarrow [0,1)$. Dann schreiben wir die Dezimaldarstellung für den Wertebereich als

```{math}
f(\ell) = 0,a_1^\ell a_2^\ell \ldots
```

mit $a_i^\ell \in \{0,1,\ldots,9\}$. Nun definieren wir

```{math}
x=0,b_1 b_2 \ldots
```

mit $b_i \in \{1,\ldots,8\}$ so, dass $|b_i - n_i^i| \geq 2$. Damit folgt $|x-f(\ell)|\geq 10^{-\ell}$, also insbesondere $x \neq f(\ell)$ für alle $\ell \in \N$. Damit kann $f$ nicht surjektiv sein und $\R$ nicht abzählbar
````

Wir sehen also, dass die Mächtigkeit von $\R$ eine größere Art von Unendlich ist als die Mächtigkeit von $\N$, dies gilt auch für die irrationalen Zahlen im Vergleich zu den rationalen. Wir definieren diese deshalb als zweite Kardinalzahl $|\R|= \aleph_1$.

## Infima und Suprema

Intuitiv würden wir gerne von einem größten und kleinsten Element einer Menge (Maximum bzw. Minimum) sprechen, wenn wir eine vollständige Ordnung haben. Dies ist aber nicht immer gegeben, wie eine Betrachtung verschiedener Intervalle in $\R$ zeigt. Für $a,b \in \R$ mit $a < b$ definieren wir
\begin{align*}
[a,b] &:= \{x \in \R~|~a \leq x \leq b\} \\
(a,b) &:= \{x \in \R~|~a < x < b\} \\
[a,b) &:= \{x \in \R~|~a \leq x < b\} \\
(a,b] &:= \{x \in \R~|~a < x \leq b\}.
\end{align*}
Wir nennen $[a,b]$ geschlossenes Intervall, $(a,b)$ offenes Intervall und die anderen beiden halboffene Intervalle. Das geschlossene Intervall hat ein Maximum ($b$) und ein Minimum ($a$), das offene Intervall aber nicht, denn einerseits existiert für jedes $\epsilon > 0$ ein $x \in \R$ mit $x>b-\epsilon$, also müsste ein Maximum größer gleich $b$ sein. Alle reellen Zahlen größer gleich $b$ liegen aber nicht in $(a,b)$. In einem solchen Fall werden wir $b$ ein Supremum nennen (und analog $a$ ein Infimum), dies führt auf die folgende Definition:

````{prf:definition}
Sei $K$ eine Menge mit Ordnungsrelation $\preceq$ und $M \subset K$.

* $z \in K$ heisst obere Schranke für $M$, wenn für alle $x \in M$ gilt: $x \preceq z$.

* $z \in K$ heisst untere Schranke für $M$, wenn für alle $x \in M$ gilt: $z \preceq x$.

* $M$ heisst nach oben / unten beschränkt, wenn eine obere / untere Schranke existiert. $M$ heisst beschränkt, wenn sie nach oben und unten beschränkt ist.* Eine obere Schranke $s \in K$ heisst Supremum, wenn für alle anderen oberen Schranken $z$ gilt $s \preceq z$.

* Eine untere Schranke $i \in K$ heisst Infimum, wenn für alle anderen unteren Schranken $z$ gilt $z \preceq i$.

````

Wir wenden dies nun auf die reellen Zahlen an:

````{prf:theorem}
$M \subset \R$ ist beschränkt genau dann wenn es ein $g \in \R_+$ gibt, sodass für alle $x \in M$ gilt: $|x|\leq g$.Ist $M \neq \emptyset$ und $M$ nach oben und unten beschränkt, dann besitzt $M$ ein Supremum und ein Infimum. Diese sind jeweils eindeutig.
````

````{prf:proof}
 Zunächst sehen wir, dass für beschränkte Mengen in $\R$ Schranken $a,b \in \R$ existieren, mit $a \leq x  \leq b$ für alle $x \in M$. Nun wählen wir $g=\max\{|a|,|b|\}$ und erhalten $|x|\leq g$. Umgekehrt können wir im Fall $|x|\leq g$ für alle $x \in M$ einfach $g$ als obere und $-g$ als untere Schranke wählen.

Um ein Supremum zu konstruieren beginnen wir mit $m_0 \in M$ und einer oberen Schranke $s_0 \in \R$. Nun definieren wir iterativ zunächst $x_i=\frac{m_i+s_i}2$. Ist $x_i$ obere Schranke, dann setzen wir $s_{i+1}=x_i$ und $m_{i+1}=m_i$. Andernfalls setzen wir $m_{i+1}=x_i, s_{i+1}=s_i$. In beiden Fällen ist $M \cap [m_{i+1},s_{i+1}] \neq \emptyset$. Wir sehen auch

```{math}
|s_{i+1} - m_{i+1}| = \frac{1}2 |s_i - m_i|
```

und daraus folgt
```{math}
|s_n - m_n| = \frac{1}{2^n} |s_0-m_0|,
```

also ist $(s_n-m_n)$ ein Nullfolge. Darüber hinaus sehen wir
```{math}
 |s_{i+1}-s_i| \leq \frac{1}2 |s_i - m_i|  = \frac{1}{2^{i+1}} |s_0-m_0|
```

und erhalten für $m\geq n$

```{math}
 |s_m - s_n| = |\sum_{i=n}^{m-1} s_{i+1}-s_i| \leq \sum_{i=n}^{m-1} |s_{i+1}-s_i| \leq  \sum_{i=n}^{m-1}\frac{1}{2^{i+1}} |s_0-m_0| = \frac{1}{2^{n+1}}  |s_0-m_0| \sum_{i=0}^{m-n-1}\frac{1}{2^{i}} \leq \frac{1}{2^{n}}  |s_0-m_0|.
```

Also ist $(s_n)$ eine Cauchy-Folge und analog zeigen wir, dass auch $(m_n)$ eine Cauchy-Folge ist. Da jede Cauchy-Folge in $\R$ konvergiert gibt es einen Grenzwert $s$, der für beide Folgen gleich ist. Aus der Konstruktion sehen, wir dass $s_n$ für jedes $n$ eine obere Schranke ist. Nehmen wir an, dass es ein $m \in M$ gibt mit $m > s$, dann ist $m=s+\epsilon$ für ein $\epsilon > 0$. Andererseits existiert $n_0$ mit $|s-s_{n_0}|< \epsilon$ und damit$s_{n_0} < s + \epsilon = m$. Dies ist ein Widerspruch dazu, dass $s_{n_0}$ eine obere Schranke ist, also $m \leq s_{n_0}$. Damit ist $s$ eine obere Schranke und es kann keine kleinere obere Schranke geben, da es für jedes $\epsilon > 0$ ein $m \in M$ mit $m > s-\epsilon$ gibt. Also ist $s$ ein Supremum. Ist $s'$ ein weiteres Supremum, dann gilt $s \leq s'$ und $s' \leq s$, also $s=s'$. Die Existenz und Eindeutigkeit eines Infimums folgt analog
````

Für unbeschränkte Mengen gibt es nicht unbedingt ein Infimum oder Supremum. Wir können dies erzwingen indem wir $\R$ erweitern zu

```{math}
 \overline{\R} = \R \cup \{+\infty,-\infty\},
```

wobei wir $\pm \infty$ so definieren, dass

```{math}
 \forall x\in \R \cup \{+\infty\} : - \infty < x
```

und

```{math}
 \forall x\in \R \cup \{+\infty\} : x < \infty 
```

gilt.

## Komplexe Zahlen

In $\R$ können wir die Quadratwurzel einer positiven Zahl ziehen, nicht aber aus einer negativen. Dies bedeutet, dass nicht jede quadratische Gleichung eine Lösung hat, z.B.

```{math}
 x^2 +1 = 0
```

ist nicht in $\R$ lösbar. Allgemeiner gibt es viele algebraische Gleichungen, d.h. Gleichungen der Form

```{math}
 \sum_{j=0}^n a_j x^j = 0,
```

die nicht lösbar sind oder äquivalent hat nicht jedes nichtkonstante Polynom eine Nullstelle in $\R$. Um dies zu beheben führen wir eine imaginäre Zahl $\i$ ein, sodass

```{math}
 \i^2 = (-\i)^2 = -1
```

gilt. Dann können wir auch reelle Zahlen zu $\i$ addieren oder reelle Vielfache von $\i$ betrachten, z.B. sollte gelten $(2\i)^2=-4$. Also erhalten wir komplexe Zahlen in der Form

```{math}
 z = a + b \i, \qquad a, b \in \R.
```

Wir nennen $a$ den Realteil und $b$ den Imaginärteil, sehen also, dass im wesentlichen die komplexen Zahlen dem $\R^2 = \R \times \R$ entsprechen.
Für die Addition und Multiplikation verwenden wir Assoziativität, Distributivität und Kommutativität, damit ist

```{math}
 z_1+z_2 = (a_1+a_2) + (b_1+b_2)\i,
```

und

```{math}
 z_1 ~z_2 = a_1 a_2 + a_1 b_2 \i + a_2 b_1 \i + b_1 b_2 \i^2 = (a_1 a_2 - b_1 b_2) + ( a_1 b_2   + a_2 b_1) \i .
```

Dies führt auf die Definition der komplexen Zahlen als $\C = \R \times \R$ mit den Rechenregeln

```{math}
 (a_1,b_1) +(a_2,b_2) := (a_1+a_2,b_1+b_2)
```

und

```{math}
 (a_1,b_1) ~(a_2,b_2) := (a_1 a_2 - b_1 b_2,a_1 b_2   + a_2 b_1).
```

Damit erhalten wir:

````{prf:theorem}
Die komplexen Zahlen $\C$ sind ein Körper
````

````{prf:proof}
 Zunächst sehen wir sofort, dass $(\C,+)$ eine abel'sche Gruppe mit neutralem Element $(0,0)$ und zu $(a,b)$ inversem Element $(-a,-b)$ bildet. Darüber hinaus sehen wir, das $(\C,\cdot)$ eine abel'sche Gruppe mit Einselement $(1,0)$ und zu $(a,b)$ inversem Element $(\frac{a}{a^2+b^2},  \frac{-b}{a^2+b^2}) $ bildet. Das Assoziativ- und Distributivgesetz kann man direkt mit den entsprechenden Gesetzen für die Multiplikation in $\R$ nachrechnen
````

Mit der Abbildung $x \in \R \mapsto (x,0) \in \C$ haben wir eine kanonische Einbettung der reellen Zahlen in $\C$. Wir schreiben dann allgemein wieder $z=a+b\i$ und sagen $z \in\R$ wenn der Imaginärteil $b=0$ ist.  Die imaginäre Zahl $\i$ können wir also mit $(0,1)$ identifizieren.  Wir schreiben auch $a=$Re$(z)$ und $b=$Im$(z)$. Wir definieren den Betrag einer komplexen Zahl als

```{math}
 |z| := \sqrt{a^2+b^2}
```

und die konjugierte Zahl als

```{math}
 \overline{z} := a - b \i.
```

Als Beispiel betrachen wir $z= 4+3\i$, dann ist $|z|=5$ und $\overline{z}=4-3\i$.

Den folgenden Satz geben wir ohne seinen (einfachen) Beweis an:

````{prf:theorem}
Sei $z \in \C $, dann gilt:

```{math}
  |z| \geq 0\quad \text{ und } |z|=\sqrt{z \overline{z}}\1
```

darüber hinaus ist $|z|=0$ genau dann wenn $z=0$ gilt.Sind $x,y \in \C$, dann gilt

```{math}
 |xy|=|x|~|y|,\qquad |x+y| \leq |x|+|y| .
```

````

Ist $y \in \C$ und $n\in \N\setminus\{0,1\}$, dann heisst $x \in \C$ die $n$-te Wurzel von $y$, wenn $y=x^n$ gilt.Eine Wurzel ist eine Nullstelle des Polynoms $p:\C \rightarrow \C, x \mapsto x^n-y$. Eine solche Wurzel existiert immer in $\C$, allgemeiner gilt der _Hauptsatz der Algebra_ (hier ohne Beweis):

````{prf:theorem}
Jedes Polynom```{math}
p: \C \mapsto \C, x \mapsto \sum_{j=0}^n a_j x^j
```

mit $n \in \N\setminus\{0\}$, $a_j \in \C$, $a_n \neq 0$ hat eine komplexe Nullstelle, d.h. es existiert ein $\overline{x} \in \C$ mit $p(\overline{x})=0$
````

````{prf:example}
Das quadratische Polynom $p(x) =x^2+1$ hat die Nullstellen $\i$ und $-\i$
````

````{prf:example}
Das kubische Polynom $p(x) =x^3+1$ hat die Nullstellen $-1$, $\frac{-1+\sqrt{3}\i}2$ und $\frac{-1-\sqrt{3}\i}2$
````

In den Beispielen sehen wir, dass zu jeder Nullstelle auch die konjugierte Zahl Nullstelle ist. Dies gilt allgemein für komplexe Polynome: ist $z \in \C$ Nullstelle, dann ist auch $\overline{z}$ eine Nullstelle.
