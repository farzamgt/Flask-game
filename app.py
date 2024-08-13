from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

user_score = 0
computer_score = 0
counter = 0
options = ['paper', 'rock', 'scissors']
final_user_score = 0
final_computer_score = 0

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        return redirect(url_for('game'))
    return render_template('start.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    global user_score, computer_score, counter, final_computer_score, final_user_score

    result = None
    if counter < 3:
        if request.method == 'POST':
            user_choice = request.form.get('choice').lower()

            if user_choice == "q":
                return "Goodbye!"

            random_number = random.randint(0, 2)
            computer_choice = options[random_number]

            if user_choice == "rock" and computer_choice == "scissors":
                result = "You win this round!"
                user_score += 1
            elif user_choice == "paper" and computer_choice == "rock":
                result = "You win this round!"
                user_score += 1
            elif user_choice == "scissors" and computer_choice == "paper":
                result = "You win this round!"
                user_score += 1
            else:
                result = "Computer wins this round!"
                computer_score += 1

            counter += 1

        return render_template('index.html', result=result, user_score=user_score, computer_score=computer_score, counter=counter)
    else:
        winner = "It's a tie!"
        if user_score > computer_score:
            final_user_score += 1
            winner = "You won the game!"
        elif computer_score > user_score:
            final_computer_score += 1
            winner = "Computer won the game!"
        
        user_score = 0
        computer_score = 0
        counter = 0

        return render_template('result.html', winner=winner, user_score=final_user_score, computer_score=final_computer_score)

if __name__ == '__main__':
    app.run(debug=True)
