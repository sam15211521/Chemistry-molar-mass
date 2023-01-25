dict = {'reactants' : :, 'products' : }

def adding_to_dict(string):
    
    equation_dictionary = string 
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

