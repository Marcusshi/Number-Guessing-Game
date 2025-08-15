from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/')
def index():
    if 'secret' not in session:
        session['secret'] = random.randint(1, 100)
        session['attempts'] = 0
        session['max_attempts'] = 10
        session['message'] = 'Enter your guess!'
        session['message_color'] = 'info'
    
    return render_template('game.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        guess = int(request.form['guess'])
        
        if not 1 <= guess <= 100:
            session['message'] = '❌ Please enter a number between 1 and 100!'
            session['message_color'] = 'danger'
            return redirect(url_for('index'))
            
    except ValueError:
        session['message'] = '❌ Please enter a valid number!'
        session['message_color'] = 'danger'
        return redirect(url_for('index'))
    
    session['attempts'] += 1
    
    if guess == session['secret']:
        session['message'] = f'🎉 Congratulations! You guessed it in {session["attempts"]} attempts!'
        session['message_color'] = 'success'
    elif guess < session['secret']:
        session['message'] = f'📈 Too low! Try a higher number. ({session["max_attempts"] - session["attempts"]} attempts left)'
        session['message_color'] = 'warning'
    else:
        session['message'] = f'📉 Too high! Try a lower number. ({session["max_attempts"] - session["attempts"]} attempts left)'
        session['message_color'] = 'warning'
    
    if session['attempts'] >= session['max_attempts'] and guess != session['secret']:
        session['message'] = f'😔 Game Over! The number was {session["secret"]}'
        session['message_color'] = 'danger'
    
    return redirect(url_for('index'))

@app.route('/new_game')
def new_game():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
