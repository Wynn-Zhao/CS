from flask import Flask, render_template, request, redirect, url_for, session
from Black_Jack import Card, Deck, Player, Game
app = Flask(__name__)
app.secret_key = 'rdyhgjhjkjhgdfsxcvbhj'


@app.route('/')
def index():
   return render_template('index.jinja')


@app.route('/game', methods = ['GET', 'POST'])
def game():
   player = Player('Player')
   new_game = True 

   while (new_game):
      game = Game(player) 
      next_card = True
      while (next_card):
         game_continue = game.turn()
         session['cards'] = game.return_card()
         if (not game_continue):
            break

         if (request.method == 'POST'):
            answer = request.form.get('answer')
            if (answer != 'yes'):
               next_card = False
   return render_template('game.jinja')


if __name__ == '__main__':
   app.run()