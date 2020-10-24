import random


class Die:

    def __init__(self, sides):
        if sides <= 0 :
            raise ValueError('Die cannot be created with 0 or fewer sides.')
        self.sides = sides
        self.past_rolls = []
        self.val = None


    def roll(self):
        self.past_rolls.append(self.val)
        self.val = random.randint(1, self.sides)


class DiceRoll:

    def __repr__(self):
        return 'Dice Roll - Total {} ({})'.format(
            self.total(), 
            ', '.join([str(d.val) for d in self.dice])
        )

    
    def __init__(self, dice):
        self._dice = dice

    
    @property
    def dice(self):
        return self._dice


    def total(self):
        return sum(map(lambda d: d.val, self.dice))

    
    def re_roll_lowest(self, n):
        if n <= 0:
            raise ValueError('n must be higher than 0 to re-roll')
        sort_dice = sorted(self.dice, key=lambda d: d.val)
        re_roll = sort_dice[:n]
        for d in re_roll:
            d.roll()


    def re_roll_highest(self, n):
        if n <= 0:
            raise ValueError('n must be higher than 0 to re-roll')
        sort_dice = sorted(self.dice, key=lambda d: d.val)
        re_roll = sort_dice[(len(sort_dice) - n):]
        for d in re_roll:
            d.roll()

    