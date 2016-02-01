from game_data import World, Item, Location
from player import Player


def go_action(world, player, choice):
    '''
    if the key word 'go' is in the choice, this function first checks if the command
    is a valid command. If it is valid , the function changes the player's cordinate
    on the world according to the choice, otherwise it will a warn the player a 
    invalid command is being entered.
    :param world: World Object
    :param player: Player Object
    :param choice: a string representing player's command
    :return Ture: if a valid go command is being processed
    :retrun False: if a invalid command is being entered
    '''
    y = player.y
    x = player.x
    if choice == "go south":
        if [x,y+1] in world.walk_able_location():
            player.y += 1
            player.steps -= 1
            return True
        else:
            print('\n--> can not go south, there is no room there\n')
    elif choice == "go north" :
        if [x,y-1] in world.walk_able_location():
            player.y -= 1
            player.steps -= 1
            return True
        else:
            print('\n--> can not go north, there is no room there\n')
    elif choice == "go east" :
        if [x+1,y] in world.walk_able_location():
            player.x += 1
            player.steps -= 1
            return True
        else:
            print('\n--> can not go east, there is no room there\n')        
    elif choice == "go west" :
        if [x-1,y] in world.walk_able_location():
            player.x -= 1
            player.steps -= 1
            return True
        else:
            print('\n--> can not go west, there is no room there\n')   
    else :
        print('\n--> invalid go command\n')
    return False
def pick_action(player,location,choice):
    '''
    if the key word 'pick' is in the choice, this function first checks if the command
    is a valid command(check if items exist). If it is valid , the function adds the item to the player's
    inventory and remove the item from the location,
    otherwise it will a warn the player a invalid command is being entered
    :param player: Player Objectbrief
    :param location: Location Object
    :param choice: a string representing player's command
    '''    
    command = choice.split(' ',1)
    if command[0] == 'pick' and len(command)==2 :
        for item in location.get_item_list():
            if item.get_name() == command[1]:
                if item.get_pick_able():
                    player.add_item(item)
                    location.drop_item(item)
                else:
                    print('\n--> You can not pick up this item\n')
                return 
    print('\n--> invalid pick command\n')


def drop_action(player,location,choice):
    '''
    if the key word 'drop' is in the choice, this function first checks if the command
    is a valid command(check if items exist). If it is valid , the function drops the item from the player's
    inventory and adds the item to the location,
    otherwise it will a warn the player a invalid command is being entered
    :param player: Player Object
    :param location: Location Object
    :param choice: a string representing player's command
    '''     
    command = choice.split(' ',1)
    if command[0] == 'drop' and len(command)==2:

        for item in player.get_inventory():
            if item.get_name() == command[1]:

                location.add_item(item)
                if location.get_location_number() == item.get_target_location():
                    player.add_score(item.get_target_points())
                    item.clear_target_points()
                    player.add_required_item()
                player.drop_item(item)
                return 
    print('\n--> invalid drop command\n')                
                
def use_action(player,location, choice):
    '''
    if the key word 'use/on' is in the choice, this function first checks if the command
    is a valid command(check if items exist). If it is valid , the function then checks if the two item that
    the combination of the items that the player chooses will produce anything new,
    otherwise it will a warn the player a invalid command is being entered
    :param player: Player Object
    :param location: Location Object
    :param choice: a string representing player's command
    '''     
    split_index = choice.index('on')
    use_command = choice[:split_index-1].split(' ',1)
    on_command = choice[split_index:].split(' ',1)
    all_items = player.get_inventory() + location.get_item_list()
    for use_item in player.get_inventory():
        if use_item.get_name() == use_command[1]:
            for on_item in all_items:
                if on_item.get_name() == on_command[1]:
                    if 'metal' in on_item.get_name() and use_item.get_name()=='magnet':
                        ITEM =Item('detector', -1, -1, 0, 'None',1)
                        player.add_item(ITEM)
                        player.add_score(5)
                        player.use_item(use_item)
                        for item in location.get_item_list():
                            if on_item.get_name() == item.get_name():
                                    location.use_item(on_item)
                                    return 
                        player.use_item(on_item)
                        return 

                    elif 'cash' == use_item.get_name() and 'vendor machine' == on_item.get_name():
                        player.add_item(on_item.secret_item)
                        player.add_score(5)
                        print('\n--> You found '+on_item.secret_item.get_name())
                        on_item.secret_item ='None'
                        player.use_item(use_item)
                        return 

                    elif use_item.get_name() == 'detector':
                        if on_item.secret_item !='None':
                            if 'key' in on_item.secret_item.get_name():
                                player.add_item(on_item.secret_item)
                                player.add_score(5)
                                print('\n--> You found '+on_item.secret_item.get_name())
                                on_item.secret_item ='None'
                                player.use_item(use_item)
                                return 

                    elif 'key' in use_item.get_name() and 'treasure box' in on_item.get_name():
                        color = on_command[1].split()[0]
                        if use_item.get_name() == color + ' key':
                            print ('\n-->You found :' + on_item.secret_item.get_name())
                            player.add_item(on_item.secret_item)
                            player.add_score(5)
                            player.use_item(use_item)
                            on_item.secret_item = 'None'
                            return 
                    print('\n--> Nothing happended!\n')
                    return 
    print('\n--> invalid use/on command')
            
        

def examine_action(player,location,choice):
    '''
    if the key word 'examine' is in the choice, this function first checks if the command
    is a valid command(check if items exist). If it is valid , the function then checks if the two item that
    the there is anything hidden behind the item and adds it to the player's inventory,
    otherwise it will a warn the player a invalid command is being entered
    :param player: Player Object
    :param location: Location Object
    :param choice: a string representing player's command
    '''     
    command = choice.split(' ',1)
    all_items = location.get_item_list() + player.get_inventory()
    for item in all_items:
        if item.get_name() == command[1]:
            if item.secret_item == 'None':
                print('\n-->There is nothing special\n')
                return 
            elif 'treasure box' in command[1]:
                print('\n-->You do not have the key to open this\n')
                return 
            elif 'key' in item.secret_item.get_name() or item.get_name()=='vendor machine':
                print('\n-->There seems to be something\n')
                return 
            else:
                print ('\n-->You found :' + item.secret_item.get_name())
                player.add_item(item.secret_item)
                item.secret_item = 'None'
                return 
    print('\n --> invalid examine command\n')
    
def inventory_action(player,location):
    '''print all the items that are in the player's inventory and
    the items placed at the location
    :param player: Player Object
    :param location: Location Object
    '''
    inventory_num = 1
    print('\n************* INVENTORY ***************')
    print('Items in your bag:(drop items)')
    if len(player.get_inventory()) == 0:
        print('Nothing')
    else:
        for item in player.get_inventory():
            print(str(inventory_num)+'. '+item.get_name())
            inventory_num +=1
    
    inventory_num = 1
    print('\nItems at the location:(pick items)')
    if len(location.get_item_list()) == 0:
        print('Nothing')
    else:    
        for item in location.get_item_list():
            print(str(inventory_num)+'. '+item.get_name())
            inventory_num +=1    
    print('********** END OF INVENTORY ************\n')
def available_actions(world, player, location):
    '''
    -- Suggested Method (You may remove/modify/rename this as you like) --
    Return list of the available actions in this location.
    The list of actions should depend on the items available in the location
    and the x,y position of this location on the world map.
    :param world: World Object
    :param player: Player Object
    :param location: Location Object    
    '''
    available_action = []
    x = player.x
    y = player.y    
    if [x+1,y] in world.walk_able_location():
        available_action.append('go east')
    if [x-1,y] in world.walk_able_location():
        available_action.append('go west')
    if [x,y-1] in world.walk_able_location():
        available_action.append('go north')    
    if [x,y+1] in world.walk_able_location():
        available_action.append('go south')
    
    return available_action
def print_location_information(world, player):
    '''print the remaing steps that the player has,the introduction of the
    current location and return a location object where the player is standing
    :param world: World Object
    :param player: Player Object
    :param location: Location Object
    :return location: the location of the player
    '''
    location = world.get_location(player.x, player.y)
    print('\nSTEPS: '+str(player.steps)+'   *************************************************************************'  )
    if location.visited :
        print(location.get_brief_description())
    else:
        print(location.get_full_description())
        location.change_visit_status()  
    return location  

def print_option(world,player,location):
    ''' print the possible moves that the player can go from the current location
    :param world: World Object
    :param player: Player Object
    :param location: Location Object
    '''
    print('<---------------------------->')
    option_num = 1
    print('    possible steps:')
    for action in available_actions(world,player,location): 
        if 'go' in action:
            print('     --> '+str(option_num)+'. '+action)
            option_num +=1       
    print('<---------------------------->')
    print("What to do? ")    

def game_engine(world,player,location):
    '''
    phrase the user's command and deterime what action should be
    called
    :param world: World Object
    :param player: Player Object
    :param location: Location Object
    '''   
    menu = ["look", "inventory", "score", "quit", "pick item","drop item","examine item","use item on item","go direction"]
    while not player.victory  :
        choice = input("Enter action: \n").strip()
        if choice == 'menu':
            print(menu)
        elif 'go' in choice:
            if go_action(world, player, choice) :
                location = print_location_information(world,player)
                print_option(world,player,location)
        elif choice == 'look':
            print(location.get_full_description())
        elif choice == 'inventory' :
            inventory_action(player, location)           
        elif 'pick' in choice:
            pick_action(player, location, choice)
        elif 'use' and 'on' in choice:
            use_action(player, location, choice)
        elif 'drop' in choice:
            drop_action(player, location, choice)
        elif 'examine' in choice:
            examine_action(player, location, choice)
        elif choice == 'quit':
            player.victory = True
        elif choice == 'score':
            print('--> YOUR CURRENT SCORE: '+str(player.score)+'\n')
        else :
            print('--> invalid command\n')
        player.check_victory()    
if __name__ == "__main__":
    file = open('introduction.txt')
    for line in file:
        print(line.strip())
    file.close()
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(1,1,50) # set starting location of player; you may change the x, y coordinates here as appropriate
    location = print_location_information(WORLD,PLAYER)   
    print_option(WORLD,PLAYER,location)     
    game_engine(WORLD, PLAYER, location)
