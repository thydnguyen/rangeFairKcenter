# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:00:42 2022

@author: Thy Nguyen
"""
from time import time as time
import numpy as np
from scipy.spatial import distance
from kcenter import HeuristicA, fairKcenterRange
from baseline import HeuristicB
from copy import deepcopy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("numIter", type = int, help = "Number of iterations for taking average")
parser.add_argument("alpha", type = float, help = "Lower bound percentage of points selected as centers for each group")
parser.add_argument("beta", type = float, default = None, help = "Upper bound percentage of points selected as centers for each group")
parser.add_argument("K", type = float, help = "Number of centers as a fraction of the dataset")
parser.add_argument("algorithm", type = str, help = "Selected fair k-centers algorithm")
parser.add_argument("path" , type = str, help = "Path to the dataset")
parser.add_argument('--largeFirst', action='store_true')


args = parser.parse_args()

numIter = args.numIter
alpha = args.alpha
beta = args.beta
K_percent = args.K
algorithm = globals()[args.algorithm]
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
PATH = script_dir + args.path

def evaluate(X,C):
  low = 0
  high = X.shape[0]
  batch = 1000
  result = 0
  while low < high:
      end = min(low + batch, high)
      tmp = max(np.min(distance.cdist(X[low:end], X[C]), axis = 1))
      result = max(result, tmp)
      low = end
  return result

def wrapper(iterN, func, *args):
    totalTime = []
    totalLoss = [] 
    for i in range(iterN):
        ARGS = deepcopy(args)
        start = time()
        C = func(*ARGS)
        elapse = time() - start
        loss = evaluate(ARGS[0], np.array(C).astype(int))
        # if not np.array_equal(args[2] , np.unique(np.array(args[1])[C], return_counts=True)[1]):
        #     print("Required:",args[2] )
        #     print("Got", np.unique(np.array(args[1])[C], return_counts=True)[1])
        #     print("Fairness not satisfied")
        totalLoss.append(loss)
        totalTime.append(elapse)
    return totalLoss, totalTime

def wrapperRange(iterN, func, *args):
    totalTime = []
    totalLoss = [] 
    for i in range(iterN):
        ARGS = deepcopy(args)
        start = time()
        C = func(*ARGS)
        elapse = time() - start
        loss = evaluate(ARGS[0], np.array(C, dtype= object).astype(int))
        countResult = np.unique(np.array(args[1])[C], return_counts=True)[1]
        #print(countResult)
        # if not all(countResult <= np.array(args, dtype = object)[2]) and all(countResult >=np.array(args, dtype = object)[3]):
        #     print("Fairness not satisfied")
        totalLoss.append(loss)
        totalTime.append(elapse)
    return totalLoss, totalTime

    
'''
Load the data from the npz file and set up the constraint vector to make sure the representation of each group
in the chosen centers to be approximately equal
'''
def test_file(PATH):
    data = np.load(PATH)
    X = data['x']
    classTable  = data['y']
    k = int(np.ceil(len(X) * K_percent))
    _, count = np.unique(data['y'], return_counts=True)
    constraints = np.array([int(np.ceil(k * c* alpha/ len(X) )) for c in count])
    lowerbound = np.copy(constraints)
    if beta!= -1:
        upperbound = np.array([int(np.ceil(k * c* beta/ len(X) )) for c in count])
    else:
        upperbound = np.copy(count)

    heuristic_constraints = np.copy(lowerbound)
    #heuristic_constraints =  np.array([int(np.ceil(k * c / len(X) )) for c in count])
    # counter = 0
    # while sum(heuristic_constraints) < k:
    #     group = counter % len(count)
    #     # if heuristic_constraints[group] < upperbound[group]:
    #     heuristic_constraints[group] += 1
    #     counter += 1
            
    order = np.argsort(count)
    if args.largeFirst:
        order = order[::-1]
    
    for i,c in enumerate(count[order]):
        to_fill = k - sum(heuristic_constraints)
        if to_fill == 0:
            break
        room = c - heuristic_constraints[i]
        heuristic_constraints[i] += min(room, to_fill)
        
    
    print()
    if algorithm != fairKcenterRange:
        print("Running", args.algorithm, ": alpha = " + str(args.alpha),  "beta = " + str(args.beta ), "n = " + str(len(X)) + " m = " + str(len(constraints)), "Major = " + str(args.largeFirst), "k = " + str(k) )
        objective, runtime = wrapper(numIter, algorithm ,X,classTable,heuristic_constraints )
    else:
        print("Running", args.algorithm, ": alpha = " + str(args.alpha),  "beta = " + str(args.beta ), "n = " + str(len(X)) + ", m = " + str(len(constraints)), "k = " + str(k))
        objective, runtime = wrapperRange(numIter, algorithm ,X,classTable, upperbound, lowerbound, k )
        
    print("Our algorithm has mean objective value", np.mean(objective),"std", np.std(objective), "and", np.mean(runtime), "seconds mean runtime over", numIter, "runs")

if __name__ == '__main__':
    print("PATH", PATH)
    test_file(PATH)


