# Mengenlehre und Logik

Ein wichtiges Konzept um Mathematik aufzuschreiben sind sogenannte _Mengen_. Eine Menge ist eine Sammlung unterscheidbarer Objekte, die wir innerhalb der Mengenklammern $\{ \ldots \}$ notieren. Wir unterscheiden endliche Mengen, wie

```{math}
 M_1 =  \{1,2,3\}, \qquad M_2=\{\text{Baum},\text{Wiese}\} ,
```

oder

```{math}
 M_3=\{\text{James}, \text{Davis}, \text{Caruso}, \text{Caldwell-Pope},\text{Green}\}
```

und unendliche Mengen wie natürlichen Zahlen

```{math}
\N =\{0,1,2,3,4,\ldots\}.
```

Dabei ist die Reihenfolge der Elemente unerheblich, also können wir genauso $ M_1 = \{1,3,2\}$ oder $M_1=\{3,2,1\}$ schreiben. Auch $M_1=\{1,2,2,3\}$ ist immer noch die gleiche Menge, da wir nur unterscheidbare Objekte betrachten.
Eine Menge $M$ besteht aus ihren Elementen $x$, wir schreiben $x \in M$. Ist $x$ nicht in $M$ enthalten, so schreiben wir $x \notin M$.

````{prf:definition}
Seien $M$ und $\tilde M$ Mengen, dann heißt $\tilde M$ _Teilmenge_ von $M$, wenn für alle $x \in \tilde M$ folgt, dass $x \in M$ gilt. Gibt es ein $x \in M$ mit $x \notin \tilde M$, dann heißt $\tilde M$ _echte Teilmenge_.
````

Jede Menge hat zumindest eine Teilmenge, die sogenannte leere Menge $\emptyset$. Ein einfaches Beispiel für eine Teilmenge ist $\N \subset \Z$, es ist auch eine echte Teilmenge, da z.b. $-1 \in \Z$ und $-1 \notin \N$.
Wir beachten auch den Unterschied zwischen $x$ und der Menge $\{x\}$. So gilt im obigen Beispiel etwa $1 \in M_1$, aber $\{1\} \subset M_1$.

Wir können (Teil)Mengen auch durch Aussagen definieren. Gegeben eine Menge $M$ und eine Aussage $A(x)$ über Elemente in $x$, die entweder wahr oder falsch ist, erhalten wir

```{math}
 \tilde M = \{ x\in M ~|~A(x)\}
```

als Teilmenge jener Elemente von $M$, für die $A(x)$ wahr ist. Als Beispiel betrachten wir $M_1$ wie oben und

```{math}
 \tilde M_1 = \{x \in M_1 ~|~x \text{ ist gerade.}\} = \{2\}
```

oder als Teilmenge der reellen Zahlen

```{math}
 M = \{ x \in \N~|~x \text{ ist Quadratzahl. }\} = \{0,1,4,9,16,25,\ldots\}.
```

## Mengensysteme und Mengenoperationen

In dem wir Mengen selbst in Mengen stecken, erhalten wir Mengensysteme. Als Beispiel betrachten wir

```{math}
 S = \emptyset,\{1\_,\{1,2\},\{1,2,3\} \}.
```

$S$ ist eine Teilmenge der sogenannten Potenzmenge von $\{1,2,3\}$ Allgemein nennen wir die Menge aller Teilmengen von $M$ die Potenzmenge ${\cal P}(M)$ (oder auch $2^M$). So gilt etwa

```{math}
 {\cal P}(\{1,2,3\}) = \emptyset,\{1\_,\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\}\{1,2,3\} \}.
```

Ist $M$ endlich und bezeichnet $\vert M \vert$ die Anzahl der Elemente in $M$, so hat ${\cal P}(M)$ genau $2^{\vert M \vert}$ Elemente.
Auf Mengensystemen können wir auch Operationen definieren wie etwa den Durchschnitt oder die Vereinigung:

````{prf:definition}
Sei $S$ ein Mengensystem. Dann ist der Durchschnitt definiert als

```{math}
 \bigcap_{M \in S} M = \{x ~|~ \forall M \in S: x \in M \}
```

und die Vereinigung als

```{math}
 \bigcup_{M \in S} M = \{x ~|~ \exists M \in S: x \in M \}.
```

````

Für endliche Systeme $S=\{M_1,M_2,\ldots,M_n\}$ schreiben wir auch

```{math}
 \bigcap_{M \in S} M  = M_1 \cap M_2 \cap \ldots \cap M_n
```

bzw.

```{math}
 \bigcup_{M \in S} M  = M_1 \cup M_2 \cup \ldots \cup M_n.
```

Gilt $M_1 \cap M_2 = \emptyset$, so heißen $M_1$ und $M_2$ disjunkt. Gilt $M_1 \cap M_2 = \emptyset$ für alle $M_1$ und $M_2$ in $S$, so heißen die Elemente von $S$ paarweise disjunkt.
Wir können auch die Teilmengeneigenschaft über den Schnitt definieren:

````{prf:lemma}
$\tilde M \subset M$ gilt genau dann wenn $\tilde M \cap M = \tilde M$
````

````{prf:proof}
$\tilde M  \subset M$ ist äquivalent zu

```{math}
 \forall x \in \tilde M: x \in M,
 
```

dies ist gilt natürlich auch genau dann wenn

```{math}
 \forall x \in \tilde M \cap M: x \in M.
 
```

Die letzte Aussage ist gleichbedeutend mit $\tilde M \cap M = \tilde M$.
$\square$
````

Wir definieren noch einige weitere Operationen auf Paaren von Mengen:

* Die Differenzmenge $M \setminus \tilde M$ ist gegeben durch

```{math}
 M \setminus \tilde M = \{ x \in M ~|~ x \notin \tilde M\}
 
```

* Die symmetrische Differenz $M \Delta \tilde M$ ist gegeben durch

```{math}
 M \Delta \tilde M = (M \setminus \tilde M ) \cup (\tilde M \setminus M)
```

* Das kartesische Produkt zweier Mengen ist die Menge aller geordneten Paare aus Elementen, d.h.

```{math}
 M \times \tilde M = \{ (m,\tilde m) ~|~ m \in M, \tilde m \in \tilde M\}
 
```

Dies kennen wir auch aus der Definition des $\R^2 = \R \times \R$ über zwei kartesische Koordinaten.

Neben Operationen können wir auch sogenannte Relationen auf Paaren von Mengen oder einzelnen Mengen definieren. Dazu konstruieren wir eine neue Menge $R$, in die wir alle geordneten Paare aus $M \times \tilde M$ schreiben, für die eine Relation gelten soll:

````{prf:definition}
Eine Teilmenge $R \subset M \times \tilde M$ heißt Relation zwischen $M$ und $\tilde M$. Eine Teilmenge $R \subset M \times M$ heißt Relation auf $M$.
````

Als Beispiel können wir die Menge $M$ der Bundesliga-Teams betrachten und definieren eine Relation wenn zwei Teams bereits gegeneinander gespielt haben. $R$ besteht also aus allen Spielpaaren $(x,y)$. Wollen wir nicht nach Heim- oder Auswärtsspielen unterscheiden, so schreiben wir neben $(x,y)$ auch $(y,x)$ in $R$.

````{prf:definition}
Eine Relation $R \subset M \times M$ heißt\begin{*ize}
* _reflexiv_, wenn für alle $x \in M$ gilt: $(x,x) \in R$

* _symmetrisch_, wenn $(x,y) \in R$ impliziert: $(y,x) \in R$

* _antisymmetrisch_, wenn $(x,y) \in R$ und $(y,x) \in R$ impliziert, dass $y=x$ gilt

* _transitiv_, wenn aus $(x,y) \in R$ und $(y,z) \in R$ folgt, dass $(x,z)  \in R$ gilt.
\end{*ize
````

Das obige Beispiel der Bundesligamannschaften ist nie reflexiv und nur dann symmetrisch, wenn wir nicht zwischen Heim- und Auswärtsspielen unterscheiden. Als weiteres Beispiel betrachten wir wieder $M_1 = \{1,2,3\}$ und

```{math}
 R=\{(x,y) \in M_1 \times M_1~|~x \leq y\} = \{ (1,1),(1,2),(1,3),(2,2),(2,3),(3,3)\}.
 
```

Diese Relation ist reflexiv, anti-symmetrisch und transitiv.
Relationen mit diesen drei Eigenschaften (Reflexivität, Anti-Symmetrie, Transitivität) nennen wir Ordnungsrelation (oder Halbordnung). Statt $(x,y) \in R$ schreiben wir auch $x \preceq y$. Eine Halbordnung heißt Ordnung, wenn sich alle Paare vergleichen lassen, d.h. es gilt $x \preceq y$ oder $y \preceq x$.

````{prf:example}
Sei $M= \N \setminus \{0\}$ und $R=\{(x,y) \in M \times M~|~x \text{ teilt } y\}$. Dies ist eine Halbordnung auf $\N \setminus 0$, die keine Ordnung ist, da z.B. $2$ und $3$ nicht vergleichbar sind.
````

Eine weitere wichtige Klasse sind Äquivalenzrelationen:

````{prf:definition}
Eine Relation $R \subset M \times M$ heißt Äquivalenzrelation, wenn sie reflexiv, symmetrisch und transitiv ist. Für $(x,y) \in R$ schreiben wir dann auch $x \sim y$.
````

````{prf:example}
Sei $M= \Z$ und $x \sim y$ wenn
```{math}
x-y \in 2 \Z = \{ 2 z ~|~z \in \Z \}
```

gilt. D.h. $x \sim y$ wenn beide gerade oder beide ungerade sind. In diesem Beispiel kennen wir schon die Einteilung in sogenannte Äquivalenzklassen, nämlich die geraden und die ungeraden Zahlen. Solche kann man auch für allgemeine Äquivalenzrelationen definieren
````

````{prf:definition}
Die von $m \in M$ erzeugte Äquivalenzklasse unter einer Äquivalenzrelation ist gegeben durch

```{math}
 [m] = \{ n \in M ~|~n \sim m\}.
```

Jedes Element einer Äquivalenzrelation heißt Repräsentant
````

Im Beispiel der Aufteilung in gerade und ungerade Zahlen sind typische Repräsentanten die Zahlen $0$ (für gerade) und $1$ (für ungerade). Wir wissen auch, dass eine Zahl entweder gerade oder ungerade ist und eine solche Eigenschaft gilt ebenfalls für allgemeine Äquivalenzrelationen:

````{prf:lemma}
Gegeben sei eine Äquivalenzrelation $\sim$ auf $M$. Dann ist jedes Element $m \in M$ in genau einer Äquivalenzklasse enthalten. Für alle $m,n \in M$ gilt entweder

```{math}
[m] = [n] \quad \text{oder} \quad [m] \cap [n] = \emptyset .
```

````

````{prf:proof}
 $[m]$ ist wegen der Reflexivität nicht leer ($m \in [m]$) und jedes Element ist damit auch in mindestens einer Äquivalenzklasse enthalten. Sei nun $m \in [n]$ für $n \neq m$, dann folgt wegen der Symmetrie auch $n \in [m]$. Wegen der Transitivität gilt

```{math}
p \in [m] \Leftrightarrow p \sim m \Rightarrow p \sim n \Rightarrow p \in [n]
```

und

```{math}
 p \in [n] \Leftrightarrow p \sim n \Rightarrow p \sim m \Rightarrow p \in [m].
```

Also folgt $[m]=[n]$. Sei nun $m \not\sim n$. Dann gilt für $p \sim m$ auch $p \not\sim n$, da sonst wegen der Transitivität $m \sim n$ folgt. Also gilt für jedes $p \in [m]$ auch $p \notin [n]$. Mit exakt demselben Argument folgern wir aus $p \in [n]$ dann $p \notin [m]$. Damit ist $[n] \cap [m] = \emptyset$
````

Bei der Relation

```{math}
 x \sim y \Leftrightarrow x-y \in 2 \Z ,
```

gibt es zwei Äquivalenzklassen, die geraden und die ungeraden Zahlen. Allgemeiner gibt es für $n \in \N \setminus \{0,1\}$ und

```{math}
x \sim y \Leftrightarrow x - y \in n \Z
```

genau $n$ Äquivalenzklassen, die charakterisiert sind durch den Rest bei der Division durch $n$, d.h. die Repräsentanten $0,1,\ldots,n-1$. Man spricht deshalb auch von Restklassen.

Für eine Relation $R$ auf $M$ (oder kurz $\sim$) bezeichnen wir mit der Faktormenge $M/R$ (oder $M/\sim$) die Menge der Äquivalenzklassen. Wir beachten, dass wir jede Äquivalenzklasse mit einem beliebigen Repräsentanten identifizieren können. So gilt bei der Einteilung in gerade und ungerade Zahlen $M/\sim = \{[0],[1]\}$, was wir auch mit $\{0,1\}$ identifizieren können.

## Abbildungen

Eine Abbildung oder Funktion $f:M_1 \rightarrow M_2$ ordnet jedem Element $m_1 \in M_1$ ein Element $m_2 =f(m_1) \in M_2$ zu.
Die Bedeutung von _Zuordnung_ ist zwar relativ klar, mathematisch sauberer  ist eine Betrachtung als Mengen bzw. wieder als spezielle Relation:

````{prf:definition}
Eine Relation $f \subset M_1 \times M_2$ heißt Funktion (oder Abbildung) von $M_1$ nach $M_2$, wenn

* $i)$ $D(f) = \{m_1 \in M_1~|~\exists m_2 \in M_2: (m_1,m_2) \in f \} = M_1 $

* $ii)$ $(m,n) \in f$ und $(m,p) \in f$ impliziert $n=p$.
````

Wir nennen $M_1$ den Definitionsbereich und $M_2$ den Bildbereich von $f$.

```{math}
f(M_1) = \{m_2 \in M_2~|~\exists m_1 \in M_1: (m_1,m_2) \in f)\}
```

heißt Wertebereich (oder Bild) von $f$.
Da zu jedem $m_1 \in M_1$ nun genau ein $m_2 \in M_2$ mit $(m_1,m_2) \in f$ existiert, können wir hier auch die Zuordnung $m_2=f(m_1)$ definieren. Damit haben wir die gewohnte Form

```{math}
f: M_1 \rightarrow M_2, m \mapsto f(m),
```

die wir im Folgenden für Funktionen auch meist verwenden werden. Wir beachten, dass die Sichtweise über die Relation dem Funktionsgraphen bestehend aus den Punkten $(m,f(m))$ entspricht.

````{prf:definition}
Eine Funktion $f:M_1 \rightarrow M_2$ heißt

* _surjektiv_, wenn Bildbereich und Wertebereich übereinstimmen, d.h. $f(M_1)=M_2$

* _injektiv_, wenn aus $(m_1,n) \in f$ und $(m_2,n) \in f$ (bzw. $f(m_1) =f(m_2)$) folgt $m_1=m_2$.

* _bijektiv_, wenn sie injektiv und surjektiv ist.
````

Ist $f$ bijektiv, dann erfüllt die Relation

```{math}
 f^{-1} = \{(m_2,m_1) ~|~ (m_1,m_2) \in f\}
```

auch die Eigenschaften einer Funktion und wir nennen $f^{-1}$ die Umkehrfunktion von $f$. Es gilt dann

```{math}
\forall m_1 \in M_1: f^{-1}(f(m_1))=m_1
```

und

```{math}
\forall m_2 \in M_2: f(f^{-1}(m_2))=m_2.
```

Wir beachten, dass $f^{-1}$ als Relation auch definiert ist, wenn $f$ nicht bijektiv ist, $f^{-1}$ ordnet dann jedem $m_2$ eine Teilmenge von $M_1$ zu (die auch leer sein kann).
Die Einschränkung einer Funktion auf $U \subset M_1$ bezeichnen wir mit

```{math}
f|_U = \{ (m_1,m_2) \in f~|~ m_1 \in U\}.
```

## Mächtigkeit von Mengen

Mit Hilfe von Abbildungen können wir die Mächtigkeit, d.h. die Größe, von Mengen vergleichen. Für endliche Mengen ist die Mächtigkeit genau die Anzahl der Elemente, die wir einfach durchzählen können. Dies bedeutet wir konstruieren eine bijektive Abbildung von $\{1,\ldots,n\}$ auf $M$ und schreiben als Mächtigkeit dann $\vert M \vert$. Für die leere Menge setzen wir $\vert \emptyset \vert =0$. Dies können wir allgemeiner zum Vergleich der Mächtigkeit verwenden. Wir sagen, dass zwei Mengen $M_1$ und $M_2$ die gleiche Mächtigkeit haben, wenn es eine Bijektion $f: M_1 \rightarrow M_2$ gibt.
Die _kleinste_ undendliche Menge ist $\N$, wir definieren die Mächtigkeit von $\N$ als $\aleph_0$ (gesprochen Aleph Null) als kleinstes Maß für Unendlichkeit, diese nennen wir erste Kardinalzahl. Mengen $M$, die durch eine Bijektion auf $\N$ abgebildet werden können, nennen wir abzählbar (oder abzählbar unendlich) und schreiben dementsprechend $|M|=\aleph_0$.

````{prf:example}
Es gilt $|\Z|=\aleph_0$. Wir betrachten dazu die bijektive Abbildung $f: \N \rightarrow \Z$,

```{math}
f(n) = 
\begin{pmatrix} \frac{n}2 & \text{falls } n \text{ gerade}\\
- \frac{n+1}2 & \text{falls }n\text{ ungerade} 
\end{pmatrix}.
```
````

````{prf:example}
Sei $M= \N \times \N = \N^2$, dann gilt auch $|M|=\aleph_0$. Wir betrachten dazu die bijektive Abbildung

```{math}
f: M \rightarrow \N, \quad (m,n) \mapsto \frac{1}2(m+n)(m+n+1) + n.
```

Es gilt mit Hintereinanderausführung ähnlicher Abbildung übrigens auch $|\N^n|=\aleph_0$.
````

```{margin} Bertrand Russell
[Bertrand Arthur William Russell](https://de.wikipedia.org/wiki/Bertrand_Russell) (\* 18. Mai 1872 bei Trellech, Monmouthshire, Wales; † 2. Februar 1970 in Penrhyndeudraeth, Gwynedd, Wales) war ein britischer Philosoph, Mathematiker, Religionskritiker und Logiker.
```

Die Mengenlehre stößt an ihre Grenzen, wenn man Selbstbezüge in der Definition von Mengen einbaut. Dies zeigt ein bekanntes Beispiel von Bertrand Russell.


Sei

```{math}
 M=\{ x ~|~x \text{ ist } Menge \}
```

und

```{math}
N = \{x \in M~|~x \notin x\}.
```

Damit können wir die unbeantwortbare Frage _Gilt $N \in N$ ?_ stellen. Nehmen wir an es gilt $N \in N$, dann ist per Definition von $N$ auch $N \notin N$ und umgekehrt. Diese sogenannte Russell'sche Antinomie legt nahe, dass man Selbstbezüge in der Definition von Mengen vermeiden sollte um logisch konsistent zu bleiben.

## Logik und Aussagen

Im Folgenden werden wir nun etwas näher die Aussagenlogik betrachten. Eine Aussage $A$ ist für uns ein Element der Menge $\{\text{wahr},\text{falsch}\}$. Eine Aussageform ist eine Abbildung von einer Menge an Möglichkeiten in die Menge $\{\text{wahr},\text{falsch}\}$. So ist etwa $4$ ist gerade eine (wahre) Aussage, und $x \in N, x$ gerade eine Aussageform. Wir identifizieren im Folgenden meist die Aussage $A$ mit der Abbildung $M_A:M \rightarrow \{\text{wahr},\text{falsch}\}$, solange der Zusammenhang klar ist.
Sind $A,B$ zwei Aussagen, dann können wir mit sogenannten Junktoren neue Aussagen herleiten:

* _Negation:_ nicht $A$, geschrieben $\lnot A$, entspricht der Abbildung, die falsch liefert wenn $A$ wahr liefert und umgekehrt.

* _Konjunktion:_ $A$ und $B$, geschrieben $A \land B$, ist eine Abbildung, die wahr liefert wenn $A$ und $B$ wahr sind, sonst erhalten wir falsch.

* _Disjunktion:_ $A$ oder $B$, geschrieben $A \lor B$, ist eine Abbildung, die falsch liefert wenn $A$ und $B$ falsch sind, sonst erhalten wir wahr.

* _Implikation:_ wenn $A$, dann $B$, geschrieben $A \Rightarrow B$.

* _Äquivalenz:_ $A$ äquivalent zu $B$, $A \Leftrightarrow B$.

Bei zwei Aussagen können wir die Verknüpfung durch Junktoren mit Fallunterscheidungen charakterisieren, die sogenannten Wahrheitstafeln, eine Tabelle der Form

| A        | B        | J(A,B)   |
| :------: | :------: | :------: |
|        W |        W | *        |
|        W | F        | *        |
|        F |     W    | *        |
| F        | F        | *        |

wobei $J(A,B)$ die Junktion bezeichnet. Als Beispiel betrachten wir das logische Und:

:::{table}
:align: center
:widths: grid

| A        | B        | A $\land$ B |
|-------:|-------:|----------:|
| W        | W        | W           |
| W        | F        | F           |
| F        | W        | F           |
| F        | F        | F           |
:::

Mit Hilfe von Wahrheitstafeln können wir auch Verknüpfungen von Junktoren betrachten und deren Äquivalenz zu anderen Formen nachweisen. Als Beispiel betrachten wir $\lnot (A \land B)$.
Die Wahrheitstafel liefert

| A   | B  | $\lnot (A \land B)$ | $(\lnot A) \lor (\lnot B)$|
| :-- | :- | :------------------ | :------------------------ |
| W   | W  | F                   | F                         |
| W   | F  | W                   | W                         |
| F   | W  | W                   | W                         |
| F   | F  | W                   | W                         |

Damit sehen wir

```{math}
\lnot (A \land B) = (\lnot A) \lor (\lnot B).
```

Wie bereits vorher verwendet können wir Quantoren wie $\forall$ und $\exists$ verwenden und diese auch verknüpfen.

* $\forall x \in M: A(x) $ bedeutet, dass die Aussageform $A$ für alle $x$ in $M$ wahr ist.

* $\exists x \in M: A(x) $ bedeutet, dass die Aussageform $A$ für zumindest ein $x$ in $M$ wahr ist (oder äquivalent nicht für alle $x \in M$ falsch ist).

Mit offensichtlichen Ergebnissen erhalten wir auch die Negation, Konjunktion etc. von Quantoren. So gilt etwa

```{math}
\lnot( \forall x \in M: A(x) ) = \exists x \in M: \lnot A(x)
```

und

```{math}
\lnot( \exists x \in M: A(x) ) = \forall x \in M: \lnot A(x)
```
