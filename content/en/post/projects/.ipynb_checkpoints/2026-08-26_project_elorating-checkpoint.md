---
title: "Something (Hopefully) Big is in the Works"
subtitle: "The classic picking of teams sucks. Let's change it."
date: 2026-08-26
author: "Gerrit Stahn"
language: "en"
description: "Looking back at the frustration of picking teams in sports and how a custom-built app idea is designed to ensure fair, randomized team distributions."
keywords:
  - Team Assignment App
  - R Shiny
  - Python
  - Team building
  - Algorithm
  - Sports
tags:
  - App Development
  - Programming
  - Volleyball
  - Projects
draft: false
---

## Background

As a child and teenager, I hated it when teams had to be picked at the beginning of P.E. class. Not only did it take forever (first, captains were appointed, then they had to figure out among themselves - via *Tip-Top* - who goes first, and only then did the picking start). Even in my low-birth-rate year, the process took ages, with the result that the group of *last-picked* kids was already mentally humiliated before the starting whistle. Only those who were already good at the game were in good spirits afterwards, and thanks to a fair amount of various forms of early-childhood nepotism[^1] and the teachers' dedicated lack of interest, the resulting matchups were absolutely unbalanced. Awesome (not).[^2]

[^1]: As a result, the popular average players were also frequently picked second or third. 

[^2]: Back then in the after-school soccer club, I was repeatedly picked last. It hurt every time. To compensate for this humiliation (and my lack of soccer skills), I played [Catenaccio](https://en.wikipedia.org/wiki/Catenaccio) at a Sunday-league level. I hereby officially apologize for some of the bruises on some of my teammates (and to some I don't). 

A few years ago, this waste of time and the associated trauma caught up with me again. Back then, I joined my beloved volleyball club [SC261 Halle e.V.](https://www.sc261.de/) in Germany. Teams were picked there too, and the phenomena I was already well acquainted with occurred there as well. Unlike in the soccer club, however, I wouldn't (and couldn't) vent my frustration through a dirty style of play (volleyball is not a contact sport). 

So I thought: "There has to be a better way!". As a convinced disciple of random distribution as a method for making groups comparable, I already had an idea...

## Stage 1: The Team Assignment App

I started developing an app in my free time to tackle this problem. The result was the [Team Assignment App](https://github.com/GStahn/Shiny_random_teams), a password-protected **R Shiny application** for efficient player management and fair randomized team generation. The user interface is based on **Bootstrap 5 (`bslib`)** and offers a responsive design, including an integrated help system and automatic scrolling to the team section. 

Core features include managing a player list, marking present participants, and a well-thought-out captain logic: Specific players can be defined as captains, are automatically placed at the top of each team, and can be adjusted via a dropdown menu later if necessary. After the error-proof and random distribution of the remaining players into a selectable number of teams, these can be edited manually. The tool also provides protective mechanisms against incorrect assignments as well as a direct **PDF export** of the teams with clear captain indicators. While the current development version works locally with a predefined list, an optional connection to Google Sheets and Google Drive is prepared in the code.

In short: This small app with a simple random mechanism was a success for me. It solved the problems mentioned above, I learned Shiny, app development, and web hosting in the process, and was proud as punch every time I shouted loudly across our sports hall, "Today's teams are...".[^3]

[^3]: If you'd like to try it out, you can do so via the following [link](https://gstahn.shinyapps.io/Teams_randomizer/) (Username: admin | Password: change_me_1). But beware: The free shinyapps.io server I used for hosting runs on a potato for a CPU. Long loading times might induce '90s nostalgia. 

## Stage 2: After the App is Before the App

My best friend Felix wasn't quite as happy with my idea, though. Admittedly, it took a certain amount of time (I first had to overcome the [IKEA Bias](https://en.wikipedia.org/wiki/IKEA_effect)) until I could understand his reasons for this: 

* A random assignment mechanism where only the top players are fixed to the teams and everyone else is assigned randomly naturally ignores the many nuances in skills.
* Tied to the first point: Conversely, the clustering of a few relatively less gifted players[^4] in a purely random distribution mechanism can still lead to very one-sided matches. 
* The selection of the top players remains subjective, depending on the user of the app. At our club, there were two players at the time who were indisputably the best two in the club. With three teams or more, however, it became difficult to decide who the third best was. The more teams that need to be formed, the more subjective it becomes.

[^4]: Wasn't relevant for our club. :-) 

Felix also knew a solution to these problems. I don't want to go into detail about it here, because (spoiler) this app is currently still in development and might even lead to a product that could potentially be sold. I'll just say this much: Felix was inspired by so-called matchmaking algorithms, which are used in online games, for example. The same problem has existed there for decades: How do we ensure that Beginner A is not immediately matched with Professional B in an online match? 

![Our current Logo](/img/elorating_app/logo_landing.svg)

*The current logo of our app.*

After months of Felix working on me to completely rebuild and further develop this app, the penny finally dropped for me, and we threw ourselves into development in the summer months of '26. We even currently have a beta version that we are testing in the club right now. We also recently brought André (founder of [ISN GmbH](https://isn-systems.com/) and former chairman of SC261 -- affectionately and deservedly called *Chefchen* [little boss] by me) on board.  

By now, I'm absolutely fired up about this project, because through it I've once again learned new skills or deepened existing ones. These include (**Dear recruiters, pay attention - please start reading from here**): 

* **Python Programming:** Solid knowledge of Python for implementing the application and core logic.
* **Web Frameworks (Shiny for Python):** Experience with Shiny for Python to build the interactive user interface (UI) and the server backend.
* **Databases & SQL:** Handling relational databases (e.g., SQLite) for the structured storage of player data.
* **Algorithm Design:** Understanding and implementing rating systems and optimization logic for fair team assignment.
* **Version Control & Cloud Integration:** Confident use of Git and GitHub for collaboration, deployment, and automated backups (via GitHub APIs).
* **Web Deployment & Hosting:** Basics in operating and deploying web applications (e.g., via Posit Connect Cloud or standalone servers).
* **Frontend Basics (HTML/CSS):** Customizing interfaces, assets, and logos in the corresponding `/www/` folders.

## Final Thought

Perhaps (perhaps, perhaps, perhaps) a project managed together with my best friend for our beloved club might eventually lead to something that can be used wherever time is still being wasted today, kids are bullied, everyday nepotism is practiced, and thus many (mental and physical) injurys still occur. It definetly sounds like a dream too perfect to be true. 