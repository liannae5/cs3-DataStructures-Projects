'''
CS 2302
Lab 3: Lists
CircularShift.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 2/28/2022
'''
import sys
sys.setrecursionlimit(10**6) #increases recursion limit to test larger data sets
##################################
#            PART 2              #
##################################

# Circular Shift, Solution 1
def circularshift_1(lst, k):

    if len(lst) <= 1 or k == 0 or k == len(lst): #For these cases, the original list can be returned
        return lst

    #If k is positive a shift to the right is performed
    if k > 0:

        # if k > lst length, we only need to perform a switch of the remainder
        if k > len(lst):
            k = k%len(lst) #finds the remainder of k divided by lst length

            #if k = 0 the original lst is returned
            if k == 0:
                return lst

        #when k=1, only the last element needs to be shift to the beggining
        if k == 1:
            newLeft = [lst[len(lst)-1]] #stores first element of shifted list
            newRight = lst[:len(lst)-1] #stores remaining elements of shifted list


        else:
            split = len(lst)-k #sets the index where to split the list
            newRight = lst[:split] #sets index 0 to index before split as list's right side
            newLeft = lst[split:] #sets index split to last index as list's left side

    # if k < 0, a shift to the left is performed
    elif k < 0:

        #if the absolute value of k is greater than lst's length, only a shift of the remainder is required
        if abs(k) > len(lst):
            k = abs(k)%len(lst) #finds the remainder to use as new shift value


            if k == 0:
                return lst
        k = abs(k) #makes k positive so it can be used later in the program

        # when k=1, only the last element needs to be shift to the end
        if k == 1:
            newRight = [lst[0]] #sets ending element
            newLeft = lst[1:] #sets list of preceding elements

        else:

            split = abs(k) #sets the index to split the lst
            newLeft = lst[split:] #sets left to list starting from split index to end of list
            newRight = lst[:split] #sets right to list starting at index 0 until index before split

    # returns shifted list
    #print("left side " +str(newLeft))
    #print("right side "+str(newRight))

    newList = newLeft + newRight

    return newList



# Circular Shift, Solution 2
def circularshift_2(lst, k):

    isNegative = False #sets variable to check if k is negative

    #sets isNegative to true if k is negative and sets k to its absolute value
    if k < 0:
        isNegative = True
        k = abs(k)

    #if k is greater than lst's length, only a shift of the remainder of k/len(lst) is necessary
    if k >= len(lst):
        k = k%len(lst) #fins the remainder of k/len(lst)

    #For the cases in the conditional the shift would result in the orginal list order
    if len(lst) <= 1 or k == len(lst) or k == 0:
        return lst #returns original list

    #if k is originally positive, a right shift is performed
    if isNegative == False:
        start = 0 #start index set to beginning of list
        end = len(lst)-k #end index set to end of list minus k

        while start < len(lst)-1: #iterates through list from beginning

            #shift right swap
            swap = lst[start] #holds inital value at start index
            lst[start] = lst[end] #sets start index's value to end index's value
            lst[end] = swap #sets end index's value to orignal start index's value

            #if end is lest than last index of list, end index increases
            if end < len(lst)-1:
                end += 1

            #otherwise end is reset to len(lst)-k to perform remaining swaps
            else:
                end = len(lst)-k
            start += 1 #increases start index

    #if k was orginally negative, a left shift is performed
    else:
        start = k-1 #sets start index equal to k-th element
        end = len(lst)-1 #sets end index equal to last index in list

        #iterates through list backwards
        while end > 0:

            #shift left swap
            swap = lst[start] #holds inital value at start index
            lst[start] = lst[end] #sets start index's value to end index's value
            lst[end] = swap #sets end index's value to orignal start index's value

            #while start is greater than 0 start decreases
            if start > 0:
                start -= 1

            #otherwise start is set back to k-1 to perform remaining required swaps
            else:
                start = k-1
            end -= 1 #decreases end index

    # returns shifted list
    return lst
