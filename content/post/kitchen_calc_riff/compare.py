import helpers as h

weekly = h.BaseTimeFrame(7)
monthly = h.BaseTimeFrame(31)

# Twice a week is how many times per month?

apples = h.Consumption(2, weekly)
oranges = h.Consumption(3, monthly)

apples / oranges