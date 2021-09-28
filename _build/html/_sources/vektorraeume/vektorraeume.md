Vektorräume und lineare Abbildungen
===

Die komplexen Zahlen aus dem letzten Abschnitt sind ein einfaches Beispiel eines Vektorraums, nun wollen wir Vektorräume etwas genauer betrachten, die allgemein folgendermaßen definiert sind:

````{prf:definition}
Sei $V$ eine Menge und $\K$ ein Körper. Gegeben seien die Addition $\oplus: V \times V \rightarrow V$ und die Skalarmultiplikation $\odot: \K \times V \rightarrow V$. $(V,\oplus,\odot)$ heisst Vektorraum, wenn für alle $u,v \in V$ und alle $\alpha, \beta \in \K$ die folgenden Eigenschaften gelten:


* $(V,\oplus)$ ist eine abel'sche Gruppe.

* $\alpha \odot (u \oplus v) = \alpha \odot(v \oplus u) = (\alpha \odot u) \oplus (\alpha \odot v)$

* $(\alpha + \beta) \odot v = (\alpha \odot v) \oplus (\beta \odot v)$

* $(\alpha \beta)\odot v = \alpha \odot (\beta \odot v)$

* $1 \odot v = v$, wobei $1$ das Einselement der Multiplikation in $\K$ ist.
````

Wir werden im Folgenden einfach $u +v$ statt $u \oplus v$ und $\alpha v$ statt $\alpha \odot v$ schreiben.

````{prf:example}
$\R^n$ ist ein Vektorraum über $\R$, allgemein ist $\K^n$ ein Vektorraum über $\K$.
````

````{prf:example}
$\R^\N =  \{(x_n):\N \rightarrow \R\}$ ist Vektorraum über $\R$.
````

````{prf:example}
$\ell^\infty(\N) = \{(x_n) \in \R^\N~|~\sup_n |x_n| < \infty\}$ ist ein Vektorraum über $\R$
````

````{prf:example}
$\C = \{ a + b \i ~|~ a,b \in \R\}$ ist ein Vektorraum über $\R$
````

Im Fall der komplexen Zahlen haben wir den Vektorraum über eine _\2_ (also Vielfache und Summen) gewisser Elemente, nämlich $1$ und $\i$, definiert. Dies ist auch in den anderen Vektorräumen der Fall, z.B. können wir in $\R^n$ alles als Linearkombination der Einheitsvektoren

```{math}
 e_i = (\delta_{ij})_{j=1}^n
```

schreiben, wobei $\delta_{ij}$ das Kronecker-Delta bezeichnet, definiert als $\delta_{ii}=1$ und $\delta_{ij}=0$ sonst. Diese Elemente sind aber nicht eindeutig, z.B. können wir im $\R^2$ auch alles als Linearkombination von $(1,1)$ und $(1,-1)$ schreiben, es gilt

```{math}
 (a,b) = \lambda_1 (1,1) + \lambda_2 (1,-1)
```

mit $\lambda_1 = \frac{a+b}2$, $\lambda_2 = \frac{a-b}2$.

````{prf:definition}
Seien $v_1,\ldots,v_n \in V$.

* Seien $\lambda_1,\ldots,\lambda_b \in \K$, dann heisst
```{math}
 v = \sum_{i=1}^n \lambda_i v_i
```

Linearkombination der $v_i$.

* Die Elemente $v_1,\ldots,v_n$ ( bzw. $\{v_1,\ldots,v_n\}$) die Menge heissen linear unabhängig, wenn aus$\sum_{i=1}^n \lambda_i v_i =0$ folgt, dass $\lambda_1 = \lambda_2 \ldots = \lambda_n = 0$.
* Eine Menge $W \subset V$ heisst linear unabhängig für alle $n \in \N \setminus \{0\}$, $n \leq |W|$ jede Teilmenge $\{v_1,\ldots,v_n\}$ linear unabhängig ist. Andernfalls nennen wir $W$ linear abhängig.

* Sei $W \subset V$, dann ist die lineare Hülle

```{math}
 \text{lin}(W) = \{ \sum_{i=1}^n \lambda_i v_i~|~ n \in \N, \lambda_i \in \K, v_i \in W\}
```

gegeben als die Menge aller Linearkombinationen von Elementen aus $W$.

* $W$ heisst Erzeugendensystem, wenn lin$(W)=V$.

* $B \subset V$ heisst Basis von $V$, wenn $B$ Erzeugendensystem und linear unabhängig ist.

* Ist $B$ Basis von $V$ und $n=|B| < \infty$, dann heisst $V$ endlichdimensionaler Vektorraum und $n$ die Dimension von $V$.

* Ist $W \subset V$ selbst ein Vektorraum, d.h. abgeschlossen bezüglich Addition und Skalarmultiplikation, dann nennen wir $W$ Unterraum von $V$.

````

````{prf:example}
Wir betrachten wieder den $\R^2$. $B=\{(1,0),(0,1)\}$ ist eine Basis, $W= \{(1,0),(0,1),(1,1)\}$ ist ein Erzeugendensystem, aber nicht linear unabhängig, da
```{math}
 (1,0) + (0,1) - (1,1) = 0.
```

````

````{prf:example}
Für $V=\R^3$ ist $W=\{(1,0,0),(0,1,0)\}$  linear unabhängig, aber kein Erzeugendensystem, da wir kein $\lambda_1,\lambda_2 \in \R$ finden können mit

```{math}
(0,0,1) =  \lambda_1 (1,0,0)+ \lambda_2 (0,1,0) = (\lambda_1,\lambda_2,0).
```

Tatsächlich entspricht lin$(V)$ dem $\R^2$ mit einer zusätzlichen Null in der dritten Variable.
````

````{prf:example}
Sei $V=\R^N$, $W=\{(\delta_{in})_n ~|~i \in \N\}$. Dann ist $W$ linear unabhängig, aber keine Basis. Es gilt
```{math}
 \text{lin}(W) = \{ (x_n) \in \R^\N~|~ \exists n_0 \in \N \forall n \geq n_0: x_n =0 \},
```

die lineare Hülle entspricht also den Folgen, die nach endlich vielen Indizes null werden.
````

Wir machen einige Beobachtungen:

* Ist $W$ linear unabhängig, so ist natürlich auch jede nichtleere Teilmenge von $W$ linear unabhängig. Ist $W$ ein Erzeugendensystem, dann ist auch jedes $W'$ mit $W \subset W'$ Erzeugendensystem.

* Eine Menge, die $v=0$ enthält ist nie linear unabhängig, da $\lambda   v  = 0$ für alle $\lambda \in \K$.

Linearkombinationen führen in natürlicher Weise auf lineare Gleichungssysteme für die Koeffizienten $\lambda_i$, dies sehen wir noch mal am Beispiel

```{math}
 (a,b) = \lambda_1 (1,1) + \lambda_2 (1,-1),
```

das wir auch  als Gleichungssystem

```{math}
 \lambda_1 + \lambda_2 = a, \qquad \lambda_1 - \lambda_2 = b
```

für $\lambda_1$, $\lambda_2$ schreiben können. Die Möglichkeit $v$ als Linearkombination von $v_1, \ldots,v_n$ darstellen zu können, ist dann die Frage der Lösbarkeit eines linearen Gleichungssystems für $n$ unbekannte Koeffizienten, die wir noch intensiv diskutieren werden. Der Einfachheit halber werden wir uns dazu auf $\K=\R$ beschränken.

````{prf:theorem}
Sei $W \subset V$, dann ist lin$(W)$ ein Teilraum von $V$.
````

````{prf:proof}
 Da die Gesetze der Addition und Multiplikation auch in lin$(W) \subset V$ gelten, müssen wir nur nachprüfen, dass $+:$lin$(W) \times$ lin$(W) \rightarrow $lin$(W)$ und $\cdot:\R \times$ lin$(W) \rightarrow$ lin$(W)$ gilt.Ist $v \in $ lin$(W)$, dann gilt
```{math}
 v = \sum_{i=1}^n \lambda_i v_i, \qquad \lambda_i \in \R, v_i \in W
```
 und
damit auch

```{math}
 \alpha v = \sum_{i=1}^n (\alpha \lambda_i) v_i \quad \in \text{ lin}(W).
```

Ist darüber hinaus $w \in $ lin$(W)$, dann gilt

```{math}
 v = \sum_{i=1}^n \mu_i w_i, \qquad \mu_i \in \R, w_i \in W
```
 und
damit

```{math}
 v+ w = \sum_{i=1}^{n+m} \lambda_i v_i \qquad \lambda_i \in \R, v_i \in W,
```

wobei wir $\lambda_{n+i} = \mu_i$ und $v_{n+i} = \mu_i$ setzen. Also ist auch $v+w \in $ lin$(W)$. 
````

````{prf:theorem}
Sei $V$ ein Vektorraum und $B \subset V$ eine Basis mit $|B|=n$. Dann gilt für jede linear unabhängig Menge $W$ auch $|W| \leq n$ und für jedes Erzeugendensystem $E$ auch $|E| \geq n$.
````

````{prf:proof}
 Sei $W$ eine  Menge und nehmen wir an es gibt $n+1$ linear unabhängige Elemente $w_1, \ldots w_{n+1}$ in $W$. Dann gibt es für jedes $w_i$ eine Darstellung in der Basis $B=\{b_1,\ldots,b_n\}$, d.h.
```{math}
 w_i =  \sum_{j=1}^n \lambda_{ij} b_j.
```

Wir beginnen mit $i=1$. Da nicht alle $\lambda_{1j} =0 $ sein können, nehmen wir ohne Beschränkung der Allgemeinheit an, dass $\lambda_{11} \neq 0$ gilt. Also folgt

```{math}
 - \lambda_{11} w_i + \lambda_{i1} w_1 = \sum_{j=2}^n \lambda_{ij}^{(2)}  b_j, \qquad i=2,\ldots,n+1
```

mit neuen Koeffizienten $\lambda_{ij}^{(2)}$. Da nicht alle $\lambda_{2j}^{(2)} $ gleich Null sein können, nehmen wir wieder an, $\lambda_{22}^{(2)} \neq 0$. Mit analogem Vorgehen erhalten wir eine Darstellung der Form

```{math}
 \alpha_{1i} w_1 + \alpha_{2i} w_2 + \beta_i w_i = \sum_{j=3}^n \lambda_{ij}^{(3)}  b_j, \qquad i=3,\ldots,n+1.
```

Wenden wir dieses Argument wiederholt an, so gilt nach $n$ Schritten

```{math}
 \alpha_{1,n+1} w_1 + \alpha_{2,n+1} w_2 + \ldots \alpha_{n,n+1} w_n + \beta_{n+1} w_{n+1} = 0
```

und damit sind die $w_i$ linear abhängig.
Ist umgekehrt $v_1, \ldots, v_m$ ein Erzeugendensystem mit $m<n$, so können wir $b_1,\ldots,b_{m+1}$ wie oben durch die $v_i$ ausdrücken und analog folgern, dass die Menge $\{b_1,\ldots,b_{m+1}\}$ linear abhängig ist. Dies widerspricht aber der Basis-Eigenschaft.

````

Wir sehen insbesondere, dass jede Basis eines Vektorraums die gleiche Anzahl an Elementen haben muss, sobald eine endliche Basis existiert. Wir sprechen dann von der Dimension eines Vektorraums, die wir gleich der Anzahl der Basiselemente setzen. Ist $|B|$ nicht endlich, so sprechen wir von einem unendlich-dimensionalen Vektorraum. In einem Raum der Dimension $n$ können (und werden) wir immer jedes Element als Linearkombination aller $n$ Basiselemente schreiben und ggf. Koeffizienten gleich Null setzen.
Im Allgemeinen sehen wir auch, dass die Entwicklung von $V$ in einer Basis, d.h. eine Linearkombination aus Basiselementen, eindeutig ist:

````{prf:theorem}
Sei $V$ ein Vektorraum mit Basis $B$ und $v \neq \in V$. Dann existiert genau ein $n \in \N$ und eine Teilmenge $\{b_i\}_{i=1,\ldots,n} \subset V$ sowie Koeffizienten $\lambda_i \in \R$ mit

```{math}
 v =  \sum_{i=1}^n \lambda_i b_i .
```

````

````{prf:proof}
 Sei
```{math}
 v = \sum_{i=1}^n \lambda_i b_i = \sum_{j=1}^m \lambda_j' b_j'
```

mit $b_j' \in B$. Dann gilt mit $\lambda_{n+i} = -\lambda_i'$ und $b_{n+i}=-b_i'$
```{math}
 \sum_{i=1}^{n+m} \lambda_i b_i = 0.
```

Wegen der linearen Unabhängigkeit der Basis folgt dann aber $v=0$. 
````

Wir definieren nun noch die Summe zweier Vektorräume $V$ und $W$, die beide Unterräume eines größeren Raums $U$ sind, als

```{math}
 V+W = \{ v + w ~|~ v \in V, w \in W \}.
```

````{prf:example}
Sei
```{math}
 V= \{(x,0)~|~x \in  \R \}, \qquad W= \{(0,y)~|~Y \in  \R \},
```

dann gilt  $V+W = \R^2$.  
````

Analog definieren wir $\sum_{i=1}^m V_i$ für mehrere Vektorräume   $V_i$.Eine Summe von Vektorräumen heisst _\2_, wenn für jedes $w \in \sum_{i=1}^m V_i$ eine eindeutige Zerlegung$w=\sum_{i=1}^n v_i$, $v_i \in V_i$ existiert. Wir schreiben dann für direkte Summe zweier Vektorräume $V$ und $W$ auch $V \oplus W$.


````{prf:lemma}
Seien $V$ und $W$ Vektorräume mit Summe $V+W$. Die Summe ist direkt genau dann, wenn $V \cap W = \{0\}$.
````

````{prf:proof}
 Wir zeigen die äquivalente Aussage $V \cap W \neq \{0\}$ genau dann, wenn die Summe $V+W$ nicht direkt ist. Sei $w \neq 0, w \in V \cap W$. Dann ist wegen der Vektorraumeigenschaft auch $-w \in W$. Damit hat
```{math}
 0  = 0 + 0 = w + (-w) \in V + W
```
eine nichteindeutige Darstellung als Summe. Sei umgekehrt die Summe nicht direkt, dann gibt es $v_1,v_2 \in V$, $v_1 \neq v_2$ and $w_1, w_2 \in W$, $w_1 \neq w_2$ mit

```{math}
 v_1 + w_1 = v_2 + w_2.
```

Nun definieren wir $v = v_1-v_2 = w_2 -w_1$ und sehen sofort $v \in V\cap W \setminus\{0\}$.  
````
