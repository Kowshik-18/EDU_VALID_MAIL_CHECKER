"""
Created on TU Sep 15 8:13:34 2020

@author: Kowshik
"""
import os
cwd = os.getcwd()
inputdirectory = cwd + '\INPUT'
if not os.path.isdir(inputdirectory):
    os.mkdir(inputdirectory)

print("######  #####    #      #    ###      ###        #        ###  #       ")
print("#       #     #  #      #    #  #   #   #       # #        #   #       ")
print("#       #     #  #      #    #   # #    #      #   #       #   #       ")
print("######  #     #  #      #    #    #     #     # # # #      #   #       ")
print("#       #     #  #      #    #          #    #       #     #   #       ")
print("#       #     #  #      #    #          #   #         #    #   #       ")
print("######  #####     ######     #          #  #           #  ###  ########")
print("")
print("      _  R V E N C L A W _       ")

print("")
print("")
print("ALWAYS NAME THE FILE YOU WANT TO SEPARATE ONLY EDU MAIL= input.txt")
print("PLACE the input.txt FILE in INPUT DIRECTORY.")
print("ALWAYS NAME THE FILE OUTPUT OF EDU MAIL= edu.txt")
print("PLACE the edu.txt FILE in OUTPUT DIRECTORY.")
print("")


my_file = os.path.join(inputdirectory, 'mix.txt')
directory = cwd + '\OUTPUT'
if not os.path.isdir(directory):
    os.mkdir(directory)
file_path = os.path.join(directory, 'edu.txt')

def initials(combo):
    s = ".edu"
    result = ""
    if combo.find(s) > -1:
        result = combo[combo.index("@")+1:combo.index(":")]
    return result

with open(my_file, "r") as mixfile:
    with open(file_path, "w") as edufile:
        for line in mixfile:
            if '.edu' in initials(line):
                edufile.write(line)



