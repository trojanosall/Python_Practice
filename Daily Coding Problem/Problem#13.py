# Good morning! Here's your coding interview problem for today.
# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


# define character range
CHAR_RANGE = 128


# Function to find longest substring of given containing
# k distinct characters using sliding window
def longestSubstr(str, k):

    # stores longest substring boundaries
    end = begin = 0

    # set to store distinct characters in a window
    window = set()

    # count list to store frequency of characters present in current window
    # we can also use a dictionary instead of count list
    freq = [0] * CHAR_RANGE

    # [low..high] maintain sliding window boundaries
    low = high = 0

    while high < len(str):

        window.add(str[high])
        freq[ord(str[high])] = freq[ord(str[high])] + 1

        # if window size is more than k, remove characters from the left
        while len(window) > k:

            # if the frequency of leftmost character becomes 0 after
            # removing it in the window, remove it from set as well
            freq[ord(str[low])] = freq[ord(str[low])] - 1
            if freq[ord(str[low])] == 0:
                window.remove(str[low])

            low = low + 1	   # reduce window size

        # update maximum window size if necessary
        if end - begin < high - low:
            end = high
            begin = low

        high = high + 1

    # return longest substring found at str[begin..end]
    return str[begin:end + 1]


if __name__ == '__main__':

    str = "abcbdbdbbdcdabd"
    k = 2

    print(longestSubstr(str, k))
