## @file SeqADT.py
#  @author Ji Who Choi
#  @brief Provides the Seq ADT class for representing sequence
#  @date 1/21/2018

## @brief An ADT that represents a sequence
class SeqT:
  ## @brief SeqT constructor
  #  @details Initializes a SeqT object
    def __init__(self):
        self.elements = []

  ## @brief Gets the index and the value and insert it to the SeqT object at the
  #  index
  #  @details Assume that the index, i is a positive integer
  #  @param i an integer index where the value, v should be inserted
  #  @param v a value added to the SeqT object
  #  @exception ValueError Throws if supplied i is not within the range of 0 to
  #  the length of the sequence + 1
    def add(self, i, v):
        if (i < len(self.elements) + 1):
           self.elements.insert(i,v)
        else:
            raise ValueError("Index is not within the range")

  ## @brief Gets the index,i and delete the value at i
  #  @details Assume that the index is less than the length of the sequence
  #  @param i an integer index where the value should be deleted
    def rm(self, i):
        if (i < len(self.elements)):
            del self.elements[i]

  ## @brief Gets the index,i and the value, v and sets v at i
  #  @details Assume that the index, i is a positive integer
  #  @param i an integer index where the value, v should be set
  #  @param v a value set to the SeqT object
    def set(self, i, v):
        if (i < len(self.elements)):
            self.elements[i] = v

  ## @brief Gets the index,i and return the value at i
  #  @details Assume that the index, i is a positive integer
  #  @param i an integer index where the value, v should be returned
    def get(self,i):
        return self.elements[i]

  ## @brief Gets the size of a SeqT object
  #  @return the size of a SeqT object
    def size(self):
       return len(self.elements)

  ## @brief Gets the value, v and finds the index of the sequence such that
  #  s.get(i) <= v <= s.get(i+1)
  #  @details Assume that the value, v is in the range. If not in the range,
  #  the Indexerror will occur.
  #  @param v is a real number
  #  @return the index such that s.get(i) <= v <= s.get(i+1)
    def indexInSeq(self, v):
        for i in range(len(self.elements)):
            if (self.get(i) <= v <= self.get(i + 1)):
                return i
