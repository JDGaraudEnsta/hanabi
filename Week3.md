# 3rd week's work

## Discussion

Do we need a private repository?


## unittest (<1h)

- (students) create a branch + cherrypick the commits you want to push
- (teacher) check contributions, iterate id needed, accept pull-requests
- by the way, if you want to unittest Exceptions, it is fairly easy:

```
class DeckTest(unittest.TestCase):
  def test1(self):
    deck = hanabi.Deck()
    with self.assertRaises(KeyError):
      deck.deal(nhands=6)
    hands = deck.deal(nhands=2)
    ...
```

- (teacher+students) : verify  that 100% of tests are Ok.

- run coverage again to see if we're good. 


## Back to AIs (>2h)

Last week's instructions still apply.

Some new ideas: 

- AI that plays all hinted cards (from newest to oldest).
      How can it save bombs, when the 2nd hinted cards is not playable? Can it anticipate on the other players play? Should it hint then complete the hint on a 2nd turn? Should it refuse to hint in the first place? 
      
- AI that plays the newest hinted card, then wait for confirmation. 
      How can it confirm a hint?
      The "age" of a hint becomes an importannt information (does it? did it already for previous AIs?)
      
- Cheater is not yet as good as HanSim's Cheater (average e24.87 on 10^6 games, see page).

- Debug games for 3, 4, 5 players


    
    

## Documentation (10 min)

`make doc` should work. 
If not, `pip3 install --user python3-sphinx`.

There's a little report to do at the end of the project.

(teacher: test md+sphinx. )


