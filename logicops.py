# if an applicant has good credit and good income

has_good_income = True 
has_good_credit = True

if has_good_income and has_good_credit:
    print("GIVE US YOUR MONEY")
else:
    print('YOU SUCK')

has_good_income = False 
has_good_credit = False

if has_good_income or has_good_credit:
    print("GIVE US YOUR MONEY")
else:
    print('YOU SUCK')