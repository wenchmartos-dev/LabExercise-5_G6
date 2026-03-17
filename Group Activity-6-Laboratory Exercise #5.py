# 1. Calculate the length and character count of the string
# -------------------------------------------------------------------------------------------
print("1. Length of String and Character Count")

text = input("   Enter text here to count the length of string and characters: ")
length = len(text)

print(f"   → Length: {length} characters")
print(f"   → Number of characters: {length}\n")
# -------------------------------------------------------------------------------------------

# 2. Change all occurrences of first character to '$' except the first one
# -------------------------------------------------------------------------------------------
print("2. Replace later occurrences of first character with '$'")

s = input("   Enter a string → ")

if len(s) == 0:
    print("   → Empty string!")
elif len(s) == 1:
    print("   → Result:", s)
else:
    first = s[0]
    changed = first + s[1:].replace(first, '$')
    print("   → Result:", changed)

print()  # blank line
# -------------------------------------------------------------------------------------------

# 3. Combine two strings + swap first two characters of each
# -------------------------------------------------------------------------------------------
print("3. Swap first two letters of two strings and join them")

a = input("   First string  → ")
b = input("   Second string → ")

if len(a) < 2 or len(b) < 2:
    print("   → Both strings must have at least 2 characters!")
else:
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    result = new_a + " " + new_b
    print("   → Result:", result)

print()
# -------------------------------------------------------------------------------------------

# 4. Concatenate 4 variables using +
# -------------------------------------------------------------------------------------------
print("4. Concatenate 4 variables with spaces")

var1 = "Python"
var2 = "coding"
var3 = "is"
var4 = "enjoyable"

sentence = var1 + " " + var2 + " " + var3 + " " + var4
print("   →", sentence)
print()
# -------------------------------------------------------------------------------------------

# 5. Get two strings from user and concatenate them
# -------------------------------------------------------------------------------------------
print("5. Concatenate two strings entered by user")

str1 = input("   Enter first text  → ")
str2 = input("   Enter second text → ")

together = str1 + str2
together_spaced = str1 + " " + str2

print("   → Without space  :", together)
print("   → With space     :", together_spaced)
print()
# -------------------------------------------------------------------------------------------

# 6. Name and age in a paragraph using +
# -------------------------------------------------------------------------------------------
print("6. Name + age in a sentence/paragraph")

my_name = input("   Enter your name → ")
my_age  = input("   Enter your age  → ")

# Make sure age is treated as string safely (input already gives string)
msg = "Hello! My name is " + my_name + " and I am " + my_age + " years old."
print("   → Short version:", msg)

paragraph = (
    "My name is " + my_name + ". " +
    "I am " + my_age + " years old and " +
    "I am currently taking BSIT. " +
    "Right now I am learning string manipulation in Python."
)

print("   → Paragraph:")
print("     " + paragraph)

# -------------------------------------------------------------------------------------------
