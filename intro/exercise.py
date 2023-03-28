# shorter approach

def takeHome():

    income = int(input("Enter the annual income: "))
    state = input("Enter the state to calculate tax: ")
    stateTax = {'AR':22, 'CA':25.5, 'NJ':28, 'TX':27, 'NY':30}

    # calculating federal tax
    income = income - (income * 0.10)

    if state in stateTax:
        netIncome = income - (income * stateTax[state] / 100)
        print("Your net income after all the taxes is: " ,netIncome)
        return netIncome
    else:
        print("State not in the list")
        return None


takeHome()

'''
def takeHome():

    income = int(input("Enter the annual income: "))
    state = input("Enter the state to calculate tax: ")
    stateTax = {'AR':22, 'CA':25.5, 'NJ':28, 'TX':27, 'NY':30}
    federalTax = 10

#As dictionary is not ordered, it can't be accessed with declaration like stateTax[0]
    if state == 'AR':
        netIncome = income - (income * stateTax['AR']/100)
    elif state == 'CA':
        netIncome = income - (income * stateTax['CA']/100)
    elif state == 'NJ':
        netIncome = income - (income * stateTax['NJ']/100)
    elif state == 'TX':
        netIncome = income - (income * stateTax['TX']/100)
    elif state == 'NY':
        netIncome = income - (income * stateTax['NY']/100)
    else:
        print("your state is not listed")
        return 0

    netIncome = netIncome - (netIncome/10)
    print("Your net income after all deductions is: " ,netIncome)


takeHome()

'''