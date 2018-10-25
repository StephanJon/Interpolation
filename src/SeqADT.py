## @file SeqADT.py
#  @author Stephanus Jonatan
#  @date January 21, 2018

## @brief SeqT is a class that creates an empty list/sequence.
#  @details SeqT has a constructor, and a few accessors and mutators.
class SeqT(object):
    ## @brief Initializes an empty Sequence.
    def __init__(self):
        self.Seq = []

    ## @brief add(i, v) inserts an element into a list (mutator).
    #  @details It either appends or inserts at a specific position in the list.
    #  @param i is the index of the list to which the user wants to add a value to.
    #  @param v is the value the user wants to add to the list.
    #  @return An updated list is returned.
    def add(self, i, v):
        # Checks if sequence is empty
        if self.Seq == 0:
            return self.Seq.append(v)
        # Checks if index i exists
        elif i >= len(self.Seq):
            return self.Seq.append(v)
        else:
            return self.Seq.insert(i, v)

    ## @brief Removes an element from a list (mutator).
    #  @param i is the index of the element that the user wants to remove.
    #  @return An updated list is returned.
    def rm(self, i):
        return self.Seq.pop(i)

    ## @brief Modifies an element in a list (mutator).
    #  @param i is the index of the element that the user wants to modify.
    #  @param v is the value that the user wishes to replace the old value with.
    #  @return An updated list is returned.
    def set(self, i, v):
        # Checks if index i exists
        if i >= len(self.Seq):
            # prints error message when index doesn't exists
            print("Index does not exists. Nothing to modify")
        else:
            self.Seq[i] = v
            return self.Seq

    ## @brief Accesses an index of a list (accessor).
    #  @param i is the index that is being accessed.
    #  @return Returns the value at the index i.
    def get(self, i):
        # Checks if index i exists
        if i >= len(self.Seq):
            # prints error message when index doesn't exists
            print("Index does not exists")
        else:
            return self.Seq[i]

    ## @brief Checks for the size of a list.
    #  @returns the the size of a list.
    def size(self):
        return len(self.Seq)

    ## @brief Finds the approximate position for a value in a sorted list (accessor).
    #  @details The value does not have to exist in the list, but has to be >= than the first element and <= the last element of the list.
    #  @param v is the value being searched for in the list.
    #  @return Returns the approximate index of the value v.
    def indexInSeq(self, v):
        for i in range(0, self.size()):
            if (self.get(i) <= v) and (v <= self.get(i + 1)):
                return i
