import linked_list_ADT as N


def split_chain(node_chain):
    """
    Purpose:
        Splits the given node chain in half, returning the second half.
        If the given chain has an odd length, the extra node is part of
        the second half of the chain.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Post-conditions:
        the original node chain is cut in half!
    Return:
        :return: A tuple (nc1, nc2) where nc1 and nc2 are node-chains
         each containing about half of the nodes in node-chain
    """

    # Returning the node chain if it is empty.
    if node_chain is None:
        return None, None
    elif node_chain.get_next() is None:
        return None, node_chain
    else:
        # the chain is 2 nodes long or longer
        # technique: Two walkers, one hops twice as fast
        # when the fast walker gets to the end,
        # the slow one is half-way down
        walker = node_chain
        half_speed = node_chain
        prev = None
        while walker is not None:
            walker = walker.get_next()
            # hop a second time, but carefully!
            if walker is not None:
                walker = walker.get_next()
                prev = half_speed
                half_speed = half_speed.get_next()

        # split the chain right in front of the slow walker
        prev.set_next(None)

        return node_chain, half_speed


def merge(nc1, nc2):
    """
    Purpose:
        Combine the two sorted node-chains nc1 and nc2 into a single
        sorted node-chain.
    Pre-conditions:
        :param nc1: a node-chain, possibly empty,
        containing values sorted in ascending order.
        :param nc2: a node-chain, possibly empty,
        containing values sorted in ascending order.
    Post-condition:
        None
    Return:
        :return: a sorted node chain (nc) that contains the
        values from nc1 and nc2. If both node-chains are
        empty an empty node-chain will be returned.
    """
    # first, check for empty node-chains
    if nc1 is None:
        # could copy the other node-chain, but why bother?
        return nc2
    elif nc2 is None:
        return nc1
    # neither is None, so look at the data value to see which goes first
    elif nc1.get_data() < nc2.get_data():
        result = N.node(nc1.get_data())
        nc1 = nc1.get_next()
    else:
        result = N.node(nc2.get_data())
        nc2 = nc2.get_next()

    # result refers to the first node in the merged node chain
    # need a walker to make the appropriate connections
    rwalker = result

    while nc1 is not None and nc2 is not None:
        # look for the smaller of the two data values
        # advance only the one with the smaller value
        if nc1.get_data() < nc2.get_data():
            new_data = nc1.get_data()
            nc1 = nc1.get_next()
        else:
            new_data = nc2.get_data()
            nc2 = nc2.get_next()

        # create a new node, and advance the walker
        rwalker.set_next(N.node(new_data))
        rwalker = rwalker.get_next()

    # here, we've reached the end of one or both of the original chains
    if nc1 is None:
        # could copy the other node-chain, but why bother?
        rwalker.set_next(nc2)
    else:
        # could copy the other node-chain, but why bother?
        rwalker.set_next(nc1)

    # finally, return the result
    return result


def merge_sort(node_chain):
    """
    Purpose:
        Sorts the given node chain in ascending order using the
        merge sort algorithm.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty,
        containing only numbers
    Post-condition:
        the original node_chain may be modified and will likely
        not contain all the original elements
    Return
        :return: a new node-chain with the same values as the
        original node chain sorted in ascending order.
        Ex: 45->1->21->5. Becomes 1->5->21->45
    """

    # Base case.
    if node_chain is None or node_chain.get_next() is None:
        return node_chain

    # Divide.
    nc1, nc2 = split_chain(node_chain)

    # Recursively sort.
    nc1 = merge_sort(nc1)
    nc2 = merge_sort(nc2)

    # Combine.
    node_chain = merge(nc1, nc2)

    # Return the sorted chain.
    return node_chain
