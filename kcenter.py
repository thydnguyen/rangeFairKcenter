import numpy as np
from scipy.spatial import distance
from sklearn.metrics import pairwise_distances
from rangeFlow import testRangeFlow
from time import time as time

def min_metric(x,X, metric = 'euclidean'):
  distance_matrix = distance.cdist(x, X, metric).flatten()
  return np.min(distance_matrix)


def gonzalez(X,k, metric = 'euclidean'): 
    '''  
    X :the data set, 2d-aray
    k : is the number of cluster, unsigned int
    RETURNS: list of potential unfair centers
    '''
    C = [] #list of centers to return
    C.append(np.random.randint(0, X.shape[0]))
    K = 1
    kDistance = [] #table storing distance of k centers to other points
    minDist = distance.cdist(X[C], X, metric).flatten()
    kDistance.append(minDist)
    while k!=K:
        candidate = np.argmax(minDist)
        C.append(candidate)
        K = K+1
        newDist = distance.cdist([X[candidate]], X, metric ).flatten()
        kDistance.append(newDist)
        if k!= K:
            minDist = np.min(np.vstack((minDist, newDist)), axis = 0)
    return C, kDistance

def gonzalez_return(Y,k, given_centers, lowerbound, classTable, upperbound = [] , metric = 'euclidean'): 
    '''  
    X :the data set, 2d-aray
    k : is the number of cluster, unsigned int
    RETURNS: list of potential unfair centers
    '''
    X =np.copy(Y)
    C = np.copy(given_centers).tolist() #list of centers to return
    
    potentials = [i for i in range(len(X)) if i not in given_centers and lowerbound[classTable[i]] > 0]
    if len(potentials) == 0:
        potentials =  [i for i in range(len(X)) if i not in C and upperbound[classTable[i]] > 0]
    #print(potentials)
    ii = np.random.choice(potentials)
    C.append(ii)
    lowerbound[classTable[ii]] = lowerbound[classTable[ii]] - 1
    K = len(C)
    minDist = np.min(distance.cdist(X[C], X[potentials], metric), axis = 0)

    
    while k!=K:
        #print("max", max(minDist))
        sortedIndices = np.argsort(minDist)
        candidate = potentials[sortedIndices[-1]]
        potentials.remove(candidate)
        minDist = np.delete(minDist, sortedIndices[-1], axis = 0)
        C.append(candidate)
        if len(upperbound) != 0:
            upperbound[classTable[candidate]] -=1
        K = K+1
        if len(potentials) == 0:
            potentials = [i for i in range(len(X)) if i not in C and upperbound[classTable[i]] > 0]
        # if len(potentials) == 0:
        #     if k!= K:
        #         print(k, K, "not satisfied")
        #     return C
        newDist = distance.cdist([X[candidate]], X[potentials], metric ).flatten()
        minDist = np.min(np.vstack((minDist, newDist)), axis = 0)

    return C




def gonzalezNoStore(X,k, metric = 'euclidean'): 
    '''  
    X :the data set, 2d-aray
    k : is the number of cluster, unsigned int
    RETURNS: list of potential unfair centers
    '''
    C = [] #list of centers to return
    C.append(np.random.randint(0, X.shape[0]))
    K = 1
    minDist = distance.cdist(X[C], X, metric).flatten()

    while k!=K:
        candidate = np.argmax(minDist)
        C.append(candidate)
        K = K+1
        newDist = distance.cdist([X[candidate]], X, metric ).flatten()
        if k!= K:
            minDist = np.min(np.vstack((minDist, newDist)), axis = 0)
      
    return C


def gonzalez_variant(X,candidates, k, given_dmat, metric= 'euclidean'): 
    '''  
    X :the data set, 2d-aray
    k : is the number of cluster, unsigned int
    given_dmat: distance matrice that's already computed
    candidates: list of indices considered for greedy selection
    RETURNS: list of potential unfair centers
    '''
    X_sub = X[candidates]
  
    C = [] #list of centers to return
    given_dmat_min = np.min(given_dmat, axis = 0)
    candidate_given_dmat_min = given_dmat_min[candidates]
    C.append(candidates[np.argmax(candidate_given_dmat_min)])
    
    minDist = distance.cdist(X[C], X, metric).flatten()
    candidate_minDist = minDist[candidates]
    if  k == 1: 
        return C,  np.concatenate((given_dmat , [minDist]), axis = 0) 

    K = 1
    kDistance = []  
    candidate_minDist = np.min(np.vstack((candidate_minDist, candidate_given_dmat_min)), axis = 0)
    kDistance.append(minDist)
    while k!=K :
        candidate = np.argmax(candidate_minDist)
        C.append(candidates[candidate])
        K = K+1
        newDist = distance.cdist([X_sub[candidate]], X, metric ).flatten()
        kDistance.append(newDist)
        if k!= K:
            candidate_minDist = np.min(np.vstack((candidate_minDist, newDist[candidates])), axis = 0)

    return C,  np.concatenate((given_dmat , kDistance), axis = 0) 


def testFairShiftFlowFull(centers, closestCenters, distances, classTable, constraints, minDist):
    """
    tests the fair shift using a modified Hopcroft-Karp
    """
    k = len(centers)
    n = len(closestCenters)
    M = len(constraints)
    matchC = [None for i in range(k)] # partners of the centers
    matchG = [[] for i in range(M)]
    num_matched = [0 for i in range(M)]
    match_count = 0
    
    # build the bipartite graph between centers and groups
    neighbors = [[] for i in range(k)]
    for i in range(n):
        if (distances[i] <= minDist):
            neighbors[closestCenters[i]].append((classTable[i], i))

    # initialize greedy matching
    for u in range(k):
        for v, shift_target in neighbors[u]:
            if num_matched[v] < constraints[v]:
                matchC[u] = (v, num_matched[v], shift_target)
                matchG[v].append(u)
                num_matched[v] += 1
                match_count += 1
                break
   
    while True:
        # use BFS to construct layered graph
        distC = [-1 for i in range(k)]
        distG = [-1 for i in range(M)] 
        queue = []
        for u in range(k):
            if matchC[u] == None:
                distC[u] = 0
                queue.append(u)
        head = 0
        found_augmenting_path = False
        while head < len(queue):
            u = queue[head]
            head += 1
            for v, shift_target in neighbors[u]:
                if distG[v] == -1:
                    distG[v] = distC[u] + 1
                    if num_matched[v] < constraints[v]:
                        found_augmenting_path = True
                    for u1 in range(num_matched[v]):
                        distC[matchG[v][u1]] = distG[v] + 1
                        queue.append(matchG[v][u1])

        if not found_augmenting_path:
            if match_count < k:
                return False
            return [x[2] for x in matchC]
            
        # use DFS to find blocking flow in the layered graph
        scan_next = [0 for i in range(M)]
        
        def DFS(u):
            for v, shift_target in neighbors[u]:
                if distG[v] == distC[u] + 1:
                    if num_matched[v] < constraints[v]:
                        matchC[u] = (v, num_matched[v], shift_target)
                        matchG[v].append(u)
                        num_matched[v] += 1
                        return True
                    
                    while scan_next[v] < num_matched[v]:
                        idx = scan_next[v]
                        scan_next[v] += 1
                        u1 = matchG[v][idx]
                        if DFS(u1):
                            matchC[u] = (v, idx, shift_target)
                            matchG[v][idx] = u
                            return True
            return False

        for u in range(k):
            if matchC[u] == None:
                if DFS(u):
                    match_count += 1


def findAllNeighbors(classTable, M, kDistance_i):
  '''
  classTable: class assignment for each point, integer-vector of length m with entries in 0,...,k and sum over entries equaling k
  M: number of groups
  kDistance_i: vector containing the distance of the center i to all other points
  RETURNS: a list object that closest to center i to each group and a list that contains the corresponding distance
  '''
  
  distTable = [float('infinity')] * M
  neighborTable = [-1] * M
  for D, currentGroup,m in zip(kDistance_i, classTable, list(range(len(classTable)))):
      if D < distTable[currentGroup]:
          distTable[currentGroup] = D
          neighborTable[currentGroup] = m
  return neighborTable, distTable



def recomputeClosestCentersNostore(X, closestCenters, currdist, centers, lorange, hirange, metric = 'euclidean'):
  """
  Update the closest centers of points and range of centers to check, update centers
  X: dataset
  closestCenters: list of closestCenters to update and restore
  currdist: distance between items in X and their closestCenters
  centers: list of centers
  lowrange, hirange: check centers[i] for i in [lorange, hirange)
  """
  # compute distances in batches
  batch = 1000
  index = lorange
  while index < hirange:
    end = min(index + batch, hirange)
    cts = [X[centers[i]] for i in range(index, end)]
    dist = distance.cdist(X, cts, metric)
    closest = np.argmin(dist, axis=1)
    for j in range(X.shape[0]):
      if closestCenters[j] >= hirange - 1 or dist[j][closest[j]] < currdist[j]:
        closestCenters[j] = index + closest[j]
        currdist[j] = dist[j][closest[j]]
    index = end
    
  return closestCenters, currdist




def HeuristicA(X, classTable, constraints, metric='euclidean'):
  """
  Implementation of Alg2-Seq
  X: dataset
  classTable: class assignment for each point, integer-vector of length m with entries in 0,...,k and sum over entries equaling k
  constraints: required count for each group  , integer-vector with entries in 0,...,n-1
  RETURNS: list of fair centers
  """

  k = np.sum(constraints)
  n = X.shape[0]
  classTable = classTable.tolist()
  unfairCenters = gonzalezNoStore(X, k, metric=metric)
  first = 0
  last = k - 1
  fairshift = None
  bestMid = -float('Infinity')
  bestRadius = float('Infinity')
  bestFairShift = None
  
  # instead of remembering distances of classes for each center, instead remember the closest "active" center for each point
  # here we are remembering by index in unfairCenters
  # A is analagous to old_mid
  currentDistanceA = distance.cdist(X, [X[unfairCenters[0]]], metric).flatten()
  currentDistanceMid = distance.cdist(X, [X[unfairCenters[0]]], metric).flatten()
  closestCenterA = [0] * n
  closestCenterMid = [0] * n

  while (first < last):
    mid = (first + last + 1) // 2
    # first, update distances for mid
    closestCenterMid, currentDistanceMid = recomputeClosestCentersNostore(X, closestCenterA.copy(), currentDistanceA.copy(),
                                                                          unfairCenters, first + 1, mid + 1, metric)
    minDist = min_metric([X[unfairCenters[mid]]] , X[unfairCenters[:mid]]) / 2
    if mid > 0:
      start = time()
      fairshift = testFairShiftFlowFull(unfairCenters[:mid + 1], closestCenterMid, currentDistanceMid, classTable,
                                    constraints, minDist)
    else:
      fairshift = True
    if fairshift == False:
      last = mid - 1
    else:
      first = mid
      currentDistanceA = currentDistanceMid
      closestCenterA = closestCenterMid
      bestMid = mid
      bestRadius = minDist
      bestFairShift = np.copy(fairshift)

  mid = bestMid
      
  minDist = bestRadius
  candidateRadius = sorted([x for x in currentDistanceA if x <= minDist])
  
  bestMinDist = minDist

  first = 0
  last = len(candidateRadius) - 1
  fairshift = None

  while (first <= last):
    midRadius = (first + last) // 2
    minDist = candidateRadius[midRadius]
    fairshift = testFairShiftFlowFull(unfairCenters[:mid + 1], closestCenterA, currentDistanceA, classTable, constraints,
                              minDist)
    if fairshift != False and minDist <= bestMinDist:
      bestMinDist = minDist
      bestFairShift = np.copy(fairshift)
      last = midRadius - 1
    else:
      first = midRadius + 1

  classTable = np.array(classTable)
  fairshift = np.copy(bestFairShift)
  constraintsSatisfied, constraintsSatisfiedCount = np.unique(np.array(classTable)[fairshift], return_counts=True)
  for c in range(len(constraintsSatisfied)):
    constraints[constraintsSatisfied[c]] = constraints[constraintsSatisfied[c]] - constraintsSatisfiedCount[c]

  if len(fairshift) == k:
    return fairshift

  #print("Points left:", k - len(fairshift))
  # for i in range(len(classTable)):
  #   if i not in fairshift and constraints[classTable[i]] > 0:
  #     try:
  #       fairshift.append(i)
  #     except:
  #       fairshift = fairshift.tolist()
  #       fairshift.append(i)
  #     constraints[classTable[i]] = constraints[classTable[i]] - 1
  #     if len(fairshift) == k:
  #       break


  return gonzalez_return(X,k, fairshift, constraints, classTable)



def fairKcenterRange(X, classTable, constraints, lowerbound, k, metric='euclidean'):
  """
  Implementation of Alg2-Seq
  X: dataset
  classTable: class assignment for each point, integer-vector of length m with entries in 0,...,k and sum over entries equaling k
  constraints: required count for each group  , integer-vector with entries in 0,...,n-1
  RETURNS: list of fair centers
  """
  
  classCount = np.unique(classTable, return_counts=True)[1]
  n = X.shape[0]
  classTable = classTable.tolist()
  unfairCenters = gonzalezNoStore(X, k, metric=metric)
  first = 0
  last = k - 1
  fairshift = None
  bestMid = -float('Infinity')
  bestRadius = float('Infinity')
  bestFairShift = None
  
  # instead of remembering distances of classes for each center, instead remember the closest "active" center for each point
  # here we are remembering by index in unfairCenters
  # A is analagous to old_mid
  currentDistanceA = distance.cdist(X, [X[unfairCenters[0]]], metric).flatten()
  currentDistanceMid = distance.cdist(X, [X[unfairCenters[0]]], metric).flatten()
  closestCenterA = [0] * n
  closestCenterMid = [0] * n


  while (first < last):
    mid = (first + last + 1) // 2
    # first, update distances for mid
    closestCenterMid, currentDistanceMid = recomputeClosestCentersNostore(X, closestCenterA.copy(), currentDistanceA.copy(),
                                                                          unfairCenters, first + 1, mid + 1, metric)
    minDist = min_metric([X[unfairCenters[mid]]] , X[unfairCenters[:mid]]) / 2
    if mid > 0:

      fairshift = testRangeFlow(unfairCenters[:mid + 1], closestCenterMid, currentDistanceMid, classTable,
                                    constraints, lowerbound, classCount, k, minDist)

    else:
      fairshift = True
    if fairshift == False:
      last = mid - 1
    else:
      first = mid
      currentDistanceA = currentDistanceMid
      closestCenterA = closestCenterMid
      bestMid = mid
      bestRadius = minDist
      bestFairShift = np.copy(fairshift)

  mid = bestMid

      
  minDist = bestRadius
  candidateRadius = sorted([x for x in currentDistanceA if x <= minDist])
  
  bestMinDist = minDist

  first = 0
  last = len(candidateRadius) - 1
  fairshift = None

  while (first <= last):
    midRadius = (first + last) // 2
    minDist = candidateRadius[midRadius]
    fairshift = testRangeFlow(unfairCenters[:mid + 1], closestCenterA, currentDistanceA, classTable, constraints,
                                      lowerbound, classCount, k, minDist)
    
    if fairshift != False and minDist <= bestMinDist:
      bestMinDist = minDist
      bestFairShift = np.copy(fairshift)
      last = midRadius - 1
    else:
      first = midRadius + 1

  classTable = np.array(classTable)
  
  fairshift = np.copy(bestFairShift)
  if len(fairshift) == k:
    return fairshift
  constraintsSatisfied, constraintsSatisfiedCount = np.unique(np.array(classTable)[fairshift], return_counts=True)
  lowerbound_ = np.copy(lowerbound)
  upperbound_ = np.copy(constraints)

  for c in range(len(constraintsSatisfied)):
    lowerbound_[constraintsSatisfied[c]] = lowerbound[constraintsSatisfied[c]] - constraintsSatisfiedCount[c]
    upperbound_[constraintsSatisfied[c]] = upperbound_[constraintsSatisfied[c]] - constraintsSatisfiedCount[c]
  

  return gonzalez_return(X,k, fairshift, lowerbound_, classTable, upperbound_) 

  


