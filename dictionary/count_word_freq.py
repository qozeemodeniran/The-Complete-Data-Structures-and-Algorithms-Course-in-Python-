"""
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}
"""


def count_word_frequency(words):
    if not words:
        return {}

    freq = {i: words.count(i) for i in words}
    return freq


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))


"""
SOLUTION - Time and Space Complexity of Count Word Frequency
def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
 
Explanation:

Define a function count_word_frequency(words) that takes a list of words as its input.

Initialize an empty dictionary word_count to store the frequency of each word in the list.

Iterate through the list of words using a for loop.

For each word, use the get() method to retrieve the current count of the word in the word_count dictionary. If the word is not yet present in the dictionary, get() returns the default value (0). Then, increment the count by 1 and update the dictionary.

After iterating through all the words, return the word_count dictionary containing the word frequencies.

Time complexity:

The time complexity of this exercise is O(n), where n is the number of words in the input list. The loop iterates through each word in the list once, and the dictionary operations (get and update) take constant time, O(1), on average.

Space complexity:

The space complexity of this exercise is also O(n), where n is the number of unique words in the input list. In the worst case, all words are unique, and the word_count dictionary will have n entries.


"""