# import numpy

# # print(type(numpy.arange(5)))

# # txt="hHI"
# # print(txt.lower())

# # print([None]*4)

# def handleError(method):
#     def decorator(ref, *args, **kwargs):
#         try:
#             method(ref, *args,**kwargs)
#         except Exception as err:
#             print(type(err))
#             print(err)
#     return decorator

# n=0

# class Check:
#     @handleError
#     def __init__(self,n):
#         self.n= n
#         if(self.n==0):
#             raise Exception("Cannot be zero")
#     @handleError
#     def check(self):
#         if(self.n==0):
#             raise Exception("Cannot be zero")
#     # def check1(self):
#     #     if(self.n==0):
#     #         raise Exception("Cannot be zero")

# # check(n)


# n1= Check(n)
# print(type(n1))
# n1.check()
# # new.check1()

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()
print(fig)
print(ax)

ax.plot(x, y, linewidth=2.0)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

x = np.arange(8)
print(x)