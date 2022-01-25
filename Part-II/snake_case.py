# From Wikipedia,
# Snake case (stylized as snake_case) refers to the style of writing in which each space is replaced by an underscore (_) character, and the first letter of each word written in lowercase. It is a commonly used naming convention in computing, for example for variable and subroutine names, and for filenames. One study has found that readers can recognize snake case values more quickly than camel case.

# Write a Python program to convert a given string to snake case.

# Use re.sub() to match all words in the string, str.lower() to lowercase them.
# Use re.sub() to replace any - characters with spaces.
# Finally, use str.join() to combine all words using - as the separator.


from re import sub
def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

print(snake_case('JavaScript'))
print(snake_case('Foo-Bar'))
print(snake_case('foo_bar'))
print(snake_case('--foo.bar'))
print(snake_case('Foo-BAR'))
print(snake_case('fooBAR'))
