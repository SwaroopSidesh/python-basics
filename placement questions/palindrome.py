def is_palindrome(text):

    # Step 1: Reverse the string using loop
    reversed_text = ''

    for char in text:
        reversed_text = char + reversed_text

    # Step 2: Compare original and reversed string
    return text == reversed_text


print(is_palindrome('radar'))
print(is_palindrome('cat'))