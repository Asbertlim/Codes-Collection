from collections import defaultdict

def count_emergencies(reports): #1
  freq = defaultdict(int)
  for report in reports:
    freq[report[1]] += 1

  return freq
# ------------------------------------------------
def most_dangerous_location(reports): #2
  current = float("-inf")
  loc = None
  freq = defaultdict(int)
  
  for report in reports:
    freq[report[0]] += report[2]
  for block, value in freq.items():
    if value > current:
      current = value
      loc = block
  return loc
# ------------------------------------------------
def most_critical(reports): # 3 
  freq = defaultdict(int)
  current = float("-inf")
  crit = None

  for report in reports:
    if report[2] == 5:
      freq[report[0]] += 1
  for block, value in freq.items():
    if value > current:
      crit = block
  return crit
  
# ------------------------------------------------
def dispatch(reports): # 4
  lst = []

  for report in reports:
    if report[2] == 5:
      if report[1] == "Fire":
        lst.append((report[0], "Fire Team"))
      else:
        lst.append((report[0], "Medical Team"))
  return lst
# ------------------------------------------------
# Test cases
reports = [
    ("Block A", "Fire", 5),
    ("Block C", "Medical", 3),
    ("Block A", "Medical", 2),
    ("Block B", "Fire", 4),
    ("Block C", "Medical", 5),
    ("Block A", "Fire", 5)
]
print(dispatch(reports))
