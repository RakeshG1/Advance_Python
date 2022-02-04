import os
import time 

##### Log File Path #####
logfile_path = os.getcwd()+"/Advance_Python/Logs/Datalog.log"
# print(logfile_path)
file_read_mode = "r"

class With_Example():
    '''  
    Context Manager : with
    When you use 'with' statement with open function, you do not need to close the file at the end, because 'with' would automatically close it for you
    '''
    def __init__(self, logfile_path=''):
        ''' 
        Intialises the object of class[Context_Manager_Example]
        @param: self(object specific parameter)
        @param: logfile_path(logfile path)(default = '')
        '''
        self.logfile_path = logfile_path

    def read_log_data(self):
        ''' 
        https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters
        Operates Log File Using ContextManager[with] & Exception Handling
        @param: self(object specific parameter)
        '''
        with open(self.logfile_path) as f:
            for row in f.readlines():
                try :
                    if "----" in row:
                        raise Exception("raise exception due to --> special characters : '--------'")                
                    if "Message_6" in row:
                        print(row)       
                except Exception as error:
                    print("Error is %s" % (error))                        
                    pass 
                    ''' 
                    'pass' statement simply does nothing. 
                    We can use 'pass' statement when we want to create a method that we didn't wrote implementation logic, yet.
                    Where 'continue' statement skip all the remaining statements in the loop and goes back to the starting of the loop
                    '''
        print("Is file closed after with block of code ? :", f.closed)


class Open_Example():
    '''  
    When you use just 'open' function without with statement, you need to close the file at the end, because just 'open' would not automatically close it for you
    '''
    def __init__(self, logfile_path='', mode=''):
        ''' 
        Intialises the object of class[Context_Manager_Example]
        @param: self(object specific parameter)
        @param: logfile_path(logfile path)(default = '')
        '''
        self.logfile_path = logfile_path
        self.mode = mode

    def read_log_data(self):
        ''' 
        https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters
        Operates Log File Using ContextManager[with] & Exception Handling
        @param: self(object specific parameter)
        '''
        f = open(self.logfile_path, self.mode)
        for row in f.readlines():
            try:
                if "----" in row:
                    raise Exception("raise exception due to --> special characters : '--------'")
                if "Message_6" in row:
                    print(row)                    
            except Exception as error:
                print("Error is %s" % (error))                        
                pass    
            finally:
                f.close()
        print("Is file closed after try-catch-finally blocks ? : {}".format(f.closed)) 


if __name__ == "__main__":
    print("*********************************************************")
    print("********* Using[With-Context Manager] : Started *********")
    print("*********************************************************")
    context_mang = With_Example(logfile_path)
    context_mang.read_log_data()
    print("*********************************************************")
    print("********* Using[With-Context Manager] : Stopped *********")
    print("*********************************************************")
    print("\n")
    print("**************************************************")
    print("********* Using[Open-Operator] : Started *********")
    print("**************************************************")
    context_mang = Open_Example(logfile_path, file_read_mode)
    context_mang.read_log_data()
    print("**************************************************")
    print("********* Using[Open-Operator] : Stopped *********")    
    print("**************************************************")