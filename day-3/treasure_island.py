print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

art = r"""

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           '.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
"""
print(art)

user_input = input("left or right? ")
if user_input == 'right':
    print("Fall into a hole.\nGame Over.")
else:
    user_input = input("swim or wait? ")
    if user_input == 'swim':
        print("Attacked by trout.\nGame Over")
    else:
        user_input = input('Which door? ')
        if user_input == 'red':
            print('Burned by fire\n. Game Over.')
        elif user_input == 'yellow':
            print('You Win')
        elif user_input == 'blue':
            print('Eaten by beasts\nGame Over')
        else:
            print('Game Over')