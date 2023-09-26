import re

def reflexive_closure(setA, relation):
    reflexive_sets = set([(x,x) for x in setA])
    closure = set(relation)
    for i in reflexive_sets:
        if(i not in closure):
            closure.add(i)
    
    print("T: ", set( (reflexive_sets) ))
    print("R U T: ", set((closure)))

def symmetric_closure(relation):
    symmetric_sets = set([x[::-1] for x in relation])
    closure = set(relation)
    for i in symmetric_sets:
        if(i not in closure):
            closure.add(i)
    print("R^-1: ", set((symmetric_sets)))
    print("R U R^-1: ", set( (closure) ))

def transitive_closure(relation):
    closure = set(relation)
    while True:
        new_relation = set((x,w) for x,y in relation for q,w in relation if q == y)
        temp_closure = closure | new_relation
        if(temp_closure == closure):
            break
        closure = temp_closure

    print("R^*: ",set((closure)))

input_set = input("Please input the set on the form {1,2,3...}: ")
input_relation = input("Please input the relation on the form {(1,1),(1,2)...}: ")

input_set =  input_set.replace('{','').replace('}','').split(",")
input_relation = [(x.split(',')[0],x.split(',')[1]) for x in re.findall(r'\(([^)]+)\)', input_relation)]
A = set(input_set)
R = set(input_relation)

# use this as a test if you want
# {hej,med,dig}
# {(hej,hej),(dig,med),(med,dig)}
# 
# {1,2,3,4} 
# {(1,1),(1,2),(4,3),(3,2),(2,4)}

print("A: ", set(sorted(A)))

print("R: ", set(sorted(R)))
print("---------------------------------")

reflexive_closure(A,R)
print("---------------------------------")

symmetric_closure(R)
print("---------------------------------")

transitive_closure(R)