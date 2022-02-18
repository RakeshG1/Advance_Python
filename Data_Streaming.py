##### Installing skmultiflow Through Command Line #####
# $ pip install pandas --upgrade
# $ pip install numpy --upgrade
# pip install scikit-multiflow
# pip install scikit-multiflow==0.5.3


##### Running Through Command Line #####
# $ /usr/bin/python3 /Users/rock/Git_Repo/Advance_Python/Data_Streaming.py
# $ /opt/anaconda3/bin/python /Users/rock/Git_Repo/Advance_Python/Data_Streaming.py

##### Importing Packages
import pandas as pd
import numpy as np
import time
import os
from skmultiflow.data.file_stream import FileStream

class Stream_File():
    def __init__(self, csv_file_path):
        ''' 
        Default Constructor
        Args:
            csv_file_path : Path of .csv File
        Returns:
            Save csv file path details to Stream_File class object
        '''
        self.csv_file_path = csv_file_path

    def read_data(self):
        stream = FileStream(self.csv_file_path)
        print("Stream Info --> ", stream.get_data_info())
        return stream

    def stream_csv(self):
        print("--"*20)
        print("Streaming : Started")
        print("--"*20)    
        try:
            stream = self.read_data()
            while(True):
                ##### Stream Through Single Record : Get Next 1 Record
                stream_value = stream.next_sample()
                # print(stream_value) # (array([], shape=(1, 0), dtype=float64), array([1]))
                value_list = stream_value[1] 
                if (len(value_list) < 1):
                    break
                else:
                    value = value_list[0]
                    time_value = time.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Timetsamp : {time_value}, Value : {value}") 
                ##### Stream Through Bulk : Get Next 5 Records
                # stream.next_sample(5)
                ##### Wait Fpr 2 Seconds Before Streaming Next Record
                time.sleep(2)
        except Exception as e:
            print(e)
        finally:
            print("--"*20)
            print("Streaming : Completed")
            print("--"*20)
    

if __name__ == "__main__":
    ##### Csv File Path
    csv_filepath = os.getcwd()+"/Advance_Python/Sample_Data/Sample.csv"
    ##### Creating Stream File Object 
    strm = Stream_File(csv_filepath)
    ##### Calling CSV File Streaming Function 
    strm.stream_csv()


# $ /opt/anaconda3/bin/python xxx/Advance_Python/Data_Streaming.py
# ----------------------------------------
# Streaming : Started
# ----------------------------------------
# Stream Info -->  Sample.csv - 1 target(s), 6 classes
# Timetsamp : 2022-02-18 10:58:22, Value : 1
# Timetsamp : 2022-02-18 10:58:24, Value : 4
# Timetsamp : 2022-02-18 10:58:26, Value : 2
# Timetsamp : 2022-02-18 10:58:28, Value : 6
# Timetsamp : 2022-02-18 10:58:30, Value : 3
# Timetsamp : 2022-02-18 10:58:32, Value : 6
# Timetsamp : 2022-02-18 10:58:34, Value : 3
# Timetsamp : 2022-02-18 10:58:36, Value : 5
# ----------------------------------------
# Streaming : Completed
# ----------------------------------------
# $     