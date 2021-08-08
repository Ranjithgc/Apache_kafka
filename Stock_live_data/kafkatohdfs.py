"""
@Author: Ranjith G C
@Date: 2021-08-07
@Last Modified by: Ranjith G C
@Last Modified time: 2021-08-07 
@Title : Program Aim is to work with Hadoop commands.
"""
import subprocess

def run_cmd(args_list):
        """
        Description:
                run linux commands.
        Parameter: 
                it takes args_list as parameter.
        Return:
                it returns s_return, s_output, s_err.
        """
        print('Running system command: {0}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return =  proc.returncode
        return s_return, s_output, s_err 

if __name__ == "__main__":
    #Run Hadoop mkdir command in python
    #mkdir = run_cmd(['hdfs', 'dfs', '-mkdir', '-p', '/kafka_stock_data1'])

    #Run Hadoop put command in Python
    abc = run_cmd(['hdfs', 'dfs', '-copyFromLocal', '/home/ubunta/Desktop/Kafka/Stock_live_data/stock.txt', '/kafka_stock_data1'])
