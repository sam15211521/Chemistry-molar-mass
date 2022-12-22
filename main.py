from time import sleep
import os
import elements as ele
class Chemical:
    def __init__(self, formula):
        self.formula = formula
        self.element_dict = self.find_elements()
        self.mass  = 0
        
        self.determining_atomic_mass()

    def determine_mass(self):
        return self.mass

    def determine_formula(self):
        return self.formula

    def determine_element_amounts(self):
        return self.element_dict
    
    def update_mass(self, new_mass):
        self.mass = new_mass
        
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    # this function returns a dictionary of all the elements of a chemical formula
    # the input is only the formula with NO spaces
    def find_elements(self):
        element_dict = {}
        current_symbol = ""
        element_amount = 0
        formula_index = 0
        formula = self.formula

        for symbol in formula:
        
# If nothing is in the current symbol, then place the current symbol there
            if current_symbol == "":
                current_symbol = symbol.upper()
                formula_index +=1

# if the symbol is lowercase, add it to the second symbol  
            elif symbol.islower() is True:
                current_symbol += symbol
                formula_index += 1
                 
# if the symbol is a digit, then place it into the element amount. 
# if the previous symbol was a number, then add it to the end of the number 
            elif symbol.isdigit() is True:
                if formula[formula_index-1].isdigit():
                    element_amount = element_amount * 10 + int(symbol)
                else:
                    element_amount += int(symbol)
                formula_index += 1

# if the current symbol is already there and there and the symbol is uppercased
# then place the symbol into current symbol into the dictionary with the element
# amount  
            elif current_symbol !="" and symbol.isupper() is True: 
                # first place the element symbol and the amount of atoms into the element_dict
                if element_amount == 0:
                    element_amount += 1
                if current_symbol in element_dict:
                    element_dict[current_symbol] += element_amount
                else:
                    element_dict[current_symbol] = element_amount

               # then place current symbol as the former symbol, and reset the element amount to 1
                current_symbol = symbol
                element_amount = 0
                formula_index += 1

# if at the end of the formula, then add what you have into the element dict
            if len(formula) == formula_index :
                if element_amount == 0:
                    element_amount = 1
                if current_symbol in element_dict:
                   element_dict[current_symbol] += element_amount
                else:
                    element_dict[current_symbol] = element_amount
                
        self.element_dict = element_dict
        return self.element_dict

#//////////////////////////////////////////////////////////////////////////////
    
    def determining_atomic_mass(self):
        formula_mass = 0
        element_dict = self.element_dict
        for element in element_dict:
            element_string = f"ele.{element}.get_mass()"
            element_mass = eval(element_string)

            total_mass_of_the_element = element_mass * element_dict[element]
            formula_mass += total_mass_of_the_element 
        self.update_mass(formula_mass)


#/

#//////////////////////////////////////////////////////////////////////////////

def classing_formulas(chemical_formula):
    chemical_to_add = Chemical(chemical_formula)

    return chemical_to_add

#//////////////////////////////////////////////////////////////////////////////

def yes_no_choice(statment, statment_check_input = "", yes_choice = "", no_choice = "", statment_return = False):
    while True:

        if statment_return == False:
            return_statment = input(f"\n{statment} \n")
        else:
            return_statment = statment

        while True:
            statment_check = input(
                f"__________\n\n{return_statment}\n\n {statment_check_input} (Y/N)\n"
                )
            if statment_check.upper() == "Y":
                print(yes_choice)
                if statment_return == False:
                    return return_statment
                else:
                    return statment
            elif statment_check.upper() == "N":
                break
            else:
                print(
                        '_______________________\n'
                        'please enter "Y" or "N"'
                        '\n_______________________')
                continue

#///////////////////////////////////////////////////////

def startup():
    welcome = input("""
    Welcome to Chemical Finder!!!!

    Please decide what you want to do.

    1) Find the mass of a chemical formula
    2) Find the mass of a chemical equation
    0) EXIT

    """)

    while welcome != "1" and welcome != "2" and  welcome != "0":
        welcome = input("""
Please enter the number of your choice
    1) Find the mass of a chemical equation
    2) Find the mass of a chemical formula
    0) EXIT

    """)
    return welcome

#////////////////////////////////////////////////////////
    
def enter_equation():
# This part enters the reactants
    reactant_chemical_equation = yes_no_choice(
            statment =(
                "\n\nPlease enter reactants of the chemical equation you want "
                "to analyze\nPlease make sure you use appropriate capitlization"
                "of symbols\n\n"),
            statment_check_input= "do the reactants look correct?")

# This part enters the products

    product_chemical_equation = yes_no_choice(
            statment = (
                "\n\nPlease enter the products of the chemical equation you want to analyze"
                "\nPlease make sure you use appropriate capitlization of symbols\n\n"),
                statment_check_input= "do the products look correct?")


    chemical_equation_final_check = (
            f"\n{reactant_chemical_equation} --> {product_chemical_equation}")
    chemical_equation_return = yes_no_choice(
            statment =(chemical_equation_final_check),
            statment_check_input = (
                "Does the chemical equation look correct \n"
                "Do not worry about if the equation is ballanced"), 
            statment_return = True)

    return chemical_equation_return

#//////////////////////////////////////////////////////////////////////////////
# Allows users to enter a chemical formula to analyze with the 1st choice of the 
# program.

def enter_formula():

    chemical_formula = yes_no_choice(
                statment=(
                    "\n\nPlease enter the chemical formula you want "
                    "to analyze \nPlease make sure you use appropriate capitilization of "
                    "symbols \n\n"), statment_check_input = "Is this the correct formula?" 
                )
    return chemical_formula


#/////////////////////////////////////////////////////////////////////////////
# Allows users to choose what they want to do with the chemical formula just created

def chemical_equation_choice():
    choices = input("""What do you want to do with the equation?
    1) find the mass of each compound
    2) ballance the chemical equation
    3) ballance the chemical equation and find the molar masses of each compound
    4) ballance the chemical equation and launch the stoichiometry app 
    0) Exit the program
    """)
    while True:
        if choices == '1':
            pass
        elif choices == '2':
            pass
        elif choices == '3':
            pass
        elif choices == '4':
            pass
        elif choices == '0':
            exit()
        break

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Here is the start of the programing

os.system('cls')
os.system('clear')
chemical_formula = ''
chemical_equation = ''
function_choice = ""
while True:

    function_choice = startup()
    if function_choice == "1":
        print(
"""\n_______________________\n
starting formula
\n_______________________\n""")
        sleep(1)

        chemical_formula = enter_formula()
        sleep(1)
        os.system('cls')
        os.system('clear')
        print(chemical_formula)
        new_chemical_formula = classing_formulas(
                                chemical_formula = chemical_formula)
        print(
f"\nThe formula mass of {new_chemical_formula.determine_formula()} is:" 
f"{new_chemical_formula.determine_mass()}")
        print(
            """
            
            -_____________________________________________-

            """)

    elif function_choice == "2":
        print(
"""\n_______________________\n
starting equation
\n_______________________\n""")
        sleep(1)

        chemical_equation = enter_equation()        
        sleep(1)
        os.system('cls')
        os.system('clear')
        print(f"""The chemical equation is:
        {chemical_equation}""")
        break

    if function_choice == "0":
        os.system('cls')
        os.system('clear')
        exit()

if function_choice == '2':
    chemical_equation_choice()
