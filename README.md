# Hanabi project

A python3 module that knows Hanabi:

* card deck and dealer
* CLI, verify that your moves are allowed
* GUI
* AI


## Tasks

This project is for 3 to 4 students:

* Aisha is in charge of the AI.
* Cliona is in charge of the main module and command-line interface.
* Electra is the free-electron: project manager, superviser, end-user, tester, debugger.
* Guido is in charge of the GUI.

Make sure you discuss a lot, and share information. 
This will help designing a readable/usable code.


### Week 1

* Electra: fast-prototype the module's interface, keeping in mind the 3 use-cases: command-line, GUI and AI auto-play. Very quickly, we'll want a "replay" feature, for debugging: design a way to do this.
* Cliona: program the module and a CLI (keep it simple).
* Aisha: read the article, design you own idea, summarize the algorithm(s). Write 1 or 2 algorithms (will help the design of module's interface).
* Guido: try a simple GUI (PySide), start experimenting, prepare canvas.


### Week 2

* Stabilize the module: because from now on all devels will have to use it.

* Guido: make an usable GUI
* Aisha: Implement the random-AI and cheater-AI
* Cliona and Electra: play a few games. Design a way to replay games (test-suite). Keep track of score, so that Aisha has someone to compete against.

### Week 3

* Test, experiment, put in production.
* Everyone designs a more advanced AI.
* Someone can take care of 3-5 players.
* Write short report, documentation (e.g. sphinx), ...


### Extra

* Answer the question from the paper: what is the average score. Compare with the Cheater's score. Add divination for Cheater (she can see through the deck).



## Bibliography

### Other Hanabi projects

* [A C++ bot: some strategies and success rates](https://github.com/Quuxplusone/Hanabi)
* [HanSim: the Hat guessing strategy](https://d0474d97-a-62cb3a1a-s-sites.googlegroups.com/site/rmgpgrwc/research-papers/Hanabi_final.pdf?attachauth=ANoY7cp_mjjD7lCb5HFxBphRWpSkE8SabM7PiOVWFwcNKSnpxENRLwTsQEgDMC6PIHuBmzP4oixvH_B8PZQmrHDyfA-ZLSKWb-Lx1WJNIUKUoxV1w0K0bWXelLPCi5MbXaByoVcukH4CEg-5N_iJP7mKSDHiV5ImwGDBCwQoT4mwvppVyA0BVb2Lhr-mGYFtUw3uBlds77azk5RjFZHGvAtvx6idYLvunLLj6BStHWHrNovX8p5KGFk%3D&attredirects=0)
* [HanSim: source code](https://github.com/rjtobin/HanSim)
* [boardgame arena](https://fr.boardgamearena.com/#!gamepanel?game=hanabi)
* [hanabi conventions (hanabi-live)](https://github.com/Zamiell/hanabi-conventions), and references therein.


### AI

* [deepmind: Atari](https://arxiv.org/pdf/1312.5602v1.pdf)
* [deepmind: SC2](https://arxiv.org/abs/1708.04782)
* [deepmind: Hanabi](https://arxiv.org/abs/1902.00506)
* todo: find non-deepmind references?



### Misc (coding principles, project, ...)

* [keep it simple](https://en.wikipedia.org/wiki/KISS_principle)
* [rule of least surprise](http://www.catb.org/esr/writings/taoup/), [catbaz](http://www.catb.org/esr/writings/cathedral-bazaar/)
* [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
* [markdown](https://guides.github.com/features/mastering-markdown/)
