from black_jack import Card, Deck, Player, Game

# player pays $100 to play a game
# they get $500 if sum = 21
# they get $300 if sum = 20
# they get $200 if sum = 19
# they get $150 if sum = 18
# they get $50 if sum = 17
# they get $10 if sum = 16



def main():
    player = Player('Daniyar')
    new_game = True

    while (new_game):
        game = Game(player) 
        next_card = True
        while (next_card):
            game_continue = game.turn()
            if (not game_continue):
                break


            x = input('Do you want to take a card (y/n): ')
            if (x == 'n' or x=='N' or x=='no' or x=='NO'):
                next_card = False
    
        payoff = game.stop()
        print('You won: $' + str(payoff))
        print('You now have $' + str(player.money))
        
        x = input('do you want to play another game (y/n): ')
        if (x == 'n' or x=='N' or x=='no' or x=='NO'):
            new_game = False

    print('Thank you for visiting 4Schoolers BlackJack')
    print('You now have: $' + str(player.money))



if __name__ == '__main__':
    main()