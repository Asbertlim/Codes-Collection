# sliding window application


def busiest_period(passengers, limit):
    current = 0
    left = 0
    best = len(passengers) + 1

    for right in range(len(passengers)):
        current += passengers[right]

        while current >= limit:
            length = right - left + 1
          
            if length < best:
                best = length
              
            current -= passengers[left]
            left += 1
          
        if best = len(passengers) + 1:
            return -1
      
    return best
