#!/usr/bin/env python3

import requests

URL= "https://opentdb.com/api_config.php"

def get_amount():
  while True:
    clear()
    print('Enter number of question(1-10): ')
    selection = int(input())

    if selection in range(1,10):
      return str(selection)

def get_category():
  categories = {
    '1': 'Any',
    '2': 'General Knowledge',
    '3': 'Entertainment: Books',
    '4': 'Entertainment: Film',
    '5': 'Entertainment: Music',
    '6': 'Entertainment: Television',
    '7': 'Science & Nature',
    '8': 'Science: Computers',
    '9': 'Science: Mathematics',
    '10': 'Sports',
    '11': 'Geography',
    '12': 'History',
    
  }

  while True:
    clear()
    print('Categories:\n')

    for i in categories:
      print(f'{i} : {categories[i]}')

    print('\nEnter the number of your selection: ')
    selection = int(input())
    
    if selection in range(1, 12):
      return str(selection + 7) 

def get_difficulty():
  while True:
    clear()
    print('Difficulty:\n')
    print('1: Any\n2: Easy\n3: Medium\n4: Hard\n')
    print('Enter the number of your selection.')
    selection = int(input())
    
    if selection == 1:
      return 'any'
    if selection == 2:
      return 'easy'
    if selection == 3:
      return 'medium'
    if selection == 4:
      return 'hard'

def get_game_type():
  while True:
    clear()
    print('Game Types:\n')
    print('1: Any Type')
    print('2: Multiple Choice')
    print('3: True/False')
    print('\nEnter the number of your selection: ')
    selection = int(input())

    if selection == 1:
      return 'any'
    if selection == 2:
      return 'multiple'
    if selection == 3:
      return 'boolean'   

def get_json():
  amount = get_amount()
  category = get_category()
  difficulty = get_difficulty()
  game_type = get_game_type()

  full_url = base_url 
  full_url += f'?amount={amount}'
  if int(category) > 8:
    full_url += f'&category={category}'
  if difficulty != 'any':
    full_url += f'&difficulty={difficulty}'
  if game_type != 'any':
    full_url += f'&type={game_type}'

  r = requests.get(full_url)
  j = json.loads(r.text)
  return j['results']

def true_or_false(data):
  print('1: True')
  print('2: False\n')

  selecting = True
  while selecting:
    print('Make your selection: ')
    answer = int(input())

    if answer == 1:
      answer = 'true'
      selecting = False
    if answer == 2:
      answer = 'false'
      selecting = False

  if answer == data['correct_answer']:
    print('Correct!')
    time.sleep(2)
    return True
  else:
    print(f"Incorrect! The correct answer was {data['correct_answer']}")
    time.sleep(2)
    return False

def multiple_choice(data):
  answers = [ 
    data['correct_answer'],
    data['incorrect_answers'][0],
    data['incorrect_answers'][1],
    data['incorrect_answers'][2]
  ]

  random.shuffle(answers)

  for i in range(0, 4):
    print(f'{i + 1}: {answers[i]}')
  print('\n')

  selecting = True
  while selecting:
    print('Enter your selection: ')
    choice = int(input())

    if choice in range(1, 4):
      selecting = False

  if answers[choice - 1] == data['correct_answer']:
    print('Correct!')
    time.sleep(2)
    return True
  else:
    print(f"Incorrect! The correct answer was {data['correct_answer']}")
    time.sleep(2)
    return False

def display_summary(score, num_questions):
  clear()
  print('Game over!\n')
  print(f'{score}/{num_questions} correct.\n')
  print('Would you like to play again?\n')
  print('1: Yes\n2: No\b')

  while True:
    print('Enter your selection: ')
    choice = int(input())
    if choice == 1:
      return True
    if choice == 2:
      return False  

def play_game():
  score = 0
  num_questions = 0 
  data = get_json()
  
  for i in data:
    num_questions += 1

    clear()
    print(f"Question #{num_questions}")
    print(f"Category: {i['category']}")
    print(f"Difficulty: {i['difficulty']}\n")
    print(f"Question:\n{i['question']}\n") 

    if i['type'] == 'boolean':
      correct = true_or_false(i)
    else:
      correct = multiple_choice(i)

    if correct:
      score += 1

  return display_summary(score, num_questions) 
 
def main():
  play = True
  while play:
    play = play_game()


main()
