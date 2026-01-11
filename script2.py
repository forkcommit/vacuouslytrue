print("VACOUS TRUTH\np → q is equivalent to ¬p ∨ q\n        ")#version 0.2
#print("default settings are false for both premise and conclusion")
p = False    # the premise
q = False   # the conclusion
#prompt
print("hello user, welcome\n names for the premise and conition and inputs 0/1 for the following two input requests")
#premise data:name and truth value
stringone=input("name your premise p: ")
i1 = int(input("request1\nEnter truth value for premise p 1 for on and 0 for off: "))
#conclusion data :name and truth value
stringtwo=input("name your conclusion q: ")
i2 = int(input("request2\nEnter truth value for conclusion q 1 for on and 0 for off: "))
#proceessing the int required input to affect the boolean values
#premise bool:
if i1 == 1:
    p = True
elif i1 == 0:
    p = False
else: #INVALID INPUT
    p=False
    print("invalid input for premise, defaulting to False")
#conclusion bool:
if i2 == 1:
    q = True
elif i2 == 0:
    q = False
else: #INVALID INPUT
    q=True
    print("invalid input for conclusion, defaulting to True")
#DISCRETE MATH LOGIC PROCESS:
##topics: implication logic and demorgan's law
implication = (not p) or q  
neg_implication = not implication  
demorgan_result = (p) and (not q)  
#rsults output:
resultprompt = f"the following premise:\n if\n {stringone} given its {p}\n then\n {stringtwo} given its {q}\nis::::::::::::"
print(resultprompt)
print(" implication:", (not neg_implication))  
print("not(p and not q):", not demorgan_result) 
#offer user a chance to connect the puzzle
stringthree=input("what is your conclusion?\n")
#print("bye")        # should match neg_implication
#processing the premise and conclusion to low cab for honest snd high cap for dishonest
if p==True:
    lowcab=stringone.lower()
elif p==False:
    highcap=stringone.upper()
if q==True:
    lowcab=stringtwo.lower()
elif q==False:
    highcap=stringtwo.upper()  
#prmompting a modfied result with the becausing 
print(
    f"\nok\b as for the following premise:\n"
    f" if\n {stringone} given its {p}\n"
    f" then\n {stringtwo} given its {q}\n"
    f"is::::::::::::\n"
    f" implication: {not neg_implication}\n"
    f"not(p and not q): {not demorgan_result}\nbesause: {stringthree.upper()}"
)


