# Lineare Abbildungen

Wir können nun Abbildungen zwischen zwei Vetorräumen $V_1$ und $V_2$ betrachten, die einfachsten sind dabei die linearen, die auch eine wichtige Klasse bilden.

````{prf:definition}
Wir bezeichnen eine Abbildung $L: V_1 \rightarrow V_2$ als linear, wenn die Addition und Skalarmultiplikation unter $L$ erhalten bleibt, d.h.
* $\forall v,w \in V_1: L(v+w) = L(v) + L(w).$

* $\forall v \in V_1, \alpha \in \R: L(\alpha v) = \alpha L(v)$

````

Wir sehen einfach durch einen induktiven Beweis, dass für alle $n \in \N$, $\lambda_i \in \R$ und $v_i \in V_1$ dann gilt

```{math}
 L(\sum_{i=1}^n \lambda_i v_i) = \sum_{i=1}^n \lambda_i L(v_i) .
```

Daraus sehen wir auch, dass es genügt eine lineare Abbildung auf einer Basis $B$ von $V_1$ zu definieren, denn ein beliebiges $v \in V_1$ können wir dann als $v= \sum_{i=1}^n \lambda_i b_i$ schreiben und daraus folgt

```{math}
 L(v) = \sum_{i=1}^n \lambda_i L(b_i).
```

Sind umgekehrt $L(b_i)$ festgelegt, erhalten wir daraus immer mit der obige Setzung eindeutig eine lineare Abbildung.

````{prf:example}
$L: \R \rightarrow \R$ erfüllt $L(x) = x L(1)$ für alle $x \in \R$, also ist die lineare Abbildung durch den Wert am einzigen Basiselement $b_1=1$ festgelegt (diesen nennen wir Steigung).
````

````{prf:example}
$L: \R^2 \rightarrow \R, (x_1,x_2) \mapsto x_1 +x_2$ ist festgelegt durch $L((1,0)) = 1$ und $L((0,1))=1$.
````

````{prf:example}
$L: \R^2 \rightarrow \R^2, (x_1,x_2) \mapsto (2x_1-x_2,2x_2+x_1)$ ist festgelegt durch $L((1,0)) = (2,1)$ und $L((0,1))=(-1,2)$.
````

Wir sehen in den Beispielen, dass wir eine lineare Abbildung zwischen einem $n$-dimensionalen Vektorraum und einem $m$-dimensionalen Vektorraum durch $nm$ reelle Zahlen festlegen können, indem wir die $L(b_i)$, $i=1,\ldots,n$ in einer Basis von $V_2$ entwickeln.

Wir wollen nun die Injektivität und Surjektivität linearer Abbildungen genauer betrachten. Dies ist direkt verwandt mit der Eindeutigkeit und Lösbarkeit linearer Gleichungen: $L(v) = w$ hat für jedes $w$ eine Lösung $v$, wenn $L$ surjektiv ist. Die Lösung ist eindeutig, wenn $L$ injektiv ist. Eine bijektive lineare Abbildung nennen wir Isomorphismus.

````{prf:lemma}
Ein linearer Operator $L$ ist injektiv genau dann, wenn aus $L(v) = 0$ folgt $v=0$.
````

````{prf:theorem}
Sei dim$(V) =n$, dann existiert ein Isomorphismus von $V$ nach $\R^n$.
````

````{prf:proof}
 Wir definieren für die Basiselemente $L(b_i) = e_i = (\delta_{ij})_{j=1,\ldots,n}$ und entsprechend

```{math}
 L(v) = L(\sum_{i=1}^n \lambda_i b_i) = \sum_{i=1}^n \lambda_i e_i = (\lambda_1, \ldots, \lambda_n) \in \R^n .
```

L ist injektiv, da aus $L(v) = 0$ folgt $\lambda_1=\ldots,\lambda_n = 0$ und damit $v=0$. $L$ ist surjektiv, da jedes

```{math}
 (\lambda_1, \ldots, \lambda_n) \in \R^n 
```
 gleich $L(v)$ mit $v = \sum_{i=1}^n \lambda_i b_i$ ist. 
````

Damit können wir im Prinzip jeden endlichdimensionalen Vektorraum mit $\R^n$ identifizieren, indem wir einfach die Koeffizienten in der Basisentwicklung betrachten.

````{prf:theorem}
Sei $L: V_1 \rightarrow V_2$ eine lineare Abbildung zwischen endlichdimensionalen Vektorräumen. Dann gilt:

* Ist $L$ injektiv, so folgt dim$(V_2) \geq $ dim$(V_1)$.
* Ist $L$ surjektiv, so folgt dim$(V_2) \leq $ dim$(V_1)$.
````

````{prf:proof}
 Sei dim$(V_1)=n$ und $\{b_i\}_{i=1,\ldots,n}$ eine Basis für $V_1$. Man sieht sofort, dass $\{L(b_i)\}_{i=1,\ldots,n}$ ein Erzeugendensystem für das Bild von $L$ ist. Ist $L$ surjektiv, dann wissen wir auch dim$(V_2) \leq n$ gilt. Ist $L$ injektiv, dann folgt aus
```{math}
 0 = \sum_{i=1}^n \lambda_i L(b_i) = L( \sum_{i=1}^n \lambda_i b_i)
```
 auch$\sum_{i=1}^n \lambda_i b_i = 0$ und damit $\lambda_1=\ldots=\lambda_n = 0$ und damit ist $\{L(b_i)\}_{i=1,\ldots,n}$ ein linear unabhängiges System. Daraus folgt dim$(V_2) \geq n$. 
````

\begin{cor}
Sei $L: \R^n \rightarrow \R^m$. Ist $m < n$, dann ist $L$ nicht injektiv. Ist $m> n$, dann ist $L$ nicht surjektiv.\end{cor}
Wir sehen dies auch in den obigen Beispielen von $\R^2$ nach  $\R$ (nicht injektiv, aber surjektiv) bzw. von $\R^2$ nach $\R^2$ (bijektiv).

Eine lineare Abbildung von $\R^n$ nach $\R^m$ können wir durch eine Matrix $A \in \R^{m \times n}$ darstellen, wir schreiben

```{math}
 A = \left( \begin{array}{ccc} a_{11} &\ldots& a_{1n} \\ a_{21} &\ldots &a_ {2n} \\ \vdots &\ddots &\vdots \\ a_{m1} &\ldots& a_{mn} \end{array} \right)
```

wobei

```{math}
 \left( \begin{array}{c} a_{1i} \\ a_{2i}  \\ \vdots \\ a_{mi}  \end{array} \right) = L(e_i)
```

ist. An dieser Stelle müssen wir das erste Mal darauf achten, ob wir Zeilen- oder Spaltenvektoren schreiben.Ein Zeilenvektor ist dann eine Matrix in $\R^{1 \times n}$, ein Spaltenvektor in $\R^{m \times 1}$.Solange wir keine Matrizen verwenden ist die Unterscheidung unerheblich, aber etwa bei der Konstruktion von $A$ oder bei der Multiplikation einer Matrix mit einem Vektor wird dies wichtig. Letztere können wir definieren, in dem wir wieder die Matrix $A$ mit dem linearen Operator $L$ identifizieren. Ist $x$ ein Spaltenvektor, dann schreiben wir

```{math}
 A x := L(x) = \left( \begin{array}{c} \sum_{i=1}^n a_{1i} x_i \\ \sum_{i=1}^n a_{2i} x_i \\ \vdots \\ \sum_{i=1}^n a_{mi} x_i  \end{array} \right) .
```

Damit berechnen wir also immer das Skalarprodukt einer Zeile von $A$ (ein Zeilenvektor der Länge $n$) mit dem Vektor $x$ (ein Spaltenvektor der Länge $n$. Wir werden sehen, dass dies auch bei allgemeiner Matrixmultiplikation der Fall ist. Um diese zu definieren können wir einfach die Hintereinanderausführung linearer Operatoren betrachten. Sind $L_1: \R^n \rightarrow \R^m$ und  $L_2: \R^m \rightarrow \R^k$ dargestellt durch Matrizen $A \in \R^{m \times n}$ bzw. $B \in \R^{k \times n}$, dann definieren wir das Matrixprodukt $C = BA \in \R^{n \times k}$ als Darstellung der Abbildung $x \mapsto L_2(L_1(x))$. Damit ist insbesondere

```{math}
 C e_j = BAe_j = B (\sum_{k=1}^n a_{ik} \delta_{kj})_{i=1,\ldots,m} = B (a_{ij})_{i=1,\ldots,m} = (\sum_{p=1}^m b_{ip} a_{pj})_{i=1,\ldots,k}.
```

Insgesamt gilt dann

```{math}
 C = BA =  (\sum_{p=1}^m b_{ip} a_{pj})_{i=1,\ldots,k; j=1,\ldots,m} .
```
