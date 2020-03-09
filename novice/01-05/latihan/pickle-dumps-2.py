
# Python program to illustrate 
#Picle.dumps() 
import pickle 
   
data = [ { 'a':'A', 'b':2, 'c':3.0 } ] 
data_string = pickle.dumps(data) 
print ('PICKLE:', data_string)