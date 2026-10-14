# Task 1
def calculate_totals(scores):
  robots = {}
  for score in scores:
    if score[0] not in robots:
      robots[score[0]] = score[1]
    else:
      robots[score[0]] += score[1]
  return robots



# Task 2
def rank_robots(totals):
  lst = list(totals.items())
  lst = sorted(lst, key=lambda robot:(-robot[1], robot[0]))
  return lst

print(rank_robots(calculate_totals([("Scout", 12), ("Bolt", 15), ("Scout", 8), ("Atlas", 20), ("Bolt", 5), ("Atlas", 3), ("Nova", 23)])))
