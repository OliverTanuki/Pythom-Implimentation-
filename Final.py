
# Code by Oliver Suares
# Data collection final project
#
#
#
#



import pandas as pd
import numpy as np



class funct:

   
   #Format the list into an array of arrays which contain single word elements
    def formatList(list):
        act = []
        b = []


        for a in list:
            a[0] = a[0].lower()
            b = a[0].split( )
            
            act.append(b)
        


        return act


    #Function to find the number of occurances of each value
    def findItems(list, file):
        values = []
        act = []
        
        for a in list:

            for b in a:
                found = 0
                file.write(b +" ")

                if len(act) == 0:
                    act.append(b)
                    values.append(1) 

                for x in act:
                    if b == x:
                        values[act.index(x)]+=1
                        found = 1
                        break
                    
                if found == 0:
                    act.append(b)
                    values.append(1) 

                    


                
        final = [[act[i],values[i]] for i in range(len(act))]
        return final

    #Filter the larger list into a smaller one by using a specified benchmark

    def frequentWord(list, bench):

        act = []

        for (word, value) in list:
            #Check if the value reaches the required benchmark
            if value >= bench:
                
                act.append((word, value))
        return act




            



   
class main():

    #Read in the designated file
    data = pd.read_csv("imdb_top_1000.csv")
    fullL = open("fullList.txt", "a")

    #Format into the frame
    df = pd.DataFrame(data, columns=['Series_Title'])
    
    #Convert to a string array
    df = df.to_numpy(dtype=str)
    
    


    dft = funct.formatList(df)
   


    dft = funct.findItems(dft, fullL)
    
    


    dft = funct.frequentWord(dft, 5)

    for x in dft:
        print(x)
    

    
