# 1st week's work

## Download, install and test 

    git clone ...
    cd hanabi
    make   # read the help mesg
    make module
    make doc
    make test

If everything is properly set up, you should see:

- after make module
```
Installed /home/you/.local/lib/python3.5/site-packages/hanabi-0.1.0-py3.5.egg
Processing dependencies for hanabi==0.1.0
Finished processing dependencies for hanabi==0.1.0
```

- after make doc
```
Build finished. The HTML pages are in build/html
```

- after make test
```
========= Summary ===========
test       score ref  status
game1.py       4   4    Ok
game2.py      20  20    Ok
game3.py      24  24    Ok
game4.py      25  25    Ok
game5.py      21  21    Ok
game6.py      24   0  No ref
game7.py      11   0  No ref
game8.py      19   0  No ref
All tests are ok
```

Play a quick game by running `hanabi` (if this doesn't work, look at [installation](https://github.com/JDGaraudEnsta/hanabi#installation)).


## Now let's go through the code

The main file is `src/hanabi/deck.py`, we'll go through it step by step.

- Start by looking at the class `Card`, make sure you understand how it works. The `__eq__` function *is* not trivial, discuss it.
- Now look at `Color` (note the derivation)
- Now Hand and `Deck`. Explain what `Deck.__init_` does. Explain how `Deck.deal` differs from a human dealer.
- Now for class `Game`: it is too big. We'll look at it via sphinx: open `./doc/build/html/index.html` in a navigator.

Finally look at `ai.py`: is contains a Cheater AI. 
Note that it is coded using imperative programming.

Today's job is to code a new AI.

But before you start, **fork the project**!

## Fork 

https://help.github.com/en/articles/fork-a-repo


## Code a new AI

Do not forget last week's TDD concepts:

 - write at least 1 test, 
 - then document you AI, 
 - now (and only now) should you start to code something.

Some example of simple AIs: `Random`, `RandomButNotTotallyDumb`, `DirectClue`, `SuperSafe`, ...
