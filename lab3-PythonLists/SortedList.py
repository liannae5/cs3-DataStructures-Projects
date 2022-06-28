'''
CS 2302
Lab 3: Lists
SortedList.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 2/28/2022
'''
import sys
sys.setrecursionlimit(10**6) #increases recursion limit to test larger data sets
##################################
#            PART 1              #
##################################

class SortedList:
    # Constructor
    def __init__(self):
        self.data = list()
        self.len = 0 #added to keep length of list


    # getitem method
    # This method is executed when you use []
    # to get data from the list
    # i.e. x = mySortedList[3]
    def __getitem__(self, idx):
        if idx>=self.len or idx < 0:
            print("Invalid index")
            return
        return self.data[idx]  #returns element at given index

    # len method
    # Returns the length of the Sorted List
    def __len__(self):
        return self.len #returns length of list
        
    # add method
    # Adds "value" to the list, in the right position
    def add(self, value):

        #if list is empty, adds first value
        if(len(self) == 0):
            self.data += [value] # adds value to list
            self.len += 1 #increases length

        #if value is less than the min value, the value is added to the end of the list
        elif value <= self.min():
            self.data += [value] #adds value to end of list
            self.len +=1 #increases list length

        #if value is greater than max value, the value is added to beginning
        elif value >= self.max():
            self.data = [value] + self.data[0:] #adds value to beginning
            self.len +=1 #increases list length

        # otherwise the proper index to insert value in determined
        else:
            index = self.posSearch(value, self.len) #stores index to split list at
            rightSide = self.data[index+1:] #stores right side of the list
            leftSide = self.data[:index+1] + [value] #stores left side of list updated with new value
            self.data = leftSide + rightSide #concatenates updated sides of the list
            self.len += 1 #increases list length

    #Searches for index where to split length and insert a given value
    def posSearch(self, value, length):

        index = length // 2 #gives middle index of list

        #Base cases
        # if index is 0, returns 0
        if index == 0:
            return index

        #if value <= element at index we have found the closest element to value
        elif value <= self.data[index]:
            return index #returns index closest to value

        #otherwise, the function called on halved list (first half)
        return self.posSearch(value,index)


    # indexof method
    #performs binary search on the list to find the value
    def indexof(self, value):
        if self.len == 0:
            print("List is empty, cannot complete search")
            return

        start = 0 #sets start index to beginning of list
        end = self.len-1 #sets end index to end of list

        while start <= end:
            middle = (start+end) // 2 #gets middle index
            if self.data[middle] > value:
                start = middle + 1 #sets start to middle + 1 if middle element > value
            elif self.data[middle] < value:
                end = middle - 1 #sets end to middle - 1 if middle element < value
            else:
                return middle #returns middle index if it equals the value
        return -1 #returns -1 if value not found

    # clear method
    # Removes all elements from the list
    def clear(self):
        self.data = list() #sets list to an empty list
        self.len = 0 #resets list length to zero

    # min method
    # Returns the smallest element in the list
    def min(self):
        #if list is empty it informs the user and returns None
        if self.len < 1:
            print("List is empty")
            return
        #otherwise returns the last value in the list
        return self.data[self.len-1]

    # max method
    # Returns the smallest element in the list
    def max(self):

        #informs user that list is empty and returns None
        if self.len < 1:
            print("List is empty")
            return

        #otherwise returns first item in list
        return self.data[0]

    # popmin method
    # Returns the smallest element in the list,
    # and remove that element from the list
    def popmin(self):

        #informs user that list is empty and returns Nonoe
        if self.len < 1:
            print("List is empty")
            return

        #Otherwise pops min value
        val = self.min() #holds min value
        self.len -=1 #decreases list's length
        self.data = self.data[:self.len] #removes min value from list
        return val #returns the value that was removed

    # all unique method
    # Returns True if all the elements in the list are unique
    # Returns False if there are repeated elements
    def allunique(self):

        #iterates through entire list
        for i in range(self.len-1):
            if(self.data[i] == self.data[i+1]): #compares 2 consecutive elements in list
                return False #returns False if 2 elements are equal
        return True #otherwise returns true

    # Other useful methods
    # (You do not need to update these)
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __iter__(self):
        for n in self.data:
            yield n
