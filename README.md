# json_project

The files for US_Fires function by taking information from two different JSON files that include a list with multiple dictionaries in each list,
each dictionary counts as one fire.

3 Lists are then created, lons, lats, and brights.

Each list is appended by a for loop with an IF function inside that stops the appending on any fire that does not have a brightness of over 450.

The program then creates an HTML webpage scattegeo plot based on each fire, with coloring dependent on the brightness of the fire. When hovering over the dots, you will
the latitude and longitude of the fire, along with the number relating to the brightness of the fire.
