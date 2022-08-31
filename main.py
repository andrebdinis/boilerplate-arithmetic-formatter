# This entrypoint file to be used in development. Start by reading README.md
from pytest import main
from arithmetic_arranger import arithmetic_arranger


#problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
problemsAll = [
  ['3801 - 2', '123 + 49'],
  ['1 + 2', '1 - 9380'],
  ['3 + 855', '3801 - 2', '45 + 43', '123 + 49'],
  ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'],
  ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'],
  ['3 / 855', '3801 - 2', '45 + 43', '123 + 49'],
  ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'],
  ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
]
problemsTrue1 = [
  ['3 + 855', '988 + 40'], True
]
problemsTrue2 = [
  ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True
]
result = arithmetic_arranger(problemsAll[0], False)
print(result)


# Run unit tests automatically
main(['-vv'])
