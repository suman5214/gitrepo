class Player:

    def __init__(self, x, y,steps):
        '''
        Creates a new Player.
        :param x: x-coordinate of position on map
        :param y: y-coordinate of position on map
        :param steps: the total steps that the player can move
        :return:

        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you see fit.
        Consider every method in this Player class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.steps = steps
        self.inventory = []
        self.victory = False
        self.score = 0
        self.required_item = 0
    
    def add_score(self,score):
        '''
        Given integer score, and add on the current score that player has(self.score += score)
        :param score : integer
        :return:
        '''
        self.score += score
    
    def add_required_item(self):
        '''
        Add one to the current required_item that player has(self.required_item += 1)
        :param: 
        :return:
        '''        
        self.required_item += 1     
    
    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        :param dx:
        :param dy:
        :return:
        '''
        pass
    
    def check_victory(self):
        '''
        Checks if the required item is being collected or the assigned steps are all being
        used, and change teh status of self.victory according to the situation
        :param:
        :return:
        '''
        if self.required_item == 3:
            print('Congratulation you found everything !!')
            self.victory = True
        elif self.steps == 0 :
            print('Game over, you ran out of steps !!')
            self.victory = True            
    
    def move_north(self):
        '''
        if the player chose to move north then minuse 1 on its y-cordinate
        :param: None
        :return: None
        '''
        self.move(0,-1)

    def move_south(self):
        '''
        if the player chose to move south then add 1 on its y-cordinate
        :param: None
        :return: None
        '''
        self.move(0,1)

    def move_east(self):
        '''
        if the player chose to move east then add 1 on its x-cordinate
        :param: None
        :return: None
        '''        
        self.move(1,0)

    def move_west(self):
        '''
        if the player chose to move west then minus 1 on its x-cordinate
        :param: None
        :return: None
        '''        
        self.move(-1,0)

    def add_item(self, item):
        '''
        Add item to inventory.
        :param item:
        :return:
        '''
        self.inventory.append(item)
        print('\n--> You have picked up: ' + item.get_name()+'\n')
    
    def use_item(self,item):
        '''
        Remove the item from inventory,and print a line that 
        indicates the item has being consumed 
        :param item:
        :return :
        '''
        self.inventory.remove(item)
        print('\n--> You just used: ' + item.get_name()+'\n')        
    
    def drop_item(self, item):
        '''
        Remove item from inventory.
        :param item:
        :return:
        '''
        self.inventory.remove(item)
        print('\n--> You just dropped: ' + item.get_name()+'\n')
    
    def get_inventory(self):
        '''
        Return inventory.
        :return:
        '''
        return self.inventory
