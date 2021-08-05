def final_value(movements = []):
  # Your solution
  noMoves = 0

  while noMoves <= 9:

    data = input("write the movements: \n ")

    movements.append(data)
    noMoves += 1

  print("Ready!", safe(movements))


def safe(movements):

  position = 0

  for element in movements:

    element = int(element)

    position += element



  # for i in movements :
    
  #   i = int(i)
  #   print(sum(i))


  # for element in movements:

  #   element = int(element)

  #   result = position + element



    # if(element >= 0):
    #   print("positive \n")

    # elif(element <= 0):
    #   print("negative \n")

  return  position



if __name__ == "__main__":
  # Code written here or in other files will be ignored by the automated tests.
  # You can run this code when running the file with `python safe.py`
  final_value()
