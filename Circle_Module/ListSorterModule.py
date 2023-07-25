def sortAscBubble(unsorted):
  size = len(unsorted)
  for x in range(size - 1):
    for y in range(size - 1):
      if unsorted[y + 1] < unsorted[y]:
        temp = unsorted[y]
        unsorted[y] = unsorted[y + 1]
        unsorted[y + 1] = temp
  return unsorted


def sortDescBubble(unsorted):
  size = len(unsorted)
  for x in range(size - 1):
    for y in range(size - 1):
      if unsorted[y + 1] > unsorted[y]:
        temp = unsorted[y]
        unsorted[y] = unsorted[y + 1]
        unsorted[y + 1] = temp
  return unsorted


def sortAscExchange(unsorted):
  size = len(unsorted)
  for x in range(size - 1):
    for y in range(x + 1, size):
      if unsorted[y] < unsorted[x]:
        temp = unsorted[x]
        unsorted[x] = unsorted[y]
        unsorted[y] = temp
  return unsorted


def sortDescExchange(unsorted):
  size = len(unsorted)
  for x in range(size - 1):
    for y in range(x + 1, size):
      if unsorted[y] > unsorted[x]:
        temp = unsorted[x]
        unsorted[x] = unsorted[y]
        unsorted[y] = temp
  return unsorted


def sortAscInsertion(unsorted):
  size = len(unsorted)
  for x in range(size):
    key = unsorted[x]
    y = x - 1
    while y >= 0 and unsorted[y] > key:
      unsorted[y + 1] = unsorted[y]
      y -= 1
    unsorted[y + 1] = key
  return unsorted


def sortDescInsertion(unsorted):
  size = len(unsorted)
  for x in range(size):
    key = unsorted[x]
    y = x - 1
    while y >= 0 and unsorted[y] < key:
      unsorted[y + 1] = unsorted[y]
      y -= 1
    unsorted[y + 1] = key
  return unsorted


def sortAscSelection(unsorted):
  size = len(unsorted)
  for x in range(size - 1):
    key = x
    for y in range(x + 1, size):
      if unsorted[y] < unsorted[key]:
        key = y
    temp = unsorted[key]
    unsorted[key] = unsorted[x]
    unsorted[x] = temp
  return unsorted


def sortDescSelection(unsorted):
  size = len(unsorted)
  for x in range(size - 1):
    key = x
    for y in range(x + 1, size):
      if unsorted[y] > unsorted[key]:
        key = y
    temp = unsorted[key]
    unsorted[key] = unsorted[x]
    unsorted[x] = temp
  return unsorted