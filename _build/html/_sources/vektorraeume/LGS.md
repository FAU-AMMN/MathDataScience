# Lineare Gleichungssysteme

Im Folgenden werden wir uns mit linearen Gleichungssystemen der Form

```{math}
\begin{matrix}
a_{11} x_1 &+& a_{12}x_2 &+& \ldots &+& a_{1n}x_n &=& y_1 \\
a_{21} x_1 &+& a_{22}x_2 &+& \ldots &+& a_{2n}x_n &=& y_2 \\
\vdots &&  \vdots && \ddots && \vdots && \vdots \\
a_{m1} x_1 &+& a_{m2}x_2 &+& \ldots &+& a_{mn}x_n &=& y_m
\end{matrix}
```

mit $m,n \in \N$, $a_{ij} \in \R$ und $y_i \in \R$. Die Unbekannten sind dabei $x_i \in \R$. Schreiben wir die $x_i$ und $y_i$ jeweils wieder in einen Spaltenvektor $x$ bzw. $y$ und die $a_{ij}$ in eine Matrix $A \in \R^{m \times n}$, so erhalten wir die kürzere Matrixform

```{math}
 A x = y .
```

Ist $m=n=1$, so können wir einfach durch $A$ dividieren um die Gleichung zu lösen, für größere $m$ und $n$ benötigen wir eine Verallgemeinerung dieses Vorgangs.
Wir wissen schon, dass die Lösung nur dann eindeutig ist, wenn das homogene System $A x = 0$ nur die eindeutige Lösung $x=0$ hat. Ist dies nicht der Fall, dann nennen wir

```{math}
 {\cal N}(A) = \{ x \in \R^n ~|~ Ax = 0 \}
```

den Nullraum der Matrix $A$ (analog definieren wir den Nullraum einer linearen Abbildung). Wegen der Linearität prüft man leicht nach, dass ${\cal N}(A)$ ein Unterraum des $\R^n$ ist. Wir nennen

```{math}
 \text{Rg}(A) := n - \text{dim}({\cal N}(A))
```

den Rang der Matrix $A$. Dazu definieren wir den Range (oder auch das Bild) von $A$ als

```{math}
 {\cal R}(A) = \{ y \in \R^m~|~\exists x \in \R^N: y = Ax\}.
```

````{prf:example}
Die Matrix

```{math}
 A = \left(\begin{matrix} 1 & 2 & 1 \\ 1 & 0 & 0  \\ 2 & 2 & 1  \end{matrix} \right)
```

hat den Nullraum

```{math}
 {\cal N}(A) = \{ x \in \R^3 ~|~x_1=0, x_3= -x_2\} =\{ \left(\begin{matrix} 0 \\ t  \\ -t  \end{matrix} \right) ~|~ t \in \R\}
```

und den Range

```{math}
 {\cal R}(A) = \{ y \in \R^3~|~y_3 = y_1 + y_2\}=\{ \left(\begin{matrix} s \\ t  \\ s+t  \end{matrix} \right) ~|~ s,t \in \R\}
```

Hier ist der Rang zwei, dies ist gleich der Dimension von ${\cal R}(A)$.
````

````{prf:lemma}
Sei dim$(V)=n$ und für $k < n$ sei $\{b_1,\ldots,b_k\}$ eine linear unabhängige Menge. Dann existieren $b_{k+1}, \ldots, b_n$, sodass $\{b_1,\ldots,b_n\}$ eine Basis von $V$ ist.
````

````{prf:proof}
 Wir wählen nacheiander $b_{j+1} \in $ lin$(\{b_1,\ldots,b_j\})$ für $j=k,\ldots,n-1$ und sehen dann$ \{b_1,\ldots,b_j,b_{j+1} \}$ ist linear unabhängig. Für $j=n-1$ sind wir dann bei einer Basis von $V$ angekommen. 
````

````{prf:lemma}
Sei $A \in \R^{m \times n}$. Dann gilt Rg$(A)=$dim $({\cal R}(A))$.
````

````{prf:proof}
 Sei $k=$dim$({\cal N}(A))$ und $\{b_1,\ldots,b_k\}$ eine Basis von ${\cal N}(A)$. Dann können wir nach dem obigen Lemma zu einer Basis $\{b_1,\ldots,b_n\}$ erweitern. Nun sehen wir, dass $\{Ab_{k+1},\ldots,Ab_n\}$ ein Erzeugendensystem für ${\cal R}(A)$. Andererseits sehen wir auch, dass $\{Ab_{k+1},\ldots,Ab_n\}$ linear unabhängig ist. Nehmen wir an es gibt $\lambda_i \in \R$ mit

```{math}
 0 = \sum_{i=k+1}^n \lambda_i A b_i = A(\sum_{i=k+1}^n \lambda_i b_i).
```

Da per Konstruktion $\sum_{i=k+1}^n \lambda_i b_i$ nur dann im Nullraum von A liegt, falls $\sum_{i=k+1}^n \lambda_i b_i = 0$ ist, folgt $\lambda_i=0$  wegen der linearen Unabhängigkeit der $b_i$.
Damit ist $n-k=$Rg$(A)=$dim$({\cal R}(A))$. 
````

Wir sehen, dass der Rang angibt wie groß der Raum möglichen $y$ ist, für die $Ax = y$ lösbar ist. Andererseits gibt uns der Rang auch Information über die mögliche Anzahl der Lösungen, wenn das Problem lösbar ist. Grundlage dafür ist folgendes Resultat:

````{prf:lemma}
Sei $x_0 \in \R^n$ eine Lösung von $A x = y$. Dann ist die Menge aller Lösungen gegeben durch

```{math}
 x_0 + {\cal N}(A) = \{ x \in \R^n ~|~x=x_0+z, z \in {\cal N}(A)\}.
```

````

````{prf:proof}
 Sei $x_0$ eine Lösung, dann gilt für $z \in {\cal N}(A)$ auch

```{math}
 A(x_0+z) = Ax_0  + A_z =y,
```

also ist $x_0 + z$ Lösung. Ist umgekehrt $x$ eine weitere Lösung neben $x_0$, dann gilt

```{math}
 A(x-x_0)  = Ax - Ax_0= y - y=0,
```

also ist $x \in x_0 + {\cal N}(A)$. 
````

Allgemein nennen wir für einen Teilraum $U \subset V$ und $x \in V$ die Menge  $M= x + U$ eine _lineare Mannigfaltigkeit_.

## Transponierte Matrizen und Skalarprodukte

Zu einer Matrix $A=(A_{ij})_{i=1,\ldots,m;j=1,\ldots,n} \in \R^{m \times n}$ definieren wir die transponierte Matrix $A^T
\in \R^{n \times m} $ als

```{math}
 A^T =  (A_{ji})_{i=1,\ldots,n;j=1,\ldots,m}.
```

Die transponierte Matrix entsteht durch Wechseln zwischen Zeilen und Spalten, die Zeilen von $A$ sind die Spalten von $A^T$ und umgekehrt. Wir sehen leicht, dass $(A^T)^T = A $ gilt und darüber hinaus rechnen wir

```{math}
 (AB)^T = (\sum_{p } A_{jp} B_{pi} ) = (\sum_{p } B_{pi} A_{jp}  ) = B^T A^T.
```

Eine Matrix heisst symmetrisch, wenn $A=A^T$ gilt.

Wir beachten, dass wir $A^T A \in \R^{n \times n}$ und $AA^T \in \R^{m \times m}$ berechnen können, während $A A $ für $m \neq n$ nicht definiert ist. Deshalb sind die Ausdrücke $AA^T$ und $A^T A$  geeignete Verallgemeinerung des Quadrats auf eine Matrix. Im Fall von Vektoren $x \in \R^{n \times 1}$ können wir

```{math}
 x^T x = \sum_{i=1}^n x_i^2 \in \R
```

berechnen und sehen $x^T x > 0$ für $x \neq 0.$  Als Verallgemeinerung des Betrags definieren wir die Euklidische Norm

```{math}
 \Vert x \Vert := \sqrt{x^T x}.
```

Allgemeiner können wir für zwei Vektoren $x,y \in \R^{n \times n}$ das _Skalarprodukt_

```{math}
 x \cdot y := x^T y = y^T x =  \sum_{i=1}^n x_i y_i
```

definieren. Das Skalarprodukt erlaubt eine Verallgemeinerung von Orthogonalität, wir sagen $x$ und $y$ sind orthogonal, wenn$ x^T y  = 0.$ Dies können wir auch für Basen definieren:

````{prf:definition}
Eine Basis $\{b_1,\ldots,b_n\}$ der $\R^n$ heisst Orthogonalbasis, falls $b_i^T b_j = 0$ für $i \neq j$ gilt. Gilt zusätzlich $\Vert b_i \Vert=1$ für $i=1,\ldots,n$, dann sprechen wir von einer Orthonormalbasis. Analog definieren wir eine Orthogonalbasis oder Orthonormalbasis eines beliebigen Unterraums $U \subset \R^n$.
````

Wir können aus einer beliebigen Basis $\{b_1,b_2, \ldots,b_n\}$ eine Orthonormalbasis konstruieren, mit dem sogenannten _Gram-Schmidt Verfahren_. Dabei beginnen wir mit $b_1$ und normieren es einfach zu $\tilde b_1 = \frac{b_1}{\Vert b_1\Vert}$. Wir beachten, dass $\Vert b_1\Vert \neq 0$ gilt, da sonst $b_1=0$ wäre und die Annahme einer Basis falsch wäre. $\tilde b_2$ konstruieren wir als Linearkombination $\tilde b_2 = \alpha \tilde b_1 + \beta b_2$ mit $\alpha, \beta \in \R$, die wir so bestimmen, dass

\begin{align*}
0 &=  \tilde b_1^T \tilde b_2 = \alpha \tilde b_1^T \tilde b_1 + \beta \tilde b_1^T b_2\\
1 &=  \tilde b_2^T \tilde b_2 = \alpha^2 \tilde b_1^T \tilde b_1 + 2 \alpha \beta \beta \tilde b_1^T b_2 + \beta^2 b_2^T b_2.
\end{align*}

Wegen $1 = \tilde b_1^T \tilde b_1 = \Vert \tilde b_1 \Vert^2$ folgt aus der ersten Gleichung

```{math}
 \alpha = - \beta \tilde b_1^T b_2.
```

Setzen wir dies in die zweite Gleichung ein, so folgt

```{math}
 1 = \beta^2 ( b_2^T b_2 - (\tilde b_1^T b_2)^2).
```

Dies Gleichung hat einer reelle Lösung $\beta$, da wegen der Cauchy-Schwarz Ungleichung (siehe Vorkurs) gilt

```{math}
 (\tilde b_1^T b_2)^2 \leq \Vert \tilde b_1 \Vert^2 \Vert b_2 \Vert^2 =  b_2^T b_2 ,
```

mit Gleichheit wenn $\tilde b_1$ und $b_2$ linear abhängig sind. Dies ist wegen der Basiseigenschaft ausgeschlossen, also ist

```{math}
 \beta = \frac{1}{\sqrt{b_2^T b_2 - (\tilde b_1^T b_2)^2}} 
```

eine positive reelle Zahl.Nun gehen wir schrittweise weiter so vor und konstruieren $\tilde b_{j+1}$ als Linearkombination von $\tilde b_1, \ldots, \tilde b_j$ und $b_{j+1}$, aus den Gleichungen

```{math}
 \tilde b_i^T \tilde b_{j+1} = 0, \qquad i=1,\ldots,j
```

und

```{math}
 \tilde b_{j+1}^T \tilde b_{j+1} = 1.
```

Das Vorgehen ist dabei völlig analog zur Bestimmung von $\tilde b_2$, aus den ersten $j$ Gleichungen können wir die ersten $j$ Koeffizienten durch den Koeffizienten von $\tilde b_{j+1}$ ausdrücken und diesen wieder aus der letzten Gleichung bestimmen.
Wir bemerken, dass wir im Fall einer Orthonormalbasis $\{b_1,\ldots,b_n\}$ die Koeffizienten durch Skalarprodukte ausdrücken können. Ist

```{math}
 x = \sum_{i=1}^n \lambda_i b_i,
```

dann gilt

```{math}
 b_j^T x = \sum_{i=1}^n \lambda_i b_j^T b_i = \lambda_j.
```

Also erhalten wir

```{math}
 x= \sum_{i=1}^n (b_i^T x) b_i.
```

Wir sehen dann auch nochmal eine allgemeine Version des Satz von Pythagoras, es gilt

```{math}
 \Vert x \Vert^2 = \sum_{i=1}^n (b_i^T x)^2.
```

Nun wenden wir uns noch ein wenig dem Range und dem Nullraum von Operatoren zu. Insbesondere betrachten wir ${\cal R}(A)$ und ${\cal N}(A^T)$. Wir werden sehen, dass diese Räume orthogonal sind. Wir sprechen von zwei orthogonalen Unterräumen $U$ und $V$, wenn $u^T v = 0$ für alle $u \in U$ und $v \in V$ gilt. Damit gilt insbesondere $U \cap V = \{0\}$.

````{prf:theorem}
Es gilt

```{math}
 \R^m  = {\cal R}(A) \oplus {\cal N}(A^T), \qquad \R^n = {\cal R}(A^T) \oplus {\cal N}(A ),
```

dazu sind die beiden Teilräume jeweils orthogonal.
````

````{prf:proof}
Wir zeigen zunächst die Orthogonalität. Ist $y=Ax \in {\cal R}(A)$ und $z \in {\cal N}(A^T)$, dann gilt

```{math}
 z^T y = z^T A x = (A^T z)^T x = 0.
```

Damit folgt insbesondere, dass die Summe aus den beiden Unterräumen direkt ist und wir müssen nur noch nachweisen, dass sie auch gleich dem $\R^m$ ist. Sei zunächst $\{b_1,\ldots,b_k\}$ eine Basis von ${\cal R}(A)$ und $\{b_{k+1},\ldots,b_m\}$ eine Basiserweiterung. Dann können wir mit dem Gram-Schmidt Verfahren eine Orthonormalbasis  $\{\tilde b_1,\ldots, \tilde b_m\}$
konstruieren. Da $\{\tilde b_1, \ldots, \tilde b_k\}$ aus Linearkombinationen von $\{b_1, \ldots b_k\}$ entsteht, ist es eine Orthonormalbasis von ${\cal R}(A)$. Für $j > k$ gilt nun $\tilde b_i^T \tilde b_j = 0$ für $j \leq k$ und damit auch
```{math}
 y^T \tilde b_j = (Ax)^T \tilde b_j = x^T (A^T \tilde b_j) = 0
```

für alle $x \in \R^n$ und damit $y \in {\cal R}(A)$. Insbesondere folgt daraus $A^T \tilde b_j = 0$ für $j > k$. Damit ist $\tilde b_j \in {\cal N}(A^T)$. Wegen $\R^m  = $lin$(\{\tilde b_i\}_{i=1,\ldots,m})$ folgt dann direkt
```{math}
 \R^m  = {\cal R}(A) \oplus {\cal N}(A^T).
```


Die zweite Identität folgt direkt aus der ersten wegen $(A^T)^T = A$. 
````

Neben dem Skalarprodukt können wir auch das _äußere Produkt_ $x \otimes y = x y^T \in \R^{n \times n}$ berechnen. Für die Matrix $A=x y^T$ gilt $A z = x(y^T z)$, d.h. alle Elemente von ${\cal R}(A)$ sind skalare Vielfache von $x$. Ist $x \neq 0$ ist deshalb Rg$(A) = $dim$({\cal R}(A))$.

## Lösbarkeit

Basierend auf Skalarprodukten und der transponierten Matrix können wir auch eine Lösbarkeitsbedingung für das lineare Gleichungssystem $A x = y$ herleiten. Es gilt

```{math}
 z^T y = z^T A x = (A^T z)^T x.
```

Ist nun $z \in {\cal N}(A^T)$, so muss $z^T y = 0$ sein. Dies ist aber nicht nur notwendige, sondern auch hinreichende Bedingung.

````{prf:theorem}
$Ax=y$ ist lösbar, genau dann wenn $z^T y = 0$ für alle $z \in {\cal N}(A^T)$ gilt.
````

````{prf:proof}
 Die eine Richtung haben wir schon oben gesehen. Nun nehmen wir an, $z^T y = 0$ für alle $z \in {\cal N}(A^T)$ gilt.  
````

````{prf:example}
Sei

```{math}
A = \left(  \begin{matrix} 2 & 1 \\ 1  & 0 \\ -1 & 1\end{matrix} \right), \qquad A^T = \left(  \begin{matrix}
2 & 1 & -1 \\ 1 & 0 & 1 \end{matrix} \right).
```

Dann gilt

```{math}
 {\cal N}(A^T) = t \begin{pmatrix} 1 \\ - 3 \\ -1\end{pmatrix},
```

also ist $Ax =y$ lösbar, wenn $y_1 - 3y_2 -y_3 = 0$ gilt.
````

Wir haben nun die Lösbarkeit und die Lösungsmenge untersucht, als nächsten Schritt wollen wir nun konkreter die Berechnung einzelner Lösungen untersuchen. Dazu können wir das Problem auf eines mit quadratischer Matrix zurückführen: Ist $m > n$, dann haben wir ein überbestimmtes Problem. Statt $Ax = y$ können wir

```{math}
A^TA x = A^T y
```

lösen. Ist ${\cal N}(A^T) =\{0\}$, dann ist eine Lösung von $A^T A x=A^Ty$ auch eine Lösung von $Ax =b$. Andernfalls ist das Problem nur lösbar, wenn $y$ orthogonal zu ${\cal N}(A^T)$ ist und damit ist wiederum jede Lösung von $A^T A x=A^Ty$ auch eine Lösung von $Ax =y$.

Ist $m < n$, dann ist das Problem unterbestimmt und der Nullraum von $A$ in jedem Fall nichttrivial. Hier können wir eine Lösung der Form $x=A^T z$ suchen, also das Problem $AA^T z = y$ lösen.

## Quadratische Matrizen und Inverse

Im Folgenden betrachten wir nun Systeme $Ax = y$ mit $A \in \R^{n \times n}$. In diesem Fall können wir bestenfalls das System für alle $y \in \R^n$ eindeutig lösen, d.h. die Abbildung $x \mapsto Ax$ ist bijektiv.

````{prf:definition}
Eine Matrix $A \in \R^{n \times n}$ heisst regulär, wenn für alle $y \in \R^n$ eine eindeutige Lösung des linearen Systems $Ax=y$ existiert. Andernfalls heisst $A$ singulär.
````

Ist $A$ regulär, dann können wir insbesondere eindeutige Lösungen $b_i$ zu $y=e_i$ finden, d.h. $A b_i = e_i$. Schreiben wir die Spaltenvektoren $b_i$ in eine Matrix $B \in \R^{n \times n}$ und analog die Spaltenvektoren $e_i$ in die Einheitsmatrix $I$, dann gilt $AB=I$, d.h. $B$ ist die inverse Matrix $B=A^{-1}$. Also ist eine reguläre Matrix immer invertierbar im Sinne der Matrixmultiplikation und umgekehrt, denn für invertierbare Matrizen ist $x=A^{-1}y$ die eindeutige Lösung.Wir sehen, dass die invertierbaren Matrizen im $\R^{n \times n}$ eine Gruppe bilden mit $I$ als neutralem Element, diese wird allgemeine lineare Gruppe (englisch general linear group), GL$(n)$ genannt.

````{prf:example}
Sei

```{math}
 A = \left( \begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22}  \end{matrix} \right).
```

Wir berechnen $b_1$ als Lösung von $Ax = e_1$, d.h.
```{math}
 a_{11} b_{11} + a_{12} b_{21} = 1, \quad a_{21} b_{11} + a_{22} b_{21} = 0.
```

Wir multiplizieren die erste Gleichung mit $a_{22}$ und die zweite mit $-a_{12}$ und addieren die beiden, dann erhalten wir

```{math}
 (a_{11} a_{22} - a_{12} a_{21}) b_{11} = a_{22},
```

also, falls der Nenner ungleich Null ist

```{math}
 b_{11} = \frac{a_{22}}{a_{11} a_{22} - a_{12} a_{21}}, \quad b_{21} = \frac{-a_{12}}{a_{11} a_{22} - a_{12} a_{21}}.
```

Analog können wir die zweite Spalte $b_2$ der inversen Matrix als

```{math}
 b_{22} = \frac{a_{11}}{a_{11} a_{22} - a_{12} a_{21}}, \quad b_{12} = \frac{-a_{21}}{a_{11} a_{22} - a_{12} a_{21}} 
```

berechnen. Damit erhalten wir

```{math}
 A^{-1} = \frac{1}{a_{11} a_{22} - a_{12} a_{21}} \left( \begin{matrix} a_{22} & -a_{12} \\ - a_{21} & a_{11}  \end{matrix} \right).
```

Die Inverse existiert unter der Bedingung, dass $a_{11} a_{22} - a_{12} a_{21} \neq 0$.
````

## Determinanten

Im letzen Beispiel haben wir gesehen, dass wir die Invertierbarkeit einer $2 \times 2$ Matrix durch eine einzige Zahl, die sogenannte Determinante

```{math}
 \text{det}(A) = a_{11} a_{22} - a_{12} a_{21}
```

 charakterisieren können. Wir werden sehen, das eine analoge Eigenschaft für $n \times n$ Matrizen gilt. Wie im Fall von $n=2$ werden wir Determinanten als Summe über Produkte definieren, in denen wir aus jeder Zeile (bzw. Spalte) genau ein Element verwenden. Dann müssen wir nur noch die jeweiligen Vorzeichen klären. Um dies strukturiert zu machen führen wir das Konzept der Permutation ein:

````{prf:definition}
Eine _Permutation_ ist eine bijektive Abbildung $\pi: \{1,\ldots,n\} \rightarrow \{1,\ldots,n\} $. Die Menge der Permutationen zur Mächtigkeit $n$ nennen wir $\Pi_n$.
````

Wir unterscheiden monotone Teile der Permutation ($i \leq j$ und $\pi(i) \leq \pi(j)$), sowie nichtmonotone ($i < j$ und $\pi(i) > \pi(j)$), letztere nennt man _Fehlstände_ oder Inversionen

```{math}
 \text{inv}(\pi): = \{(i,j)~|~i<j, \pi(i) > \pi(j) \}.
```

Basierend darauf definieren wir das Vorzeichen einer Permutation als

```{math}
 \text{sign}(\pi) =(-1)^{|\text{inv}(\pi)|}.
```

````{prf:example}
Wir betrachten nochmal die Determinante einer $2 \times 2$ Matrix. Dort gibt es zwei Permutationen in $\Pi_2$, nämlich
```{math}
 \pi_1(1)=1, \pi_1(2)=2,
```

und

```{math}
 \pi_2(1)=2, \pi_2(2)=1.
```

$\pi_1$ hat keine Fehlstände, inv$(\pi_1)=\emptyset$, also sign$(\pi_1)=1$. $\pi_2$ hat einen Fehlstand, inv$(\pi_2)={(1,2)}$,
also  sign$(\pi_2)=-1$. Die Determinante können wir dann als

```{math}
 \text{det}(A) =  \text{sign}(\pi_1) a_{1\pi_1(1)} a_{2\pi_1(2)} + \text{sign}(\pi_2) a_{1\pi_2(1)} a_{2\pi_2(2)} 
```

schreiben.
````

Die Einsicht des obigen Beispiels ist die Grundlage der Definition der Determinante einer $n \times n$ Matrix:

````{prf:definition}
Sei $A \in \R^{n \times n}$, dann ist die Determinante von $A$ definiert als

```{math}
 \text{det}(A) = \sum_{\pi \in \Pi_n} \text{ sign}(\pi) \prod_{j=1}^n a_{j \pi(j)}.
```

````

Wir sehen, dass durch die Eigenschaft der Permutationen in jedem Produkt genau ein Element aus jeder Zeile bzw. Spalte steht.

````{prf:example}
Für die Einheitsmatrix $I \in \R^{n \times n}$ gilt det$(I)=1$.
````

````{prf:example}
Für eine Dreiecksmatrix  $A \in \R^{n \times n}$ ($A_{ij} = 0$ für $i< j$ oder $A_{ij} = 0$ für $i> j$) gilt det$(A)=\prod_{i=1}^n A_{ii}$.
````

Eine besonders wichtige Eigenschaft ist der sogenannte Determinantenproduktsatz, der auf einer einfachen Eigenschaft von Permutationen beruht, die wir hier nicht beweisen:

````{prf:lemma}
Seien $\pi_1, \pi_2 \in \Pi_n$, dann gilt
```{math}
  \text{sign}(\pi_1 \circ \pi_2) = \text{ sign}(\pi_1) \text{ sign}(\pi_2).
```

````

Wir wollen nun die Determinante eines Produkts $A B$ berechnen, dazu betrachten wir zunächst wieder das Beispiel $n=2$

````{prf:example}
Wir berechnen det$(AB)$ für

```{math}
 A = \left( \begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22}  \end{matrix} \right),  B = \left( \begin{matrix} b_{11} & b_{12} \\ b_{21} & b_{22}  \end{matrix} \right).
```

Dann ist
```{math}
 C = A B = \left( \begin{matrix} a_{11} b_{11} + a_{12} b_{21}   & a_{11} b_{12} + a_{12} b_{22} \\ a_{21} b_{11} + a_{22} b_{21}    & a_{21} b_{12} + a_{22} b_{22}   \end{matrix} \right)
```

und
```{math}
 \text{det}(C) = (a_{11} b_{11} + a_{12} b_{21}) (a_{21} b_{12} + a_{22} b_{22}) - (a_{11} b_{12} + a_{12} b_{22}) (a_{21} b_{11} + a_{22} b_{21}).
```

Nach ausmultiplizieren erhalten wir
\begin{align*}
  \text{det}(C) =& (a_{11} b_{11} a_{21} b_{12}  +  a_{11} b_{11} a_{22} b_{22} + a_{12} b_{21} a_{21} b_{12} +  a_{12} b_{21}a_{22} b_{22}) - \\& (a_{11} b_{12} a_{21} b_{11} + a_{11} b_{12}  a_{22} b_{21} + a_{12} b_{22} a_{21} b_{11} + a_{12} b_{22} a_{22} b_{21}) \\ =& a_{11} a_{22} b_{11}  b_{22} - a_{12} a_{21}   b_{11} b_{22}   -  a_{11} a_{22}  b_{12}  b_{21} +  a_{12}  a_{21} b_{12} b_{21}  +\\ &    a_{11} a_{21} b_{11}  b_{12} - a_{11} a_{21} b_{11}  b_{12}   +  a_{12} a_{22} b_{21} b_{22}  -  a_{12} a_{22} b_{21} b_{22}  \\=& (a_{11} a_{22} - a_{12} a_{21} )(b_{11}  b_{22}  - b_{12}  b_{21} ).
\end{align*}
Wir sehen also det$(C)$= det$(A)$ det$(B)$.
````

````{prf:theorem}
Seien $A,B \in \R^{n \times n}$. Dann gilt

```{math}
 \text{det}(AB) = \text{ det}(A) \text{ det}(B).
```

````

````{prf:proof}
 Sei $C=AB$, dann gilt

\begin{align*}
\text{det}(C) &= \sum_{\pi \in \Pi_n} \text{ sign}(\pi) \prod_{i=1}^n C_{i\pi(i)} \\
&= \sum_{\pi \in \Pi_n} \text{ sign}(\pi) \prod_{i=1}^n ( \sum_{j_i=1}^n a_{ij_i} b_{j_i\pi(i)})  .
%&= \sum_{\pi \in \Pi_n} \text{ sign}(\pi) \sum_{j=1}^n \prod_{i_j=1}^n (  a_{i_j j} b_{j \pi(i_j)}) \\
%&= \sum_{j=1}^n \sum_{\pi \in \Pi_n} \text{ sign}(\pi)  \prod_{i_j=1}^n (  a_{i_j j} b_{j \pi(i_j)}).
\end{align*}

Nun wollen wir die letzte Summe und das Produkt vertauschen, d.h. ein allgemeines Distributivgesetz anwenden.Dazu definieren wir die Indexmenge $ I_n = \{1,\ldots,n\}^n$, die als mögliche Einträge für die Vektoren $J=(j_1,\ldots,j_n)$ vorkommen. Nun sehen wir, dass

```{math}
 \prod_{i=1}^n ( \sum_{j_i=1}^n a_{ij_i} b_{j_i\pi(i)}) = \sum_{J \in I_n} \prod_{i=1}^n  a_{ij_i} b_{j_i\pi(i)}
```

gilt, was wir bei der Determinantenberechnung verwenden können:
\begin{align*} \text{det}(C) &= \sum_{\pi \in \Pi_n} \text{ sign}(\pi) \sum_{J \in I_n} \prod_{i=1}^n  a_{ij_i} b_{j_i\pi(i)}  \\ &= \sum_{J \in I_n}  \sum_{\pi \in \Pi_n} \text{ sign}(\pi)\prod_{i=1}^n  a_{ij_i} b_{j_i\pi(i)}\end{align*}Nun betrachten wir die Summanden, in denen $J$ nicht lauter verschiedene Einträge hat, d.h. $j_k = j_\ell$ für $k \neq \ell$. Dann ist

```{math}
 \prod_{i=1}^n  a_{ij_i} b_{j_i\pi(i)} = a_{kj_k} b_{j_k\pi(k)} a_{\ell j_k} b_{j_k\pi(\ell)} \prod_{i=1, i \neq k, i \neq \ell}^n  a_{ij_i} b_{j_i\pi(i)}. 
```

Sei nun $\tilde \pi$ die Permutation mit $\tilde \pi(\ell)=k, \tilde \pi(k) = \ell$ und $\tilde \pi(i)=\pi(i)$ sonst. Dann hat $\tilde \pi$ einen zusätzlichen Fehlstand zu $\pi$, d.h. sign$(\tilde \pi)= - $ sign$(\pi)$. Darüber hinaus gilt

```{math}
 \prod_{i=1}^n  a_{ij_i} b_{j_i\tilde \pi(i)} = a_{kj_k} b_{j_k\pi(\ell)} a_{\ell j_k} b_{j_k\pi(k)} \prod_{i=1, i \neq k, i \neq \ell}^n  a_{ij_i} b_{j_i\pi(i)} = \prod_{i=1}^n  a_{ij_i} b_{j_i\pi(i)} . 
```

Damit sind heben sich die beiden Terme mit $\pi$ und $\tilde \pi$ in der Summe über alle Permutationen weg und wir folgern für solche $J$

```{math}
 \sum_{\pi \in \Pi_n} \text{ sign}(\pi)\prod_{i=1}^n  a_{ij_i} b_{j_i\pi(i)}  = 0.
```

Damit bleiben nur jene $J$ übrig, in denen jeder Index in $\{1,\ldots,n\}$ genau einmal vorkommt. Diese entsprechen genau den Permutationen in $\Pi_n$. Damit erhalten wir

```{math}
 \text{det}(C) =  \sum_{\sigma \in \Pi_n} \sum_{\pi \in \Pi_n} \text{ sign}(\pi)\prod_{i=1}^n  a_{i\sigma(i)} b_{\sigma(i) \pi(i)} =  \sum_{\sigma \in \Pi_n} \sum_{\pi \in \Pi_n} \text{ sign}(\pi)\prod_{i=1}^n  a_{i\sigma(i)} \prod_{j=1}^n  b_{j \pi(\sigma^{-1}(j))},
```

wobei $\sigma^{-1}$ die Umkehrung von $\sigma$ und damit wieder eine Permutation ist. Nun sehen wir leicht, dass

```{math}
 \{ \pi \circ \sigma^{-1}~|~\pi \in \Pi_n\} = \Pi_n
```

gilt und wegen des obigen Lemmas zum Vorzeichen der Hintereinanderausführung gilt

```{math}
 \text{sign}(\pi \circ \sigma^{-1}) = \text{ sign}(\pi) \text{ sign}(\sigma^{-1}) = \text{ sign}(\pi) \text{ sign}(\sigma ) 
```

bzw.

```{math}
  \text{sign}(\pi ) = \text{ sign}(\sigma)  \text{sign}(\pi \circ \sigma^{-1}).
```

Also folgt
\begin{align*} \text{det}(C) &=  \sum_{\sigma \in \Pi_n} \sum_{\pi' \in \Pi_n} \text{ sign}(\pi') \text{ sign}(\sigma) \prod_{i=1}^n  a_{i\sigma(i)} \prod_{j=1}^n  b_{j \pi'(j)} \\  &= \sum_{\sigma \in \Pi_n} \sum_{\pi' \in \Pi_n} \text{ sign}(\pi') \text{ sign}(\sigma) \prod_{i=1}^n  a_{i\sigma(i)} \prod_{j=1}^n  b_{j \pi'(j)}  \\  &= \sum_{\sigma \in \Pi_n} \text{ sign}(\sigma) \prod_{i=1}^n  a_{i\sigma(i)} \sum_{\pi' \in \Pi_n} \text{ sign}(\pi')   \prod_{j=1}^n  b_{j \pi'(j)}  = \text{ det}(A) \text{ det}(B). \end{align*}
 
````

```{sidebar} Gabriel Cramer
[Gabriel Cramer](https://de.wikipedia.org/wiki/Gabriel_Cramer) (\* 31. Juli 1704 in Genf; † 4. Januar 1752 in Bagnols-sur-Cèze, Frankreich) war ein Genfer Mathematiker.
```

Aus dem Determinantenproduktsatz können wir die Cramer'sche Regel, eine Formel für die Lösung des Gleichungssystems $Ax=y$ herleiten, aus der wir auch die Lösbarkeit sehen, wenn die Determinante nicht verschwindet. Sei dazu $X_i \in \R^{n \times n}$ die Matrix, die aus der Einheitsmatrix entsteht, wenn man die $i$-te Spalte durch $x$ ersetzt. Dann gilt $A X_i = A_i$, wobei $A_i \in \R^{n \times n}$ die Matrix ist, die aus $A$ entsteht, wenn man die $i$-te Spalte durch $y=Ax$ ersetzt.  Nach dem Determinantenproduktsatz gilt dann

```{math}
 \det(A) \det(X_i) = \det(A_i).
```

Wir sehen sofort $\det(X_i)=x_i$, also ist das System für jeden Eintrag von $x$ lösbar, wenn $\det(A)\neq 0$ und wir erhalten

```{math}
 x_i = \frac{\det(A_i)}{\det(A)},
```

die sogenannte Cramer'sche Regel.

````{prf:theorem}
$A \in \R^{n \times n}$ ist regulär genau dann wenn $\det(A)\neq 0$.
````

````{prf:proof}
Die eine Richtung sehen wir sofort aus der Cramer'schen Regel. Ist umgekehrt $A$ regulär, dann folgt aus dem Determinantenproduktsatz

```{math}
 \det(A) \det(A^{-1}) = \det(I) = 1,
```

damit kann $\det(A)$ nicht verschwinden. $\square$
````

Die Cramer'sche Regel ist theoretisch sehr angenehm, aber ungeeignet für die praktische Anwendung bei großen linearen Gleichungssystemen, da die Berechnung der Determinanten sehr aufwändig ist. Es gibt $n!$ verschiedene Permutationen, für jede davon ist ein Produkt aus $n $ Faktoren zu berechnen. Deshalb betrachten wir alternative Verfahren und überlegen zuerst für welche Matrizen das System $Ax=y$ einfach zu lösen ist.

````{prf:definition}

* $D \in \R^{n \times n}$ heisst Diagonalmatrix, wenn $D_{ij} =0 $ für $i \neq j$ gilt.

* $L \in \R^{n \times n}$ heisst linke untere Dreiecksmatrix, wenn $L_{ij} =0 $ für $i < j$ gilt.

* $R \in \R^{n \times n}$ heisst rechte obere Dreiecksmatrix, wenn $R_{ij} =0 $ für $i > j$ gilt.
````

Im Fall einer Diagonalmatrix ist die Lösung von $Dx = y$ direkt durch

```{math}
 x_i = \frac{y_i}{D_{ii}}
```

gegeben. Im Fall einer linken unteren Dreiecksmatrix berechnen wir die Einträge nacheinander (sogenanntes Vorwärtseinsetzen)

\begin{align*}
x_1 &= \frac{y_1}{L_{11}} \\
x_2 &= \frac{y_2-L_{21} x_1}{L_{22}} \\
x_3 &= \frac{y_3-L_{31} x_1-L_{32} x_2}{L_{33}} \\
\ldots
\end{align*}

Im Fall einer rechten oberen Dreiecksmatrix gehen wir umgekehrt vor und beginnen beim letzten Eintrag (sogenanntes Rückwärtseinsetzen)

\begin{align*}
x_n &= \frac{y_n}{R_{nn}} \\
x_{n-1} &= \frac{y_{n-1}-R_{n-1,n} x_n}{R_{n-1,n-1}} \\
x_{n-2} &= \frac{y_{n-2}-R_{n-2,n} x_n-R_{n-2,n-1} x_{n-1}}{R_{n-2,n-2}} \\
\ldots
\end{align*}

Dasselbe Vorgehen ist auch möglich, wenn wir eine Matrix $A$ haben, die sich durch Vertauschen von Zeilen und Spalten in eine linkere und rechte obere Dreiecksmatrix überführen lässt. Zeilenvertauschung bedeutet, dass wir Gleichungen umnummerieren, Spaltenvertauschung, dass wir Variablen umnummerieren.
Wie können wir nun ein allgemeines System $Ax = y$ mit $A \in \R^{n \times n}$ lösen ? Die grundlegende Idee ist es, das System auf eine Dreiecksform zu bringen und dann Vorwärts- oder Rückwärtseinsetzen zu benutzen. Dies erreicht das sogenannte Gauss-Verfahren. Hier beginnen wir mit der ersten Gleichung

```{math}
 a_{11}x_1 + a_{12} x_2 + \ldots + a_{1n} x_n = y_n.
```

Ist $a_{11}=0$ so vertauschen wir die erste Gleichung mit einer anderen Gleichung $k \in \{2,\ldots,n\}$, sodass $a_{k1} \neq 0$ gilt. Ist $a_{k1}=0$ für alle $k$, so sehen wir sofort dass $\det(A)=0$ und damit die Gleichung nicht eindeutig lösbar (wenn überhaupt) ist.  Nachdem wir ggf. vertauscht haben, können wir eine Linearkombination von Zeilen durchführen, die die Lösungsmenge unverändert lässt. Wir ziehen für $k=2,\ldots,n$ ein Vielfaches $\ell_{k1} = - \frac{a_{k1}}{a_{11}}$ der ersten von der $k$-ten Zeile ab. $\ell_{k1}$ ist genau so gewählt, dass $x_1$ aus den Gleichungen verschwindet. Wir erhalten mit

```{math}
\tilde a_{ki} = a_{ki} + \ell_{k1} a_{1i}, \qquad \tilde y_k = y_k + \ell_{k1} y_1
```

die Gleichungen

```{math}
 \sum_{i=2}^n \tilde a_{ki} x_i = \tilde y_k, \qquad k=2,\ldots,n.
```

Damit haben wir ein lineares Gleichungssystem in $\R^{n-1 \times n-1}$ und können nun analog weiter verfahren. Die neue erste Variable ist $x_2$ und die neue erste Zeile ist die Gleichung mit $k=2$. Nun können wir völlig analog vorgehen bis wir bei $k=n$ angekommen sind, hier erhalten wir einfach ein $1x1$ System für $x_n$, das wir direkt lösen können. Nun berechnen wir die anderen Variablen durch Rückwärtseinsetzen. Für $x_{n-1}$ verwenden wir die erste Gleichung im $2 \times 2$ System aus dem vorletzten Schritt, für $x_{n-2}$ die erste Gleichung aus dem $3 \times 3$ System im drittletzten Schritt und so weiter.  Dieses Verfahren nennt man Gauss-Elimination.

````{prf:example}
Wir betrachten $Ax=y$ mit

```{math}
 A = \left( \begin{matrix} 1 & 2 & 2 \\ 2 & 4 & 3 \\ 0 & -1 & 1 \end{matrix} \right).
```

Hier ist $a_{11}=1$, damit $\ell_{21} = -2, \ell_{31} = 0. $ Als erste Gleichung, die wir uns für später merken, erhalten wir

```{math}
 x_1 + 2 x_2 + 2x_3 = y_1
```

und nach Elimination von $x_1$ aus der zweiten und dritten Gleichung bleibt das $2 \times 2 $ System.
```{math}
 0 x_2 -x_3 = y_2 -2 y_1, \qquad -x_2 + x_3 = y_3.
```

Da nun der erste Koeffizient $0$ ist, vertauschen wir die beiden Gleichungen und haben dann das gestaffelte System (entsprechend rechter oberer Dreiecksmatrix\begin{align*}
x_1 + 2 x_2 + 2x_3 &= y_1 \\ -x_2 + x_3 &= y_3 \\
-x_3 &= y_2 -2 y_1
\end{align*}Durch Rückwärtseinsetzen berechnen wir

```{math}
 x_3=2y_1 - y_2, \quad x_2 = 2 y_1 -y_2 -y_3, \quad x_1 = - 7 y_1 + 4y_2 +2 y_3.
```

````

Um die Rechnung bei der Gauss Elimination ein wenig strukturierter durchführen zu können definieren wir eine rechte obere Dreiecksmatrix $R \in \R^{n \times n}$ im Laufe des Verfahrens. Im ersten Schritt setzen wir $R_{1i}=a_{1i}$ für $i=1,\ldots,n$ und $z_1=y_1$. Im zweiten Schritt setzen wir $R_{21} =0$ und $R_{2i} = \tilde a_{2i}$ für $i=2, \ldots,n$ mit $\tilde a_{2i}$ wie oben, und so fahren wir auch für $k=3$ bis $m$ fort. Damit haben wir am Ende ein System $Rx=z$, das wir durch Rückwärtseinsetzen lösen können.

````{prf:example}
Für
```{math}
 A = \left( \begin{matrix} 1 & 2 & 2 \\ 2 & 4 & 3 \\ 0 & -1 & 1 \end{matrix} \right)
```

wie oben erhalten wir
```{math}
 R = \left( \begin{matrix} 1 & 2 & 2 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{matrix} \right).
```

````

Wir sehen auch, dass wir eigentlich keine Gleichungen schreiben müssen, sondern alles direkt auf Ebene der Matrix $A$ und des Vektors $y$ durchführen können. Die wichtigste Erkenntnis ist, dass eine Linearkombination von Zeilen in einer Matrix der Multiplikation mit einer Matrix von links entspricht. Wir führen dies für das Gauss-Verfahren nochmal durch. Im ersten Schritt multiplizieren wir mit einer Matrix

```{math}
L_1 = \left( \begin{matrix} 1 & 0 & 0 & \ldots & 0 \\ \ell_{21} & 1 & 0 &\ldots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\ \ell_{n1} & 0 & 0 & \ldots & 1 \end{matrix} \right)
```

bzw. im $k$-ten Schritt mit einer Matrix $L_k$, die neben der Diagonale nur Einträge in der $k$-ten Spalte unter der Diagonale hat, d.h.

```{math}
(L_k)_{ij} = \left\{ 
\begin{matrix} 
1 & i=j \\ 0 & i < j \\ 
0 & i > j, j \neq k \\ 
\ell_{ik} & i=k,j >k
\end{matrix}
\right\}.
```

Damit entspricht das Gauss-Verfahren einfach einer wiederholten Multiplikation des Systems $Ax=y$ mit solchen Matrizen, bis wir

```{math}
 Rx = L_{n-1} L_{n-2} \ldots L_2 L_1 A x = L_{n-1} L_{n-2} Ax  \ldots L_2 L_1 y = z
```

erhalten. Man prüft leicht nach, dass $L_k$ invertierbar ist mit einer sehr einfach zu berechnenden Inverse

```{math}
(L_k^{-1})_{ij} = \left\{ \begin{matrix} 1 & i=j \\ 0 & i < j \\ 0 & i > j, j \neq k \\ - \ell_{ik} & i=k,j > k\end{matrix}\right.
```

Damit können wir auch die Identität

```{math}
  R  = L_{n-1} L_{n-2} \ldots L_2 L_1 A
```

nochmal neu betrachten. Es gilt dann

```{math}
 A =  L_1^{-1}   L_2^{-1} \ldots  L_{n-2}^{-1} L_{n-1}^{-1} R  = L R,
```

wobei $L= L_1^{-1}   L_2^{-1} \ldots  L_{n-2}^{-1} L_{n-1}^{-1}$. Nun kann man leicht nachrechnen, dass $L$ eine linke untere Dreiecksmatrix ist, deren Diagonaleinträge alle gleich eins sind. Wir haben also damit $A$ in eine linke untere und eine rechte obere Dreiecksmatrix zerlegt. Hat man dies einmal berechnet, dann ist es genauso aufwändig, sich die Matrix $A$ zu merken wie $L$ und $R$ (für $L$ die Einträge unter der Diagonale, für $R$ auf und über der Diagonale). Sind $L$ und $R$ bekannt, kann das System $Ax=y$ leicht gelöst werden durch

```{math}
 L z = y, \qquad Rx = z.
```

Damit müssen wir einmal und Vorwärts- und einmal Rückwärtseinsetzen.

Kommt nun auch die Vertauschung von Zeilen hinzu, so benötigen wir auch dafür geeignete Matrizen, die sogenannten Permutationsmatrizen. Zu jeder Permutation $\pi \in \Pi_n$ können wir eine Permutationsmatrix $P^\pi \in \R^{n \times n}$ definieren als $P_{ij}^\pi = (\delta_{i\pi(i)})$, d.h. $P^\pi$ hat in jeder Zeile und Spalte einen Eintrag eins und $n-1$ Einträge null. Eine Multiplikation $PA$ entspricht einer Vertauschung von Zeilen $AP$ einer Vertauschung von Spalten. Im Fall des Gauss-Verfahrens benötigt man in jedem Schritt nur die Vertauschung der $k$-ten Zeile mit einer Zeile $p \geq k$, d.h. die Einträge von $P^\pi$ entsprechen in $n-2$ Zeilen der Einheitsmatrix, nur in Zeile $k$ ist das $p$-te Element gleich eins und umgekehrt. Das Gauss-Verfahren mit Vertauschung ist dann

```{math}
 R=L_{n-1} P_{n-1} L_{n-2} P_{n-2}\ldots L_2 P_2 L_1 P_1 A ,
```

mit entsprechenden Permutationsmatrizen $P_j$ für Zweiervertauschungen. Die Zerlegung insgesamt kann dann am Ende in der Form

```{math}
 P A = L R
```

geschrieben werden mit einer allgemeinen Permutationsmatrix $P$.
