'''
Put list of card and value in the while loop
use if to determine h or s
use if to determine if the value is >, = or < than 21
use continue to ignore all the follow code if anyone wins
'''
import random
while True:
    cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
    values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]
    print('================================ RESTART ================================')
    num1 = random.randint(0,len(values))
    cards.remove(cards[num1])
    values.remove(values[num1])
    num2 = random.randint(0,len(values))
    cards.remove(cards[num2])
    values.remove(values[num2])
    print('Players hand: [',cards[num1],',',cards[num2],'] is worth',values[num1]+values[num2])
    if values[num1]+values[num2]== 21:
        print('Player got 21! Backjack!\nPlayer Wins!')
        continue
    answer = input('(h)it or (s)tand?')
    if answer == 'h':
        num = random.randint(0,len(values))
        cards.remove(cards[num])
        values.remove(values[num])
        print('You drew',cards[num])
        print('Players hand: [',cards[num1],',',cards[num2],',',cards[num],'] is worth',values[num1]+values[num2]+values[num])
        if values[num1]+values[num2]+values[num] == 21:
            print('Player got 21! Backjack!\nPlayer Wins!')
        elif values[num1]+values[num2]+values[num] >= 21:
            print('Bust!\nComputer Wins!')    
        else:
            answer = input('(h)it or (s)tand?')
            if answer == 'h':
                num3 = random.randint(0,len(values))
                cards.remove(cards[num3])
                values.remove(values[num3])
                print('You drew',cards[num3])
                print('Players hand: [',cards[num1],',',cards[num2],',',cards[num],cards[num3],'] is worth',values[num1]+values[num2]+values[num]+values[num3])
                if values[num1]+values[num2]+values[num]+values[num3] == 21:
                    print('Player got 21! Backjack!\nPlayer Wins!')
                elif values[num1]+values[num2]+values[num]+values[num3]>= 21:
                    print('Bust!\nComputer Wins!')
            else:
                comp1 = random.randint(0,len(values))
                cards.remove(cards[comp1])
                values.remove(values[comp1])
                comp2 = random.randint(0,len(values))
                cards.remove(cards[comp2])
                values.remove(values[comp2])
                print('Computers hand: [',cards[comp1],',',cards[comp2],'] is worth',values[comp1]+values[comp2])
                if values[comp1]+values[comp2]==21:
                    print('Computer Wins, BlackJack')
                    continue
                elif values[comp1]+values[comp2]>values[num1]+values[num2]:
                    print('Computer Wins!')
                    continue
                else:
                    comp3 = random.randint(0,len(values))
                    cards.remove(cards[comp3])
                    values.remove(values[comp3])
                    print('Computer drew',cards[comp3])
                    print('Computers hand: [',cards[comp1],',',cards[comp2],cards[comp3],'] is worth',values[comp1]+values[comp2]+values[comp3])
                    if values[comp1]+values[comp2]+values[comp3]==21:
                        print('Computer Wins, BlackJack')
                        continue
                    elif values[comp1]+values[comp2]+values[comp3]>values[num1]+values[num2]:
                        print('Computer Wins!')
                        continue
                    elif values[comp1]+values[comp2]+values[comp3]>21:
                        print('Bust!\nPlayer Wins')
                    else:
                        comp4 = random.randint(0,len(values))
                        cards.remove(cards[comp4])
                        values.remove(values[comp4])
                        print('Computer drew',cards[comp4])
                        print('Computers hand: [',cards[comp1],',',cards[comp2],cards[comp3],cards[comp4],'] is worth',values[comp1]+values[comp2]+values[comp3]+values[comp4])
                        if values[comp1]+values[comp2]+values[comp3]+values[comp4]==21:
                            print('Computer Wins, BlackJack')
                            continue
                        elif values[comp1]+values[comp2]+values[comp3]+values[comp4]>values[num1]+values[num2]:
                            print('Computer Wins!')
                            continue
                        elif values[comp1]+values[comp2]+values[comp3]+values[comp4]>21:
                            print('Bust!\nPlayer Wins')
                            continue
    else:
        comp1 = random.randint(0,len(values))
        cards.remove(cards[comp1])
        values.remove(values[comp1])
        comp2 = random.randint(0,len(values))
        cards.remove(cards[comp2])
        values.remove(values[comp2])
        print('Computers hand: [',cards[comp1],',',cards[comp2],'] is worth',values[comp1]+values[comp2])
        if values[comp1]+values[comp2]==21:
            print('Computer Wins, BlackJack')
            continue
        elif values[comp1]+values[comp2]>values[num1]+values[num2]:
            print('Computer Wins!')
            continue
        else:
            comp3 = random.randint(0,len(values))
            cards.remove(cards[comp3])
            values.remove(values[comp3])
            print('Computer drew',cards[comp3])
            print('Computers hand: [',cards[comp1],',',cards[comp2],cards[comp3],'] is worth',values[comp1]+values[comp2]+values[comp3])
            if values[comp1]+values[comp2]+values[comp3]==21:
                print('Computer Wins, BlackJack')
                continue
            elif values[comp1]+values[comp2]+values[comp3]>values[num1]+values[num2]:
                print('Computer Wins!')
                continue
            elif values[comp1]+values[comp2]+values[comp3]>21:
                print('Bust!\nPlayer Wins')
            else:
                comp4 = random.randint(0,len(values))
                cards.remove(cards[comp4])
                values.remove(values[comp4])
                print('Computer drew',cards[comp4])
                print('Computers hand: [',cards[comp1],',',cards[comp2],cards[comp3],cards[comp4],'] is worth',values[comp1]+values[comp2]+values[comp3]+values[comp4])
                if values[comp1]+values[comp2]+values[comp3]+values[comp4]==21:
                    print('Computer Wins, BlackJack')
                    continue
                elif values[comp1]+values[comp2]+values[comp3]+values[comp4]>values[num1]+values[num2]:
                    print('Computer Wins!')
                    continue
                elif values[comp1]+values[comp2]+values[comp3]+values[comp4]>21:
                    print('Bust!\nPlayer Wins')
            
