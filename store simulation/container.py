class Container:
    """A container that holds objects.

    This is an abstract class. Only child classes should be instantiated.
    """

    def add(self, item):
        """Add <item> to this Container.

        @type self: Container
        @type item: object
        @rtype: None
        """
        raise NotImplementedError

    def remove(self):
        """Remove and return a single item from this Container.

        @type self: Container
        @rtype: object
        """
        raise NotImplementedError

    def is_empty(self):
        """Return True iff this Container is empty.

        @type self: Container
        @rtype: bool
        """
        raise NotImplementedError


class PriorityQueue(Container):
    """A queue of items that operates in priority order.

    Items are removed from the queue according to priority; the item with the
    highest priority is removed first. Ties are resolved in FIFO order,
    meaning the item which was inserted *earlier* is the first one to be
    removed.

    """


    def __init__(self):
        """Initialize an empty PriorityQueue.

        @type self: PriorityQueue
        @rtype: None
        """
        self._items = []

    def remove(self):
        """Remove and return the next item from this PriorityQueue.

        Precondition: <self> should not be empty.

        @type self: PriorityQueue
        @rtype: object

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('arju')
        >>> pq.add('mona')
        >>> pq.add('hat')
        >>> pq.remove()
        'arju'
        >>> pq.remove()
        'fred'
        >>> pq.remove()
        'hat'
        >>> pq.remove()
        'mona'
        """
        return self._items.pop(0)

    def is_empty(self):
        """
        Return true iff this PriorityQueue is empty.

        @type self: PriorityQueue
        @rtype: bool

        >>> pq = PriorityQueue()
        >>> pq.is_empty()
        True
        >>> pq.add('fred')
        >>> pq.is_empty()
        False
        """
        return len(self._items) == 0

    def add(self, item):
        """Add <item> to this PriorityQueue.

        @type self: PriorityQueue
        @type item: object
        @rtype: None

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('arju')
        >>> pq.add('mona')
        >>> pq.add('hat')
        >>> pq._items
        ['arju', 'fred', 'hat', 'mona']
        """
        if self.is_empty():
            
            self._items.append(item)
        else :
            for event in self._items:
                if item <= event:
                    self._items.insert(self._items.index(event),item) # this will pust insert the event at the required postion in the list
                    return
            self._items.append(item)
            
