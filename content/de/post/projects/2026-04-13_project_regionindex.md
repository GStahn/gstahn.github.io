---
title: "RegioIndex: Finde Deinen Lieblingsort in Deutschland"
date: 2026-05-13
author: "Gerrit Stahn"
language: "de"
description: "Eine kurze Vorstellung von RegioIndex, einer Shiny-App, die deutsche Kreise und Gemeinden auf Basis nutzerdefinierter Präferenzen rankt."
keywords:
  - RegioIndex
  - deutsche Kreise
  - Landkreise
  - Stadtkreise
  - Gemeinden
  - Shiny App
  - regionale Daten
  - Datenvisualisierung
  - gewichteter Index
  - Deutschland
tags:
  - R
  - Shiny
  - Data Science
  - Regionalanalyse
  - Deutschland
draft: false
---

## Hintergrund

Vor ein paar Monaten --- gegen Ende meiner Promotion --- kamen die letzten fünf Gehirnzellen, die nicht von meiner Dissertation besetzt waren, auf eine schwierige Frage: *Was machst du nach deiner Promotion?* Sofort hatte ich die einzig gute Antwort parat: *Ich weiß es nicht.* Meine Gehirnzellen antworteten: *Hmm - ok. Aber wo willst du leben?* *Verdammt, gute Frage!* - antwortete ich. Als guter Mann habe ich mir dafür natürlich Hilfe von meiner Freundin geholt und nach einigem Nachdenken entschieden wir uns, *temporär* nach Vancouver, BC, zu ziehen. *Frage geklärt!*, dachte ich zuerst. *Oh nein - Frage nur verschoben...*, antworteten meine fünf Gehirnzellen. Da meine Freundin und ich eine Vereinbarung getroffen haben - hauptsächlich erzwungen durch unsere Eltern -, irgendwann in Zukunft nach Deutschland zurückzukehren, war die Frage also noch nicht wirklich beantwortet.

Als guter Ökonom versuchte ich, ein Modell zu finden, das mir bei dieser Entscheidung helfen könnte. Und ich konnte keines für Deutschland finden.

## Warum ist die App anders?

Es gibt bereits hervorragende Tools zur Erkundung regionaler Daten in Deutschland, zum Beispiel den [INKAR Online-Atlas](https://www.inkar.de/), den [Regionalatlas von Destatis](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/regionalatlas.html), den [Deutschlandatlas](https://www.deutschlandatlas.bund.de/) oder den [Thünen-Landatlas](https://www.landatlas.de/). Aber ich wollte etwas leicht anderes: Statt einzelne Indikatoren nur nacheinander anzuschauen, wollte ich meine eigenen Prioritäten definieren, verfügbare Daten gewichten und diese Variablen zu einem personalisierten Index kombinieren. Mit anderen Worten: Die bisherigen Apps sind großartig, um zu fragen: „Wie schneidet diese Region/dieser Kreis/diese Gemeinde ab?“ — aber ich wollte wissen: „Welche Region passt am besten zu *mir*?“ Und ehrlich gesagt fühlt sich das deutlich unterhaltsamer an, als auf eine weitere statische Karte zu starren und so zu tun, als hätte man die Verwaltungsgrenzen verstanden.

*Warum nicht zuerst alle potenziellen Regionen besuchen, ein Gefühl für sie bekommen und dann entscheiden?*, könnte man fragen. Nun, Deutschland hat rund 400 Kreise — und über 10.000 Gemeinden, die sich höflich darin verstecken. Das sind ziemlich viele Orte, die man besuchen müsste. Und meine FOMO — und die meiner Freundin — kickt heftig, wenn wir uns auf eine Region einigen, die sich nur *so ungefähr richtig* anfühlt. Nein, ich brauchte einen etwas ausgefeilteren Ansatz. Deshalb habe ich **RegioIndex** entwickelt --- eine Shiny-Anwendung, mit der Nutzerinnen und Nutzer deutsche Kreise ranken können — einschließlich `Landkreise` und `Stadtkreise` — basierend auf dem, was *ihnen* tatsächlich wichtig ist. Infrastruktur? Wohnen? Luftqualität? Jobs? Bildung? Wirtschaftliche Indikatoren? Schieberegler bewegen, Präferenzen anpassen und zuschauen, wie deutsche Kreise und ihre Gemeinden sich entsprechend präsentieren.

Keine Rankings nach dem Motto „one size fits all“. Kein so tun mehr, als wollten alle am selben „besten“ Ort leben. RegioIndex stellt die wichtige Frage:

> Was, wenn dein Traumkreis nicht der Traumkreis aller anderen ist — und was, wenn das völlig in Ordnung ist?

## Was macht RegioIndex?

Die App nimmt regionale Indikatoren, normalisiert sie, wendet nutzerdefinierte Gewichtungen an und berechnet daraus einen individuellen Index von 0 bis 100. Anders gesagt: Sie verwandelt deine persönlichen Präferenzen in ein Ranking deutscher Kreise.

Du kannst vergleichen:

- alle deutschen `Kreise`,
- nur `Stadtkreise`,
- nur `Landkreise`,
- und, sofern verfügbar, Gemeinden innerhalb eines ausgewählten Kreises.

Dazu kommen Visualisierungen, interaktive Ergebnisse und genug Schieberegler, damit sich jeder Datenfan (zumindest ein bisschen zu) mächtig fühlen kann.

## Vom ersten Prototypen zur Beta-Version

Dieses Repository ist eine Weiterentwicklung meines früheren Projekts:

[https://github.com/GStahn/ranking_german_districts](https://github.com/GStahn/ranking_german_districts)

Das ursprüngliche Projekt konzentrierte sich darauf, deutsche Kreise anhand eines individuell gewichteten Index zu ranken. Nutzerinnen und Nutzer konnten ihre eigenen Prioritäten definieren, und das Skript berechnete und visualisierte anschließend die bestplatzierten Kreise.

Das neue Projekt baut auf dieser Idee auf und macht daraus eine interaktivere Shiny-Beta-Version:

[https://github.com/GStahn/ranking_german_counties](https://github.com/GStahn/ranking_german_counties)

Anstatt Gewichtungen direkt im R-Code anzupassen, können Nutzerinnen und Nutzer nun mit Schiebereglern im Browser arbeiten. Außerdem erweitert die App die Analyse, indem man auf einen Kreis klicken und, sofern verfügbar, die gerankten Gemeinden darin erkunden kann.

Kurz gesagt:

> Das erste Repository fragte: „Welcher deutsche Kreis passt zu deinen Präferenzen?“  
> Die neue Beta fragt: „Sehr gut — und was passiert, wenn wir das Ganze interaktiv machen und weiter hineinzoomen?“

Das ist Fortschritt. Oder zumindest eine sehr ausgefeilte Art, Schieberegler zu bewegen und Orte zu beurteilen.

## Wie kommt man zur Beta-Version?

Die aktuelle Beta-Version ist hier verfügbar:

[https://gstahn.shinyapps.io/Beta_counties/](https://gstahn.shinyapps.io/Beta_counties/)

Da es sich noch um eine Beta-Version handelt, ist der Zugriff durch einen einfachen Login geschützt. Nach dem Öffnen der App gib den Benutzernamen **icke** und das Passwort **hack** ein.[^1]

[^1]: Ich habe diese Login-Seite eingebaut, weil ich die App eigentlich an irgendein Unternehmen verkaufen wollte, das daran interessiert ist. Das Bild auf der Login-Seite sagt alles. Aber ich habe nie angefangen, Unternehmen zu kontaktieren. Das wäre mir zu viel Arbeit gewesen, dachte ich mir, und mit dem Projekt online zu flexen ist auch genug Lohn.

![Login screen of the RegioIndex beta version](/img/regioindex/start.png)

*Screenshot 1: Der Login-Screen der Beta-Version. Hier Benutzernamen und Passwort eingeben, um die App zu nutzen.*

Nach dem Login kannst du sofort mit dem Ranking experimentieren. Bitte daran denken: Es ist noch eine Beta-Version, also kann sich etwas manchmal merkwürdig verhalten.

## Schritt 1: Wähle aus, was dir wichtig ist

Die Grundidee hinter RegioIndex ist einfach: Unterschiedliche Menschen interessieren sich für unterschiedliche Dinge.

Deshalb lässt dich die App die Wichtigkeit verschiedener regionaler Indikatoren mithilfe von Schiebereglern anpassen. Jeder Schieberegler steht für eine Dimension regionaler Attraktivität. Durch die Gewichtungen entscheidest du, wie stark ein Faktor das finale Ranking beeinflussen soll.

![Slider interface for weighting regional indicators](/img/regioindex/slider.png)

*Screenshot 2: Die Schieberegler. Hier legst du fest, welche Indikatoren für dein persönliches Kreis-Ranking besonders wichtig sind.*

Die Schieberegler können von negativen bis positiven Werten reichen. Das bedeutet: Nutzerinnen und Nutzer können Indikatoren belohnen, die sie wünschenswert finden, und Indikatoren bestrafen, die sie eher negativ bewerten. Viele Ladepunkte für Elektroautos könnten zum Beispiel ein Plus sein, während Verkehrsunfälle oder Luftverschmutzung etwas sein könnten, das du negativ gewichten möchtest: weniger ist besser.

Einige Kategorien können außerdem aufgeklappt werden. Über die Detail-Checkbox können Nutzerinnen und Nutzer über die grobe Kategorie hinausgehen und die darunterliegenden Indikatoren einzeln anpassen. Hier wird RegioIndex gleichzeitig nützlich und potenziell zeitintensiv für alle, die gerne Dinge feinjustieren.

![Detailed slider view and district-type selection](/img/regioindex/slider_district_type.png)

*Screenshot 3: Detail-Schieberegler erlauben es, einzelne Indikatoren anzupassen. Über die Auswahlbuttons kann man alle Kreise, nur Stadtkreise oder nur Landkreise vergleichen.*

Am unteren Ende des Slider-Panels können Nutzerinnen und Nutzer entscheiden, welche Art von Kreis in das Ranking aufgenommen werden soll:

- **Alle Kreise**: alle Kreise
- **Nur Stadtkreise**: nur Stadtkreise
- **Nur Landkreise**: nur Landkreise

So lassen sich sehr unterschiedliche Orte vergleichen — oder man vermeidet es, Äpfel, Birnen und berlinförmige Verwaltungsrätsel miteinander zu vergleichen.[^2]

[^2]: Der letzte Ausdruck wurde von ChatGPT vorgeschlagen. Ich weiß nicht, wie es auf diesen Unsinn gekommen ist. Aber ich habe ihn drin gelassen, als Erinnerung daran, dass LLMs oft Mist bauen.

Zum Beispiel könnte eine Person vor allem Wert auf Wohnen und Infrastruktur legen. Eine andere priorisiert vielleicht wirtschaftliche Indikatoren, Bildung oder Umweltbedingungen. RegioIndex berechnet das Ranking dann auf Basis dieser Präferenzen neu.

Das bedeutet: Es gibt nicht den einen finalen „besten“ Kreis.

Es gibt nur den besten Kreis **gemäß deiner ausgewählten Gewichtungen** — was ehrlicher und unterhaltsamer ist.

## Schritt 2: Sieh dir deine bestplatzierten Kreise an

Nachdem die Gewichtungen gesetzt wurden, berechnet die App einen personalisierten Index und zeigt die **Top 20 Kreise** an.

Diese erste grafische Ausgabe gibt einen schnellen Überblick darüber, welche `Landkreise`, `Stadtkreise` oder `Alle Kreise` unter deinem gewählten Gewichtungsschema am besten abschneiden.

![Top twenty ranked German districts in RegioIndex](/img/regioindex/first_output.png)

*Screenshot 4: Die erste grafische Ausgabe zeigt die Top 20 deutschen Kreise auf Basis der gewählten Indikatorgewichtungen.*

Das Ranking ist vollständig präferenzbasiert. Änderst du die Schieberegler, können sich auch die Top 20 ändern. Genau hier wird die App überraschend süchtig machend. Plötzlich kann ein Regler, der um fünf Punkte verschoben wird, einen Kreis im Ranking massiv nach oben klettern lassen.

Die vertikale Linie markiert den Idealwert des hypothetisch perfekten Index. Je näher ein Kreis an diese Linie kommt, desto besser passt er zu den ausgewählten Präferenzen. Im Beispiel oben schneidet München unter dem gewählten Gewichtungsschema stark ab — was entweder deine Erwartungen bestätigt oder dich sofort misstrauisch gegenüber deinen eigenen Entscheidungen macht.

## Schritt 3: Klicke auf einen Kreis für mehr Details

Die App hört nicht auf Kreisebene auf. Wenn du auf einen gerankten Kreis klickst, kann RegioIndex eine zweite Ausgabe anzeigen, die die Gemeinden innerhalb dieses Kreises zeigt — sofern der ausgewählte Kreis Gemeinden enthält.

Diese Gemeinden werden anhand **derselben Gewichtungslogik** gerankt wie das Kreis-Ranking.

![Ranked municipalities within a selected district](/img/regioindex/second_output.png)

*Screenshot 5: Nach dem Klick auf einen Kreis zeigt die zweite Ausgabe gerankte Gemeinden innerhalb dieses Kreises, basierend auf denselben ausgewählten Gewichtungen.*

Das erlaubt den Wechsel von einer breiteren regionalen Perspektive zu einer detaillierteren lokalen Perspektive. Anders gesagt, zuerst kannst du fragen:

> Welcher Kreis passt am besten zu meinen Präferenzen?

Und danach:

> Schön. Aber wo genau in diesem Kreis sollte ich eigentlich suchen?

Für `Stadtkreise` oder Kreise ohne Gemeindeinformationen in der App kann es sein, dass diese zweite Ausgabe nicht erscheint oder kein zusätzliches Gemeinde-Ranking enthält. Das ist kein Bug — das ist einfach deutsche Verwaltungsgeographie, die deutsche Verwaltungsgeographie ist.

## Warum das Ganze?

Wie am Anfang gesagt: Die „beste Region“ ist ein persönliches Konzept.

Für eine Person ist gute öffentliche Infrastruktur vielleicht alles. Für eine andere zählen Wohnkosten oder Luftqualität mehr. Wieder jemand anderes möchte starke wirtschaftliche Indikatoren, gute Bildung oder einfach einen Ort, bei dem die Daten sagen: „Ja, dieser Kreis könnte deine Lebensentscheidungen tolerieren.“

RegioIndex ist mein Versuch, regionale Vergleiche interaktiver, transparenter und präferenzbasierter[^3] zu machen.

[^3]: Als Ökonom liebe ich dieses Wort: **Präferenzen**.

## Probier es selbst aus

Die Beta-Version ist hier verfügbar:

[https://gstahn.shinyapps.io/Beta_counties/](https://gstahn.shinyapps.io/Beta_counties/)

Das Projekt-Repository findest du hier:

[https://github.com/GStahn/ranking_german_counties](https://github.com/GStahn/ranking_german_counties)

Das frühere Kreis-Ranking-Repository findest du hier:

[https://github.com/GStahn/ranking_german_districts](https://github.com/GStahn/ranking_german_districts)

Nochmal: Die App ist noch in der Beta-Version, also können sich Dinge ändern, verbessern oder gelegentlich merkwürdig verhalten.

## Abschließender Gedanke

RegioIndex wird dir nicht sagen, wo du leben *musst*.

Aber die App kann dir dabei helfen herauszufinden, welcher deutsche Kreis — und vielleicht sogar welche Gemeinde darin — am besten zu deinen Präferenzen passt.

Oder sie gibt dir zumindest eine sehr datengestützte Ausrede, um beim Abendessen über regionale Attraktivität zu diskutieren.

