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
    print(termcolor.colored("HunG 0.0.4 [Alpha,29-12-2019|11.40AM]", color="cyan"))
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
    print(
        termcolor.colored(
            """
                                   )  (       
 (   (     )  (   (      )  ( /(  )\   (  
 )\  )\ ( /(  )(  )\  ( /(  )\())((_) ))\ 
((_)((_))(_))(()\((_) )(_))((_)\  _  /((_)
\ \ / /((_)_  ((_)(_)((_)_ | |(_)| |(_))  
 \ V / / _` || '_|| |/ _` || '_ \| |/ -_) 
  \_/  \__,_||_|  |_|\__,_||_.__/|_|\___| 
    """,
            color="yellow",
        )
    )
    write_delay("Variable is the primary way that allows data to be maniputated.\n\n")
    write_delay(
        "In HunG, there are only 2 types of variable which is num and str.\nThe are both declared using the var keyword and the type will be auto-magically assigned from the data.\nFor example:\n"
    )
    print(termcolor.colored("var age = 18", color="cyan"))
    print(termcolor.colored("var name = 'Dai Hung'", color="cyan"))
    write_delay(
        "In Hung programming language, the string or str data type are written in single quotation mark.\n\n"
    )
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


def var_dump(datas):
    for key, data in datas.items():
        es(key, str(data))
    if len(datas.keys()) == 0:
        print("No variable had been initialized")


def main():
    # main program
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

