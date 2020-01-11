import lexer, hung_parser, interpreter
import sys, os
import termcolor
from time import sleep

# helper functions

def write_delay(text):
    for char in text:
        sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()


def es(name, desc):
    SPACING = 20 - len(name)
    print(name + " " * SPACING + "| " + desc)


def print_help():
    es(".debug", "Show a verbose log of the interpreter.")
    es(".vardump", "Dump the variable symbol table to the terminal.")
    es(".clear", "Clear the terminal window.")
    es(".exit", "Exit the HunG interpreter.")
    es(".version", "Show the version of the HunG interpreter.")
    es(".started", "Show the getting started guide of HunG.")
    es(".help", "Show this dialog")


def title():
    print(
        termcolor.colored(
            """    __  __            ______
   / / / /_  ______  / ____/
  / /_/ / / / / __ \/ / __  
 / __  / /_/ / / / / /_/ /  
/_/ /_/\__,_/_/ /_/\____/   
""",
            color="cyan",
        )
    )
    print(termcolor.colored("HunG 0.1.0 [ BETA , 10-1-2020 | 11.40AM ]", color="cyan"))
    print(f"Running on top of Python {sys.version}\nUse .help to view help page\n")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def getting_started():
    clear_screen()
    print(
        termcolor.colored(
            """
     (  (           (                        
 )\))(   '   (  )\             )      (  
((_)()\ )   ))\((_) (   (     (      ))\ 
_(())\_)() /((_)_   )\  )\    )\  ' /((_)
\ \((_)/ /(_)) | | ((_)((_) _((_)) (_))  
 \ \/\/ / / -_)| |/ _|/ _ \| '  \()/ -_) 
  \_/\_/  \___||_|\__|\___/|_|_|_| \___| 
    """,
            color="yellow",
        )
    )
    write_delay("Welcome to getting started with HunG\n\n")
    write_delay("I'm going to explain everything you need to know about HunG.\n")
    write_delay(
        "HunG is an interpreted language that is build on top of python3,\nit is created in order to facilitate people who are getting started with programming.\nIt is also created to be as simple as possible in order to achieve this.\n\n"
    )
    input("Press enter to continue...")
    clear_screen()
    print('Variable & Data Types.')
    print("Variable is the primary way that allows data to be maniputated.\n\n")
    print(
        "In HunG, there are only 2 types of variable which is num and str.\nThe are both declared using the var keyword and the type will be auto-magically assigned from the data. Currently the only data type which is already implemented is num, in HunG num apply for both integer and float, also the implementation of booleans are done in num (True is 1.0 and False is 0.0).\nFor example:\n"
    )
    print(termcolor.colored("var age = 18", color="cyan"))
    print(termcolor.colored("var name = 'Dai Hung'", color="cyan"))
    print(termcolor.colored("var isMan = 1.0", color="cyan"))
    print(
        "In Hung programming language, the string or str data type are written in single quotation mark.\n\n"
    )
    input("Press enter to continue...")
    print('\nComparator Operator')
    print('In HunG, the are mainly 3 comparator operator which are greater(>),smaller(<),and equal to(:). There are no greater and equal or smaller and equal, these functionality can be achieved by using bitwise operation. There are 3 bitwise operation that is currently supported by hung, which is NOT(!),AND(&),and OR(|).\n\nThese are the implementation of those operators')
    print(termcolor.colored("19 > 10 , will result in 1.0", color="cyan"))
    print(termcolor.colored("19:10 , will result in 0.0", color="cyan"))
    print(termcolor.colored("19>10 & 10>5 , will result in 1.0", color="cyan"))
    print(termcolor.colored("(10:100)+5 > 1 , will result in 1.0", color="cyan"))

    input("Press enter to continue...")
    print('\nConditional Statements')
    print('In HunG there are currently 1 way of doing conditional staements which is by the "THEN"(~) statemens, this statement can be stacked in order to achieve branching capabilities.')
    print('The structure is CONDITION ~ RESULT')
    print('The condition is anything that will result in 1.0 or 0.0 (Boolean)')
    print('\nThe example of the implementation:')
    print('10<12~20 , this will result in 20')
    print('We can also do else statements')
    print('(10<5~5):0~10 , will result in 10 as 10 is not smaller than 5')
    input("Press enter to continue...")

    # end of getting started
    clear_screen()
    print(
        termcolor.colored(
            """
 (                         
 )\ )                      
(()/(                 (    
 /(_))   (    (      ))\   
(_))_    )\   )\ )  /((_)  
 |   \  ((_) _(_/( (_))    
 | |) |/ _ \| ' \))/ -_) _ 
 |___/ \___/|_||_| \___|(_)
                           
    """,
            color="yellow",
        )
    )
    input("Press enter to return to interpreter...")
    clear_screen()
    title()

#Dump all variable with it's value to the terminal
def var_dump(datas):
    for key, data in datas.items():
        es(key, str(data))
    if len(datas.keys()) == 0:
        print("No variable had been initialized")


def main():
    # main program
    #create a symbol table for the HunG.
    symbol_table = interpreter.SymbolTable()
    debug = False
    running = True
    clear_screen()
    title()
    while running:
        data = input(termcolor.colored("HunG> ", color="cyan"))
        if data == ".clear":
            clear_screen()
            continue
        elif data == ".exit":
            running = False
            continue
        elif data == ".debug":
            debug = not debug
            print(f'Verbose output is {"on" if debug else "off"}!')
            continue
        elif data == ".help":
            print_help()
            continue
        elif data == ".version":
            title()
            continue
        elif data == ".started":
            getting_started()
            continue
        elif data == ".vardump":
            var_dump(symbol_table.dump())
            continue
        l = lexer.Lexer(data, "<HunGConsole>").get_tokens()
        if l[0] == None:
            print(l[1])
        else:
            if debug:
                print("Tokens: ", l[0])
            p = hung_parser.Parser(l[0], "<HunGConsole>", data).parse()
            if p[0] == None:
                print(p[1])
            else:
                if debug:
                    print("AST: ", p[0])
                i = interpreter.Interpreter(
                    p[0], "<HunGConsole>", data, symbol_table
                ).interpret()
                print(i)

