import sys, os

try:
    import termcolor
except:
    #Display error if depedency is not satisfied.
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """    __  __            ______
   / / / /_  ______  / ____/
  / /_/ / / / / __ \/ / __  
 / __  / /_/ / / / / /_/ /  
/_/ /_/\__,_/_/ /_/\____/   
"""
    )
    print("HunG 0.1.0 [ BETA , 10-1-2020 | 11.40AM ]")
    print("Depedency not satisfied, termcolor not found!\n\n")
    print("Should we attempt to perform installation of [Termcolor]?")
    data = input("Y/N >")
    if data.lower() == "y":
        #Open an system cli stream and attempt to perform installation
        streams = os.popen(
            "py -m pip install termcolor"
            if os.name == "nt"
            else "python3 -m pip install termcolor"
        )
        stream = streams.readlines()
        result = stream[len(stream) - 1]
        print("\n" + str(result))
        if len(result.split("Successfully installed")) > 1:
            print("Please re-run the program!\n")
            input("Press any key to continue...")
else:
    #Run the main program if there is no problem with depedency.
    import shell
    shell.main()
