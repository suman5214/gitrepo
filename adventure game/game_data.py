class Location:

    def __init__(self,location_number, brief_description, long_description):
        '''Create Location with a location_number indicating the position in the world map,
        two strings: brief_description,long_description that describes the location.
        
        :param location_number: a position in the world map,
        :param brief_description: a brief description,
        :param long_description: a long description,
        :param :

        '''

        self.location_number = location_number
        self.brief_description = brief_description
        self.long_description = long_description
        self.items = []       #the items that are in the location
        self.visited = False  #if the player has visited this location
    def get_location_number(self):
        ''' Return the assigned location number '''
        return self.location_number

    def get_brief_description (self):
        '''Return str brief description of location.'''
        return self.brief_description

    def get_full_description (self):
        '''Return str long description of location.'''
        return self.long_description
    def get_item_list(self):
        '''Return a list of items that is in the location'''
        return self.items
    def change_visit_status(self):
        '''Change the status of self.visited upon player's visitation'''
        self.visited = not self.visited     
                
    def add_item(self,item):
        '''
        Add the item to the lcation's list, which stores the items that it has.
        :param item: Item Object
        :return:
        '''
        self.items.append(item)
    
    def drop_item(self,item):
        '''
        Drop the item from the lcation's list, which stores the items that it has.
        :param item: Item Object
        :return:
        '''        
        self.items.remove(item)
    
    def use_item(self,item):
        '''
        Drop the item from the lcation's list, and print a line that 
        indicates the item has being consumed.
        :param item: Item Object
        :return:
        '''         
        print('\n--> the '+item.get_name()+' just disappeared from the location\n')
        self.items.remove(item)

class Item:

    def __init__ (self, name, start, target, target_points, secret_item,if_pick_able):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, 
        integer target_points being the number of points player gets
        if item is deposited in target location, a screct_item if any 
        other item is hidden inside and if_pick_able tells if the item
        can pe picked up by the player.
        
        :param name: a string representing the name of the item
        :param start: a integer representing the origin location of the item
        :param target: a integer representing the location that player gets point
                       if item is deposited here
        :param target_points: the points that the player gets if item is deposited correcty
        :param secret_item: a item obecjt that is hidding inside of the item
        :param if_pick_able: indicated if the item is pickable

        '''
        if secret_item == 'None' :
            self.secret_item = 'None'
        else:
            self.secret_item = Item(secret_item, start, target, 5,'None',1)         

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points
        if if_pick_able == 1:
            self.pick_able = True
        else:
            self.pick_able = False
    def clear_target_points(self):
        '''Once the player gets the item's target point, this change the self.target_points to 0
        to avoid repeated obtention
        '''
        
        self.target_points = 0
    def get_pick_able(self):
        '''Return self.pick_able which indicated if the item could be picked up or not'''
        
        return self.pick_able
    def get_starting_location (self):
        '''Return int location where item is first found.'''
        
        return self.start

    def get_name(self):
        '''Return the str name of the item.'''
        
        return self.name

    def get_target_location (self):
        '''Return item's int target location where it should be deposited.'''
        
        return self.target

    def get_target_points (self):
        '''Return int points awarded for depositing the item in its target location.'''

        return self.target_points

class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        You may ADD parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''
        self.locations = []
        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        # self.locations ... You may choose how to store location and item data.
        self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...
        
    def add_location(self, location):
        '''the World Obejct has a list that stores Location objects, this adds a new lcation object
        to the list
        :param location: Location Object
        :return:
        '''
        self.locations.append(location)
    
    def load_map(self, filename):
        '''
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map" as a nested list of strings OR integers like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']] OR [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        :param filename: string that gives name of text file in which map data is located
        :return: return nested list of strings/integers representing map of game world as specified above
        '''
        file = open(filename)
        map = []
        for line in file:
            string_line = line.split()
            int_line = []
            for char in string_line:
                int_line.append(int(char))
            map.append(int_line)
        file.close()
        return map

    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename:
        :return:
        '''
        location_list = []
        file = open(filename)
        line = file.readline()
        while line :
            location_number = line.strip()
            location_number = int(location_number[9:])
            brief_description = file.readline().strip()
            long_description = file.readline()
            line = file.readline()
            while "END" not in line:
                long_description += line
                line = file.readline()
            LOCATION = Location(location_number, brief_description, long_description)
            self.add_location(LOCATION)
            line = file.readline()
            line = file.readline()
        file.close()
    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename:
        :return:
        '''

        file = open(filename)
        for line in file:
            item_description = line.strip().split(',')
            ITEM = Item(item_description[3], int(item_description[0]), int(item_description[1]), int(item_description[2]),item_description[4],int(item_description[5]))
            for location in self.locations:
                if location.get_location_number() == ITEM.get_starting_location():
                    location.add_item(ITEM)
        file.close()
    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''
        try:
            location_num = self.map[y][x]
            if location_num == -1 :
                return None
            else :
                for location in self.locations:
                    if int(location.get_location_number()) == int(location_num):
                        return location            
        except IndexError :
            return None
        
    def walk_able_location(self):
        '''Return a list that has all the locations that the player can move to'''
        
        walk_able = []
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] != -1:
                    walk_able.append([x,y])
        return walk_able
            



