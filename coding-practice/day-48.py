# World problem

# Task 1
from collections import defaultdict
def total_passengers(reports):
  psg = defaultdict(int)
  for i in reports:
    psg[i[0]] += i[1]

  return psg

# Task 2
from collections import defaultdict
def most_delayed_route(reports):
  delays = defaultdict(int)
  count = defaultdict(int)
  for i in reports:
    delays[i[0]] += i[2]
    count[i[0]] += 1
  avg = {}
  for i in delays:
    avg[i] = round(delays[i]/count[i], 2)
  max = 0
  for i in avg:
    if avg[i] > max:
      max = avg[i]
      best = i
    
  return best

# Task 3
from collections import defaultdict
def congested_routes(reports):
  count = defaultdict(int)
  for report in reports:
    if report[1] >= 35 and report[2] >= 5:
      count[report[0]] += 1

  lst = []
  for i in count:
    if count[i] >= 2:
      lst += [i]
  return sorted(lst)

# Sample Test 
[
    ("Route 23", 35, 4),
    ("Route 10", 42, 8),
    ("Route 23", 40, 7),
    ("Route 10", 38, 3),
    ("Route 15", 25, 10),
    ("Route 23", 30, 2),
    ("Route 15", 32, 6)
]
