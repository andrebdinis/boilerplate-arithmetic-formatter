import re
# Regex Examples:
# re.search("regex", string)
# lst = re.findall('\S+@\S+', s)
# x = re.findall('^X\S*: ([0-9.]+)', line)

# Problems Example:
# ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


def arithmetic_arranger(problems, solveOption = False):
  # verify if problems have errors
  errorFound = checkForErrors(problems)
  if errorFound: return errorFound

  # problems valid, thus print
  result = getResult(problems, solveOption)
  return result


def checkForErrors(problems):
  size = len(problems)
  if size > 5: return "Error: Too many problems."
  for problem in problems:
    found = re.search('^[\d]{1,4}[ ][+-][ ][\d]{1,4}$', problem)
    if not found:
      pieces = problem.split(' ')
      if len(pieces) < 3:
        return "Error: Invalid format."
      elif not onlyDigits(pieces[0]) or not onlyDigits(pieces[2]):
        return "Error: Numbers must only contain digits."
      elif not onlyFourDigits(pieces[0]) or not onlyFourDigits(pieces[2]):
        return "Error: Numbers cannot be more than four digits."
      elif not validateOperator(pieces[1]):
        return "Error: Operator must be '+' or '-'."
      else:
        return "Error: unknown error."
  return False

def onlyDigits(string):
  found = re.search('^[\d]+$', string)
  if not found: return False
  else: return True
    
def onlyFourDigits(string):
  found = re.search('^[\d]{1,4}$', string)
  if not found: return False
  else: return True

def validateOperator(string):
  found = re.search('^[+-]$', string)
  if not found: return False
  else: return True

def widestNumberLength(numOneLength, numTwoLength):
  widestNum = None
  if numOneLength > numTwoLength: widestNum = numOneLength
  else: widestNum = numTwoLength
  return widestNum

def sumOrSubtract(operator, numOne, numTwo):
  total = None
  if operator == "+": total = (numOne + numTwo)
  elif operator == "-": total = (numOne - numTwo)
  return total

def notLastProblem(problemIndex, problems):
  return problemIndex < (len(problems) - 1)


def getResult(problems, solveOption):
  spacesBetweenProblems = "    "
  operatorSpaceLength = 2
  rowLimit = 4
  row = 0
  result = ""
  while row < rowLimit:

    for problemIndex, problem in enumerate(problems):
      pieces = problem.split(' ')

      # widest number
      numOneLength = len(pieces[0])
      numTwoLength = len(pieces[2])
      widestNumLength = widestNumberLength(numOneLength, numTwoLength)

      # problem width
      problemWidth = operatorSpaceLength + widestNumLength

      # print each row of all problems
      resultArray = getProblemsRows(result, row, pieces, problemWidth, problemIndex, problems, spacesBetweenProblems, solveOption)
      result = resultArray[0]
      row = resultArray[1]

  return result


def getProblemsRows(result, row, pieces, problemWidth, problemIndex, problems, spacesBetweenProblems, solveOption):
  col = None
  value = None
  valueLength = None

  if row == 0:
    # line of spaces + number 1
    col = 0
    numOne = pieces[0]
    value = numOne
    valueLength = len(numOne)

  elif row == 1:
    # line of operator + spaces + number 2
    col = 1
    numTwo = pieces[2]
    value = numTwo
    valueLength = len(numTwo)
    operator = pieces[1]
    result += operator

  elif row == 2:
    # line of dashes ---
    col = 0
    dash = "-"
    value = dash
    valueLength = len(dash)

  elif row == 3 and solveOption:
    # line of solution (if function has second parameter as True)
    col = 0
    numOne = int(pieces[0])
    numTwo = int(pieces[2])
    operator = pieces[1]
    total = str(sumOrSubtract(operator, numOne, numTwo))
    value = total
    valueLength = len(total)
  else:
    row += 1
    return [result, row]

  while col < problemWidth:
    if (col + valueLength) == problemWidth:
      result += value
      if notLastProblem(problemIndex, problems):
        result += spacesBetweenProblems
      else:
        if (row < 2) or (row == 2 and solveOption):
          result += "\n"
        row += 1
      return [result, row]
    else:
      if row != 2:
        result += " "
      else:
        result += value
      col += 1
      