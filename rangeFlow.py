# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:12:58 2020

@author: Thy Nguyen
"""
from time import time as time


def testRangeFlow(centers, closestCenters, distances, classTable, constraints, lowerbound, classCount, K, minDist):

    k = len(centers)
    n = len(closestCenters)
    M = len(constraints)
    remainingCenters = K - k
    matching = Dinic(4 + k + M)
    source = 0
    sink = 1 + k + M
    highCapacityVertice = sink + 1
    realsink = sink + 2
    neighbors = [[-1]*M for i in range(k)]
    for i in range(1, k+1):
        matching.add_edge(0, i, 1)
    for i in range(n):
        if (distances[i] <= minDist):
            currentCenter = closestCenters[i]
            currentTarget = classTable[i]
            matching.add_edge(currentCenter+1, currentTarget + 1 + k, 1)
            neighbors[currentCenter][currentTarget] = i

    for i in range(M):
        current = i + 1 + k
        lb = lowerbound[i]
        ub = constraints[i]
        diff = ub-lb
        matching.add_edge(highCapacityVertice, current, classCount[i])
        matching.add_edge(current, realsink, lb)
        matching.add_edge(current, sink, diff)

    matching.add_edge(source, sink, sum(lowerbound))
    matching.add_edge(source, highCapacityVertice, remainingCenters)
    matching.add_edge(sink, realsink, k)
    flow = matching.max_flow(source, realsink)

    returnCenters = []
    if flow == k + sum(lowerbound):
        for i in range(1, k+1):
            for j in matching.adj[i]:
                if j[2] == 1 and j[0] != 0:
                    returnCenters.append(neighbors[i-1][j[0] - 1 - k])
                    break
        return returnCenters
    else:
        return False
    return False 


class Dinic:
    def __init__(self, n):
        self.num_vertex = n
        self.lvl = [0] * n  # this keeps track of the lvl
        # this helps ignoring the edges we already traversed in dfs
        self.start = [0] * n
        self.queue = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, flow=0):
        self.adj[a].append([b, c, 0, len(self.adj[b])])
        self.adj[b].append([a,  flow, 0, len(self.adj[a]) - 1])

    def resetGraph(self, source):
        self.lvl = [0] * self.num_vertex
        self.start = [0] * self.num_vertex
        self.lvl[source] = 1

    def max_flow(self, source, sink):
        flow, self.queue[0] = 0, source
        while True:
            self.resetGraph(source)
            qi, qe = 0, 1
            while qi < qe and not self.lvl[sink]:
                v = self.queue[qi]
                qi += 1
                for neighbor in self.adj[v]:
                    if not self.lvl[neighbor[0]] and (neighbor[1] - neighbor[2]) > 0:
                        self.queue[qe] = neighbor[0]
                        qe += 1
                        self.lvl[neighbor[0]] = self.lvl[v] + 1

            if not self.lvl[sink]:
                break
            newflow = self.dfs(source, sink, float("inf"))
            while newflow:
                flow += newflow
                newflow = self.dfs(source, sink, float("inf"))
        return flow

    def dfs(self, vertex, sink, inflow):
        if vertex == sink or not inflow:
            return inflow
        for i in range(self.start[vertex], len(self.adj[vertex])):
            neighbor = self.adj[vertex][i]
            if self.lvl[neighbor[0]] == self.lvl[vertex] + 1:
                newflow = self.dfs(neighbor[0], sink, min(
                    inflow, neighbor[1] - neighbor[2]))
                if newflow:
                    self.adj[vertex][i][2] += newflow
                    self.adj[neighbor[0]][neighbor[-1]][2] -= newflow
                    return newflow
            self.start[vertex] = self.start[vertex] + 1
        return 0
