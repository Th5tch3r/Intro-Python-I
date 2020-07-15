"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt') as foo:
    read_foo = foo.read()
    print(read_foo)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_content = """Hello guys, my name is Thatcher and I am 20 years old.
\nI started coding when I was 18 and I hope I will pursue in a coding job.
\nCoding has always been something I am very interested in learning and work on!"""

with open("bar.txt", "w") as bar:
    write_data = bar.write(bar_content)

with open("bar.txt") as bar:
    read_bar = bar.read()
    print(read_bar)