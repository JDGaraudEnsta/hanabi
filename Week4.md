# Some more git tips

* On github, click Insights -> Network

For instance: https://github.com/JDGaraudEnsta/hanabi/network


# Refactoring

Have a look at your current code(s).

From time to time, try to see if some functions would be better in the base class, as it was just done for `AI.other_hands` and `AI.other_players_cards` in commit d5defb2.

 
# Solution to the Fork + pull-request

## Solution via patch

Il suffit de créer le patch avec les bonnes modifications :

    git diff 634d774..e5e4fcf -- test/hanabi_unittest.py > patch

puis d'envoyer ce patch au mainteneur du projet (par mail, ...).
C'est une solution assez universelle (fonctionne avec tous les logiciels de versionnage, peut vous servir à stocker un brouillon).


## Solution via git et github

Pour faire proprement un pull-request, il faut avoir créé/identifié une branche contenant les modifications qu'on veut proposer.

Le mieux est d'avoir anticipé la création d'une branche avec juste ce qu'il faut. Dans le cas contraire, on va cherry-picker les bonnes lignes de commit.

Exemple, pour le dépôt de Julie, l'idée est de recréer une branche avec juste ce qu'il faut, à partir du bon point de départ (le dernier merge upstream->origin) :

    git lg
    ...
    | *   634d774 - (13 days ago)  Merge branch 'master' of github.com:JDGaraudEnsta/hanabi 

    git branch unittest-contibutions 634d774
    git checkout unittest-contibutions

Puis on repère les modifications au(x) fichier(s) qu'on veut proposer :

    git lg test/hanabi_unittest.py
    * e5e4fcf - (13 days ago)  Revert "Suppression dune ligne inutile" 
    * 1863292 - (13 days ago)  Suppression dune ligne inutile 
    * 25d1aad - (13 days ago)  test unitaire color 
    * 4d2a63a - (13 days ago)  (HEAD -> unittest-contributions) Discussion topics for Week2 

Et on les réapplique (avec l'option `-n` pour ne pas créer de commit) :

    git cherry-pick -n 25d1aad 1863292 e5e4fcf
    git status
    # on constate que le fichier est "staged"
    # si on veut voir les différences :
    git tkdiff --staged

Finalement, on commit dans la branche :

    git branch 
    # vérifier qu'on est bien sur la branche unittest-contributions
    git commit -m "Add unittest for Color"
    git push origin unittest-contributions



Voir aussi: https://stackoverflow.com/questions/5717026/how-to-git-cherry-pick-only-changes-to-certain-files
Notamment l'utilisation de l'option `-p` combinée à checkout :

    git checkout -b 'unittest-with-selection' 634d774
    git checkout master test/hanabi_unittest.py -p
