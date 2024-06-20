import random
from hangman_art import logo
print(logo)
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_len = len(chosen_word)


lives = 6
end_of_game = False

display = []
for _ in range(word_len):
  display += "_"
print(display)


while end_of_game == False:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already guessed {guess}, so choose different letter")
  for position in range(word_len):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
  
 
  if guess not in chosen_word:
    lives -= 1
    print(f"{guess} is not in the word. Don't use that again, You will lose a life")
    if lives == 0:
      end_of_game = True
      print("You lose.")
      print(f"The word was {chosen_word}")
      
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    print("You won")
    end_of_game=True
    
  from hangman_art import stages
  print(stages[lives])