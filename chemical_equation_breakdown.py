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


#//////////////////////////////////////////////////////////////////////////////







#//////////////////////////////////////////////////////////////////////////////

# given a string break down the string into a list of compounds and place the 
# resulting two lists into a dictionary with the reactants and products as keys
def chemical_equation_to_compound_dictionary(chemical_equation):
    compound_dict = {}
    reactants_and_products = chemical_equation.replace(" ", "").split('-->')
    compound_dict['reactants'] = reactants_and_products[0].split('+')
    compound_dict['products'] = reactants_and_products[1].split('+')
    return compound_dict

#//////////////////////////////////////////////////////////////////////////////


print(chemical_equation_to_compound_dictionary('CH4 + O2 --> CO2 + H2O'))


a = Chemical("H2O2")
