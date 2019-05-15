# Situation: 1 phone number and 1000 routes in a text file

# Step 0: Copy full phone number including '+' and ',', for example '+14105548067,'.
# Step 1: Open routes file.
# Step 2: Search for phone number using CMD+F (or CTRL+F on windows).
#         If there are no search results, remove the last digit in search bar before the ','
#         Ex: '+1410554806,' '+141055480,' '+14105548,' '+1410554,'
# Step 3: Continue repeating Step (2) until you get a match.
#         In the unlikely event you get several matches, choose the cheapest.
#         If you keep deleting numbers until you only have a '+,' left, there's no match
# Step 4: You're done!
#         - If you found a match in Step (3), the cost is the number on the right side of the comma.
