import os

def command_help():
    '''
    Print out help for the system. That is...
    :return: a string indicating any errors, "" for no errors
    '''

    help = """
    Help for Calendar. The calendar commands are

    add DATE DETAILS               add the event DETAILS at the specified DATE
    show                           show all events in the claendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user input follows command:

    command: add 2015-10-12 dinner with jane
    added

    command: show
        2015-10-12:
            0: Eye doctor
            1: lunch with sid
            2: dinner with jane
        2015-10-29:
            0: Change oil in blue car
            1: Fix tree near front walkway
            2: Get salad stuff, leuttice, red peppers, green peppers
        2015-11-06:
            0: Sid's birthday

    command: delete 2015-10-29 2
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2015-12-21
    2016-01-02

    Event DETAILS consist of alphabetic characters, not tabs or newlines allowed.
    """
    print(help)
    return ""
 



def command_add(date, event_details, calendar):
    '''
    Add event_details to the list at calendar[date]
    Create date if it was not there

    :param date: A string date formatted as "YYYY-MM-DD"
    :param event_details: A string describing the event
    :param calendars: The calendars database
    :return: a string indicating any errors, "" for no errors

    >>> calendar = {}
    >>> command_add("2015-10-20", "Python class", calendar)
    ''
    >>> calendar == {'2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "CSC108 test 2", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2'], '2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2', 'go out with friends after test'], '2015-10-20': ['Python class']}
    True
    >>>

    '''

    for exist_date in calendar.keys():
        if date == exist_date:
            calendar[exist_date].append(event_details)
            return ''
    calendar[date]=[event_details]
    return ''

def command_show(calendar):
    '''
    Print the list of events for calendar sorted in increasing date order
    :param calendar: the database of events
    :return: a string indicating any errors, "" for no errors

    Example:
    >>> calendar = {}
    >>> command_add("2015-10-12", "Eye doctor", calendar)
    ''
    >>> command_add("2015-10-12", "lunch with sid", calendar)
    ''
    >>> command_add("2015-10-29", "Change oil in blue car", calendar)
    ''
    >>> command_add("2015-10-12", "dinner with Jane", calendar)
    ''
    >>> command_add("2015-10-29", "Fix tree near front walkway", calendar)
    ''
    >>> command_add("2015-10-29", "Get salad stuff", calendar)
    ''
    >>> command_add("2015-11-06", "Sid's birthday", calendar)
    ''
    >>> command_show(calendar)
        2015-10-12:
            0: Eye doctor
            1: lunch with sid
            2: dinner with Jane
        2015-10-29:
            0: Change oil in blue car
            1: Fix tree near front walkway
            2: Get salad stuff
        2015-11-06:
            0: Sid's birthday
    ''
    '''
    ordered_list = []
    for key in calendar:
        if len(ordered_list) == 0:
            ordered_list.append(key)
        else:
            key_year = int(key[0]+key[1]+key[2]+key[3])
            key_month = int(key[5]+key[6])
            key_day = int(key[8]+key[9])
            key_total = (365 * key_year) + (31 * key_month) + key_day
            
            for date in ordered_list:
                date_year = int(date[0]+date[1]+date[2]+date[3])
                date_monty = int(date[5]+date[6])
                date_day = int(date[8]+date[9])
                date_total = (365 * date_year) + (31 * date_monty) + date_day
                if key_total <= date_total:
                    ordered_list.insert(ordered_list.index(date), key)
                    break
                elif ordered_list.index(date) == len(ordered_list)-1 and key_total > date_total:
                    ordered_list.append(key)
                    break
    for i in range(len(ordered_list)):
        print(ordered_list[i]+":")
        for key in calendar:
            if key == ordered_list[i]:
                for j in range(len(calendar[key])):
                    print("    "+ str(j) + ": " + calendar[key][j])
    return ''

def command_delete(date, entry_number, calendar):
    '''
    Delete the entry at calendar[date][entry_number]
    If calendar[date] is empty, remove this date from the calendar.

    :param date: A string date formatted as "YYYY-MM-DD"
    :param entry_number: An integer indicating the entry in calendar[date] to delete
    :param calendar: The calendars database
    :return: a string indicating any errors, "" for no errors

    Example:

    >>> calendar = {}
    >>> command_add("2015-10-20", "Python class", calendar)
    ''
    >>> calendar == {'2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "CSC108 test 2", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2'], '2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2', 'go out with friends after test'], '2015-10-20': ['Python class']}
    True
    >>> command_show(calendar)
        2015-10-20:
            0: Python class
        2015-11-01:
            0: CSC108 test 2
            1: go out with friends after test
    ''

    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2015-10-20", 3, calendar)
    'there is no entry 3 on date 2015-10-20 in the calendar'
    >>> command_delete("2015-10-20", 0, calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2', 'go out with friends after test']}
    True
    >>> command_delete("2015-11-01", 0, calendar)
    ''
    >>> calendar == {'2015-11-01': ['go out with friends after test']}
    True
    >>> command_delete("2015-11-01", 0, calendar)
    ''
    >>> calendar == {}
    True

    '''
    for exist_date in calendar:
        if date == exist_date :
            if entry_number not in range(len(calendar[date])):
                return('there is no entry '+str(entry_number)+' on date '+date+' in the calendar')
            else :
                calendar[exist_date].pop(entry_number)
                if len(calendar[date])==0:
                    calendar.pop(date, None)
                return '' 
    return(date + ' is not a date in the calendar') 
# ---------------------------------------------------------------------------------------------------------------------
# Functions dealing with calendar persistence
# ---------------------------------------------------------------------------------------------------------------------

'''
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

'''

def save_calendar(calendar):
    '''
    Save calendar to 'calendar.txt', overwriting it if it already exists.

    The format of calendar.txt is the following:

    date_1:description_1\tdescription_2\t...\tdescription_n\n
    date_2:description_1\tdescription_2\t...\tdescription_n\n
    date_3:description_1\tdescription_2\t...\tdescription_n\n
    date_4:description_1\tdescription_2\t...\tdescription_n\n
    date_5:description_1\tdescription_2\t...\tdescription_n\n

    Example: The following calendar...

        2015-10-20:
            0: Python class
        2015-11-01:
            0: CSC108 test 2
            1: go out with friends after test

    appears in calendar.txt as ...

    2015-10-20:Python class
    2015-11-01:CSC108 test 2    go out with friends after test

                            ^^^^ This is a \t, (tab) character.


    :param calendar:
    :return: True/False, depending on whether the calendar was saved.
    '''
    ordered_list = []
    for key in calendar:
        if len(ordered_list) == 0:
            ordered_list.append(key)
        else:
            key_year = int(key[0]+key[1]+key[2]+key[3])
            key_month = int(key[5]+key[6])
            key_day = int(key[8]+key[9])
            key_total = (365 * key_year) + (31 * key_month) + key_day
            
            for date in ordered_list:
                date_year = int(date[0]+date[1]+date[2]+date[3])
                date_monty = int(date[5]+date[6])
                date_day = int(date[8]+date[9])
                date_total = (365 * date_year) + (31 * date_monty) + date_day
                if key_total <= date_total:
                    ordered_list.insert(ordered_list.index(date), key)
                    break
                elif ordered_list.index(date) == len(ordered_list)-1 and key_total > date_total:
                    ordered_list.append(key)
                    break
    file=open('calendar.txt','w+')
    for key in ordered_list:
        detail = key + ':'
        for i in range(len(calendar[key])):
            detail+=calendar[key][i]+"\t"
        file.write(detail[:-1]+'\n')
    file.close()
    return True

def load_calendar():
    '''
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    :return: calendar, or False, if calendar could not be loaded from disk.

    '''
    calendar= {}
    if os.path.exists('calendar.txt'):
        fo = open('calendar.txt','r')
        text_line = fo.readline()
        while text_line:
            tokens = text_line.split(':')
            if len(tokens) == 2 and len(tokens[0])==10 :
                details = tokens[1][:-1].split('\t')
                calendar[tokens[0]]=details
            else:
                return False
            text_line = fo.readline()
    else:
        fo=open('calendar.txt','w+')
    fo.close()
    return calendar
# ---------------------------------------------------------------------------------------------------------------------
# Functions dealing with parsing commands
# ---------------------------------------------------------------------------------------------------------------------

def is_command(command):
    '''
    Return whether command is indeed a command, that is, one of
    "add", "delete", "quit", "help", "show"
    :param command: string
    :return: True if command is one of ["add", "delete", "quit", "help", "show"], false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''
    
    for item in ["add", "delete", "quit", "help", "show"]:
        if item == command:
            return True
    return False

def is_natural_number(str):
    '''
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    :param str: string
    :return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    for character in str:
        if character not in "0123456789":
            return False
    return True

def is_calendar_date(date):
    '''
    Return whether date looks like a calendar date
    :param date: a string
    :return: True, if date has the form "YYYY-MM-DD" and False otherwise

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    if len(date)==10:
        year = date[0]+date[1]+date[2]+date[3]
        month = date[5]+date[6]
        day = date[8]+date[9]
        if year.isdigit() and month.isdigit() and day.isdigit():
            if int(month)<=12 and int(day)<=31:
                if date[4]=='-' and date[7]=='-':
                    return True
    return False
    

def parse_command(line):
    '''
    Parse command and arguments from the line. Return a list [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid. Return ["help"] otherwise.
    The valid commands are

    1) add DATE DETAILS
    2) show
    3) delete DATE NUMBER
    4) quit
    5) help

    :param line: a string command
    :return: A list consiting of [command, arg1, arg2, ...]. Return ["error", ERROR_DETAILS], if
    line can not be parsed.

    Example:
    >>> parse_command("add 2015-10-21 budget meeting")
    ['add', '2015-10-21', 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22 Tims with Sally.")
    ['add', '2015-10-22', 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22 1")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event index']
    >>> parse_command("delete 2015-10-22 314")
    ['delete', '2015-10-22', '314']
    >>> parse_command("quit")
    ['quit']

    '''

    tokens = line.split(' ',2)
    if is_command(tokens[0]):
        if tokens[0] == 'add':
            if len(tokens) != 3:
                return  ['error', 'add DATE DETAILS']
            elif not is_calendar_date(tokens[1]):
                return ['error', 'not a valid calendar date']
            else:
                return tokens
        if tokens[0] == 'delete':
            if len(tokens) != 3:
                return  ['error', 'delete DATE NUMBER']
            elif not is_calendar_date(tokens[1]):
                return ['error', 'not a valid calendar date']
            elif not is_natural_number(tokens[2]):
                return ['error', 'not a valid event index']
            else:
                return tokens 
        if tokens[0]=='show':
            if len(tokens) != 1:
                return   ['error', 'show']
            else:
                return tokens
        if tokens[0]=='quit':
            if len(tokens) != 1:
                return   ['error', 'quit']
            else:
                return tokens                                        
    else:
        return ['help']
# ---------------------------------------------------------------------------------------------------------------------
# Functions dealing with the user. This is the calendar application.
# ---------------------------------------------------------------------------------------------------------------------

def user_interface():
    '''
    Load calendar.txt and then interact with the user. The user interface
    operates as follows, the text after command: is the command entered by the user.

    calendar loaded
    command: add 2015-10-21 budget meeting
    added
    command: add 2015-10-22 go to the gym
    added
    command: add 2015-10-23 go to the gym
    added
    command: add 2015-11-01 Make sure to submit csc108 assignment 2
    added
    command: add 2015-12-02 Make sure to submit csc108 assignment 3
    added
    command: add 2015-11-06 Term test 2
    added
    command: add 2015-10-29 Get salad stuff, leuttice, red peppers, green peppers
    added
    command: add 2015-11-06 Sid's birthday
    added
    command: show
        2015-10-21:
            0: budget meeting
        2015-10-22:
            0: go to the gym
        2015-10-23:
            0: go to the gym
        2015-10-29:
            0: Get salad stuff, leuttice, red peppers, green peppers
        2015-11-01:
            0: Make sure to submit csc108 assignment 2
        2015-11-06:
            0: Term test 2
            1: Sid's birthday
        2015-12-02:
            0: Make sure to submit csc108 assignment 3
    command: delete 2015-10-29 0
    deleted
    command: delete 2015-12-03 0
    2015-12-03 is not a date in the calendar
    command: delete 2015-12-02 0
    deleted
    command: show
        2015-10-21:
            0: budget meeting
        2015-10-22:
            0: go to the gym
        2015-10-23:
            0: go to the gym
        2015-11-01:
            0: Make sure to submit csc108 assignment 2
        2015-11-06:
            0: Term test 2
            1: Sid's birthday
    command: quit
    calendar saved

    :return: None
    '''
    
    calendar = load_calendar()
    if calendar == False :
        print('calendar loading failed ')
    else :
        print('Calender loaded')
        user_input=input('command:')
        text=parse_command(user_input)
        while text :
            if 'add' in text:
                command_add(text[1], text[2], calendar)
                print('added')
            if 'delete' in text:
                message =  (command_delete(text[1], int(text[2]), calendar))
                if message == '':
                    print('deleted')
                else :
                    print(message)
            if 'help' in text:
                command_help()
            if 'error' in text:
                print('something is wrong: '+text[1])
            if 'show' in text and len(text) == 1:
                    command_show(calendar)
            if 'quit' in text and len(text) == 1:
                text=False
            else:
                user_input=input("command: ")
                text=parse_command(user_input)
        save_calendar(calendar)
        print('calender saved')

if __name__ == "__main__":
    user_interface()