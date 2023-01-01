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

# this function removes the coeficents from a list of compounds and returns 
# an object of that chemical with the coeficent of the amount 
def remove_coeficients_return_compound_and_coeficent(compound_list): 
    fixed_current_compound = ''
    fixed_compound_and_amount = []
    for compound in compound_list:
        compound_coeficient = ''
        fixed_current_compound = compound
        for symbol in compound:
            if symbol.isalpha():
                break
            else:
                compound_coeficient += symbol
                fixed_current_compound = fixed_current_compound[1:]
        try:
            fixed_compound_and_amount.append(
                [Chemical(fixed_current_compound), int(compound_coeficient)])
        except:
            fixed_compound_and_amount.append(
                [Chemical(fixed_current_compound), 1])
        
    return fixed_compound_and_amount
    #return= [[compound1, amount1], [compound2, amount2]]
    #        [[Chemical object, 4], [chemical object, 2]]




#inputs an equation, outputs a dictionary of reactants and products that with 
#the following format:

# {chemical_compound : [chemical object, integer amount of compound]

def how_many_molecules_of_each_compound(equation):
    global global_reaction_dictionary
    reactant_product_dict = {} 
    reactants_and_products = equation.replace(' ', '').split('-->')

    reactants = reactants_and_products[0].split('+')
    products = reactants_and_products[1].split('+')

    reactants_without_coeficents = (
            remove_coeficients_return_compound_and_coeficent(reactants)
            )

    products_without_coeficents = (
            remove_coeficients_return_compound_and_coeficent(products)
            )

    reactant_product_dict['reactants'] = reactants_without_coeficents 
    reactant_product_dict['products'] =  products_without_coeficents
    
    global_reaction_dictionary = reactant_product_dict
    return reactant_product_dict


def multiply_coeficient_by_subscripts(equation_string):
    equation_dictionary = how_many_molecules_of_each_compound(equation_string)
    element_amounts_reactants= {}
    element_amounts_products = {}
    reactants = equation_dictionary['reactants']
    products = equation_dictionary['products']

    for chemical in reactants:
        compound_elements = chemical[0].determine_element_amounts()
        for element in compound_elements:
            if element not in element_amounts_reactants:
                element_amounts_reactants[eval(f'ele.{element}')] = (
                        compound_elements[element] * chemical[1]
                        )
            else:
                element_amounts_reactants[eval(f'ele.{element}')] = (
                element_amounts_reactants[element] + (
                    compound_elements[element] * chemical[1]
                    )
                )
    for chemical in products:
        compound_elements = chemical[0].determine_element_amounts()
        for element in compound_elements:
            if element not in element_amounts_products:
                element_amounts_products[eval(f'ele.{element}')] = (
                        compound_elements[element] * chemical[1]
                        )
            else:
                element_amounts_products[eval(f'ele.{element}')] = (
                element_amounts_products[element] + (
                    compound_elements[element] * chemical[1]
                    )
                )
    return [element_amounts_reactants, element_amounts_products]
    


global_reaction_dictionary = {}

chemical_equation = '24CO + 12O2 --> CO2 + 2CO'

amount_of_elements_list = multiply_coeficient_by_subscripts(chemical_equation)

for reactant_or_product in amount_of_elements_list:
    for element in reactant_or_product:
        print(element.get_mass())
print(amount_of_elements_list)

print(global_reaction_dictionary)
