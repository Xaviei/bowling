


class Frame(object):
    """Frame"""


    def __init__(self, ID):
        self.id = ID
        self.throws = []

    @property
    def is_done(self):
        return sum(self.throws) == 10 or len(self.throws) == 2
    
    @property
    def is_strike(self):
        print('strike!')
        return sum(self.throws) == 10 and len(self.throws) == 1
    
    
    @property
    def is_spare(self):

        print('Nice Spare')
        return sum(self.throws) == 10 and len(self.throws) == 2

    
    def score(self, next_throws):
        res = sum(self.throws)
        if self.is_strike:
            res += sum(next_throws[:2])
        elif self.is_spare:
            res += sum(next_throws[:1])
        return res
    
    def roll(self, pins):
        if pins < 0:# checks if pin values are correct otherwise adds pin number to score
            raise ValueError(f'pins cannot be negative but received "{pins}".')
        if pins > 10:
            raise ValueError(f'pins cannot be greater than 10 but received "{pins}".')  # noqa
        if sum(self.throws) + pins > 10:
            raise ValueError(f'A frame\'s rolls cannot exceed 10 pins.')
        self.throws.append(pins)






class Player(object):
    """Player"""
    def __init__(self):
        self.score = [Frame.score]
        self.roll = [Frame.roll()]
        self.frames = [Frame]
        self.throws = []
    
    def throws(self):
        pins = int(input)('Enter pins knocked down')
        if pins < 0:
            raise ValueError(f'Cannot enter Negative number')
        if pins > 10:
            raise ValueError(f'Stop playing, there arent even 10 pins in a lane')
        if pins == 10:
            Frame.is_strike

        

        
        
        



        
class BowlingGame(object):
    """BowlingGame"""
    
    def __init__(self):
        self.bonus_throws = []
        self.frames = [Frame(i) for i in range(10)]
        self.frame_num = 0
        

            
    
    @property
    def crnt_frame(self): #shows current frame
        return self.get_frame(self.frame_num)
        
    
    def get_frame(self, frame_num): #gets specific frame via index
        return self.frames[frame_num]
        
    
    def next_throws(self, frameID): #initilizes next frame as array and appends a new frame to the game
        next_throws = []
        next_frameID = frameID + 1
        while next_frameID < 10: #while loop that gets the next frame 
            next_throws += self.get_frame(next_frameID).throws
            next_frameID += 1
        next_throws += self.bonus_throws
        return next_throws
   
    def handle_bonus_throw(self, pins):
        if self.get_frame(9).is_spare:
            if len(self.bonus_throws) == 1:
                raise IndexError(f'Game Over.')
            self.bonus_throws += [pins]  # TODO guard against bad input
        elif self.get_frame(9).is_strike:
            if len(self.bonus_throws) == 2:
                raise IndexError(f'Game over.')
            if sum(self.bonus_throws + [pins]) > 10:
                if len(self.bonus_throws) == 1 and self.bonus_throws[0] == 10:
                    pass
                else:
                    raise ValueError(f'Why you playin!')
            self.bonus_throws += [pins]
        else:
            raise IndexError(f'Game over.')
    
    def roll(self, pins):
        if pins > 10:
            raise ValueError(f'Stop playin!')
        if self.frame_num == 10:
            self.handle_bonus_throw(pins)
        else:
            self.crnt_frame.roll(pins)
            if self.crnt_frame.is_done:
                self.frame_num += 1
   
    def score(self):
        if self.frame_num < 10:
            raise IndexError(f'All frames must be complete before scoring.')
        if self.get_frame(9).is_spare:
            if len(self.bonus_throws) != 1:
                raise IndexError(f'One bonus roll must be taken.')  # noqa
        if self.get_frame(9).is_strike:
            if len(self.bonus_throws) != 2:
                raise IndexError(f'two bonus rolls must be taken.')  # noqa
        return sum(frame.score(self.next_throws(frame.id))
                   for frame in self.frames)


print(BowlingGame.score(0))

