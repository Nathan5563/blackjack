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
        
        # Return the card and card value of a random choice from the above list
        def deal_card():
            card = random.choice(possible_cards)

            if card == 'A':
                card_value = 11
            elif card == 'J' or card == 'Q' or card == 'K':
                card_value = 10
            else:
                card_value = card

            return card, card_value

        # Player info
        first_card, first_card_value = deal_card()  # Get first player card
        second_card, second_card_value = deal_card()  # Get second player card
        
        player_cards = [first_card, second_card]  # Define list of player cards for display
        player_card_values = [first_card_value, second_card_value]  # Define list of player card values for calculations
        
        player_sum = sum(player_card_values)  # Define sum of player card values

        # Dealer info
        dealer_visible_card, dealer_visible_card_value = deal_card()  # Define visible dealer card
        dealer_hidden_card, dealer_hidden_card_value = deal_card()  # Define hidden dealer card

        dealer_cards = [dealer_visible_card, dealer_hidden_card]  # Define list of dealer cards for display
        dealer_card_values = [dealer_visible_card_value, dealer_hidden_card_value]  # Define list of dealer card values for calculations

        dealer_sum = sum(dealer_card_values)  # Define sum of dealer card values

        # Start game
        print(f"Your cards: {player_cards}")
        print(f"Dealer's first card: {dealer_visible_card}")

        # Check if 'A' should be 11 or 1 based on the sum of player card values
        if player_sum > 21:
            player_card_values.remove(11)
            player_card_values.append(1)
            player_sum = sum(player_card_values)  # Recalculate player sum

        while player_sum <= 21:
            # Check for blackjack
            if player_sum == 21 and dealer_sum == 21:
                print("Tie.")
            elif dealer_sum == 21:
                print(f"Dealer's cards: {dealer_cards}")
                print("You lose.")
                break
            elif player_sum == 21:
                print(f"Dealer's cards: {dealer_cards}")
                print("You win!")
                break

            # If the player has not yet reached nor exceeded 21, hit or stand
            hit_or_stand = input("Hit or Stand: ")
            if hit_or_stand == 'h':
                new_card, new_card_value = deal_card()  # Define the new card and card value

                # Append these values to the player's lists
                player_cards.append(new_card)
                player_card_values.append(new_card_value)

                print("Your cards: ", player_cards)  # Print new list
                player_sum = sum(player_card_values)  # Recalculate player sum

                while player_sum > 21:
                    # If the player has one or more 'A's, modify its value to 1 until the player sum is less than 21
                    if 11 in player_card_values:
                        player_card_values.remove(11)
                        player_card_values.append(1)
                        player_sum = sum(player_card_values)
                    # If the player sum is still greater than 21, player loses
                    else:
                        print("You lose.")
                        break

            elif hit_or_stand == 's':
                print(f"Dealer's cards: {dealer_cards}")
                # Calculate sums and find winner
                if sum(player_card_values) > sum(dealer_card_values):
                    print("You win!")
                elif sum(player_card_values) == sum(dealer_card_values):
                    print("Tie.")
                else:
                    print("You lose.")
                break

    else:
        break
