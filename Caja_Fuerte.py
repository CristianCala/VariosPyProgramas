def final_value(movements = []):
  # Your solution
  noMoves = 0

  while noMoves <= 1:

    data = input("write the movements: \n ")

    movements.append(data)
    noMoves += 1

  print("The position is: ", safe(movements))


def safe(movements):

# Debería llegar de 0-99 (total 10 números)

  position = 0

  for element in movements:

    element = int(element)

    position += element
    # print(position)


  result(position)


  # return result

def result(position):


  # while position > 99:
  #   result = position - 99
  #   print(result, position)

      
  # if (position >= 99):
  #   print("el número es mayor \n")
  #   while position >= 99:
  #     result = position - 99
  #     print(result)
  #     break
      


  # elif (position < 0):
  #   print("es menor \n")
  #   while position < 0:
  #     result  = position + 99 



  # return result

if __name__ == "__main__":
  # Code written here or in other files will be ignored by the automated tests.
  # You can run this code when running the file with `python safe.py`
  final_value()
