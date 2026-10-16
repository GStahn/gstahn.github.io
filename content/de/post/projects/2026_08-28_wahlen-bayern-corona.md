---
title: "Der Preis des Wählens in einer Pandemie"
date: 2026-08-28
description: "Meine erste Veröffetlichung!"
keywords: ["COVID-19", "Bayern", "Kommunalwahlen", "Wahlbeteiligung", "Pandemie", "Synthetic Control Method", "Gesundheitsökonomie"]
tags: ["Forschung", "COVID-19", "Wahlen", "Gesundheitsökonomie", "Publikation"]
slug: "wahlen-bayern-corona"
translationKey: "wahlen-bayern-corona"
author: "Gerrit Stahn"
draft: false
---

Am 15. März 2020 gingen fast zehn Millionen Wahlberechtigte in Bayern zur Kommunalwahl – nur wenige Tage, nachdem die WHO COVID-19 offiziell zur Pandemie erklärt hatte. Während andere Bundesländer und Länder Wahlen verschoben oder auf reine Briefwahl umstellten, fand in Bayern ein Großteil der Stimmabgabe ganz normal an der Wahlurne statt. Wenige Wochen später hatte Bayern die höchsten COVID-19-Fallzahlen und Todeszahlen aller deutschen Bundesländer.

War das Zufall – oder hat die Wahl selbst zur Ausbreitung des Virus beigetragen? Genau dieser Frage sind wir in unserer neuen Studie nachgegangen, die soeben vom *The European Journal of Health Economics* zur Veröffentlichung angenommen wurde.

## Wie wir vorgegangen sind

Wir haben zwei unabhängige Methoden kombiniert:

**1. Die Synthetische Kontrollmethode: Bayern vs. "Synthetisches Bayern".**
Mit der sogenannten Synthetischen Kontrollmethode (kurz: SCM, von *Synthetic Control Method*) haben wir für jeden der 96 bayerischen Landkreise aus allen nicht-bayerischen Landkreisen einen statistischen "Zwilling" konstruiert – einen synthetischen Kontrolllandkreis. Vereinfacht gesagt funktioniert das so: Ein Gewichtungsverfahren ordnet jedem nicht-bayerischen Landkreis ein Gewicht zu, je nachdem, wie ähnlich er dem betrachteten bayerischen Landkreis vor der Wahl war – gemessen an Bevölkerungsstruktur, Wirtschaft, Gesundheitsversorgung, Kinderbetreuung und den bisherigen COVID-19-Fallzahlen. Diese Gewichte werden anschließend mit den tatsächlichen COVID-19-Kennzahlen der jeweiligen Landkreise *nach* der Wahl multipliziert und aufsummiert. Das Ergebnis ist der fiktive, "synthetische" Wert, den der bayerische Landkreis vermutlich erreicht hätte, wäre er nicht von der Wahl betroffen gewesen.[^1] Summiert man diese synthetischen Werte über alle bayerischen Landkreise, erhält man eine Schätzung, wie sich die Fallzahlen in Bayern *ohne* die Wahl voraussichtlich entwickelt hätten.

[^1]: Zum Beispiel setzt sich der synthetische Zwilling der Landeshauptstadt München in unserer Basiskonfiguration zu 57 % aus Stuttgart, zu 32 % aus Frankfurt am Main und zu 11 % aus Leipzig zusammen.

![Wöchentliche COVID-19-Fälle pro 100.000 Einwohner je Bundesland](/img/bayernwahl/fig1.png)
*Grafik 1: Wöchentliche COVID-19-Fälle und Todesfälle im Bundesländervergleich – Bayern hebt sich ab der Woche nach der Wahl deutlich ab.*

![Wöchentliche COVID-19-Todesfälle pro 100.000 Einwohner je Bundesland](/img/bayernwahl/fig2.png)
*Grafik 2: Wöchentliche COVID-19-Todesfälle im Bundesländervergleich – Auch hier hebt Bayern nach der Wahl ab.*

**2. Ein Vergleich innerhalb Bayerns.**
Zusätzlich haben wir untersucht, ob bayerische Kreise mit höherer Wahlbeteiligung nach dem 15. März einen stärkeren Anstieg der Fallzahlen verzeichneten als Landkreise mit niedrigerer Wahlbeteiligung – immer unter Berücksichtigung möglicher anderer Erklärungen wie der Entfernung zum Corona-Hotspot Ischgl oder der Zahl der Starkbierfeste, die kurz vor dem Lockdown noch stattfanden.

## Was wir gefunden haben

- Bayern verzeichnete nach der Wahl einen deutlich stärkeren Anstieg der COVID-19-Fälle, als es die Entwicklung der Vergleichslandkreise erwarten ließ – **über ein Drittel** des Anstiegs der Fallzahlen nach der Wahl lässt sich nicht durch demografische, wirtschaftliche oder gesundheitsbezogene Unterschiede oder durch die Nähe zu Ischgl erklären.

![SCM-Ergebnis für die Fallzahlen](/img/bayernwahl/fig5.png)
*Grafik 3: Tatsächliche versus synthetische Fallzahlentwicklung in Bayern – die Schere öffnet sich rund zwei Wochen nach dem Wahltag.*

- Innerhalb Bayerns zeigt sich: Ein Anstieg der Wahlbeteiligung um einen Prozentpunkt ging mit rund **12,8 zusätzlichen bestätigten Fällen und 1,8 zusätzlichen Todesfällen je 100.000 Einwohner** einher – hochgerechnet auf ganz Bayern entspricht das etwa 1.680 zusätzlichen Fällen und 236 zusätzlichen Todesfällen im Zeitraum bis zum 5. April 2020.
- Der Effekt lässt sich sowohl bei der Stimmabgabe vor Ort als auch bei der Briefwahl beobachten. Das deutet darauf hin, dass nicht nur der Gang zur Wahlurne selbst eine Rolle spielte, sondern auch Begleiterscheinungen wie Wahlkampfveranstaltungen oder die Stimmenauszählung.
- Bei den Fallzahlen zeigte sich der Effekt am stärksten bei den 35- bis 59-Jährigen, bei den Todesfällen dagegen vor allem bei den über 80-Jährigen – passend zum bekannten Muster, dass ältere Menschen ein deutlich höheres Sterberisiko tragen.

![Fallzahlen: Heterogenität nach Altersgruppen](/img/bayernwahl/fig14_new.png)
*Grafik 4: Effekt der Wahlbeteiligung auf COVID-19 Fälle nach Altersgruppe.*

![Todeszahlen: Heterogenität nach Altersgruppen](/img/bayernwahl/fig15_new.png)
*Grafik 5: Effekt der Wahlbeteiligung auf COVID-19 Todeszahlen nach Altersgruppe.*

- Die Ergebnisse erwiesen sich in zahlreichen Robustheitschecks als stabil – etwa wenn statt des Meldedatums der Erkrankungsbeginn verwendet wird, oder wenn ein "Placebo-Wahltag" im Juni getestet wird, an dem es erwartungsgemäß keinen Effekt geben sollte (und es in unseren Analysen auch keinen gab).

## Warum das wichtig ist

Unsere Studie liefert einen der ersten kausal interpretierbaren Belege dafür, dass der Zeitpunkt von Wahlen in einer sich zuspitzenden Pandemie einen messbaren Einfluss auf die Ausbreitung eines Infektionsgeschehens haben kann. Das heißt nicht, dass Wahlen in Krisenzeiten grundsätzlich vermieden werden sollten – Wahlen sind schließlich ein Kernbestandteil demokratischer Systeme. Es unterstreicht aber, wie wichtig es ist, bei der Terminierung und der Ausgestaltung von Wahlen (etwa durch mehr Briefwahl oder strengere Hygienemaßnahmen an Wahllokalen, die auch für die Wahlhelfenden adressieren sollten) gesundheitliche Risiken von vornherein mitzudenken.

## Danksagung

Diese Arbeit ist das Ergebnis einer langen gemeinsamen Reise, und ich möchte mich an dieser Stelle herzlich bedanken: bei meinen Koautorinnen und Koautoren Jochen Güntner, Felix Krüger und Amelie Wuppermann für die enge und produktive Zusammenarbeit; bei unseren studentischen Hilfskräften Armando, Erika, Liselotte, Loredana und Vera an der MLU Halle-Wittenberg für ihre unschätzbare Unterstützung bei der Datenaufbereitung; bei Wolfgang Greiner als zuständigem Editor beim *European Journal of Health Economics* für die sorgfältige Betreuung des Begutachtungsprozesses; sowie bei zwei anonymen Gutachterinnen bzw. Gutachtern, deren konstruktive Kritik das Papier deutlich verbessert hat.

*Das Paper erscheint in Kürze im renomierten The European Journal of Health Economics (VHB: A). Ein Link zur finalen Version folgt, sobald sie online verfügbar ist.*
