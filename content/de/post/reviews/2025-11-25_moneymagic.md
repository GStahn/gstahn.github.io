---
title: 'Review: Money Magic'
subtitle: von Laurence J. Kotlikoff
date: "2025-11-25"
page_id: reviews
permalink: /reviews/
params:
  lang: de
---

![Cover Buch Money Magic](img/moneymagic.jpg "Title")

> „Ich fragte einmal einen ganzen Raum voller Ökonominnen und Ökonomen – die sich alle versammelt hatten, um über private Haushaltsfinanzen zu diskutieren – spontan nach der Frage der Konsumglättung für eine hypothetische vierzigjährige Person. Ich gab ihnen die relevanten Informationen und beobachtete ihre Gesichter. Sie waren nicht glücklich. Sie wussten, dass sie gleich eine sehr falsche Antwort liefern würden. Genau in diesem Moment schien ihnen klarzuwerden, dass selbst finanziell gebildete Menschen wie sie keine angemessenen finanziellen Entscheidungen allein durch Introspektion treffen können.“ (S. 6, übersetzt)

# Einleitung

Genau dieser Satz zu Beginn des Buches *Money Magic: An Economist's Secrets to more Money, less Risk, and a better Life* von **Laurence J. Kotlikoff** fasst für mich meine derzeitige Retrospektive zusammen. Selbst nach Jahren, in denen ich mich intensiv mit dem Thema finanzielle Planung beschäftigt habe, - selbst nach meinem Dotkortitle in einem Bereich, dessen Experten sich eigentlich auf die Fahne schreiben es *besser* *zu wissen* und selbst nach der Lektüre dieses so interessanten Buches muss ich etwas konstaniert feststellen: Ich weis immer noch nicht alles. Und ich glaube den "allwissenden Zustand" wird es nie geben. Aber (zum Glück) reicht es schon für vielen Entscheidungen im Leben einfach nur zu wissen, wo nützliche Informationen stehen. Und genau dabei hilft dieses Buch: Es vermittelte mir viel neues Wissen, von dem ich nun weis, wo ich es bei Bedarf auffrischen kann.

# Kurze Inhaltswiedergabe

Das im Jahr 2022 veröffentlichte Buch thematisiert umfassend das Thema Finanzielle Lebenszeitplanung und geht dabei auf viele wichtige Punkte ein, wie z. B. Wie wähle ich eine lukrative Karriere? Wie erhalte ich eine gute Ausbildung / ein gutes Studium kostengünstig? Bis wann lohnt es sich (derzeit) zu arbeiten? Lohnt es sich (aus rein finanzieller Sicht) zu heiraten oder sich zu scheiden? Und vieles mehr. Prof. Kotlikoff bindet dabei viele Beispiele der Art "Was wäre für Max Mustermann gegeben X am besten in Situation Y?" in seine Erläuterungen mit ein. Als Ökonom habe ich mich natürlich über die vielen Rechnungen gefreut, die die Punkte meist sehr gut untermauern.

# Meine Gedanken zum Buch

Das Buch war defintiv seine Anschaffungskosten (ca. 12€ auf [Amazon](https://www.amazon.de/-/en/Money-Magic-Economists-Secrets-Better/dp/0316435996/ref=tmm_pap_swatch_0)[^1]) und andere Opportunitätskosten wert. Neben den vielen interessanten Aspekten, denen ich jedem empfehlen würde, haben mich zwei Aspekte wirklich nachhaltig zum Nachdenken gebracht: das **Konzept des Lebensstandard-Kegels** (Engl. Living Standard Cone) und die Logik hinter **"Rentner sollten stärker in Aktien investieren je älter sie werden."**

[^1]: Stand: Nov. 2025

## Der Lebensstandard-Kegel

Im Kapitel 9 *Invest Like an Economist - Control Your Living Standard Trajectories* stellt Kotlikoff das Prinzip der Lebensstandard-Kegel vor. Dem zugrunde liegt die Idee, dass die jährlich durch eine Person getätigten Ausgaben dessen jährlichen Lebensstandard entsprechen. Wie viel jährlich ausgegeben werden kann, ist zu einem gewissen Teil von den getroffenen (finanziellen) Entscheidungen abhängig. Verschiedene Entscheidungen führen zu verschiedenen *Pfaden des Lebensstandards*. In Anlehnung an die Graphik im Buch[^2] habe ich in *Abbildung 1* mal Beispiele für verschieden Pfade visualisiert. Ausgehend von einem Startwert von 50.000€[^3] im Jahr 2025 sind drei Szenarien dargestellt. Die gepunktete Linie stellt einen Pfad dar in dem sich für das Individum im Schnitt über die nächsten 50 Jahre nicht viel am Lebenstandard ändert. Ich habe diesen Pfad als *Weniger glücklich* (Engl. *Less Fortunate*) bezeichnet, da er trotz seines stabilem Erscheinungsbilds graduell abbauende Kaufkraft repräsentiert. (Diese blöde Inflation!)

[^2]: Vgl. S. 242 \| Im Unterschied zu der Abbildung im Buch habe ich die Pfade in meinen Abbildungen mittels stationären Zeitreihen (ohne Trend und mit unterschiedlichen positiven Trends) in R erzeugt. Das Script dazu findest du hier: [Script_ls_cone.R](downloads/Script_ls_cone.R)

[^3]: Was gehört alles zu einem derzeitigen Lebensstandard? Dazu zählen alle Ausgaben, die man aktuell so im Jahr tätigt - inkl. Miete, Ausgaben für Essen - aber auch die jährliche Sparrate. Und hier wird es auch etwas komplizierter für alle, die ihre Lebensstandard-Pfade einmal genauer darstellen wollen, denn das Erfassen des aktuellen Lebensstandards (sprich aller Ausgaben pro Jahr) ist schon nicht einfach. Wenn man dann aber auch noch versuchen möchte Sparraten und deren Gewinne miteinzuberechnen und das über die nächsten 50 Jahre, dann kommt man (ich) schnell an seine Grenzen. Für diejenigen, die wissen wollen, wie das gemacht werden kann, empfehle ich Kapitel 10 *Making your own money magic : my top fifty secrets.*

<p align="center">

<em>Abbildung 1: Ein möglicher Lebensstandard-Kegel</em>

</p>

![Lebensstandard-Kegel](img/money_magic_plot.png)

Schon besser sehen die andere beiden Pfade aus. Der *Bessere* (Engl. *Better*) und der *noch Bessere* (Engl. *Even Better*) zeigen Verläufe an, die auch ich mir wünsche für meine finanzielle Zukunft. Von Jahr zu Jahr könnte ich etwas mehr Geld ausgeben und hoffentlich damit mehr als nur die Inflation ausgleichen.[^4]

[^4]: Tja - auch wenn die beiden "besseren" Pfade schon irgendwie beeindruckend wirken, so würde es nur der gestrichelte Pfad gerade so schaffen den Kaufkraftverlust auszugeleichen - jedenfalls wenn man die letzten 50 Jahr als Projektion für die Zukunft nimmt. Blöde Inflation!

Darüberhinaus verdeutlicht dieser Graph schon ein paar sehr interessante Überlegungen. 1. Wir werden nicht jedes Jahr immer den gleichen Betrag (geschweige denn immer mehr) ausgeben können. Ab und zu sinkt unser Lebensstandard im Vergleich zum Vorjahr. Vielleicht weil wir gesundheitlich einmal länger ausfallen und/oder eine zeitlang arbeitslos sind.

2\. Welcher Pfad es am Ende wirklich wird, ist (leider) auch mit Unsicherheit verbunden. An dieser Stelle möchte ich aber auch gleich etwas Kritik üben: In der Ökonomik werden nämlich die Begriffe *Risiko* und *Unsicherheit* nicht synonym verwendet. Während Entscheidungen unter Risiko voraussetzen, dass Menschen von jeder Entscheidung alle möglichen Konsequenzen **und** deren Wahrscheinlichkeiten kennen, sind bei Entscheidungen unter Unsicherheit diese Wahrscheinlichkeiten nicht bekannt. Obwohl im Buch fast durchgehend von „Risiko“ die Rede ist, bin ich der Ansicht, dass eigentlich Entscheidungen unter Unsicherheit gemeint sind – zumindest würde ich das so verstehen, und vermutlich geht es vielen Leserinnen und Lesern ähnlich. Dennoch macht dieser Umstand deutlich, dass wir unseren Lebensstandard nie vollständig unter Kontrolle haben.

3\. Und darauf aufbauen mein persönlicher Lieblingsfakt: Wenn man in möglichen Lebensstandard-Pfaden denkt, dann kommt es nicht nur darauf an, welcher Pfad es am Ende wird, sondern wie die Menge an **möglichen** Pfaden durch jede finanzielle Entscheidung verbessert werden können. Diese Menge an Pfaden bezeichnet Kotlikoff in seinem Buch als **Lebenstandard-Kegel** (Engl. living standard cone). Die Form (siehe graue Fläche in Abbildung 1) ergibt sich aus den beiden Endpunkten des schlechtesten Pfades und des besten Pfades sowie dem Umstand, dass alle Pfade heute (in der Abbildung 2025) starten.

Warum ist das Kegel-Konzept nun so interessant für mich? Weil es sich hervorragend eignet, die „Qualität“ finanzieller Entscheidungen zu beurteilen. Jede solche Entscheidung beeinflusst unsere möglichen Entwicklungspfade – und damit auch den Kegel. Gute Entscheidungen zeichnen sich dadurch aus, dass sie erstens den Kegel gegen den Uhrzeigersinn verschieben – der beste Fall verbessert sich und der schlechteste ebenso. Zweitens gewinnen Entscheidungen an Wert, wenn sie zusätzlich die Fläche des Kegels verkleinern, also die Anzahl möglicher Pfade reduzieren.

Wenn eine Entscheidung – wie in Abbildung 2 – bewirkt, dass sich der Kegel im Ursprung nach links dreht und gleichzeitig der schlechteste Pfad in Relation noch stärker ansteigt, dann handelt es sich um eine wirklich hervorragende Entscheidung.

<p align="center">

<em>Abbildung 2: Gute Entscheidungen drehen den Kegel nach links.</em>

</p>

![Besserer Lebensstandard-Kegel](img/money_magic_plot2.png)

## **"Rentner sollten stärker in Aktien investieren je älter sie werden."**

Die auf Seite 266 geäußerte Logik hat mich sofort beim Lesen irritiert. Eine der wenigen Empfehlungen, welche ich bisher noch mit konventionellen Finanzberatern geteilt habe, ist das Mantra: "Je jünger du bist, umso mehr solltest du in Aktien investieren. Je älter, umso mehr solltest du dein Vermögen sichern." Die Logik dahinter ist, dass als junger Mensch hat man noch einen relativ langen Anlagehorizont. Schwächephasen, wie die Finanzkrise 2008/2009, können noch durch gute Phasen am Finanzmarkt ausgegelichen werden. Denn je länger der Anlagehorizont ist, umso eher ist es der Fall, dass am Ende doch eine schön saftig große, grüne Zahl im Depot erscheint. Wenn man jedoch älter wird, dann sinkt auch die Zahl der Jahre, in denen noch Schwächephasen ausgleichen werden können. Denn im Alter ist man ja auf sein privat Erspartes angewiesen.[^5] Da will man ja eigentlich nicht weniger haben, nur weil an den Märkten gerade eine "bären Stimmung" ist. Also was steckt hinter dieser Idee von Kotlikoff?

[^5]: Vor allem meine Generation in Deutschland, wenn die derzeitige Bundespolitik (Stand Nov. 2025) mit ihrer Rentenpolitik so weitermachen möchte. (Vgl. [Tagesschau-Artikel](https://www.tagesschau.de/wirtschaft/konjunktur/oekonomen-appell-rentenpaket-100.html))

Die geäußerte Empfehlung basiert auf der Portfolio Theorie entwickelt von [Robert C. Merton](https://mitsloan.mit.edu/faculty/directory/robert-c-merton) und [Paul Samuelson](https://www.nobelprize.org/prizes/economic-sciences/1970/samuelson/biographical/). [^6] Dies basiert wiederrum auf dem Optimalitätsproblem eines Investors, der entscheiden muss, wie viel er heute konsumieren möchte und wie er sein verbleibendes Vermögen zwischen risikoreichen (z. B. Aktien) und risikofreien Anlagen aufteilen soll, um seinen erwarteten intertemporalen Nutzen zu maximieren. Dieses Optimalitätsproblem lässt sich – je nach Modellannahmen – mathematisch lösen. Dabei ergibt sich sogar eine vergleichsweise einfache Formel, mit der sich der optimale Anteil des Vermögens bestimmen lässt, der in risikoreiche Anlagen investiert werden sollte, bezeichnet mit \\(\\pi\\):

[^6]: Beide sind Preisträger des Alfred-Nobel-Gedächtnispreises für Wirtschaftswissenschaften. Samuelsons Verdienste für die Wirtschaftswissenschaften, und dei damit verbunden Gründe für den Erhalt seines Preises im Jahr 1970, kann man nicht in einer Fußnote erläutern. Für mehr Informationen hierzu verweise ich gerne auf die im Fließtext verlinkte Seite. Bei Merton *erscheint* diese Aufgabe schon etwas leichter, da dieser seinen Preis im Jahr 1997 für seine Arbeiten zum Thema auf dem Gebiet der Finanztheorie und des Risikomanagements und insbesondere für seinen Beitrag zur Bewertung von Aktienoptionen und anderen Derivaten erhalten hat.

$$
\pi(W,t) = \frac{\mu - r}{\sigma^{2} \gamma}
$$

Dieser Prozentsatz wird bestimmt durch die erwartete Rendite (\\(\\mu\\)) und Volatilität des (Aktien-)Marktes (\\(\\sigma\\)), die Verzinsung der risikofreien Anlage (\\(r\\)) sowie dem individuellen Grad an Risikoaversion (\\(\\gamma\\)). Interessant an der Formel ist, dass aus ihr ersichtlich wird, dass dieser Prozentsatz nicht abhängig ist von der Höhe des Vermögens \\(W\\) und dem Zeitpunkt der Investition \\(t\\) - denn beide Werte tauchen in der Formel nicht auf. D.h. egal welches Alter man hat, oder wie reich man ist - der Anteil an Vermögen investiert in risikoreichere Anlagen sollte immer gleich bleiben.

*Aber hä - jetzt soll der Anteil doch immer gleich bleiben, egal wie alt man ist?* Der Anteil ja, d.h. aber nicht, dass man nichts mehr machen muss, um diesen so zu halten. Die Theorie impliziert nämlich damit auch Folgendes für Aktien als risikoreichere Anlage: Wenn der absolute Wert des Vermögen, welches **sicher** ist, steigt, dann sollten auch Investititionen in Aktien steigen, um diesen Prozentsatz weiter zu erhalten. Und genau darauf baut die Idee von Kotlikoff auf. Er geht nämlich davon aus, dass man zwei Arten von Vermögen im Alter hat: Sicheres, im Intervallen zufließendes Vermögen (welches z. B. auf Einkommen aus Rentenbezügen basiert) und angelegtes Vermögen. Wenn man letzteres Vermögen im Alter sukzessiv aufbraucht, dann nimmt der Anteil des sicheren Vermögens am Gesamtvermögen immer weiter zu, bzw. bekommt ein größeres Gewicht für den Lebensstandard. Um dennoch den Prozentsatz oben konstant zu halten, muss also das verbleibende Vermögen vermehrt in Aktien investiert werden.

So spannend ich diese Überlegung auch finde und so sehr sie mich zum Nachdenken gebracht hat (siehe *Meine Take-Aways*), so finde ich es im Buch doch etwas kurzgefasst. Denn die Annahmen, die hinter diesem Modell stecken werden nur sehr kurz erwähnt, als realitätsfern bezeichnet und dann trotzdem für diese (und weitere) Empfehlung(en) verwendet. [^7]

[^7]: Siehe S. 262.

Zum einen beruht das Modell auf einem theoretischen Konstrukt einer Welt ohne Transaktionskosten. Das bedeutet, dass Aktien beispielsweise ohne Kosten gekauft und wieder verkauft werden könnten. Man könnte meinen, diese Annahme sei heute gar nicht so unrealistisch, da insbesondere durch Neo-Broker die direkten Handelskosten stark gesunken sind. Allerdings umfasst der Begriff der Transaktionskosten in der Ökonomik weit mehr als nur die Gebühren einer Transaktion. Auch der Aufwand, sich Wissen über den Finanzmarkt anzueignen, zählt dazu. Schon das Lesen dieses Artikels verursacht also Kosten – genauer: Opportunitätskosten, gemessen an der dafür aufgewendeten Zeit.

Darauf aufbauend setzt das Modell effiziente Aktienmärkte voraus: Alle verfügbaren Informationen sind bereits in den Preisen enthalten, und Kursänderungen entstehen ausschließlich durch zufällig auftretende, also nicht vorhersehbare neue Informationen. Das impliziert zugleich, dass einzelne Anlageklassen nicht systematisch risikoreicher oder ertragreicher werden. Ob Märkte tatsächlich effizient sind oder nicht – daran scheiden sich in der Ökonomik bis heute die Geister. 2013 wurden sogar zur gleichen Zeit zwei Öknomomen - [Eugen Fama](https://faculty.chicagobooth.edu/eugene-fama) und [Robert Shiller](http://www.econ.yale.edu/~shiller/) - geehrt, die unterschiedliche Sichtweisen auf diese Dinge haben. Eugene Fama sieht Finanzmärkte als weitgehend effizient an: Alle verfügbaren Informationen seien in den Preisen enthalten, weshalb systematische Fehlbewertungen (und damit die Möglichkeit für Abitrage-Gewinne) kaum möglich sind. Robert Shiller widerspricht diesem Bild und betont, dass psychologische Faktoren, Stimmungen und Herdenverhalten häufig zu Übertreibungen, spekulativen Blasen und somit zu deutlichen und vorhersagbaren Abweichungen von fundamentalen Werten führen. Während Fama also die Effizienz der Märkte betont, hebt Shiller deren wiederkehrende Ineffizienzen hervor.

Eine weitere, für viele unrealistische Annahme betrifft die vollständige Fungibilität von Vermögen und zukünftigen Einkommen. Diese besagt, dass auch zukünftiges Arbeitseinkommen sofort in Vermögen umgesetzt werden kann, in dem ich meinen Lohn z. B. gegen eine große Einmalzahlung eintausche.

Wie realistisch die Annahmen eines Modells sind, spielt für dessen Qualität zunächst keine entscheidende Rolle. Auch eine Landkarte – oder Google Maps – bildet die Realität nur durch stark vereinfachte, eigentlich „unrealistische“ Annahmen ab (zum Beispiel: *Die Welt ist zweidimensional*). Entscheidend für die Qualität eines Modells ist allein, wie gut es Vorhersagen treffen kann. Und genau an diesem Punkt habe ich ein Problem mit dem Buch. Kotlikoff betont mehrfach, dass die aus der Merton-Samuelson-Portfoliotheorie abgeleiteten Vorhersagen zum Investitionsverhalten von Anlegern in der Realität häufig nicht zu beobachten sind. Daraus schließt er, die Individuen seien entweder schlecht informiert oder schlecht beraten. Dieser Duktus irritiert mich jedoch, denn er übersieht ein durchaus plausibles drittes Szenario: Das Entscheidungsverhalten von (vielen) Anlegern könnte schlicht unzureichend modelliert sein.

*Wie jetzt? War das Kapitel am Ende doch nicht seine Opportunitätskosten wert?* Doch – absolut. Denn die Empfehlung richtet sich ausdrücklich an *Rentnerinnen und Rentner*, und darüberhinaus an solche in der heutigen Welt. Viele von ihnen haben sich bis zum Eintritt ins Rentenalter ein gewisses Finanzwissen angeeignet und können dank Neo-Brokern zu sehr geringen Kosten handeln (Annahme: keine Transaktionskosten). Was die Frage effizienter oder ineffizienter Märkte betrifft, argumentiert selbst Robert Shiller, dass mehr verfügbare Informationen die Effizienz der Märkte erhöhen. Und in unserer digitalen Welt sind Informationen nämlich so leicht zugänglich wie nie zuvor (Willkommen auf meiner Seite!).

Auch die stetig wachsende Zahl an Transaktionen, sei es durch Robo-Advisors oder ganz allgemein durch algorithmisches Trading, könnte die Finanzmärkte stabiler gegenüber psychologischen Effekten, Stimmungen oder Herdenverhalten machen (Annahme: effiziente Märkte). Ebenso erscheint die Annahme der vollständigen Fungibilität von Vermögen für viele Seniorinnen und Senioren zu Beginn ihrer Rente plausibel. Zwar erhalten sie durch das staatliche Rentensystem eine monatliche Zahlung, doch die erste Auszahlung dürfte – hoffentlich – vergleichsweise gering sein im Verhältnis zum zuvor angelegten Vermögen.

Es lässt sich also festhalten: Für Rentnerinnen und Rentner zu Beginn ihrer Pensionierung können die Annahmen des Modells durchaus sinnvoll erscheinen. Unter diesen Voraussetzungen wäre es nachvollziehbar, dass mit zunehmender Entnahme aus dem Vermögen – also je stärker die monatliche Rentenzahlung den Lebensstandard bestimmt – der verbleibende Vermögensanteil stärker in Aktien investiert werden sollte.[^8]

[^8]: Allerdings gibt es für mich an dieser Stelle noch eine offene Frage: Wie lässt sich diese Schlussfolgerung mit dem Prinzip des *Risiko-Transfers* vereinbaren, das wir (meine Kolleginnen, Kollegen und ich) in unseren Bachelorkursen lehren? Dieses Konzept basiert auf der Annahme, dass Personen mit einer Nutzenfunktion mit konstanter relativer Risikoaversion sich *pareto-verbessern* können, wenn Risiko von Menschen mit geringem Vermögen auf solche mit hohem Vermögen übertragen wird. Mit anderen Worten: Vermögendere Personen profitieren davon, Risiken von weniger vermögenden Personen zu übernehmen – beispielsweise indem sie diese gegen Unfallschäden versichern. Noch einfacher formuliert: Je reicher man ist, desto eher lohnt es sich, mehr Risiken einzugehen. Je ärmer man ist, desto stärker lehnt man Risiken ab.

    Warum aber sollten Rentnerinnen und Rentner mit angespartem Vermögen – und unter der Annahme konstanter relativer Risikoaversion – laut Merton-Samuelson-Portfoliotheorie weniger Geld in risikoreiche Anlagen investieren je reicher sie sind, während dasselbe theoretische Fundament gleichzeitig nahelegt, dass gerade Vermögende Risiken von weniger Vermögenden übernehmen sollten?

    Falls eine Leserin oder ein Leser hierzu mehr Klarheit beitragen kann, freue ich mich sehr über eine Kontaktaufnahme.
    
## Für Nicht-US-Amerikaner ist leider nicht alles relevant.

Leider bietet das Buch für nicht-US-amerikanische Leser etwas weniger Mehrwert als für US-amerikanische. Der Grund dafür ist, dass insbesondere die Kapitel 2 bis 5 stark auf die Situation in den USA zugeschnitten sind. Das ist allerdings kein Vorwurf an das Buch selbst, denn Fragen wie *Welches ist das beste Alter, um in Rente zu gehen?* oder *Wie spart man Steuern im Ruhestand?* hängen nun einmal eng vom jeweiligen Sozialsystem des Landes ab, in dem man lebt.

Im besten Fall inspiriert es vielleicht einen meiner deutschen Leser dazu, ein ähnliches Buch für den deutschen Markt zu schreiben. Ich würde es sofort kaufen!

# Mein Take-Away

Die oben erläuterten Gedanken spiegeln nur einen kleinen Teil dessen wider, was mich an diesem Buch fasziniert und aus dem ich echten Mehrwert ziehe. Wenn ich jedoch mein wichtigstes Learning knapp zusammenfassen müsste, wäre es dieses: Vielleicht sollte ich den Anteil sicherer Anlagen in meinem Vermögensmix erhöhen. Auch wenn ich noch kein Rentner bin (und dieser Zeitpunkt hoffentlich noch in weiter Ferne liegt – ich arbeite gern!), verliert mit jedem zusätzlich gesparten Euro mein regelmäßiges Einkommen ein Stück weit an relativer Bedeutung. Unter dem Blickwinkel der Lebenspfade und der Merton-Samuelson-Theorie ist es deshalb vielleicht an der Zeit, einen größeren Teil meines Vermögens wirklich sicher anzulegen.
