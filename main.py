
def is_palindrome(text):
    """Return True if the given text is a palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Return the number of vowels in the text."""
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


def reverse_string(text):
    """Return the reversed version of the text."""
    return text[::-1]


def word_count(text):
    """Return the number of words in the text."""
    words = text.split()
    return len(words)


def main():
    """Main function to demonstrate palindrome and utilities."""
    sample = "madam"
    sentence = "Hello World"

    print("Sample text:", sample)
    print("Is palindrome?", is_palindrome(sample))
    print("Sentence:", sentence)
    print("Reversed:", reverse_string(sentence))
    print("Word count:", word_count(sentence))
    print("Vowel count:", count_vowels(sentence))


if __name__ == "__main__":
    main()

