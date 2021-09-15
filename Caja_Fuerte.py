def final_value(movements = [50, 49, -4]):
  # Your solution

  data = sum(movements)

  if data >= 0:
    convertData = (((abs(data//100)*100)-data) *-1)

  else:
    convertData = ((abs(data//100)*100)+data)

  return print("The number is: ", convertData)


if __name__ == "__main__":
  # Code written here or in other files will be ignored by the automated tests.
  # You can run this code when running the file with `python safe.py`
  final_value()
