---
title: "Etwas (hoffentlich) Großes ist in der Mache"
subtitle: "Das klassische *Wählen* von Teams ist scheiße. Lasst es uns besser machen."
date: 2026-08-26
author: "Gerrit Stahn"
language: "de"
description: "Ein Rückblick auf die Frustration der Teamauswahl im Sport und wie eine eigens entwickelte App-Idee für faire, zufallsbasierte Teamverteilungen sorgen soll."
keywords:
  - Team Assignment App
  - R Shiny
  - Python
  - Teambildung
  - Algorithmus
  - Sport
tags:
  - App-Entwicklung
  - Programmierung
  - Volleyball
  - Projekte
draft: false
---

## Hintergrund

Schon als Kind und Jugendlicher konnte ich es nicht leiden, wenn zu Beginn des Sportunterrichtes wieder einmal Teams gewählt werden mussten. Nicht nur, dass es eine halbe Ewigkeit dauerte (erst wurden Kapitän*innen bestimmt, dann mussten diese untereinander ausmachen - mittels *Tip-Top* -, wer anfängt und dann wurde erst gewählt). Selbst bei meinem geburtenschwachen Jahrgang dauerte der Prozess ewig mit dem Resultat, dass die Gruppe *der Letztgewählten* schon vorm Spielanpfiff seelisch gedemütigt wurde. Nur die ohnehin schon in dem Spiel Guten waren danach guter Dinge und durch ein gehöriges Maß an verschiedenen Formen der frühkindlichen Vetternwirtschaft[^1] und dem dezidierten Desinteresse der Lehrkräfte entstanden so absolut unausgewogene Partien. Ganz toll (nicht).[^2]

[^1]: Dadurch wurden die beliebten Mittelmäßigen auch häufig an zweiter oder dritter Stelle gewählt. 

[^2]: Ich wurde damals in der Fußball-AG wiederholt als Letzter gewählt. Dies tat jedes Mal weh. Als Ausgleich für diese Schmach (und meine fehlenden Fußball-Fähigkeiten) habe ich damals [Catenaccio](https://en.wikipedia.org/wiki/Catenaccio) auf Kreisliga-Niveau gespielt. Ich entschuldige mich hier offiziell für so manche Blessur bei so manchen Mitspielern (und bei manchen auch nicht). 

Vor ein paar Jahren holte mich diese Zeitverschwendung und das dazugehörige Trauma wieder ein. Damals trat ich meinem geliebten Volleyball-Verein [SC261 Halle e.V.](https://www.sc261.de/) bei. Auch dort wurden Teams gewählt und auch dort kam es zu den bereits von mir gut bekannten Phänomenen. Anders als bei der Fußball-AG wollte (und konnte) ich meinem Frust aber keinen Weg verschaffen durch eine räudige Spielweise (Volleyball ist kein Kontaktsport). 

Ich dachte also: "Das muss doch besser gehen!". Als überzeugter Jünger der Zufallsverteilung als Methode zur Vergleichbarmachung von Gruppen, hatte ich auch schon eine Idee ...

## Stage 1: Die Team Assignment App

Ich fing an, in meiner Freizeit eine App zu entwickeln, welche dieses Problem angehen sollte. Daraus entstand die [Team Assignment App](https://github.com/GStahn/Shiny_random_teams) als eine passwortgeschützte **R Shiny-Anwendung** zur effizienten Spielerverwaltung und fairen Zufallsgenerierung von Teams. Die Benutzeroberfläche basiert auf **Bootstrap 5 (`bslib`)** und bietet ein responsives Design inklusive integriertem Hilfesystem und automatischem Scrolling zum Teambereich. 

Kernfunktionen umfassen das Verwalten einer Spielerliste, das Markieren anwesender Teilnehmer sowie eine durchdachte Kapitäns-Logik: Bestimmte Spieler können als Kapitäne definiert, automatisch an die Spitze jedes Teams platziert und bei Bedarf nachträglich per Dropdown angepasst werden. Nach der fehlergesicherten und zufälligen Verteilung der übrigen Spieler auf eine wählbare Anzahl von Teams lassen sich diese manuell nachbearbeiten. Das Tool bietet zudem Schutzmechanismen gegen falsche Zuweisungen sowie einen direkten **PDF-Export** der Teams mit klarer Kapitäns-Kennzeichnung. Während die aktuelle Entwicklungsversion lokal mit einer vordefinierten Liste arbeitet, ist eine optionale Anbindung an Google Sheets und Google Drive im Code vorbereitet.

Kurz gesagt: Diese kleine App mit einem einfachen Zufallsmechanismus war für mich ein Erfolg. Sie löste die oben genannten Probleme, ich lernte dabei Shiny, App-Entwicklung und Webhosting und war stolz wie Bolle jedes Mal, wenn ich lauthals in unsere Sporthalle rief "Die heutigen Teams sind...".[^3]

[^3]: Wer diese gerne einmal ausprobieren möchte, der kann dies über folgenden [Link](https://gstahn.shinyapps.io/Teams_randomizer/) tun (Benutzer: admin | Passwort: change_me_1). Aber Vorsicht: Der kostenlose shinyapps.io-Server, den ich für das Hosting genutzt habe, läuft mit einer Kartoffel als CPU. Lange Ladezeiten könnten 90er Jahre Nostalgie erzeugen. 

## Stage 2: Nach der App ist vor der App

Mein bester Freund Felix war allerdings nicht ganz so happy mit meiner Idee. Es brauchte auch zugegebenermaßen eine gewisse Zeit (ich musste erstmal den [IKEA Bias](https://en.wikipedia.org/wiki/IKEA_effect) überwinden), bis ich seine Gründe dafür verstehen konnte: 

* Ein zufälliger Zuteilungsmechanismus, bei dem nur die Top-Spieler fest auf die Teams aufgeteilt werden und alle anderen zufällig zugeteilt werden, verkennt natürlich die vielen Nuancen in den Fähigkeiten.
* Angelehnt an den ersten Punkt: Umgekehrt kann die Ballung von einigen, relativ weniger begabten Spielern[^4] bei einem rein zufälligen Verteilungsmechanismus dennoch zu sehr einseitigen Partien führen. 
* Die Auswahl der Top-Spieler bleibt weiterhin subjektiv abhängig vom Nutzer der App. Bei unserem Verein gab es zu dem Zeitpunkt zwei Spieler, die unbestreitbar die zwei besten des Vereins waren. Ab drei Teams wurde es jedoch schwierig zu entscheiden, wer nun der drittbeste / die drittbeste ist. Je mehr Teams gebildet werden müssen, umso subjektiver wird es auch.

[^4]: War für unseren Verein nicht relevant. :-) 

Felix kannte für diese Probleme auch eine Lösung. Diese möchte ich an dieser Stelle nicht weiter ausführen, denn (Spoiler) diese App ist derzeit noch in der Entwicklung und könnte nun vielleicht sogar zu einem Produkt führen, welches sich eventuell verkaufen lässt. Nur so viel: Felix wurde inspiriert von den sogenannten Matching-Algorithmen, die z. B. bei Online-Spielen zum Tragen kommen. Auch dort gibt es diese Problemstellung schon seit Jahrzehnten: Wie schaffen wir es, dass Anfänger A bei einer Onlinepartie nicht sofort mit Profi B gematcht wird. 

![Unser derzeitiges Logo](/img/elorating_app/logo_landing.svg)

*Das derzeitige Logo für unsere App.*

Nach Monaten der Bearbeitung durch Felix, diese App vollkommen neu aufzusetzen und weiterzuentwickeln, fiel bei mir irgendwann der Groschen und wir stürzten uns in den Sommermonaten '26 ins Entwickeln. Derzeit haben wir sogar schon eine Beta-Version, welche wir gerade im Verein testen. Auch holten wir vor kurzem André (Gründer der [ISN GmbH](https://isn-systems.com/) und ehemaligen Vorsitzenden des SC261 -- von mir deshalb verdientermaßen und liebevoll *Chefchen* genannt) ins Boot.  

Mittlerweile bin ich Feuer und Flamme für dieses Projekt, denn dadurch habe ich erneut neue Fähigkeiten gelernt oder bereits erlernte Fähigkeiten vertieft. Dazu zählen (**Liebe Recruiter aufgepasst - ab hier bitte anfangen zu lesen**): 

* **Python-Programmierung:** Fundierte Kenntnisse in Python für die Umsetzung der Anwendungs- und Kernlogik.
* **Web-Frameworks (Shiny für Python):** Erfahrung mit Shiny für Python zum Aufbau der interaktiven Benutzeroberfläche (UI) und des Server-Backends.
* **Datenbanken & SQL:** Umgang mit relationalen Datenbanken (z. B. SQLite) für die strukturierte Speicherung von Spielerdaten.
* **Algorithmen-Design:** Verständnis und Implementierung von Bewertungssystemen sowie Optimierungslogiken für eine faire Teameinteilung.
* **Versionskontrolle & Cloud-Integration:** Sicherer Umgang mit Git und GitHub für die Zusammenarbeit, das Deployment und die automatisierte Sicherung (Backups über GitHub-APIs).
* **Web-Deployment & Hosting:** Grundlagen im Betrieb und Deployment von Webanwendungen (z. B. über Posit Connect Cloud oder eigenständige Server).
* **Frontend-Grundlagen (HTML/CSS):** Anpassung von Oberflächen, Assets und Logos in den entsprechenden `/www/`-Ordnern.

## Abschließender Gedanke

Vielleicht (vielleicht, vielleicht, vielleicht) könnte es tatsächlich so sein, dass das Projekt, das mein bester Freund und ich für unseren Verein ins Leben gerufen haben, am Ende eine viel größere Wirkung entfaltet. Es könnte überall dort zum Einsatz kommen, wo noch immer Zeit verschwendet, Kinder gemobbt oder Vetternwirtschaft im alltäglichen Stil betrieben wird – und so helfen, weitere seelische und physische Verletzungen zu verhindern. Klingt wirklich zu schön, um wirklich wahr zu werden. Stay tuned. 




