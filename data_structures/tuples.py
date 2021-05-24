def tupleToList(tupleIn):
    """
    Transforms an uneditable tuple of tuples into an editable list of lists.
    """
    # TODO: Make recursive


    newList = []

    for element in tupleIn:
        if (type(element) == tuple):
            newElement = list(element)
        else:
            newElement = element

        newList.append(newElement)

    return list(newList)



def listToTuple(listIn):
    """
    Transforms an editable list of lists into an uneditable lists of lists.
    """
    # TODO: Make recursive

    newTuple = []

    for element in listIn:
        if (type(element) == list):
            newElement = tuple(element)
        else:
            newElement = element

        newTuple.append(newElement)

    return tuple(newTuple)

