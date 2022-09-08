def check_string(s):
        return s and s.strip()!=''

def check_float(f):
        try:
                return f and float(f) and float(f)>=0
        except:
                return False

def getParam():
        n, b, s = None, None, None
        n = input("What is the name of the business for this contract?\n")
        while not check_string(n):
                print('business name cannot be empty')
                n = input("What is the name of the business for this contract?\n")

        b = input("What is monthly advertising budget?\n")
        while not check_float(b):
                print('budget needs to be a non-negative number')
                b = input("What is monthly advertising budget?\n")
        b = float(b)
                
        s = input("What is the agreed Digital Advertising Setup fee?\n")
        while not check_float(s):
                print('advertising fee needs to be a non-negative number')
                s = input("What is the agreed Digital Advertising Setup fee?\n")
        s = float(s)
        return n, b, s

                
def calculation():
        n, b, s = getParam()
        fixed_fee = 2500     
        f = fixed_fee + (0.15*b)
        TAR = s+(12*f)
        c = TAR*0.05
        return n, b, s, f, TAR, c
        

def printResults(dataList):             
        total_N = total_b = total_s = total_f = total_TAR = total_c = 0
        
        print("*********\n\nThe Results of Total Revenue and Commission Calculations\n\n*********") #prints heading
        print("{0:20}{1:30}{2:20}{3:20}{4:20}{5:20}{6:20}".format("Name", "Business", "Budget", "Setup Fee", "Mgmt Fee", "Annual Revenue", "Commission"))        
        for row in dataList:
                print("{0:20}{1:<30}{2:<20.2f}{3:<20.2f}{4:<20.2f}{5:<20.2f}{6:<20.2f}".format(row[0], (row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6])))    
                #total_N = str(row[1])
                #total_b += float(row[2])
                #total_s += float(row[3])
                total_f += float(row[4])
                total_TAR += float(row[5])
                total_c += float(row[6])        
       
        print("*********\n\n")        
        print("""The total monthly management fee is \u03A3(f) = ${0:.2f}.
The total annual revenue for all projects is \u03A3(TAR) = ${1:.2f}.
The total comission to all the sales associates is \u03A3(c) = ${2:.2f}.""".format(total_f, total_TAR, total_c))              

def askData(dataList):
        a='init_value'
        while (a.lower().strip()!="q"):
                print('Enter the name of the sales associate')
                sales_name = input()
                if not check_string(sales_name):
                        print('sales associate name cannot be empty')
                        continue
                return_val = calculation()                              # Call getParam/ Calcualtion and unpack the results to 3 variables (n, b, s).
                if not return_val: continue
                n, b, s, f, TAR, c = return_val
                dataList.append([sales_name, n, b, s, f, TAR, c])                 # Add a new data point to data list
                a = input('Press q to quit or press enter to continue entering more data ')
        printResults(dataList)
        return a
      
def load_data(filename='dataListText'):
        """ Load the elements stored in the text file named filename. """
        # Open file to read
        dataList = []
        with open(filename) as f: # f is a file object
                for line in f: # Read each line as text
                        
                        dataList.append(line.split('|')) # Convert to and append to the list   
        return dataList
        
def store_data(dataList, filename='dataListText'):
        """ Allows the user to store data in a list to the text file named filename. """
        with open(filename, 'w') as f: # f is a file object
                for i in dataList:
                        l=len(i)
                        last_value = None
                        for index, data in enumerate(i):
                                f.write(str(data))# Convert integer to string to save
                                if index<l-1:
                                        f.write('|')
                                last_value = data
                        if last_value[-1]!='\n':
                                f.write('\n') # Convert integer to string to save

def main():
        print("\nSales and Sales Associate Commission Tracker by Narottam, Jordana and Taylor")
        nocalc = "\nThere are no calculations to display\nLoad a file or perform new calculations\n"        
        done = False
        while not done:
                cmd = input("""\nMain Menu:\nA)dd to an existing file \nL)oad a file and view data \nP)rint current data\nR)eset and perform new TAR calculations \nS)ave current list to a file \nQ)uit:\n""")
                if cmd.lower() == 'r':
                        dataList = []
                        askData(dataList)
                elif cmd.lower() == 'a':
                        try:
                                askData(dataList)
                        except UnboundLocalError: 
                                print(nocalc)
                elif cmd.lower() == 's': 
                        try:
                                while True:
                                        filename= input('Enter file name. Hit enter for the default file (dataListText)')
                                        if filename and filename!='dataListText':
                                                print("\nThe file doesn't exists\n")
                                        else:
                                                if filename: 
                                                        store_data(dataList, filename)
                                                else: 
                                                        store_data(dataList)
                                                break
                        except UnboundLocalError: 
                                print(nocalc)
                                input("Hit enter to go to the main menu")
                        except: pass
                elif cmd.lower() == 'p':
                        try:
                                printResults(dataList)
                        except UnboundLocalError: 
                                print(nocalc)
                                input("Hit enter to go to the main menu")
                        except: pass
                elif cmd.lower() == 'l':
                        while True:  
                                try:
                                        filename = input('Enter a file name. Hit enter for the default file (dataListText)')
                                        if filename and filename!='dataListText':
                                                print("\nThe file doesn't exists\n")                                        
                                        else:
                                                if filename: dataList = load_data(filename)
                                                else: dataList = load_data()
                                                if dataList: 
                                                        printResults(dataList)
                                                        break
                                except FileNotFoundError:
                                        print("Please provide a valid filename")    
                elif cmd.lower() == 'q':
                        done = True

if __name__ == '__main__':
        main()