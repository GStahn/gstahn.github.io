---
title: "Nein, man kann ihnen nicht trauen"
author: "Gerrit Stahn"
date: "2026-07-20"
params:
  lang: de
permalink: /posts/memes/
description: "Drei LLMs — ChatGPT, Gemini und Claude — wurden gebeten, die Zinserträge
  zweier Sparprodukte zu vergleichen. Alle drei machten denselben subtilen Timing-Fehler,
  was zeigt, warum KI-Antworten auf Finanzfragen weiterhin einen menschlichen
  Realitätscheck brauchen."
keywords:
- LLM Finanzielles Denken
- ChatGPT vs Gemini vs Claude
- KI-Zinsberechnung
- Sparvergleich
- Geldmarktfonds
- Tagesgeldkonto
- Behavioral Finance
- Gerrit
- Stahn
- Gerrit Stahn
---

## ![Anakin - Padme - Würdest du ihnen vertrauen?](/img/memes/padme_trustllms.jpg)

##

------------------------------------------------------------------------
##

**Kontext:** Nachdem ich gerade ohne festes monatliches Einkommen nach Vancouver in Kanada gezogen bin, greife ich auf mein angespartes Vermögen zurück, um meinen aktuellen Konsum zu glätten.[^1] Diese Ersparnisse verteilen sich auf ein Tagesgeldkonto und einen Geldmarktfonds, was mich vor eine sehr praktische Frage stellte: Welchen Topf sollte ich zuerst angreifen? Als Ökonom habe ich das natürlich umformuliert zu „Welche Option verursacht für den Rest des Jahres die höheren Opportunitätskosten in Form entgangener Zinsen?" — und beschlossen, entgangene Zinsen als alleiniges Maß der Opportunitätskosten zu behandeln.

[^1]: Für alle, die keine Ökonomen sind: Das bedeutet, dass ich in Kanada keinen Job habe und meine Rechnungen mit meinen Ersparnissen bezahle.

Ein paar Details machten den Vergleich kniffliger, als er zunächst scheint. Erstens: Das Tagesgeldkonto ist neu (eröffnet am 20. Mai) und bietet derzeit vier Monate lang einen Aktionszins von 4 % p.a.; sobald dieses Fenster am 20. September endet, fällt der Zinssatz auf 2 % p.a. Zweitens: Meine Position im Geldmarktfonds stammt tatsächlich schon aus August 2025, sodass die Opportunitätskosten-Uhr für dieses Konto nicht zum selben Zeitpunkt zu laufen beginnt. Drittens: Die Rendite des Fonds ist nicht fest — sie schwankt —, weshalb ich vereinfachend eine durchschnittliche Jahresrendite von 2 % angenommen habe, was einigermaßen gut mit seiner historischen Performance übereinstimmt.

Ich habe die Zahlen natürlich zuerst selbst durchgerechnet, war aber neugierig, ob ein LLM zum gleichen Ergebnis kommen würde. Unten befinden sich die Antworten von ChatGPT (GPT-5.5), Google Gemini (3.5 Flash) und Claude (Sonnet 5) auf einen identischen Prompt, mit 1.000 € auf dem Konto und 950 € im Fonds:

------------------------------------------------------------------------
> Prompt: Vergleiche die Zinserträge über einen Einjahreszeitraum (beginnend am 1. Januar 2026) für zwei verschiedene Anlagen: Anlage 1: Am 20. Mai habe ich 1.000 € investiert. Ich erhalte bis zum 20. September einen Aktionszinssatz von 4 % p.a. Ab dem 21. September sinkt der Zinssatz auf 2 % p.a. Anlage 2: Am 8. August 2025 habe ich 950 € investiert. Für diese Anlage erhalte ich dauerhaft einen Zinssatz von 2 % p.a.
------------------------------------------------------------------------

Alle drei Modelle teilen denselben grundlegenden Fehler bei Anlage 2. Bevor du weiterliest: Versuch selbst, ihn zu finden.

<div style="
  margin: 2rem auto;
  max-width: 900px;
">

  <div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  ">
    <iframe 
      src="/pdf/Investment Interest Comparison_ChatGPT.pdf"
      style="width:100%; height:850px; border:none;">
    </iframe>
  </div>
    <p style="
    text-align: center;
    margin-top: 1rem;
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #555;
  ">
    Ausgabe von ChatGPT
  </p>
</div>

------------------------------------------------------------------------
##

<div style="
  margin: 2rem auto;
  max-width: 900px;
">

  <div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  ">
    <iframe 
      src="/pdf/Investment Interest Comparison 2026 - Google Gemini.pdf"
      style="width:100%; height:850px; border:none;">
    </iframe>
  </div>
    <p style="
    text-align: center;
    margin-top: 1rem;
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #555;
  ">
    Ausgabe von Gemini
  </p>
</div>

------------------------------------------------------------------------
##

<div style="
  margin: 2rem auto;
  max-width: 900px;
">

  <div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  ">
    <iframe 
      src="/pdf/Investment Interest Comparison 2026 - Claude.pdf"
      style="width:100%; height:850px; border:none;">
    </iframe>
  </div>
    <p style="
    text-align: center;
    margin-top: 1rem;
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #555;
  ">
    Ausgabe von Claude
  </p>
</div>

------------------------------------------------------------------------
##

Hier der Haken: Jedes der drei Modelle geht davon aus, dass die Fonds-Anlage erst ab dem 1. Januar 2026 Erträge erwirtschaftet — obwohl das Geld dort tatsächlich schon seit August 2025 Rendite erzeugt. Das klingt zunächst nach einer vernünftigen Vereinfachung, da der Prompt den Vergleichszeitraum ab dem 1. Januar rahmt — aber dabei werden stillschweigend die vor diesem Datum bereits erbrachten Zinsen ignoriert. Berücksichtigt man die rund 145 Tage zwischen der Einzahlung im August 2025 und dem Jahresende, hätte der Fonds bereits Folgendes erwirtschaftet:

$$
950 \cdot \left(0.02 \cdot \frac{145}{360}\right) \approx 7{,}75€
$$

Statt der rund 19 €, die eine „sauberer Start am 1. Januar"-Annahme für 2026 impliziert, sollte der tatsächliche Jahresgewinn also die etwas größere Basis widerspiegeln, die durch diese früheren Zinsen bereits aufgebaut wurde:

$$
957{,}5 \cdot 0.02 = 19{,}15€
$$

Diese Differenz wirkt winzig, aber man bedenke: In diesem Beispiel geht es um ein eher bescheidenes Sparvermögen — alles andere als ausreichend, wenn man ohne Job in der Tasche nach Vancouver zieht.

Es lohnt sich auch, zu vergleichen, wie die drei Modelle Anlage 1 gehandhabt haben. Claude und Gemini kamen beide auf denselben Wert, den ich von Hand berechnet habe — sozusagen die „Doktortitel-in-Ökonomk"-Version. ChatGPT dagegen lieferte eine Antwort wie ein Wirtschaftsstudent im Bachelorstudium: Gemessen an seiner eigenen, eingangs formulierten Annahme technisch korrekt, aber es berücksichtigt nicht alle Informationen aus der Aufgabenstellung.

Wo also liegt das eigentliche Problem? Es stellt sich heraus, dass es in der Formulierung meines Prompts verankert ist. Ersetzt man „über einen Einjahreszeitraum (beginnend am 1. Januar 2026)" einfach durch „im Jahr 2026", verschiebt sich das Bild: Claude errechnet zwar wieder den "falschen" Betrag su, weist aber nun darauf hin, dass es Zinseszinseffekte bei der ersten Anlage außer Acht lässt. Gemini kommt zum „Doktortitel-in-Ökonomk"-Ergebnis. ChatGPT liegt weiterhin genauso weit daneben wie zuvor.

Die Erkenntnis (wieder einmal): Überlasst eure Geldentscheidungen nicht blind einem LLM — genau das ist die Pointe des Memes. Behandelt diese Tools allenfalls als Möglichkeit, eure eigene Überlegung gegenzuprüfen und nicht als Ersatz dafür. Und wenn ihre Antworten sich zu deinen widersprechen, ist das nur ein Signal, dass du falschliegen könntest — aber womöglich auch nicht.
