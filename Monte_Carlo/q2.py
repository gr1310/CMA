from random import random
import matplotlib.pyplot as plt
import numpy

def handleException(method):
    def decorator(ref, *args, **kwargs):
        try:
            method(ref, *args, **kwargs)
        except Exception as err:
            print(type(err))
            print(err)
    return decorator

class Dice:
    @handleException
    def __init__(self, sides=6):
        try:
            # checking if sides is greater than or equal to 4 or not
            
            if(sides<4):
                raise Exception("Cannot construct the dice")
            
            # if sides>=4
            else:

                # checking if number is integer or float
                if(type(sides)==int):

                    # attribute- numSides
                    self.numSides= sides
                
                # error for float
                else:
                    raise Exception("Cannot construct the dice")
                
        # if input side is str
        except TypeError:
            print("Cannot construct the dice")

        # initializing empty tuple
        # attribute- prob_dist
        self.prob_dist=()

    @handleException
    # Method to assign input tuple to the prob_dist
    def setProb(self, t):

        # checking if numSides matches the number of probabilities inputted
        if(len(t)!=self.numSides):
            raise Exception("Invalid probability distribution")
        
        # To check if all probabilities sum upto 1
        sum_prob= 0
        for x in t:
            sum_prob+=x
        sum_prob=round(sum_prob,2)
        if(sum_prob!=1.00):
            raise Exception("Invalid probability distribution")
        
        # changing value to prob_dist
        self.prob_dist=()
        self.prob_dist+=t

    def __str__(self):

        # to match the format given in the question
        str_req='{'
        if(len(self.prob_dist)>0):
            for t in self.prob_dist:
                str_req+=str(t)
                str_req+=", "
            str_req= str_req[:-2]
        str_req+='}'
        
        return f"Dice with {self.numSides} faces and probability distribution {str_req}"
    
    def roll(self, n):

        actual_data=dict()
        expected_data=dict()

        x_axis=[]

        for x in range(self.numSides):
            # initializing expected values for each face as zero
            expected_data[x+1]=0

            # actual value of each face= probability of occurance of face * number of rolls
            actual_data[x+1]= self.prob_dist[x]*n

            # x_axis
            x_axis.append(x+1)

        for _ in range(n):
            gen_radm_no= random()   #continuous random number between 0 and 1
            
            if(gen_radm_no>=0 and gen_radm_no<self.prob_dist[0]):
                actual_dice_face= 1
            else:
                sum_till_i=self.prob_dist[0]
                for i in range(1,self.numSides):
                    # i=1,2,3,4
                    sum_till_i+=self.prob_dist[i]
                    # mapping value of discrete to continuous interval
                    if(gen_radm_no>=self.prob_dist[i-1] and gen_radm_no<sum_till_i):
                        actual_dice_face= i+1
                        break
            expected_data[actual_dice_face]+=1

        y_actual= actual_data.values()
        y_expected= expected_data.values()
        
        # plotting bar graph
        actual_x_axis= [i-0.1 for i in x_axis]
        plt.bar(actual_x_axis, y_actual, 0.2, label = 'Actual') 
        expected_x_axis= [i+0.1 for i in x_axis]
        plt.bar(expected_x_axis, y_expected, 0.2, label = 'Expected') 
        
        plt.title(f"Outcome of {n} throws of a {self.numSides}-faced dice")
        plt.xlabel("Sides")
        plt.ylabel("Occurances")
        plt.legend() 
        plt.show() 
            
# Test case- 1
        
d= Dice(4)
d.setProb((0.4, 0.2, 0.3, 0.1))
print(d.prob_dist)
print(d)
d.roll(10000)

# Test case- 2
        
# d = Dice(4)
# d.setProb((0.3, 0.1, 0.3, 0.3))
# d.roll(1000)

# Test case- 3
        
# d = Dice(4)
# d.setProb((0.1, 0.2, 0.3, 0.4))
# d.roll(10000)


