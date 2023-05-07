To run an experiment:

python runExperiments.py NUMBER_OF_ITERATIONS ALPHA BETA NUMBER_OF_CENTERS ALGORITHM PATH_TO_DATASET (--largeFirst)

NUMBER_OF_ITERATIONS: number of random runs.
ALPHA: lower proportional bound on number of centers on each demographic, in (0,1]. 
BETA: upper proportional bound on number of centers on each demographic, in [1, n/k]. 
PROPORTION_OF_CENTER: proportion number of points to be selected as centers for each demograpic, in (0,1).  
ALGORITHM: fairKcenterRange, HeuristicA (Jones et al.), HeuristicB (Kleindessner et al.)
PATH_TO_DATASET: path to the .npz files in the dataset folder
--largeFirst: optional parameter, if set, will make the heuristic methods follow the Major heuristic (the default is Minor).  

Examples:
 
python runExperiments.py 20 0.9 1.1 0.07 fairKcenterRange  /dataset/synthetic/groupSize8.npz
python runExperiments.py 20 0.9 1.1 0.07 HeuristicA /dataset/synthetic/groupSize8.npz
python runExperiments.py 20 0.9 1.1 0.07 HeuristicB /dataset/synthetic/groupSize8.npz    