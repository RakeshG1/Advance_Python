import unittest

def do_addition_1(x=0, y=0):
    '''  
    Do addition x + y
    @param : x - value
    @param : y - value
    '''
    # print(x, y)
    ##### Doing Addition #####
    return x+y

def do_addition_2(x=0, y=0):
    '''  
    Do addition x + y
    @param : x - value
    @param : y - value
    '''
    # print(x, y)
    ##### Knowingly Written Mistake in Code #####
    return x*y    

class ExampleTestCase(unittest.TestCase):
    '''  
    Example Test Case
    '''    
    def test_do_addition_1(self):
        ''' 
        Testing on do_addition_1() function
        '''
        test_x_value = 10
        test_y_value = 20
        self.assertEqual(do_addition_1(test_x_value, test_y_value), 30, "Equal to 30")

    def test_do_addition_2(self):
        ''' 
        Testing on do_addition_2() function
        '''
        test_x_value = 10
        test_y_value = 20
        self.assertEqual(do_addition_2(test_x_value, test_y_value), 30, "Equal to 30")        

if __name__ == "__main__":
    unittest.main(argv=['ignored', '-v'], exit=False)