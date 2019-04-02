arryList = [5,4663,270000,12,33344,98]



sortedList = sorted(arryList)

def MaxValue(): 
    MaxValue = sortedList[-1]
    print('The MAX Value is {}'.format(MaxValue))     
    
def MinValue(): 
    MinValue = sortedList[0]
    print('The Min Value is {}'.format(MinValue))

def main():
    
    MaxValue()
    MinValue()
    
    
    
