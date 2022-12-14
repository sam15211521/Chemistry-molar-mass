import elements as ele
def determining_atomic_mass(element_dic):
    formula_mass = 0

    for element in element_dic:
        element_string = f"ele.{element}.get_mass()"
        element_mass = eval(element_string)

        total_mass_of_the_element = element_mass * element_dic[element]
        formula_mass += total_mass_of_the_element 
    return formula_mass

print(determining_atomic_mass({'H' : 2, 'O' : 1}))
        
#print(ele.H.get_mass())
