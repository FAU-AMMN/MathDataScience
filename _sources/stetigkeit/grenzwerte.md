# Grenzwerte von Funktionen

Wir betrachten nun einige Grenzwerte von Funktionen. Dazu benötigen wir zunächst das Konzept des Häufungspunkts einer Menge. Wir nennen einen Punkt  $y \in M \subset X$ einer Teilmenge eines metrischen Raums $X$ Häufungspunkt von $N \subset M$, wenn eine Folge $y_n$ in $N$ existiert mit $y= \lim y_n$. So ist etwa jedes $y \in \R$ Häufungspunkt von $\Q$. Man kann leicht zeigen, dass $M$ genau dann abgeschlossen ist, wenn $M$ alle seine Häufungspunkte enthält.

````{prf:definition}
Sei $f: X \rightarrow Y$ eine Funktion zwischen metrischen Räumen und $x \in X$ Häufungspunkt der Menge $M \subset X$. Dann hat die Funktion $f: M \rightarrow Y$ in $x \in X$ den Grenzwert $y$, wenn für jede Folge $x_n \rightarrow x$ gilt $f(x_n) = y$.
````

````{prf:example} 
Sei $f(x) =cx$ für $M = \Q$. Dann ist für $x \in \R$ und $y=cx$ auch $y$ ein Grenzwert von $f$ bei $x$.
````

````{prf:definition}
Eine auf $D \subset \R$ definierte Funktion besitzt den rechtsseitigen Grenzwert $y$ bei $x \in \R \cup \{-\infty\}$, wenn $x$  Häufungspunkt von $D_x^+=D \cup (x,\infty)$ ist und $y$ Grenzwert von $f$ in $D_x^+$ ist. D.h. für alle Folgen $(x_n) \subset D_x^+$ mit $x_n \rightarrow x$ gilt $f(x_n) \rightarrow y$.Analog definiert man den linksseitigen Grenzwert bei $x \in \R \cup \{+\infty\}$ mit $D_x^-=D \cup (-\infty,x)$.
````

````{prf:example}
Die Heaviside-Funktion hat in $x=0$ den rechtsseitigen Grenzwert $1$ und den linksseitigen Grenzwert $0$.
````

Eine reelle Funktion ist stetig in $x$ genau dann, wenn der rechts- und linksseite Grenzwert existieren und übereinstimmen.
