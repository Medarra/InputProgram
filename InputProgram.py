"""
Assignment 3.
"""
from datetime import datetime, date
import math
import sys

#These variables are preliminary so as to make the following program work.
female = ('female', 'She', 'was', 'her')
male = ('male', 'He', 'was', 'his')
non_binary = ('non-binary', 'They', 'were', 'their')
sex = {'F' : female, 'M'  : male, 'NB' : non_binary}
current_day = datetime.today()
BIRTH_FORMAT = '%Y-%m-%d'
creator_name = ('Aly', 'Alysse', 'Alysse P', 'Alysse Palmer')
creator_date = date(1995, 8, 3)

def main():

    """
    Information Statement Program:
    Takes several inputs from program user, and outputs a statement relaying the
    information back.

    """


    #These variables are inputted by the users of the program and then checked
    #for validity and if perhaps they are the same as the programmer.
    name = input('Please enter your name.').title()
    if name in creator_name:
        print("What a fantastic name you have. I approve.")
    else:
        print(f'{name} is a pretty good name, but not as great as Aly.')
    gender = input('Please enter your gender identity. (F/M/NB)').upper()
    if gender in sex:
        print("You chosen pronouns have been accepted.")
    else:
        sys.exit("Please format your identity as (F/M/NB) and run this again.")
    date_of_birth_string = input('What is your date of birth. (YYYY-mm-dd)')
    try:
        date_of_birth = datetime.strptime(date_of_birth_string, BIRTH_FORMAT)
    except ValueError:
        sys.exit("You did not format your birthday as required. Please try again.")
    if date_of_birth == creator_date:
        print("Wow, you were born on the same day as a true genius. Well done.")
    elif int(date_of_birth.year) > 2000:
        print("Wow, you weren't even around at the end of the last century.")
    else:
        print("Wow, you saw the end of last century you old fart.")
    place_of_birth = input('Where were you born?').title()
    try:
        sin_number = int(input('What is your SIN #?'))
    except ValueError:
        sys.exit('That can not be your Sin #. Please re-run this and try again.')

    #These are variables unique to the inputs the user put in.
    gender_list = sex[gender]
    age_delta = current_day - date_of_birth
    age_in_days = age_delta.days
    age = str(math.floor(age_in_days / 365.25))

    #ending statement of the program.
    print(f'{name} is a {age} year old {gender_list[0]}. {gender_list[1]} '
          f'{gender_list[2]} born in {place_of_birth} and {gender_list[3]} '
          f'SIN # is {sin_number}')

if __name__ == '__main__':
    main()
