"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""

def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """


    char_counter = {}

    for char in input_string.replace(" ", ""):
        if char not in char_counter:
            char_counter[char] = 1
        else: 
            char_counter[char] += 1

    max_value = 0
    for char, count in char_counter.items():
        if count > max_value:
            max_value = count 
            most_common_char = [char]
        elif count == max_value:
            most_common_char.append(char)

    return most_common_char



# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
    word_length_dict = {}
    final_list = []

    for word in words:
        word_length = len(word)
        if word_length in word_length_dict:
            word_length_dict[word_length].append(word)
        else: 
            word_length_dict[word_length] = [word]

    for key, value in word_length_dict.items():
        sorted_tuple = (key, sorted(value))
        final_list.append(sorted_tuple)
    
    return final_list


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
