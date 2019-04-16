# 2nd week's work

## unittest (<1h)

- Little speech on unittest and code coverage.
- Exercise: each of the 7 groups adds unit tests (using `unittest`) to cover the whole of `deck.py`:

    - Group A: `Color`
    - Group B: `Card`
    - Group C: `Hand.__special_functions__`
    - Group D: `Hand.normal_functions`
    - Group E: `Deck.__special_functions__`
    - Group F: `Deck.normal_functions`
    - Group G: `Game.__init__` and `reset`, and provide a setUp function for everyone.
  
All groups should then add a test-case for the rest of the class `Game` (lines 193-435, divided by 7 groups makes up the following partition: [193, 227, 261, 295, 329, 363, 397, 431]). See `hanabi_unittest.py`.
    
Once finished, make a pull-request to `upstream`. 


## Back to AIs (>2h)

Last week you were able to code a simple AI (something like 10-20 lines of python).
Today's work is twofold:

- design a python script that runs 1000 games, and stores some statistics on the games it just played (obviously the mean score, but min, max, nb of perfect games, reason of defeat or imperfect score, ...) 
- design a more complex AI (see suggestions and biblio in README.md)

Since you are in groups of two, work in parallel on each task, and _discuss_ on design choices every ~15 minutes.


There's a third task for the group of 3: redefine the API of `Game`, so an AI may not cheat by accident. In other words, identify properly the "public" functions and attributes of the `Game` class.
It is not yet clear whether a `CheatWarning` should be raised, or if the API should prefix the function names, or yet something else. Once done, we will discuss it all together.


## Further reading: coverage

    pip3 install --user coverage
    coverage run ./hanabi_unittest.py
    coverage report -m |sed 's/auto.*egg//'


## Git workflow

Make sure you work in a fork: a `git remote -v` should display both `origin` (your version) and `upstream` (my version), a bit like this:

    origin  	git@github.com:your_login/your_hanabi.git (fetch)
    origin  	git@github.com:your_login/your_hanabi.git (push)
    upstream	git@github.com:JDGaraudEnsta/hanabi.git (fetch)
    upstream	git@github.com:JDGaraudEnsta/hanabi.git (push)


[Sync fork with upstream from browser](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser)

Or to sync fork from upstream from the command-line (NEEDS VERIFICATION!):

    # only the integrator needs to do this
    git status # if modif, commit them first!
    git pull upstream master
    git commit -a -m "Sync fork with upstream"
    git push origin master


Some discussion topics:

- [this dev model](https://nvie.com/posts/a-successful-git-branching-model/), mostly [this section](https://nvie.com/posts/a-successful-git-branching-model/#the-main-branches)
- development vs. production code
- new attemps vs. bug fixes (new attempts are often abandoned, but we still like to keep a trace)


## Documentation

`make doc` should work.
If not, `pip3 install --user python3-sphinx`.
