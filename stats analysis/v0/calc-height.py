# Defining the `calc_height` variable.
example_input = "5-1"

def calc_height(raw_height):
# Calculates height from feet-inches to inches
# Parameters
# ---------
# Variable, feet-inches raw_height: Raw Height for example, 5-10 or 5-2 or 5-9
  height_components = raw_height.split("-")
  n_feet = int(height_components[0])
  n_inches = int(height_components[1])

  return (n_feet * 12) + n_inches

x = calc_height(example_input)
print(x)