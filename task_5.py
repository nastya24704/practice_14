def main() -> None:
  elements = input("Enter integer numbers separated by spaces: ")
  numbers = [int(num) for num in elements.split()]
  average = sum(numbers) / len(numbers)
  print(average)
