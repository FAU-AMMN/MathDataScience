# Folgen und Konvergenz

Eine Folge $(x_n)$ reeller Zahlen ist eine Zuordnung $x_n \in \R$ zu jedem $n \in \N$. Allgemeiner kann man auch Folgen anderer Objekte betrachten, aber wir belassen es hier bei reellen Folgen. Diese dienen uns als Einstieg ins _Unendliche_, wir wollen daran ein wenig das Konzept von Konvergenz und Grenzwerten beleuchten.

Wir interessieren uns besonders für die Konvergenz (oder auch Divergenz) von Folgen, d.h. das Verhalten für $n$ gegen unendlich (geschrieben als $n \rightarrow \infty$). Eine _konvergente_ Folge besitzt einen Grenzwert $\overline{x}$
(geschrieben $x_n \rightarrow \overline{x}$), wenn für größer werdende $n$ die Folgenglieder dem Wert $\overline{x}$ immer näher kommen. Nun stellt sich aber die Frage wie wir diese Aussage mathematisch präzise formalisieren können. Zunächst erkennen wir, dass _immer näher kommen_  bedeutet, dass

```{math}
:label: eq:folgengrenzewert 
\vert x_n - \overline{x} \vert < \epsilon
```

für $\epsilon > 0$ beliebig klein und $n$ hinreichend groß gilt. _Beliebig klein_ und  _hinreichend groß_ sind mathematisch aber immer noch zu schwammige Begriffe, die wir weiter präzisieren müssen. Tatsächlich tun wir dies, indem wir uns einen Zweifler an der Konvergenz vorstellen, der ein $\epsilon > 0$ vorgibt und wir müssen {eq}`eq:folgengrenzewert` nun für alle $n$ groß genug erfüllen (wobei das kleinste $n$, für das {eq}`eq:folgengrenzewert` gelten muss natürlich von $\epsilon$ abhängen kann). Wir können also folgende Definition geben:

````{prf:definition}
Eine reelle Folge $(x_n)$ heißt konvergent gegen den Grenzwert $\overline{x}$, geschrieben 

```{math}
x_n \rightarrow \overline{x} \qquad \text{oder} \lim_{n \rightarrow \infty} x_n = \overline{x},
```

genau dann, wenn für alle $\epsilon > 0$ ein $n_0 \in \N$ existiert, sodass für alle $n \geq n_0$ {eq}`eq:folgengrenzewert` erfüllt ist. 
Eine Folge heißt konvergent, wenn es ein $\overline{x}$ gibt, sodass $x_n \rightarrow x$.
````

Bei dieser Formalisierung haben wir zwei wesentliche logische Aussagen verwendet, nämlich _für alle_ und _es existiert_. Diese werden wir in der Vorlesung durch sogenannte Quantoren abkürzen:

* $\forall \equiv$ für alle,

* $\exists \equiv$ es existiert.

Damit können wir obige Aussage kompakt als

```{math}
\forall \epsilon > 0 ~\exists n_0 \in \N ~\forall n \geq n_0: ~\vert x_n - \overline{x} \vert < \epsilon
```

schreiben. Dabei haben wir den Doppelpunkt verwendet um die eigentliche Aussage zu beginnen, _:_ ersetzt also das sprachliche _gilt_.

Ist eine Folge nicht konvergent, so nennen wir sie _divergent_. Wir beachten, dass nach unserer Definition $\overline{x} \in \R$ gelten muss. Es gibt also im strengen Sinn keine Konvergenz $x_n \rightarrow \infty$ (oder analog $x_n \rightarrow -\infty$), wie man intuitiv zum Beispiel von der Folge $(x_n) = (n)$ erwarten würde. Das Problem dabei ist, dass $x_n$ ja dem Wert $\overline{x}=\infty$ nicht beliebig nahe kommt, der Unterschied ist immer unendlich groß. Deshalb sagen wir $x_n$ konvergiert gegen unendlich, $x_n \rightarrow \infty$, genau dann wenn

```{math}
 \forall \epsilon > 0 ~\exists n_0 \in \N ~\forall n \geq n_0: ~ x_n > \epsilon .
```

Hier hat $\epsilon$ eine andere Rolle als vorhin, da wir uns ja dafür interessieren, dass $\epsilon$ beliebig groß wird (nicht beliebig klein wie bei der üblichen Konvergenz), die Definition über alle $\epsilon$ deckt dies aber gut ab. Als Übung lassen wir den Fall einer Definition von $x_n \rightarrow -  \infty$. Zum Verständnis betrachten wir einige Beispiele:

````{prf:example}
Sei $(x_n)$ die konstante Folge $x_n = 1 $ für alle $n$. Diese konvergiert natürlich gegen $\overline{x} = 1$. Es gilt tatsächlich:

```{math}
 \forall \epsilon > 0 ~\forall n \geq 0:  \vert x_n - \overline{x}\vert < \epsilon, 
```

da $\vert x_n - \overline{x}\vert =0$, d.h. wir können immer $n_0=0$ wählen.
````

````{prf:example}
Sei $(x_n)$ die  Folge $x_n = \frac{1}n $ für alle $n>0$ mit $x_0$ beliebig definiert. Diese konvergiert natürlich gegen $\overline{x} = 0$. Es gilt  

```{math}
 \forall \epsilon > 0 ~\forall n \geq n_0:  \frac{1}n = \vert x_n - \overline{x}\vert < \epsilon, 
```

wenn $n > \frac{1}\epsilon$ ist. Wir wählen also $n_0$ als die nächstgrößte natürliche Zahl zu $\frac{1}\epsilon$, damit erhalten wir die Konvergenz. 
````

````{prf:example}
Sei $(x_n)$ die  Folge $x_n = (-1)^n $ für alle $n\geq 0$. Diese alternierende Folge divergiert. Ist $\overline{x} = 1$, dann gilt für ungerades $n$ beliebig groß $\vert x_n - \overline{x}\vert = 2$, also erhalten wir mit $\epsilon =1$ bereits eine Verletzung der Konvergenzbedingung. Ist $\overline{x} \neq 1$, so gilt für gerades $n$ immer $\vert x_n - \overline{x} \vert =  \vert 1-\overline{x} \vert \neq 0$. Damit erhalten wir eine Verletzung der Konvergenzbedingung mit $\epsilon = \frac{\vert 1-\overline{x} \vert}2$.

In diesem Fall gibt es aber zwei konvergente Teilfolgen $(y_n) = (x_{2n})$ mit Grenzwert $1$ und $(z_n) = (x_{2n+1})$ mit Grenzwert $-1$. Wie werden später noch häufiger mit konvergenten Teilfolgen zu tun haben. 
````

````{prf:example}
Sei $(x_n)$ die  Folge $x_n = \frac{n^2+1}{2n^2+1} $ für alle $n\geq 0$. Diese konvergiert  gegen $\overline{x} = \frac{1}2$. Es gilt  

```{math}
 \vert x_n - \overline{x}\vert = \frac{1}{4n^2+2}, 
```

dies ist kleiner $\epsilon$, wenn $n \geq n_0 > \sqrt{\frac{1}{4\epsilon}-\frac{1}2}$ (bzw. $n_0 \geq 0$ wenn $\epsilon > \frac{1}2$) gilt.  
````

Als Verallgemeinerung des letzten Beispiels können wir zeigen, dass

```{math}
 \frac{x_n}{y_n} \rightarrow \frac{\overline{x}}{\overline{y}} 
```

gilt, wenn $x_n \rightarrow \overline{x}$ und $y_n \rightarrow \overline{y} \neq 0$. Dazu machen wir mit Hilfe der Dreiecksungleichung folgende Abschätzung:

```{math}
\left\vert \frac{x_n}{y_n} -\frac{\overline{x}}{\overline{y}} \right\vert =
\left\vert \frac{x_n}{y_n} -\frac{\overline{x}}{y_n}+\frac{\overline{x}}{y_n}-\frac{\overline{x}}{\overline{y}} \right\vert \leq 
\left\vert \frac{x_n}{y_n} -\frac{\overline{x}}{y_n}\right\vert+\left\vert\frac{\overline{x}}{y_n}-\frac{\overline{x}}{\overline{y}} \right\vert = \frac{1}{\vert y_n \vert} \vert x_n - \overline{x}\vert+
\frac{\vert \overline{x} \vert}{\vert \overline{y} \vert~\vert y_n \vert} \vert y_n - \overline{y}\vert.
```

Gilt nun

```{math}
  \vert x_n - \overline{x}\vert < \epsilon_1, \qquad  \vert y_n - \overline{y}\vert < \epsilon_2 
```

Dann folgt mit der Dreiecksungleichung auch

```{math}
 \vert y_n \vert \geq \vert \overline{y}\vert - \vert y_n - \overline{y}\vert \geq \vert \overline{y}\vert - \epsilon_2 . 
```

Damit ist

```{math}
 \left\vert \frac{x_n}{y_n} -\frac{\overline{x}}{\overline{y}} \right\vert \leq \frac{\epsilon_1}{\vert \overline{y} \vert - \epsilon_2} + \frac{\overline{x}\epsilon_2}{\overline{y}(\vert \overline{y} \vert - \epsilon_2)}  . 
```

Nun wählen wir

```{math}
 \epsilon_1 <\frac{\vert \overline{y} \vert }4,  \qquad \epsilon_2 < \min\{\frac{\vert \overline{y} \vert }2, \frac{\vert \overline{y} \vert^2}{4 \vert \overline{x} \vert} \epsilon \} , 
```

dann gibt es $n_0^1$ und $n_0^2$, sodass

```{math}
 \forall n > n_0^1:~\vert x_n - \overline{x} \vert < \epsilon_1 
```

und

```{math}
 \forall n > n_0^2:~\vert y_n - \overline{y} \vert < \epsilon_2 .
```

Nun sei $n_0 = \max\{n_0^1,n_0^2\}$, dann folgt durch Einsetzen der Schranken für $\epsilon_1$ und $\epsilon_2$ in die obige Abschätzung

```{math}
  \left\vert \frac{x_n}{y_n} -\frac{\overline{x}}{\overline{y}} \right\vert < \epsilon 
```

für alle $n \geq n_0$. Als Übung überlassen wir den Fall $\overline{x} \neq 0$ und $\overline{y}=0$, hier erhält man für den Grenzwert Konvergenz gegen $+\infty$ oder $-\infty$ je nach Vorzeichen von $\overline{x}$.

````{prf:example}
Sei $(x_n)$ die  Folge $x_n = n $ für alle $n\geq 0$. Es gilt $x_n \rightarrow \infty$, da $\vert x_n \vert > \epsilon$ für $n\geq n_0$, wenn wir $n_0$ als die nächstgrößte natürliche Zahl zu $\epsilon$ wählen. 
````

Wir können die Definition der Konvergenz auch direkt auf Folgen $x_n \in \R^N$ übertragen wenn wir den Betrag durch die (Euklidische Norm) ersetzen:

```{math}
 \forall \epsilon > 0 ~\exists n_0 \in \N ~\forall n \geq n_0: ~\Vert x_n - \overline{x} \Vert < \epsilon 
```

````{prf:example}
Als Beispiel betrachten wir eine Folge $(x_n)$ im $\R^2$ gegeben durch $x_n= \veczwei{\frac{n}{n+1}}{2^{-n}}$. Dies konvergiert gegen $\overline{x}=\veczwei{1}{0}$. Es gilt

```{math}
 \Vert x_n - \overline{x} \Vert = \sqrt{\frac{1}{(n+1)^2} + 2^{-2n}} \leq \frac{\sqrt{2}}{n+1} 
```

für $n \geq 1$, da $2^n \geq n+1$. Also folgt 

```{math}
 \Vert x_n - \overline{x} \Vert < \epsilon, 
```

für $n \geq n_0$, wenn $n_0$ größer als $\frac{\sqrt{2}}\epsilon -1$ ist.
````

Wir können auch noch andere Eigenschaften von Folgen untersuchen. Eine erste ist die Anordnung, wir sagen eine Folge ist

* _monoton steigend_, wenn $x_n \leq x_{n+1}$ für alle $n\in \N$ gilt,
* _monoton fallend_, wenn $x_n \geq x_{n+1}$ für alle $n\in \N$ gilt.
\end{*ize}

Dazu können wir auch das Supremum ($\sup$) und Infimum ($\inf$) einer Folge definieren. Bei einer endlichen Menge erreicht man nach endlich vielen Schritten ja immer ein Minimum oder Maximum, bei einer unendlichen Folge ist das nicht zwangsläufig der Fall. So kommt etwa $x_n = \frac{1}n$ dem Wert $0$ beliebig nahe, erreicht ihn aber nicht. Deshalb machen wir folgende Definition:

````{prf:definition}
Wir nennen $x_* \in \R$ das Infimum der reellen Folge $x_n$ (geschrieben $x_* = \inf_n x_n$), genau dann wenn die beiden folgenden Bedingungen erfüllt sind:

* $\forall n \in \N:~x_* \leq x_n$

* $\forall \epsilon > 0~\exists n_0 \in \N: x_{n_0} < x_* + \epsilon$. 


Wir nennen $x^* \in \R$ das Supremum der reellen Folge $x_n$ (geschrieben $x^* = \sup_n x_n$), genau dann wenn die beiden folgenden Bedingungen erfüllt sind:

* $\forall n \in \N:~x^* \geq x_n$

* $\forall \epsilon > 0~\exists n_0 \in \N: x_{n_0} > x^* -\epsilon$. 
````

Analog zur Konvergenz können wir auch die Fälle $\inf_n x_n = - \infty$ und $\sup x_n = +\infty$ definieren, letzteres ist der Fall wenn

```{math}
 \forall \epsilon > 0~\exists n_0 \in \N: x_{n_0} > \epsilon . 
```

Im Fall einer monotonen Folge können wir nun direkt die Konvergenz beweisen:

````{prf:theorem}
Sei $(x_n)$ eine monoton steigende reelle Folge. Dann gibt es ein $\overline{x} \in [x_0,+\infty]$ mit $x_n \rightarrow \overline{x}$. 
````

````{prf:proof} Wir definieren $\overline{x}= \sup_n x_n$ und unterscheiden zwei Fälle. Ist die Folge unbeschränkt, d.h. $\overline{x}=\infty$, so gilt

```{math}
 \forall \epsilon > 0~\exists n_0 \in \N: x_{n_0} > \epsilon. 
```

Da die Folge monoton steigend ist, gilt $x_n \geq x_{n_0}$ für alle $n \geq n_0$. Damit ist die Bedingung

```{math}
 \forall \epsilon > 0~\exists n_0 \in \N~\forall n\geq n_0: x_{n_0} > \epsilon  
```

erfüllt.

Ist $\overline{x} < \infty$, dann gilt

```{math}
 \forall \epsilon > 0~\exists n_0 \in \N: x_{n_0} > \overline{x} -\epsilon
```

und da wieder $x_n \geq x_{n_0}$ für alle $n \geq n_0$ gilt erhalten wir auch $ x_n > \overline{x}-\epsilon$. Andererseits ist $x_n \leq \overline{x}$, also gilt für alle $n \geq n_0$ auch $ \vert x_n - \overline{x} \vert < \epsilon. $  $\square$
````

In obigem Beweis haben wir verwendet, dass aus $x_{n+1} \geq x_n$ f\"ur alle $n$ auch folgt

```{math}
 \forall m \geq n: x_m \geq x_n. 
```

Dies scheint offensichtlich, benutzt aber ein nichttriviales logisches Prinzip, die sogenannte Induktion. Dabei schließt man auf eine Aussage für alle natürlichen Zahlen, wenn man aus der Aussage für ein $n \in \N$ auch die Aussage für $n+1$ folgern kann.
