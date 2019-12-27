import sys,os

try: 
    import shell
    shell.main()
except : 
    print('''    __  __            ______
   / / / /_  ______  / ____/
  / /_/ / / / / __ \/ / __  
 / __  / /_/ / / / / /_/ /  
/_/ /_/\__,_/_/ /_/\____/   
''')
    print('HunG 0.0.2 (Early Alpha,26-12-2019:21:51:11)')
    print('Depedency not satisfied, termcolor not found!\n\n')
    print('Should we attempt to perform installation of [Termcolor]?')
    data = input('Y/N >')
    if data.lower() == "y":
        streams = os.popen('py -m pip install termcolor' if os.name == 'nt' else 'python3 -m pip install termcolor')
        stream = streams.readlines()
        result = stream[len(stream)-1]
        print('\n'+str(result))
        if len(result.split('Successfully installed')) > 1:
            input('Press any key to continue...')
            os.system('python3 main.py')

