#!/bin/bash

#COPY DATA TO REPLICATION FOLDER
cp -r /home/data/FBI/assessment /home/people/lxb998/replication

#CREATE DIRECTORIES FOR THE .fsf FILES
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3
mkdir fsf_files
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3/fsf_files
mkdir bart
mkdir ss_r1
mkdir ss_r2

#RENAME SUBJECT DIRECTORIES 
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3 
for r in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29
do
	mv sub-${r} sub0${r} 
done


#RENAME *.nii.gz & *.txt FILES   
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3/
for r in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29
do
	cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3/sub0${r}/func
	immv sub-${r}_task-balloonanalogrisktask_bold sub0${r}_task-balloonanalogrisktask_bold
	mv sub-${r}_task-balloonanalogrisktask_label-cashout.txt sub0${r}_task-balloonanalogrisktask_label-cashout.txt
	mv sub-${r}_task-balloonanalogrisktask_label-inflate.txt sub0${r}_task-balloonanalogrisktask_label-inflate.txt
	mv sub-${r}_task-balloonanalogrisktask_label-beforeexplode.txt sub0${r}_task-balloonanalogrisktask_label-beforeexplode.txt
	mv sub-${r}_task-balloonanalogrisktask_label-explode.txt sub0${r}_task-balloonanalogrisktask_label-explode.txt
	
	for t in 01 02
	do
		immv sub-${r}_task-stopsignal_run-${t}_bold sub0${r}_task-stopsignal_run0${t}_bold
		mv sub-${r}_task-stopsignal_run-${t}_label-stopcorrect.txt sub0${r}_task-stopsignal_run0${t}_label-stopcorrect.txt
		mv sub-${r}_task-stopsignal_run-${t}_label-gocorrect.txt sub0${r}_task-stopsignal_run0${t}_label-gocorrect.txt
		mv sub-${r}_task-stopsignal_run-${t}_label-stopincorrect.txt sub0${r}_task-stopsignal_run0${t}_label-stopincorrect.txt
		mv sub-${r}_task-stopsignal_run-${t}_label-goincorrect.txt sub0${r}_task-stopsignal_run0${t}_label-goincorrect.txt
	done
done

#ROBUST BET FOR EVERY PARTICIPANT
cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3
for r in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29
do
	cd /home/people/lxb998/replication/assessment/ds000009_R2.0.3/sub0${r}/anat
	bet sub-${r}_T1w T1_brain -R
done

