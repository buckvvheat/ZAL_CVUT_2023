def sortNumbers(data, condition:str):
    if condition == 'ASC':
        for i in range(len(data)):
            for k in range(len(data)-i-1):
                if data[k+1] < data[k]:
                    data[k+1], data[k] = data[k], data[k+1]
        return data
    elif condition == 'DESC':
        for i in range(len(data)):
            for k in range(len(data)-i-1):
                if data[k+1] > data[k]:
                    data[k+1], data[k] = data[k], data[k+1]
        return data
 
 
def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError('Invalid input data')
     
    temporaryList = []
    for i in range(len(weights)):
        temporaryList.append([weights[i], data[i]])
     
    if condition == 'ASC':
        for i in range(len(temporaryList)):
            for k in range(len(temporaryList)-i-1):
                if temporaryList[k+1][0] < temporaryList[k][0]:
                    temporaryList[k+1], temporaryList[k] = temporaryList[k], temporaryList[k+1]
 
    elif condition == 'DESC':
        for i in range(len(temporaryList)):
            for k in range(len(temporaryList)-i-1):
                if temporaryList[k+1][0] > temporaryList[k][0]:
                    temporaryList[k+1], temporaryList[k] = temporaryList[k], temporaryList[k+1]
    result = []
    for i in range(len(temporaryList)):
        result.append(temporaryList[i][1])
 
    return result