# given a string break down the string into a list of compounds and place the 
# resulting two lists into a dictionary with the reactants and products as keys
def chemical_equation_to_compound_dictionary(chemical_equation):
    compound_dict = {}
    reactants_and_products = chemical_equation.replace(" ", "").split('-->')
    compound_dict['reactants'] = reactants_and_products[0].split('+')
    compound_dict['products'] = reactants_and_products[1].split('+')
    return compound_dict

# given a list of compounds, return a ditionary of {"formula" : chemistry object}




print(chemical_equation_to_compound_dictionary('CH4 + O2 --> CO2 + H2O'))
