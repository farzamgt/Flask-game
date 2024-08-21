from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

user_score = 0
computer_score = 0
counter = 0
options = ['paper', 'rock', 'scissors']
final_user_score = 0
final_computer_score = 0
rounds = []

@app.route('/', methods=['GET', 'POST'])
def start():
    global rounds, user_score, computer_score, counter, final_user_score, final_computer_score

    rounds = []
    user_score = 0
    computer_score = 0
    counter = 0
    final_user_score = 0
    final_computer_score = 0

    if request.method == 'POST':
        return redirect(url_for('game'))
    return render_template('start.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    global user_score, computer_score, counter, final_computer_score, final_user_score, rounds

    if request.method == 'POST':
        if counter < 3:
            user_choice = request.form.get('choice').lower()

            if user_choice == "q":
                user_score = 0
                computer_score = 0
                counter = 0
                final_user_score = 0
                final_computer_score = 0
                rounds = []
                return redirect(url_for('start')) 

            random_number = random.randint(0, 2)
            computer_choice = options[random_number]

            if user_choice == computer_choice:
                result = "No one wins!"
            elif user_choice == "rock" and computer_choice == "scissors":
                result = "You win!"
                user_score += 1
            elif user_choice == "paper" and computer_choice == "rock":
                result = "You win!"
                user_score += 1
            elif user_choice == "scissors" and computer_choice == "paper":
                result = "You win!"
                user_score += 1
            else:
                result = "Computer wins!"
                computer_score += 1

            counter += 1

            rounds.append({'round': counter, 'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result})

            if counter == 3:
                return render_template('index.html', result=result, user_score=user_score, computer_score=computer_score, rounds=rounds)
    
    if counter == 3:
        if user_score > computer_score:
            final_user_score += 1
            winner = "You won this set!"
        elif computer_score > user_score:
            final_computer_score += 1
            winner = "Computer won this set!" 
        else:
            winner = "It's a tie for this set!"

        if final_user_score >= 3:
            winner = "Congratulations! You are the overall winner!"
        elif final_computer_score >= 3:
            winner = "Computer is the overall winner!"
        
        user_score = 0
        computer_score = 0
        counter = 0
        rounds = []        

        return render_template('result.html', winner=winner, user_score=final_user_score, computer_score=final_computer_score)
    
    result = 'No results yet!' if not rounds else rounds[-1]['result']
    return render_template('index.html', result=result, user_score=user_score, computer_score=computer_score, rounds=rounds)


if __name__ == '__main__':
    app.run(debug=True)
