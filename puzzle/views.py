import random
from django.shortcuts import render
from .forms import PuzzleForm

def puzzle_view(request):
    first_puzzle = []
    second_puzzle = []
    third_puzzle = []
    form = PuzzleForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        number = form.cleaned_data['number']
        text = form.cleaned_data['text']

        if number % 2 == 0:
            number_sqrt = number ** (1/2)
            first_puzzle.append(f"The number {number} is even. Its square root is {number_sqrt}.")
        else:
            number_cube = number ** 3
            first_puzzle.append(f"The number {number} is odd. Its cube is {number_cube}.")

        text_binary = ' '.join(format(ord(i), '08b') for i in text)
        text_vowels = sum(i.lower() in 'aeiou' for i in text)
        second_puzzle.append(f"Binary: {text_binary}")
        second_puzzle.append(f"Vowel Count: {text_vowels}")

        random_number = random.randint(1, 100)
        third_puzzle.append(f"The secret number is {random_number}.")
        guesses = []
        correct = False

        for i in range(1,6):
            guess = random.randint(1, 100)
            guesses.append(guess)
            if guess == random_number:
                third_puzzle.append(f"Attempt {i}: {guess} (Correct!)")
                correct = True
                break
            elif guess > random_number:
                third_puzzle.append(f"Attempt {i}: {guess} (Too high!)")
            else:
                third_puzzle.append(f"Attempt {i}: {guess} (Too low!)")
        else:
            third_puzzle.append("You did not find the treasure in 5 attempts.")

        if correct:
            third_puzzle.append(f"You found the treasure in {len(guesses)} attempts!")

    return render(request, 'puzzle/form.html', {
        'form': form,
        'first_puzzle': first_puzzle,
        'second_puzzle':   second_puzzle,
        'third_puzzle':   third_puzzle,
    })
