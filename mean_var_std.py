import numpy as np

def calculate(list):
    
    # Initialized value
    calculations = dict()
    mean_list = []
    variance_list = []
    standard_deviation_list = []
    max_list = []
    min_list = []
    sum_list = []
    
    # Parameter check
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    # Local array
    local_array = np.array([
        [list[0], list[1], list[2]],
        [list[3], list[4], list[5]],
        [list[6], list[7], list[8]],
    ])

    # Mean
    mean_list.append([val for val in local_array.mean(axis=0)])
    mean_list.append([val for val in local_array.mean(axis=1)])
    mean_list.append(local_array.mean())

    # Variance
    variance_list.append([val for val in local_array.var(axis=0)])
    variance_list.append([val for val in local_array.var(axis=1)])
    variance_list.append(local_array.var())

    # Standard deviation
    standard_deviation_list.append([val for val in local_array.std(axis=0)])
    standard_deviation_list.append([val for val in local_array.std(axis=1)])
    standard_deviation_list.append(local_array.std())

    # Max
    max_list.append([val for val in local_array.max(axis=0)])
    max_list.append([val for val in local_array.max(axis=1)])
    max_list.append(local_array.max())

    # Min
    min_list.append([val for val in local_array.min(axis=0)])
    min_list.append([val for val in local_array.min(axis=1)])
    min_list.append(local_array.min())
    
    # Sum
    sum_list.append([val for val in local_array.sum(axis=0)])
    sum_list.append([val for val in local_array.sum(axis=1)])
    sum_list.append(local_array.sum())
    
    # Ready for return value
    calculations['mean'] = mean_list
    calculations['variance'] = variance_list
    calculations['standard deviation'] = standard_deviation_list
    calculations['max'] = max_list
    calculations['min'] = min_list
    calculations['sum'] = sum_list
    
    return calculations