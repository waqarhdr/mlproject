'''The sys module is a built-in module in Python that provides access to various system-specific parameters and functions. 
It's a crucial module for interacting with the Python interpreter and environment.'''

import sys
# import logging

# Function which will give you the details about the error  
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line_number[{1}] error_message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


# # To test the exception handling
#     if __name__=="__main__":
#         try:
#             a=1/0
#         except Exception as e:
#             logging.info("Devide by zero")
#             raise CustomException(e,sys)    

