# The Supermarket Queue

# There is a queue for the self-checkout tills at the supermarket.
# Your task is write a function to calculate the total time required
# for all the customers to check out!

# input

# customers: an array of positive integers representing the queue.
# Each integer represents a customer, and its value is the
# amount of time they require to check out.

# n: a positive integer, the number of checkout tills.

# output
# The function should return an integer, the total time required.

# Important
# Please look at the examples and clarifications below, to ensure you
# understand the task correctly :)


# Examples

# queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
# should return 12


# Clarifications
# There is only ONE queue serving many tills, and
# The order of the queue NEVER changes, and
# The front person in the queue (i.e. the first element in the array/list)
# proceeds to a till as soon as it becomes free.



def queue_time(customers, n):
    # Create list of n tills, all starting at 0 time
    tills = [0] * n

    # For each customer
    for customer in customers:
        # Find till with minimum current time and add this customer
        tills[tills.index(min(tills))] += customer

    # Return maximum time among all tills
    return max(tills)


# Example 1: [10,2,3,3], n=2
# tills = [0, 0]  # Start with 2 empty tills

# customer = 10
# tills = [10, 0]  # 10 goes to first empty till

# customer = 2
# tills = [10, 2]  # 2 goes to second till

# customer = 3
# tills = [10, 5]  # 3 goes to second till (it has less time)

# customer = 3
# tills = [10, 8]  # 3 goes to second till

# return max([10, 8]) = 10  # Maximum time among tills


# Key points:

# tills list keeps track of total time at each till
# We always add next customer to till with minimum current time
# Final answer is maximum time among all tills