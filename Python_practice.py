# Import the datetime class from the datetime module.
import datetime as dt
import os
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    txt_file.write("Hello again")
    txt_file.write("\ndid you save the last line?")
