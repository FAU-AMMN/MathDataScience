Integralrechnung
===

Im Folgenden wollen wir uns mit der Integration von Funktionen $f:[a,b] \rightarrow \R$ beschäftigen. Für nichtnegative Funktionen soll das Integral intuitiv der Fläche unter der Funktion entsprechen, für allgemeinere Funktionen wollen wir die Differenz aus der Flächen definiert durch den positiven und negativen Teil der Funktion (den wir später noch genau definieren werden).  Um eine Fläche zu approximieren, können wir eine Zerlegung in Rechtecke verwenden, deren Fläche wir elementar als Produkt der Seitenlängen erhalten. Die Rechtecksseiten legen wir parallel zu den Koordinatenachsen, d.h. die erste Seite ist ein Abstand der Argumente, die zweite Seite entspricht im wesentlichen einem Funktionswert.
Wir führen dazu Zerlegungen

```{math}
 a = t_0 < t_1 < \ldots < t_n = b
```

ein, und schreiben $T=\{t_0,\ldots,t_n\}$. Die Menge der Zerlegungen eines Intervalls ist gegeben durch

```{math}
 {\mathcal E} = \{ T \subset [a,b]~|~ a,b \in T, \vert T \vert < \infty\}.
```

Eine Zerlegung $T$ heißt feiner als $T'$, wenn $T' \subset T$. Wir denken uns $T$ identifiziert mit den Teilintervallen $[t_i,t_{i+1}]$, $i=0,\ldots,n-1$. Diese werden wir als erste Seiten der Rechtecke verwenden, die zweite erhalten wir aus den Funktionswerten. Der klassische Ansatz zum Riemann-Integral ist es dabei zwei Rechtecke zu verwenden, ein möglichst großes und ein möglichst kleines (intuitiv mit dem maximalen und dem minimalen Funktionswert in $[t_i,t_{i+1}]$). Rechnen wir dazu (mit Vorzeichen) die Summe der Rechtecksflächen aus, dann erhalten wir die sogenannten Ober- und Untersummen

\begin{align*}
O(f,T) &= \sum_{i=0}^{n-1} (t_{i+1} - t_i) S_i(f) &S_i(f) =  \sup_{t \in  [t_i,t_{i+1}]} f(t), \\
U(f,T) &= \sum_{i=0}^{n-1} (t_{i+1} - t_i) s_i(f) &s_i(f) =  \inf_{t \in  [t_i,t_{i+1}]} f(t).
\end{align*}

Aus der Definition ist klar, dass $s_i \leq S_i$ und damit

```{math}
 U(f,T) \leq O(f,T) \qquad \forall T \in {\mathcal E}.
```

Wir beachten, dass im Fall einer stetigen Funktion, bei der im kompakten Intervall $[t_i,t_{i+1}]$ ja immer Minimum und Maximum existieren, auch wirklich

```{math}
 S_i(f) =  \max_{t \in  [t_i,t_{i+1}]} f(t), \qquad s_i(f) =  \min_{t \in  [t_i,t_{i+1}]} f(t)
```

gilt, d.h. wir bilden wirklich Rechtecke mit dem größten bzw. kleinsten Funktionswert. Die Definition mit Supremum und Infimum ist aber auch für nichtstetige Funktionen geeignet.

````{prf:example}
Sei $f:[-1,1] \rightarrow \R$ die Heaviside-Funktion, d.h. $f(x) =1 $ für $x \geq 0$ and $f(x) = 0$ für $x < 0$. Hier können wir die Fläche unter der Funktion direkt als Rechteck berechnen und erhalten also $1$ als korrekten Wert des Integrals.
Sei $k$ der maximale Index, sodass $t_k < 0$. Dann gilt

```{math}
  O(f,T) = \sum_{i=k}^{n-1} (t_{i+1} - t_i) = 1 - t_k, \qquad U(f,T) = \sum_{i=k+1}^{n-1} (t_{i+1} - t_i) = 1 - t_{k+1}. 
```

Damit sehen wir

```{math}
 U(f,T) \leq 1 \leq O(f,T).
```

Andererseits kann $O(f,T)$ beliebig nahe an $1$ kommen, wenn $t_k$ nahe genug bei $0$ liegt, während $U(f,T)$ sogar exakt gleich $1$ ist, wenn $t_{k+1} = 0$ gilt. Also ist das Integral der größtmögliche Wert der Untersummen bei allen möglichen Zerlegungen $T$ und das Infimum der Obersummen aller möglichen Zerlegungen. Dies werden wir später als Definition verwenden.
````

````{prf:lemma}
Die Unter- und Obersummen einer Funktion $f$ haben die folgenden Eigenschaften:

* $i)$ $\forall T \in {\mathcal E}: U(-f,T) = - O(f,T)$.

* $ii)$ $\forall T \in {\mathcal E}, c \geq 0: U(cf,T) = c U(f,T)$ und $O(cf,T) = c O(f,T).$

* $iii)$ $\forall T' \subset T \in {\cal E}: U(f,T) \geq U(f,T')$ und $O(f,T) \leq O(f,T')$.

* $iv)$ $\forall T, T' \in {\mathcal E}: U(f,T) \leq O(f,T')$

* $v)$ Für eine weitere Funktion $g$ gilt

```{math}
\forall T \in {\mathcal E}: U(f+g,T) \geq U(f,T) + U(g,T), \quad O(f+g,T) \leq O(f,T) + O(g,T).
```

````

````{prf:proof}

**Ad $i)$:**

Folgt direkt aus

```{math}
\inf_{t \in [t_i,t_{i+1}]}(-f(t)) = - \sup_{t \in [t_i,t_{i+1}]}(f(t))
```

**Ad $ii)$:**

Gilt wegen

```{math}
 \inf_{t \in [t_i,t_{i+1}]} (c f(t)) = c \inf_{t \in [t_i,t_{i+1}]} f(t) \qquad \sup_{t \in [t_i,t_{i+1}]} (c f(t)) = c \sup_{t \in [t_i,t_{i+1}]} f(t).
```

**Ad $iii)$:**

Gilt $T' \subset T$, dann gibt es für jedes $i$ ein $j(i)$ mit $t_i' =t_{j(i)}$. Damit folgt

\begin{align*} O(f,T') &= \sum_{i=0}^{n'-1} (t_{i+1}' - t_i') \sup_{t \in  [t_i',t_{i+1}']} f(t) =\sum_{i=0}^{n'-1} (t_{j(i+1)} - t_{j(i)}) \sup_{t \in  [t_{j(i)},t_{j(i+1)}]} f(t) \\
&= \sum_{i=0}^{n'-1} \sum_{k=j(i)}^{j(i+1)-1} (t_{k+1} - t_{k}) \sup_{t \in  [t_{j(i)},t_{j(i+1)}]} f(t)  \\
&\geq \sum_{i=0}^{n'-1} \sum_{k=j(i)}^{j(i+1)-1} (t_{k+1} - t_{k}) \sup_{t \in  [t_{k},t_{k+1}]} f(t)   =\sum_{i=0}^{n-1} (t_{k+1} - t_{k}) \sup_{t \in  [t_{k},t_{k+1}]} f(t)  \\ &= O(f,T).
\end{align*}

Der Beweis für Untersummen ist analog.

**Ad $iv)$:**

Sei $T''= T \cup T'$. Dann ist klarerweise $U(f,T'') \leq O(f,T'')$ und mit $iii)$ folgt

```{math}
 U(f,T') \leq U(f,T'') \leq O(f,T'') \leq O(f,T) .
```

**Ad $v)$:**
Folgt aus

```{math}
 \inf (f+g) \geq \inf f + \inf g, \qquad \sup (f+g) \geq \sup f + \sup g.  \square
```

````
