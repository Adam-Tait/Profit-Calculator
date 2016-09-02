import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
again = True
while again == True:
    print('--------------------------------------------------------')
    print('Welcome to the Runescape Item Crafting Calculator!')
    print('For help type "help".')
    defaultcolor = Fore.WHITE
    helpcolor = Fore.CYAN
    itemone = input('Cost of the first item: ')
    if itemone == 'help':
        print(helpcolor + 'Enter the price in gold paid for the first component in the crafting recipe. If obtained by you and not bought, enter "0".' + defaultcolor)
        itemone = input('Cost of the first item: ')
    itemtwo = input('Cost of the second item: ')
    if itemtwo == 'help':
        print(helpcolor + 'Enter the price in gold paid for the second component in the crafting recipe. If obtained by you and not bought, enter "0".' + defaultcolor)
        itemtwo = input('Cost of the second item: ')
    finalprice = input('Sell price of final product: ')
    if finalprice == 'help':
        print(helpcolor + 'Enter the price in gold recieved for selling the crafted item.' + defaultcolor)
        finalprice = input('Sell price of final product: ')
    amount = input('How many items to craft: ')
    if amount == 'help':
        print(helpcolor + 'The total amount of items to craft.' + defaultcolor)
        amount = input('How many items to craft: ')
    timetocraft = input('Time to complete (minutes): ')
    if timetocraft == 'help':
        print(helpcolor + 'Enter how long it takes to complete the crafting for the amount of items you have, it will be scaled to one hour which is the standard measurement of profit in runescape.' + defaultcolor)
        timetocraft = input('Time to complete (minutes): ')
    profit = (int(finalprice)*int(amount))-((int(itemone)+int(itemtwo))*int(amount))
    help = False
    if profit > 0:
        color = Fore.GREEN
        gain = ' gain '
    elif profit < 0:
        color = Fore.RED
        gain = ' loss '
    elif profit == 0:
        color = Fore.YELLOW
        gain = ' gain '
    if float(timetocraft) == 0 or timetocraft == None:
        profitmultiplier = 1
        profithour = 'Time not entered'
        itemsperhour = 'Time not entered'
    else:
        profitmultiplier = 60/float(timetocraft)
        profithour = profit*profitmultiplier
        itemsperhour = float(profitmultiplier)*float(amount)
    profitper = profit/int(amount)
    print(defaultcolor + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(defaultcolor + 'You have a net' + str(gain) + 'of: ' + color + str(profit))
    print(defaultcolor + 'You have an hourly net' + str(gain) + 'of: '+ color + str(profithour)+ '/hour') 
    print(defaultcolor + 'You have a' + str(gain) + 'of: '+ color + str(profitper)+ '/item' + defaultcolor)
    if float(timetocraft) == 60:
        print(defaultcolor + 'You are currently doing the amount it takes to make the hourly profit.')
    else:
        print(defaultcolor + 'It would take : ' + color + str(itemsperhour) + defaultcolor + ' items to make the hourly' + str(gain) + 'of ' + color + str(profithour) + defaultcolor)
    repeat = input('Would you like to restart the program? (y/n) ')
    if repeat == 'y' or repeat == 'ye' or repeat == 'yes':
        again = True
    else:
        print('Goodbye!')
        again = False
