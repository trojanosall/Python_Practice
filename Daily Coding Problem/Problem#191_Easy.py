# Good morning! Here's your coding interview problem for today.
# This problem was asked by Stripe.
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.
# For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.
# The intervals are not necessarily sorted in any order.

list_of_intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# list_of_intervals = [[7, 9], [2, 4], [5, 8]]
# list_of_intervals.sort()

# zipped_interval = []
# for interval in list_of_intervals:
#     for element_of_interval in interval:
#         zipped_interval.append(element_of_interval)

# list_of_acceptable_intervals = []
# element_of_whole_range_intervals = []
# for interval in list_of_intervals:
#     for x in range(interval[0], interval[1]+1, 1):
#         if x not in element_of_whole_range_intervals:
#             element_of_whole_range_intervals.append(x)
#             list_of_acceptable_intervals.append(interval)


# print(element_of_whole_range_intervals)
# print(list_of_acceptable_intervals)

