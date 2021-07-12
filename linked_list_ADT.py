class node(object):

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the node
            next:  Another node (or None, by default)
        """
        self.__data = data
        self.__next = next


    def get_data(self):
        """
        Retrieve the contents of the data field.
        Return
            the data value stored previously in the node
        """
        return self.__data


    def get_next(self):
        """
        Retrieve the contents of the next field.
        Return
            the value stored previously in the next field
        """
        return self.__next


    def set_data(self, val):
        """
        Set the contents of the data field to val.
        Pre-conditions:
            val:  a data value to be stored
        Post-conditions:
            stores a new data value, replacing  existing value
        Return
            none
        """
        self.__data = val


    def set_next(self, val):
        """
        Set the contents of the next field to val.
        Pre-conditions:
            val:  a node, or the value None
        Post-conditions:
            stores a new next value, replacing existing value
        Return
            none
        """
        self.__next = val

