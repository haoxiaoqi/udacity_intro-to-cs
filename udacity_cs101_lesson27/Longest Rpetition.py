# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(input):
    max_element = None
    count = 0
    current = None
    current_count = 0
    for element in input:
        if element != current:
            current = element
            current_count = 1
        else:
            current_count += 1
        if current_count > count:
            count = current_count
            max_element = current
    return max_element



# For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1, 2, 3, 4, 5])
# 1

print longest_repetition([])
# None

