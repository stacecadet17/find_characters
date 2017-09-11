def findcharacter(list, letter):
  new_list = []
  for item in list:
    if(item.find(letter) >= 0):
      new_list.append(item)

  return new_list

print findcharacter(['mango', 'strawberry', 'orange', 'kiwi', 'coconut'], 'o')
