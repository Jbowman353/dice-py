import random

# Die class
# Represents a die with a specified no. of sides
# constructor: Die(sides)
# | sides: no. of sides
class Die:

    def __init__(self, sides):
        if sides <= 0 :
            raise ValueError('Die cannot be created with 0 or fewer sides.')
        self.sides = sides
        self.past_rolls = []
        self.val = None


    # roll()
    # Roll this die and set its new value
    def roll(self):
        self.past_rolls.append(self.val)
        self.val = random.randint(1, self.sides)


# DiceRoll class
# represents a group of dice
# constructor: DiceRoll(dice)
# | dice: list of Die objects
class DiceRoll:

    def __repr__(self):
        return 'Dice Roll - Total {} ({})'.format(
            self.total(), 
            ', '.join([str(d.val) for d in self.dice])
        )

    
    def __init__(self, dice: list[Die]):
        self._dice = dice


    # dice property - read only    
    @property
    def dice(self):
        return self._dice


    # total()
    # returns sum of dice values
    def total(self):
        return sum(map(lambda d: d.val, self.dice))

    
    # reroll_lowest(n)
    # Params:
    # n - number of lowest-valued dice to reroll
    # -- 
    # returns re-rolled Die objects
    def reroll_lowest(self, n):
        if n <= 0:
            raise ValueError('n must be higher than 0 to re-roll')
        sort_dice = sorted(self.dice, key=lambda d: d.val)
        re_roll = sort_dice[:n]
        for d in re_roll:
            d.roll()
        return re_roll


    # reroll_highest(n)
    # Params:
    # n - number of lowest-valued dice to reroll
    # -- 
    # returns re-rolled Die objects
    def reroll_highest(self, n):
        if n <= 0:
            raise ValueError('n must be higher than 0 to re-roll')
        sort_dice = sorted(self.dice, key=lambda d: d.val)
        re_roll = sort_dice[(len(sort_dice) - n):]
        for d in re_roll:
            d.roll()


    # to_dict
    # returns a JSON-friendly dict representing the rolled dice
    def to_dict(self):
        res = {
            'total': self.total(),
            'dice': []
        }
        for die in self.dice:
            res['dice'].append({
                'sides': die.sides,
                'val': die.val
            })

        return res