""" 6-2 -- String Insertion.

Write a program that collects two strings from a user, inserts them into the 
string "Yesterday I wrote a [response_one]. I sent it to [response_two]!" and 
prints a new string.
"""


what = input("What did you write? ")
where = input("Where did you send it? ")

print("Yesterday I wrote a {}. I sent it to {}!".format(what, where))
