#!/bin/bash

#RUN 1ST LEVEL ANALYSIS FOR BART TASK
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3/fsf_files/bart

for b in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29
do
  feat design_bart_sub0${b}.fsf
done


#RUN 1ST LEVEL ANALYSIS FOR RUN 1 OF THE SS TASK 
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3/fsf_files/ss_r1

for s in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29 
do
  feat design_ss_r1_sub0${s}.fsf
done


#RUN 1ST LEVEL ANALYSIS FOR RUN 2 OF THE SS TASK 
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3/fsf_files/ss_r2

for s in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29 
do
  feat design_ss_r2_sub0${s}.fsf
done


