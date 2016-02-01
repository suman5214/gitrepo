from container import PriorityQueue
from store import GroceryStore
from event import Event, create_event_list


class GroceryStoreSimulation:
    """A Grocery Store simulation.
    This is the class which is responsible for setting up and running a
    simulation.
    """

    def __init__(self, store_file):
        """Initialize a GroceryStoreSimulation from a file.

        @type store_file: str
            A file containing the configuration of the grocery store.
        @rtype: None
        """
        self._events = PriorityQueue()
        self._store = GroceryStore(store_file)

    def run(self, event_file):
        """Run the simulation on the events stored in <event_file>.

        Return a dictionary containing statistics of the simulation,
        according to the specifications in the assignment handout.

        @type self: GroceryStoreSimulation
        @type event_file: str
            A filename referring to a raw list of events.
            Precondition: the event file is a valid list of events.
        @rtype: dict[str, object]
        """
        # Initialize statistics
        stats = {
            'num_customers': 0,
            'total_time': 0,
            'max_wait': -1
        }

        initial_events = create_event_list(event_file)
        for item in initial_events:
            self._events.add(item)
     
        while self._events.is_empty() == False:
            processEvent= self._events.remove()
            
            #change the stats acrroding to the eventbeing popped out from list
            if(processEvent.status=="Finish"):                                
                waitTime=processEvent.getWaitTime()                           
                if waitTime > stats['max_wait']:
                    stats['max_wait'] = waitTime
            if(processEvent.status=="Begin"):
                stats['num_customers']+=1
            if(self._events.is_empty() and processEvent.status=="Finish"):
                stats['total_time']=processEvent.timestamp
            
            newEvents=processEvent.do(self._store)
            if(newEvents!=None):
                for event in newEvents:
                    self._events.add(event)
          


        return stats

if __name__ == '__main__':
    sim = GroceryStoreSimulation('config.json')
    final_stats = sim.run('events.txt')
    print(final_stats)
