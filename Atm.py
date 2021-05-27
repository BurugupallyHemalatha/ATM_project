print('welcome to tech_worldh bank ATM')
restart = 'Y'
chances = 3
balance = 1500.90
while chances >= 0:
    pin = int(input('please Enter Your 4 Digit Pin:'))
    if pin == 1234:
        print('You Entered Your Pin Correctly')
        print('Please Press 1 For Your Balance')
        print('Please Enter 2 To Make a Withdrawl')
        print('Please Press 3 To Pay in')
        print('Please Press 4 To Return Card\n')
        while restart not in ('n', 'no', 'NO', 'N'):
            option = int(input('What Would You Like To Choose?:'))
            if option == 1:
                print('Your Balance is $', balance)
                restart = input('Would You Like To Go Back?')
                if restart in ('no', 'NO', 'N', 'n'):
                    print('Thank You From tech_worldh'+"\U0001f600")
                    break
                elif option == 2:
                    option2 = 'Y'
                    withdrawl = float(input('How Much Would You Like TO withdraw? 30,40,50,100 for other enter 1:'))
                    if withdrawl in [10, 20, 40, 60, 80, 100]:
                        balance = balance-withdrawl
                        print('\nYour Balance is now $', balance)
                        restart = input('Would You Like To Go Back?')
                        if restart in ('no', 'NO', 'N', 'n'):
                            print('Thank You From tech_worldh' + "\U0001f600")
                            break
                        elif withdrawl != [10, 20, 40, 60, 80, 100]:
                            print('Invalid Amout, Please Re-try\n')
                            restart = 'Y'
                        elif option == 1:
                            withdrawl = float(
                                input('please Enter Desired Amount:'))
                        elif option == 3:
                            Pay_in = float(input('How Much Would You Like TO Pay In?'))
                            balance = balance + Pay_in
                            print('\nYour Balance is now $', balance)
                            restart = input('Would You Like To Go Back?')
                            if restart in ('no', 'NO', 'N', 'n'):
                                print('Thank You From tech_worldh' + "\U0001f600")
                                break
                            elif option == 4:
                                print(' Please Wait  your card is Retuned....\n')
                                print('Thank You for Your service From tech_worldh' + "\U0001f600")
                                break
                            else:
                                print('please Enter a correct number.\n')
                                restart = 'Y'
                        elif pin != '1234':
                            print('Incorrect Password')
                            chances = chances - 1
                            if chances == 0:
                                print('\nNo more tries')
                                break
