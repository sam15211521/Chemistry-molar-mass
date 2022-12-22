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

#\\\\\ CHEMICAL EQUATION SPECIFIC PART \\\\\\\\\\\


# First equation breaks up string into individual reactants and products
# into a dictionary of reactants or products
def breaking_up_equations(equation):
    reactant_product_dict = {} 
    reactants_and_products = equation.replace(' ', '').split('-->')
    reactant_product_dict['reactants'] = reactants_and_products[0].split('+')
    reactant_product_dict['products'] = reactants_and_products[1].split('+')
    return reactant_product_dict

# second fuction  takes the dictionary from breaking_up_equations and converts
# them into objects in a dictionary 
def separating_reactants_or_products(equation_dictionary, reactant_or_product):
    chemical_dictionary = {} 
    for compound in equation_dictionary[reactant_or_product]:
        chemical = Chemical(compound)
        chemical_dictionary[chemical.determine_formula()] = chemical
    return chemical_dictionary







a = separating_reactants_or_products(
        breaking_up_equations('C + O2 --> CO2 + CO'), 
                            'products'
        )
b = separating_reactants_or_products(
        breaking_up_equations('C + O2 --> CO2 + CO'), 
                            'reactants'
        )

for i in a:
    print (a[i].determine_element_amounts())
print()
for i in b:
    print(b[i].determine_element_amounts())
