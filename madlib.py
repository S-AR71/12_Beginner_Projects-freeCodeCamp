# string concatenation (how to put strings together)
# imagine we want to create a string that says "Read more ----"
# book = "Non-Fiction"  # some string variable

# # a few ways to do this

# print("Read more " + book)
# print("Read more {}".format(book))
# print(f"Read more {book}")

# madlib

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
book_lover = input("Book lover: ")

madlib = f"Reading books is so {adj}! It makes me very excited every time because \
I love to {verb1}. Stay focused and {verb2} as if you are {book_lover}!"
print(madlib)
