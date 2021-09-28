# Riemann Integral

Da die Obersummen mit feiner werdender Zerlegung kleiner und die Untersummen größer werden, ist es naheliegend im Grenzwert auf die kleinsten Ober- bzw. größten Untersummen zu schauen. Diese existieren nicht unbedingt, aber zumindest das Infimum bzw. Supremum.

````{prf:definition}
Sei $f:[a,b] \rightarrow \R$ beschränkt. Dann heißt

```{math}
 O(f) = \inf\{ O(f,T)~|~ T \in {\cal E} \} 
```

Oberintegral und

```{math}
 U(f) =  \sup\{ U(f,T)~|~ T \in {\cal E} \} 
```

Unterintegral.
Gilt $O(f) = U(f)$, dann heißt $f$ integrierbar (im Sinn von Riemann) und man nennt

```{math}
 \int_a^b f(x)~dx := O(f) = U(f)
```

das Integral von $f$ im Intervall $[a,b]$.
````

```{margin} Bernhard Riemann
[Georg Friedrich Bernhard Riemann](https://de.wikipedia.org/wiki/Bernhard_Riemann) (\* 17. September 1826 in Breselenz bei Dannenberg (Elbe); † 20. Juli 1866 in Selasca bei Verbania am Lago Maggiore) war ein deutscher Mathematiker.
```

Im obigen Beispiel der Heaviside-Funktion sehen wir sofort $O(f)=U(f)=1$ und damit die Integrierbarkeit und
$\int_{-1}^1 f(x)~dx = 1$.
Wir beachten, dass allgemein bei einer beschränkten Funktion gilt

```{math}
O(f) \leq (b-a) \sup_{t \in [a,b]}f(t) \leq  (b-a) \sup_{t \in [a,b]} \vert f(t) \vert
```

und

```{math}
U(f) \geq (b-a) \inf_{t \in [a,b]}f(t) \leq -  (b-a) \sup_{t \in [a,b]} \vert f(t) \vert .
```

Darüber hinaus gilt wegen der Eigenschaft $U(f,T') \leq O(f,T)$ für alle $T,T'$ auch $U(f) \leq O(f)$.

````{prf:example}
Sei $f:[0,1] \rightarrow \R$ definiert durch $f(x) =1$ für $x\in \Q$ und $f(x)=0$ für $x \notin \Q$. Dann ist bei jeder Zerlegung $\sup_{t \in [t_i,t_{i+1}]}(f(t)) =1$ und $\inf_{t \in [t_i,t_{i+1}]}(f(t))=0$, da jedes Teilintervall sowohl reelle als auch rationale Zahlen enthält. Damit ist auch $O(f)=1$ und $U(f) =0$, die Funktion ist also nicht integrierbar.
````

Wir haben gesehen, dass Ober- und Untersummen einige Eigenschaften nahe an der Linearität erfüllen. Diese ist im Grenzwert des Integrals dann gegeben:

````{prf:lemma}
Sei ${\cal I}$ die Menge der integrierbaren Funktionen auf dem Intervall $[a,b]$. dann ist ${\cal I}$ ein Vektorraum. Die Abbildung

```{math}
I: {\cal I} \rightarrow \R, f \mapsto \int_a^b f(x)~dx
```

ist linear, d.h.,

```{math}
 \int_a^b (f(x)+g(x))~dx = \int_a^b f(x)~dx + \int_a^b g(x)~dx,
```

und

```{math}
 \int_a^b c f(x)~dx = c \int_a^b f(x)~dx
```

für alle $c \in \R$. Darüber hinaus ist die Abbildung $I$ monoton, d.h. falls $f \geq g$ (d.h. $f(x) \geq g(x)$ für alle $x\in[a,b]$) gilt, dann folgt $\int_a^b f(x)~dx \geq \int_a^b g(x)~dx. $
````

````{prf:proof}
Wie benutzen die Eigenschaften der Unter- und Obersummen und erhalten

```{math}
 U(f,T') + U(g,T') \leq U(f+g,T') \leq O(f+g,T) \leq O(f,T) + O(g,T) .
```

Mit der Integrierbarkeit von $f$ und $g$ folgt daraus

```{math}
 \int_a^b f(x)~dx + \int_a^b g(x)~dx \leq U(f+g) \leq O(f+g) \leq \int_a^b f(x)~dx + \int_a^b g(x)~dx.
```

Damit ist

```{math}
 U(f+g) = O(f+g) = \int_a^b f(x)~dx + \int_a^b g(x)~dx,
```

also ist $f+g$ integrierbar und es gilt die gewünschte Eigenschaft für die Summe.
Ist $c \geq 0$, dann wissen wir für alle Zerlegungen
$ U(cf,T) = c U(f,T)$, also auch $U(cf) = c U(f)$. Analog folgt $O(cf) = c O(f)$ und damit für integrierbare $f$ auch die
Integrierbarkeit von $c f$ mit

```{math}
  \int_a^b c f(x)~dx = U(cf) = O(cf) = c  \int_a^b f(x)~dx.
```

Ist $c \leq 0$, dann benutzen wir

```{math}
 U(cf,T) = U(-(-c)f,T) = _- O((-c)f,T) = - (-c) O(f,T) = c O(f,T)
```

und analog $O(cf,T) = c U(f,T)$. Damit folgern wir

```{math}
 U(cf) = \inf_T U(cf,T) = \inf_T (c O(f,T)) = c \sup_T O(f,t) = c \int_a^b f(x)~dx
```

und analog $O(cf) = \int_a^b f(x)~dx $. Also ist $cf$ integrierbar und es gilt

```{math}
  \int_a^b c f(x)~dx = c \int_a^b f(x)~dx.
```

Für die Monotonie genügt wegen der Linearität zu zeigen, dass $\int_a^b f(x)~dx \geq 0$ für nichtnegative Funktionen $f$ gilt. Dies folgt aber direkt aus $U(f,T) \geq 0$ für alle $T$. $\square$
````

Wir haben vorher schon angekündigt, dass wir das Integral als Differenz der Flächen unter positivem und negativem Teil der Funktion sehen wollen. Um dies präziser zu machen definieren wir

```{math}
 f_+(x) = \begin{pmatrix} f(x) & f(x) \geq 0 \\ 0 & \text{sonst} \end{pmatrix}.
```

und

```{math}
  f_-(x) = \begin{pmatrix}-f(x) & f(x) \leq 0 \\ 0 & \text{sonst} \end{pmatrix}.
```

Dann ist $f = f_+ - f_-$ und $|f|=f_+ + f_-$. Man kann zeigen, dass die Integrierbarkeit von $f$ äquivalent zur Integrierbarkeit von $f_+$ und $f_-$ ist und es gilt wegen der Linearität auch

```{math}
 \int_a^b f(x)~dx = \int_a^b f_+(x)~dx - \int_a^b f_-(x)~dx.
```

Eine weitere interessante Eigenschaft, die wir hier ohne Beweis angeben, ist die Additivität des Integrals bezüglich Teilintervallen: Sei $f$ auf $[a,c]$ integrierbar und $b \in (a,c)$, dann sind die Einschränkungen von $f$ auch auf $[a,b]$ und $[b,c]$ integrierbar und es gilt

```{math}
 \int_a^c f(x)~dx =  \int_a^b f(x)~dx + \int_b^c f(x)~dx .
```

Wir haben bisher die Klasse der integrierbaren Funktionen eingeführt und wenige Beispiele kennen gelernt. Der folgende Satz zeigt, dass diese Klasse sehr viele Funktionen enthält:

````{prf:theorem}
Sei $f:[a,b] \rightarrow \R$ stetig. Dann ist $f$ integrierbar.
````

````{prf:proof}
 $f$ ist stetig, damit auf dem kompakten Intervall $[a,b]$ sogar gleichmäßig stetig. Also gibt es für jedes $\epsilon >0 $ ein $\delta > 0$, sodass für alle $x,y$ mit $|x-y| < \delta$ gilt:

```{math}
 \vert f(x) - f(y) \vert < \frac{\epsilon}{b-a}.
```

Sei $t_i = a + \frac{b-a}{n} i$ mit $n > \frac{b-a}\delta$. Dann gilt für alle $x,y \in [t_i,t_{i+1}]$ auch $|x-y| < \delta$, somit folgt
$S_i - s_i < \frac{\epsilon}{b-a}$. Also erhalten wir

```{math}
 0 \leq O(f,T) - U(f,T) = \sum_{i=0}^{n-1} (t_{i+1}-t_i)(S_i-s_i) < \sum_{i=0}^{n-1} \frac{b-a}{n} ~ \frac{\epsilon}{b-a} = \epsilon.
```
Daraus folgern wir dann auch $O(f) = U(f)$, also ist $f$ integrierbar. $\square$
````
