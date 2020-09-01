# Hanabi project

This project is for educational purposes: 
its current status should represent the student's starting point.

# Hanabi module

A python3 module that knows Hanabi:

* card deck and dealer,
* CLI (command line interface), lets you play and verifies that your moves are allowed (currently limited to 2 players),
* GUI (to do),
* AI (currently only one, and it is cheating).



## Tasks

There are many possible tasks:

- read the current state of the module, 
  - complete its documentation when needed,
  - share with everyone this improvement,

- improve the CheaterAI
  -- answer the question (still an open question afaik): what is the best possible score, statistically speaking?

- add AIs. Some suggestions:
  - RandomAI (plays randomly),
  - DirectAI (plays whatever is hinted),
  - BGAAI (plays Board Game Arena's standard),
  - HansimAI (see below),
  - train a machine learning (I'm not sure if this will give anything interesting without powerful CPU/GPU resources),
  - design your own, from scratch or by improving an existing one.

Keep track of scores for all these games/AI. 
We will want to compare: different AIs on a same deck, or a given AI over a 1000 decks. 
We will need to see why a certain AI fails on a certain game.


- make it workable for up to 5 players.

- make it workable from two separate screens (network?)

- you may also design a GUI, but be warned that this is a very time-consuming task.
I like PySide2. Tkinter is more portable but harder to learn imho. 


During the project:
  - make sure you understand the "replay" mode
  - add tests (UnitTest or whole tests)
  - keep notes on your questions, decisions, discussions (github's wiki)




## Installation

### For Linux and Mac:

    git clone https://github.com/JDGaraudEnsta/hanabi
    cd hanabi
    git pull
    make        # pip installs it in the default directory ~/.local
    hanabi
    # and now you may play


If `hanabi` doesn't start (`bash: hanabi: command not found`), add this to your `~/.bashrc`:

    export PATH=$HOME/.local/bin:$PATH

### For Windows, first dependencies:

    pip install pyreadline

then the installation:
    
    cd hanabi/src
    python3 setup.py install --user

    


## Bibliography

### Other Hanabi projects

* [A C++ bot: some strategies and success rates](https://github.com/Quuxplusone/Hanabi)
* [HanSim: the Hat guessing strategy](https://d0474d97-a-62cb3a1a-s-sites.googlegroups.com/site/rmgpgrwc/research-papers/Hanabi_final.pdf?attachauth=ANoY7cp_mjjD7lCb5HFxBphRWpSkE8SabM7PiOVWFwcNKSnpxENRLwTsQEgDMC6PIHuBmzP4oixvH_B8PZQmrHDyfA-ZLSKWb-Lx1WJNIUKUoxV1w0K0bWXelLPCi5MbXaByoVcukH4CEg-5N_iJP7mKSDHiV5ImwGDBCwQoT4mwvppVyA0BVb2Lhr-mGYFtUw3uBlds77azk5RjFZHGvAtvx6idYLvunLLj6BStHWHrNovX8p5KGFk%3D&attredirects=0)
* [HanSim: source code](https://github.com/rjtobin/HanSim)
* [boardgame arena](https://fr.boardgamearena.com/#!gamepanel?game=hanabi)
* [hanabi conventions (hanabi-live)](https://github.com/Zamiell/hanabi-conventions), and references therein.


### AI (deep learning)

* [deepmind: Atari](https://arxiv.org/pdf/1312.5602v1.pdf)
* [deepmind: SC2](https://arxiv.org/abs/1708.04782)
* [deepmind: Hanabi](https://arxiv.org/abs/1902.00506)
* [facebook's](https://ai.facebook.com/blog/building-ai-that-can-master-complex-cooperative-games-with-hidden-information/)


### Misc (coding principles, project, ...)

* [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
* [keep it simple](https://en.wikipedia.org/wiki/KISS_principle)
* [rule of least surprise](http://www.catb.org/esr/writings/taoup/), [catbaz](http://www.catb.org/esr/writings/cathedral-bazaar/)
* [how to debug small programs](https://ericlippert.com/2014/03/05/how-to-debug-small-programs/), [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
* [markdown (overview)](https://guides.github.com/features/mastering-markdown/), [markdown (in details)](https://github.github.com/gfm/)
* [BGA state machine](https://www.slideshare.net/boardgamearena/bga-studio-focus-on-bga-game-state-machine)
* dive into python3, esp. chapter on Unit testing
