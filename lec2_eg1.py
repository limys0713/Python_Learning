b = ":"
c = ")"
s1 = b + 2 * c
print(s1)

# Negative index in python
s = "abc"
print(s[0])
print(s[1])
print(s[2])
print(s[-1])
print(s[-2])
print(s[-3])

# Slicing to get a SUBSTRING
# [start : stop : step]
s = "abcdefgh"

print(s[3 : 6])
print(s[3 : 6 : 1]) # same as last line
print(s[3 : 6 : 2])
print(s[:]) # same as s[0 : len(s) : 1]
print(s[::-1])
print(s[4 : 1 : -2])  # Moving reversely # Move from right-to-left

# TRY
s = "ABC d3f ghi"

print(s[3 : len(s) - 1])
print(s[4 : 0 : -1])
print(s[4 :: -1])
print(s[6 : 3]) ### NOTHING? # Working to the right(default = 1)

### PRINTING
a = "the"
b = 3
c = "musketeers"
print(a, b, c)  # ,: space between the variable
print(a + str(b) + c) # Concat 3 string

### INPUT
text = input("Type anything: ") ### Save as a string
print(5 * text)

### F-STRING
num = 3000
fraction = 1 / 3
print(f"num*fraction is {fraction * 100}% of {num}")

### BRANCHING in Python
