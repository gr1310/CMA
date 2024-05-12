# def handle_exception(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as ex:
#             exception_report = {
#                 "event": {
#                     "method": func.__name__,
#                     "message": str(ex),
#                     "args": args,
#                     "kwargs": kwargs
#                 }
#             }
#             print('exception_report ', exception_report)

#     return wrapper


# @handle_exception
# def my_method(a, b):
#     try:
#         print('Tried successfully')
#         raise Exception('Error')
#     except Exception as ex:
#         print('Error from my_method', str(ex))
#         raise

# my_method(1,1.0)    

import numpy as np

print(list(np.linspace(0,1,100)))