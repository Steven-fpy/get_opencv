import random

CARD_MAX = 100

cards = []

keepGroups = []
scores = []
opened = []

def solution():

  global cards

  while True:

    # 임의의 상자를 선택
    n = random.randrange(1, len(cards)+1)
  
    group = []

    while True:
      
      # print('num: ', num)
      if n in opened:
        break

      # 해당 번호의 상자 안에 들어 있었던 카드의 숫자
      num = cards[n-1]
     
      opened.append(n)
      group.append(n)
    
      n = num

    if len(group) > 0:
      keepGroups.append(group)
      scores.append(len(group))
   
    if len(cards) == len(opened):
      break


def openBoxRecursion(n, group:list):
  
  if n in opened:
   
    return group

  num = cards[n-1]
    
  group.append(n)
  opened.append(n)

  openBoxRecursion(num, group)
  return group


def solutionRecursion():
  
  # 임의의 상자를 선택
  n = random.randrange(1, len(cards)+1)
 
  # 재귀
  group = openBoxRecursion(n, [])
 
  if len(group) > 0:
    keepGroups.append(group)
    scores.append(len(group))
  
  if not [card for card in cards if card not in opened]:
    return

  solutionRecursion()


def displayResult():

  # 내림차순 정렬
  scores.sort(reverse=True)
     
  # 결과 출력
  print('\n:::result:::\n')
  for keep in keepGroups:
    print(keep)

  print()

  if (len(scores) <= 1):
    print(f'score: {scores[0]} x 0 = 0')
  else:
    print(f'score: {scores[0]} x {scores[1]} = {scores[0] * scores[1]}')

  print()

if __name__ == '__main__':

  while True:
    
    keepGroups = []
    scores = []
    opened = []

    # ---- 사용자 입력
    inputText = input('카드의 수를 입력하세요(2이상 100이하): ')

    if not inputText.isdigit():
      continue

    inputDigit = int(inputText)
    if inputDigit < 2 or inputDigit > 100:
      continue

    cards = [i+1 for i in range(inputDigit)]
    
    for i in range(len(cards)):
      ri = random.randrange(0, len(cards))

      temp = cards[i]
      cards[i] = cards[ri]
      cards[ri] = temp
    # 반복문
    solution()

    displayResult()