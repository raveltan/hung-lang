import sys, os

try:
    import termcolor
except:
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """    __  __            ______
   / / / /_  ______  / ____/
  / /_/ / / / / __ \/ / __  
 / __  / /_/ / / / / /_/ /  
/_/ /_/\__,_/_/ /_/\____/   
"""
    )
    print("HunG 0.0.4 [Alpha,29-12-2019|11.40AM]")
    print("Depedency not satisfied, termcolor not found!\n\n")
    print("Should we attempt to perform installation of [Termcolor]?")
    data = input("Y/N >")
    if data.lower() == "y":
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
    import shell

    shell.main()
