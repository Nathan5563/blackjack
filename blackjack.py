import random

while True:
    play_game = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

    if play_game == "y":
        print(
            """
            ┌──────────┐            ___       ___                      ___                                       ___           
            │.A........│           (   )     (   )                    (   )                                     (   )          
            │..........│            | |.-.    | |    .---.    .--.     | |   ___        .-.    .---.    .--.     | |   ___
            │........┌──────────┐   | /   \   | |   / .-, \  /    \    | |  (   )      ( __)  / .-, \  /    \    | |  (   )
            │....♥️..│.K........│   |  .-. |  | |  (__) ; | |  .-. ;   | |  ' /        (''") (__) ; | |  .-. ;   | |  ' /    
            │........│..........│   | |  | |  | |    .'`  | |  |(___)  | |,' /          | |    .'`  | |  |(___)  | |,' /       
            │........│..........│   | |  | |  | |   / .'| | |  |       | .  '.          | |   / .'| | |  |       | .  '.       
            │........│....♠️....│   | |  | |  | |  | /  | | |  | ___   | | `. \         | |  | /  | | |  | ___   | | `. \      
            └────────│..........│   | '  | |  | |  ; |  ; | |  '(   )  | |   \ \        | |  ; |  ; | |  '(   )  | |   \ \     
                     │..........│   ' `-' ;   | |  ' `-'  | '  `-' |   | |    \ .   ___ | |  ' `-'  | '  `-' |   | |    \ .    
                     │........K.│    `.__.   (___) `.__.'_.  `.__,'   (___ ) (___) (   )' |  `.__.'_.  `.__,'   (___ ) (___)   
                     └──────────┘                                                   ; `-' '                                    
                                                                                      .__.'                                     
            """
        )

        possible_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

        def deal_card():
            card = random.choice(possible_cards)

            if card == 'A':
                card_value = 11
            elif card == 'J' or card == 'Q' or card == 'K':
                card_value = 10
            else:
                card_value = card

            return card, card_value

        first_card, first_card_value = deal_card()
        second_card, second_card_value = deal_card()
        player_cards = [first_card, second_card]
        player_card_values = [first_card_value, second_card_value]
        player_sum = sum(player_card_values)

        dealer_card, dealer_card_value = deal_card()
        hidden_card, hidden_card_value = deal_card()
        dealer_cards = [dealer_card, hidden_card]
        dealer_card_values = [dealer_card_value, hidden_card_value]
        dealer_sum = sum(dealer_card_values)

        print(f"Your cards: {player_cards}")
        print(f"Dealer's first card: {dealer_card}")

        if player_sum > 21:
            player_card_values.remove(11)
            player_card_values.append(1)
            player_sum = sum(player_card_values)

        while player_sum <= 21:
            if player_sum == 21:
                print(f"Dealer's cards: {dealer_cards}")
                print("You win!")
                break
            elif dealer_sum == 21:
                print(f"Dealer's cards: {dealer_cards}")
                print("You lose!")
                break

            hit_or_stand = input("Hit or Stand: ")
            if hit_or_stand == 'h':
                new_card, new_card_value = deal_card()

                player_cards.append(new_card)
                player_card_values.append(new_card_value)

                print("Your cards: ", player_cards)
                player_sum = sum(player_card_values)

                while player_sum > 21:
                    if 11 in player_card_values:
                        player_card_values.remove(11)
                        player_card_values.append(1)
                        player_sum = sum(player_card_values)
                    else:
                        print("You lose.")
                        break

            elif hit_or_stand == 's':
                print(f"Dealer's cards: {dealer_cards}")
                if sum(player_card_values) > sum(dealer_card_values):
                    print("You win!")
                else:
                    print("You lose.")
                break

    else:
        break
