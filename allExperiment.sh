
#!/bin/bash
    

centers="0.05"
runs="20"



loc="/dataset/synthetic/groupSize2.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc --largeFirst

loc="/dataset/synthetic/groupSize4.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc --largeFirst


loc="/dataset/synthetic/groupSize8.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc --largeFirst

loc="/dataset/real/bank.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc --largeFirst

loc="/dataset/real/compas.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc --largeFirst

loc="/dataset/real/genderAdult.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc --largeFirst

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc --largeFirst
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc --largeFirst

loc="/dataset/synthetic/groupSize2.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc 

loc="/dataset/synthetic/groupSize4.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc 


loc="/dataset/synthetic/groupSize8.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc 

loc="/dataset/real/bank.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc 

loc="/dataset/real/compas.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc 

loc="/dataset/real/genderAdult.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.9 1.1  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers HeuristicB $loc 

python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicA $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers HeuristicB $loc 

loc="/dataset/synthetic/groupSize2.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers fairKcenterRange $loc 
loc="/dataset/synthetic/groupSize4.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers fairKcenterRange $loc 
loc="/dataset/synthetic/groupSize8.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers fairKcenterRange $loc 
loc="/dataset/real/bank.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers fairKcenterRange $loc 
loc="/dataset/real/compas.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers fairKcenterRange $loc 
loc="/dataset/real/genderAdult.npz"
python  runExperiments_ab.py $runs 0.9 1.1  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.8 1.2  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.7 1.3  $centers fairKcenterRange $loc 
python  runExperiments_ab.py $runs 0.6 1.4  $centers fairKcenterRange $loc 