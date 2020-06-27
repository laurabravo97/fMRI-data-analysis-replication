# Replication for DS009 analysis

## Replication steps

Describe here the exact steps that you took in order to replicate the analysis
described in Cohen's thesis.

Remember:

* be clear;
* justify all the analysis steps;



Replication of the fMRI data analysis (BART and SS task) presented in the PhD thesis of Jessica Cohen (University of California, Los Angeles).  

Materials and Methods for OpenfMRI ds009: The generality of self control -->   https://openfmri.org/media/ds000009/ds009_methods_0_CchSZHn.pdf

fMRI Data set  -->    https://openneuro.org/datasets/ds000009/versions/00002
					
RESEARCH REPORT 

Scripts containing each step were created /home/people/xxxxxx/replication/NAME_OF_STEP.sh or NAME.py and can be run in order to replicate the analysis.
The explanation of each step of the analysis carried out will be given throughout this text, numbered EXP XX. 
After each explanation, the steps to be followed to replicate the analysis will be given,  as a guide, numbered as STEP XX.    

EXP 1
First, the data was copied from the /home/data/FBI/assessment directory to my 'replication' folder /home/people/xxxxxx/replication. This step was performed because what we originally had in our 'replication' folder is a shortcut (/home/people/xxxxxx/replication/data) to the /home/data/FBI/assessment directory and we do not have write permission to edit the files inside it. 

EXP 2 
Then, all the directories for each subject inside the /home/people/xxxxxx/replication/assessment/ds000009_R2.03 folder were rename from 'subject-XX' to 'subject0XX' as well as all the bold.nii.gz files and the TASK_EVENT.txt files that will be used for the analysis /home/people/xxxxxx/replication/assessment/ds000009_R2.03/sub0XX/func. This was done in order to facilitate the process carried out to run the first level analysis, which included editing design.fsf files and running a python script (see EXP XX). Directories for this .fsf files were created to have them organised in the same folder /home/people/xxxxxx/replication/assessment/ds000009_R2.03/fsf_files/.     


Note: Most of the data and results of the analyses given below in the text can be found in /home/people/xxxxxx/replication/assessment/ds000009_R2.03. To avoid repetition, the files will be pointed out starting with the name of the directory automatically below this folder (ds000009_R2.03). In all other cases the full path will be provided.   


EXP 3
The BET tool was run to the anatomical T1 scan of each subject sub0XX/anat/sub-XX_T1w.nii.gz using a script with a for loop to speed up the process. This was in an attempt to replicate the following step from the analysis section of the thesis "Imaging data were processed and analyzed using FSL 4.1 (FMRIB's Software Library, www.fmrib.ox.ac.uk/fsl). Steps included BET to extract the brain from the skull and McFLIRT for motion correction." Since the author does not specify the characteristics she used for the BET,the robust brain centre estimation was used to extract the brains, as it is the most standardised option. 
Output: The extracted brains are located in each participant's anatomical folder sub0XX/anat/T1_brain.nii.gz. 

STEP 1: Run cp_mkdir_mv_bet.sh /home/people/xxxxxx/replication/cp_mkdir_mv_bet.sh 


EXP 4
The 1st level analyses were performed for every participant, task and run. First, I created design.fsf files from the GUI window for the BART and the run 1 of the SS task of subject 1. Then, in a text editor (gedit) I replaced the details in the design.fsf files that change from one participant to another with SUBNUM for the subject number (replace sub001 with subSUBNUM) and NTPTS for the number of time points (replace the Total volumes number with NTPTS) and created a template.fsf file (see STEPS XX). After that, I used a search/replace algorithm with a python script based on the programming work of Dr Jeanette Mumford (Unitersity of Texas). The script creates all the design.fsf files for every participant, task and run (see STEP XX). Finally, a shell script to run all the 1st level analyses was used. It is a way to simplify the process and save time by not having to set up and run all the analyses manually from the FEAT window. This would be quite time consuming, as there are 72 analyses in total. 
   

STEP 2: Create the design.fsf file for the BART task. 
Open a Terminal window and type 'Feat &'.   
- In the Data tab:
Click 'Select 4D data' and input the functional image for the BART task of participant 1 /sub001/func/sub001_task-balloonanalogrisktask_bold.nii.gz. Automatically, the Total volumes should change to 245. 

Output directory is /1/bart/sub001_bart

Set the 'High pass filter cutoff' to 66s because in the thesis the highpass temporal filtering is reported as "...Gaussian-weighted least-squares straight line fitting with sigma = 33.0s)...".   
 
- In the Pre-stats tab:
Select 'MCFLIRT' for motion correction in order to replicate the following from the thesis "...Steps included BET to extract the brain from the skull and McFLIRT for motion correction".
 
For slice timing correction select 'Interleaved'. The slice timing correction option that we select depends on the slice timing acquisition. The .json files for the BART task of each subject were checked sub0XX/func/sub-XX_task-balloonanalogrisktask_bold.json and it could be seen that the slices were acquired with interleaved order.
 
The Spatial smoothing FWHM was set to 5mm. In the thesis the author reported that "For the first level analysis, images were spatially smoothed using a Gaussian kernel of FWHM 5 mm..."

Temporal filtering was set to Highpass to replicate (in part) the following from the thesis "...Time-series statistical analysis was carried out using FILM (FMRIBs Improved Linear Model) with local autocorrelation correction after highpass temporal filtering (Gaussian-weighted least-squares straight line fitting with sigma = 33.0s)...". 

- In the Registration tab:
Select the structural image of subject 1 /sub001/anat/T1_brain to register it to standard MNI space (MNI152_T1_2mm_brain).          

- In the Stats tab: 
Check that the 'Use FILM prewhitening' box is ticked in order to replicate the following from the thesis "...Time-series statistical analysis was carried out using FILM (FMRIBs Improved Linear Model) with local autocorrelation correction after highpass temporal filtering (Gaussian-weighted least-squares straight line fitting with sigma = 33.0s)...". Functional MRI data are autocorrelated in time (due to low frequency noise, drifts related to the scanner and the physiological activity, neural activity, etc.). Pre-whitening using FILM (FMRIBs Improved Linear Model) is a way to correct this autocorrelation after removing the low frequency noise by using high-pass temporal filtering in the pre-processing of the data (pre-stats tab). The autocorrelation correction reduces the risk of obtaining false positives.

Select 'Standard Motion Parameters' to replicate the following part of the method section of the thesis "In addition to regressors of interest, estimated motion parameters and their temporal derivatives (i.e., displacement) were included as nuisance regressors. Linear contrasts were performed for comparisons of interest." 

Click Full model setup to input all the characteristics of the model according to the experimental design of the BART task. 
In the 'Evs' tab of the General Linear Model window set the 'Number of original EVs' to 4 in order to replicate the next from Cohen's thesis "...For the BART, the model included events for inflating the balloon (all but the last inflation of each trial), the last inflation before an explosion, cashing out, and a balloon explosion...". 
Name the first explanatory variable as 'cashout', the second one as 'inflate', EV3 as 'beforeexplode' and EV4 as 'explode'. 
For the Basic shape select 'Custom (3 column format)', since the .txt files containing the onset and duration of each event are available in the subjects' folders sub0XX/func/sub0XX_task-balloonanalogrisktask_label-*.txt 
In the Filename select the corresponding *.text file for each EV (e.g. for EV1 -cashout- the Filename is sub001/func/sub001_task-balloonanalogrisktask_label-cashout.txt'). These steps were performed to replicate the following from the thesis "...The three response-related events began at stimulus onset and lasted the duration of the participants RT. The explosion event began at the time of the explosion and lasted the amount of time the exploded balloon was on the screen (2 seconds)." 
For the convolution of the original waveform select a 'Double-Gamma HRF' (canonical haemodynamic response) to replicate the next from the thesis "...Regressors of interest were created by convolving a delta function representing each event of interest with a canonical (double-gamma) haemodynamic response function (Woolrich et al., 2001)."

In the 'Contrasts & F-tests' tab of the General Linear Model window we need to give a value to each explanatory variable depending on the contrast and comparisons that we want to make. Set the value to EV1 -cashout- to 1 and the value of EV2 -inflate- to -1. With this we are comparing this two EVs by subtracting the inflate event from the cashout event. This is done to replicate the analysis in Cohen's thesis and obtain the main effect of the BART task that we are interested in (cashing out - inflating the balloon). For this purpose, we do not need to make comparisons between all the explanatory variables, just this two that interest us.     

Click Done. Check the Model. 

- In the Post-stats tab:
Set the thresholding to 'Uncorrected'. In the higher level analysis we will use a cluster threshold but for the first level analysis is enough with just thresholding the uncorrected Z statistic values and it will speed up the process.

Note: Regarding the remaining parameters that have not been mentioned during this STEP 2, the default parameters should then be accepted.     
 
Finally, click on the 'Save' button, select the output directory for the design.fsf file for the BART task and click 'Ok'. 
Output: home/people/xxxxxx/replication/design_lev1_bart.fsf 


Note: As an alternative to the python script, which will be presented later, all the 1st level analysis for BART and SS task (parameters explained in STEP 3) can be run manually from the FEAT window. To do so, when you finish setting all the parameters in the FEAT window press 'Go' instead of 'Save'. When the 1st level analysis for the tasks of subject 1 is finished, load the created design.fsf file that was automatically created inside the feat directory from sub001 and change:
	- the input 4D file 
	- the output directory 
	- the BET T1 (T1_brain)
	- and the *.txt files of each EV in the Full model setup  
 

STEP 3: Create the design.fsf file for the run 1 of the SS task. 
For this step Open Feat and set up the same parameters used for the BART task in STEP 2 but selecting the files corresponding to the run 1 of the SS task instead. The parameters used in Cohen's thesis for the 1st level analysis of both tasks were the same. 
Set up the same high-pass filter cutoff, motion correction, slice timing correction, spatial smoothing FWHM, temporal filtering, main structural image (sub001/anat/T1_brain), head motion parameters, number of EVs and contrasts in the model setup (EV1=1 ; EV2=-1 ; EV3=0 ; EV4=0) and we also have the onsets and durations of the four different events in the run 1 of the SS task as *.txt files for most of the subjects.  
 
Note: Subjects 5, 9, 10, 11 and 16 have three EVs in the model setup of both runs of the SS task, because the *.txt files of the 'goincorrect' event are missing for both run 1 and run 2. Subjects 6, 7 and 28 have three EVs only in the run 2 of the SS task because their *goincorrect.txt files are missing just for the run 2 (they have four EVs in the run 1 model). An alternative for the subjects with only 3 EVs will be given later. For now, as we will use subject 1 to create the design.fsf file for the run 1 of the SS task, we will set up the number of EVs to '4'.

While setting the same parameters as in STEP 2, we need to define different paths for the files corresponding to the run 1 of the SS task:
- In the data tab: 
Select the 4D data /sub001/func/sub001_task-stopsignal_run001_bold
The Output directory is /1/ss_r1/sub001_ss_r1
- In the stats tab:
Click on Full model setup and name EV1 as 'stopcorrect', EV2 as 'gocorrect', EV3 as 'stopincorrect' and EV4 as 'goincorrect'. For the Filename select the corresponding *.text file for each EV (e.g. for EV1 -stopcorrect- the Filename is sub001/func/sub001_task-stopsignal_run001_label-stopcorrect.txt). The full model was set up in order to replicate the following from the thesis "The statistical models varied depending on the task. For the SS task, the model included events for successful go responses, successful stop responses, and unsuccessful stop responses. Incorrect and missed go trials were included in a nuisance regressor. All events began at fixation onset and lasted through the duration of the stimulus (1.5 seconds)...” 

The rest is the same as for the BART task. Click 'Save', select the output directory for the design.fsf file for the run 1 of the SS task and click 'Ok'. 
Output: home/people/xxxxxx/replication/design_lev1_ss_r1.fsf 
 

STEP 4: Create a template.fsf file for the BART task. To do so, in the same replication folder create one copy of the design_lev1_bart.fsf file and rename it as template_bart.fsf

Open the template_bart.fsf file /home/people/xxxxxx/replication/template_bart.fsf with gedit and replace the following lines with 'SUBNUM' and 'NTPTS': 
	- # Output directory
	set fmri(outputdir) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/1/bart/subSUBNUM_bart
 	- # Total volumes
	set fmri(npts) NTPTS
 	- # 4D AVW data or FEAT directory (1)
	set feat_files(1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-balloonanalogrisktask_bold"
  	- # Subject's structural image for analysis 1
	set highres_files(1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/anat/T1_brain"
	- # Custom EV file (EV 1)
	set fmri(custom1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-balloonanalogrisktask_label-cashout.txt"
	- # Custom EV file (EV 2)
	set fmri(custom2) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-balloonanalogrisktask_label-inflate.txt"
	- # Custom EV file (EV 3)
	set fmri(custom3) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-balloonanalogrisktask_label-beforeexplode.txt"
	- # Custom EV file (EV 4)
	set fmri(custom4) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-balloonanalogrisktask_label-explode.txt"


STEP 5: Create a template.fsf file for the run1 of the SS task. To do so, in the same replication folder create one copy of the design_lev1_ss_r1 file and rename it as template_ss_r1  

Open the template_ss_r1.fsf file /home/people/xxxxxx/replication/template_ss_r1.fsf with gedit and replace the same lines as in the previous step with 'SUBNUM' and 'NTPTS':
	- # Output directory
	set fmri(outputdir) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/1/ss_r1/subSUBNUM_ss_r1"
	- # Total volumes
	set fmri(npts) NTPTS
	- # 4D AVW data or FEAT directory (1)
	set feat_files(1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run001_bold"
	- # Subject's structural image for analysis 1
	set highres_files(1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/anat/T1_brain"
	- # Custom EV file (EV 1)
	set fmri(custom1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run001_label-stopcorrect.txt"
	- # Custom EV file (EV 2)
	set fmri(custom2) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run001_label-gocorrect.txt"
	- # Custom EV file (EV 3)
	set fmri(custom3) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_runR001_label-stopincorrect.txt"
	- # Custom EV file (EV 4)
	set fmri(custom4) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run001_label-goincorrect.txt"


STEP 6: Create the template.fsf file for the run 2 of the SS task. To do so, in the replication folder create a copy of the template_ss_r1.fsf file and rename it as template_ss_r2.fsf

Open the template_ss_r2.fsf file /home/people/xxxxxx/replication/template_ss_r2.fsf with gedit and replace the following lines with '2':
	- # Output directory
	set fmri(outputdir) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/1/ss_r2/subSUBNUM_ss_r2"
	- # 4D AVW data or FEAT directory (1)
	set feat_files(1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run002_bold"
	- # Custom EV file (EV 1)
	set fmri(custom1) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run002_label-stopcorrect.txt"
	- # Custom EV file (EV 2)
	set fmri(custom2) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run002_label-gocorrect.txt"
	- # Custom EV file (EV 3)
	set fmri(custom3) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run002_label-stopincorrect.txt"
	- # Custom EV file (EV 4)
	set fmri(custom4) "/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/subSUBNUM/func/subSUBNUM_task-stopsignal_run002_label-goincorrect.txt"



EXP 5
Now we have three template.fsf files (BART, run1 SS task, run2 SS task). The problem is that, as it was already mentioned, the goincorrect.txt file is missing for some subjects. Therefore, we need two more templates: one for subjects missing goincorrect.txt files in run 1 (subjects 5, 9, 10, 11 and 16 have three EVs in the run 1 of the SS task instead of 4) and another one for subjects missing the goincorrect.txt file in run 2 (subjects 5, 6, 7, 9, 10, 11, 16 and 28 also have only 3 EVs in the run 2 of the SS task).     


STEP 7: Create a template.fsf file for subjects missing the goincorrect.txt file in run 1 of the SS task.
In the terminal window type 'Feat &'. In the FEAT window click 'Load' --> template_ss_r1.fsf. In the Stats tab click 'Full model setup'. In the GLM window set the 'Number of original EVs' to 3 (automatically EV4 -goincorrect- will be eliminated from the model). Click 'Save' in the FEAT window and in the 'Selection' option put /home/people/xxxxxx/replication/template_ss_miss_r1.fsf (this is the location of the output directory). 

Note: Some errors will pop up because we are using the template.fsf file that has the paths with 'SUBNUM' instead of the number of the subjects (sub001, sub002, etc.) and the Total volumes with 'NTPTS'; and so FEAT warns you that those paths do not exist. This warnings can be ignored for our current purposes, which are only to obtain the template.fsf files for those subjects who are missing the go.incorrect.txt file. 


STEP 8: Repeat STEP 7 loading the template_ss_r2.fsf file instead and saving it as /home/people/xxxxxx/replication/template_ss_miss_r2.fsf (output directory).    


STEP 9: Use the python script to create all the design.fsf files per subject, per task, per run (72 in total) in one go. The python script is available at 
home/people/xxxxxx/replication/design_fsf_files.py

In any case, the content of design_fsf_files.py is presented below. It just need to be copied to gedit, saved and then made executable changing the mode of the file (from text file to python script) from the terminal window typing:
chmod a+x ./name_of_your_script.py

#!/usr/bin/env python

import os
import glob

	#CREATES ALL THE design.fsf FILES FOR THE 24 PARTICIPANTS IN THE BART TASK:

datadir = '/home/people/xxxxxx/replication/assessment/ds000009_R2.0.3'

fsf_files = "%s/fsf_files"%(datadir)

subdirs = glob.glob("%s/sub0[0-2][0-9]/func"%(datadir)) #glob.glob is used to simplify the process. Instead of creating a for loop to go through each subdirectory the glob module of python automatically looks for all the pathnames you need and you can store them in a variable (in this case 'subdirs').

for dir in list(subdirs):
  splitdir = dir.split('/')
  splitdir_sub = splitdir[7]
  subnum = splitdir_sub[-3:]
  print(subnum)
  fmrivols = os.popen('fslnvols %s/*balloonanalogrisktask_bold.nii.gz'%(dir)).read().rstrip()
  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
  with open("/home/people/xxxxxx/replication/template_bart.fsf") as infile:
    with open("%s/bart/design_bart_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
      for line in infile:
        for src, target in replacements.items():
          line = line.replace(src, target)
        outfile.write(line)


	#CREATES ALL THE design.fsf FILES FOR RUN 1 OF THE SS TASK:

#SUBJECTS WITH FOUR EVs (not missing the goincorrect.txt)
have_goincorrect = '01', '02', '03', '04', '06', '07', 12, 13, 14, 17, 18, 20, 21, 23, 24, 25, 26, 28, 29

for dir in have_goincorrect:
	  subnum = '0%s'%(dir)
	  print(subnum)
	  fmrivols = os.popen('fslnvols /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run001_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/xxxxxx/replication/template_ss_r1.fsf") as infile:
	    with open("%s/ss_r1/design_ss_r1_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
	      for line in infile:
		for src, target in replacements.items():
		  line = line.replace(src, target)
		outfile.write(line)

#SUBJECTS WITH THREE EVs (missing the goincorrect.txt)
miss_goincorrect = '05', '09', 10, 11, 16

for dir in miss_goincorrect:
	  subnum = '0%s'%(dir)
	  print(subnum)
	  fmrivols = os.popen('fslnvols /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run001_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/xxxxxx/replication/template_ss_miss_r1.fsf") as infile:
	    with open("%s/ss_r1/design_ss_r1_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
	      for line in infile:
		for src, target in replacements.items():
		  line = line.replace(src, target)
		outfile.write(line)


	#CREATES ALL THE design.fsf FILES FOR RUN 2 OF THE SS TASK:

#SUBJECTS WITH FOUR EVs (NOT missing the goincorrect.txt)
have_goincorrect = '01', '02', '03', '04', 12, 13, 14, 17, 18, 20, 21, 23, 24, 25, 26, 29

for dir in have_goincorrect:
	  subnum = '0%s'%(dir)
	  print(subnum)
	  fmrivols = os.popen('fslnvols /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run002_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/xxxxxx/replication/template_ss_r2.fsf") as infile:
	    with open("%s/ss_r2/design_ss_r2_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
	      for line in infile:
		for src, target in replacements.items():
		  line = line.replace(src, target)
		outfile.write(line)

#SUBJECTS WITH THREE EVs (missing the goincorrect.txt)
miss_goincorrect = '05', '06', '07', '09', 10, 11, 16, 28

for dir in miss_goincorrect:
	  subnum = '0%s'%(dir)
	  print(subnum)
	  fmrivols = os.popen('fslnvols /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run002_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/xxxxxx/replication/template_ss_miss_r2.fsf") as infile:
	    with open("%s/ss_r2/design_ss_r2_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
	      for line in infile:
		for src, target in replacements.items():
		  line = line.replace(src, target)
		outfile.write(line)

	

STEP 10: Use a shell script to run all the first level analyses (72 in total) in one go. The shell script is available at home/people/xxxxxx/replication/lev1_analysis.sh
It will also be presented below and its content can be copied to a text file, saved and made executable from the Terminal window with 
chmod a+x ./name_of_your_script.py 

#!/bin/bash

#RUN 1ST LEVEL ANALYSIS FOR BART TASK
cd /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/fsf_files/bart

for b in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29
do
  feat design_bart_sub0${b}.fsf
done

#RUN 1ST LEVEL ANALYSIS FOR RUN 1 OF THE SS TASK 
cd /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/fsf_files/ss_r1

for s in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29 
do
  feat design_ss_r1_sub0${s}.fsf
done

#RUN 1ST LEVEL ANALYSIS FOR RUN 2 OF THE SS TASK 
cd /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/fsf_files/ss_r2

for s in 01 02 03 04 05 06 07 09 10 11 12 13 14 16 17 18 20 21 23 24 25 26 28 29 
do
  feat design_ss_r2_sub0${s}.fsf
done


Output directories for the 1st level analyses:
For the BART task: /1/bart/sub0XX_bart.feat
For the run 1 of the SS task: /1/ss_r1/sub0XX_ss_r1.feat
For the run 2 of the SS task: /1/ss_r2/sub0XX_ss_r2.feat



EXP 6 
Once we have done the 1st level analysis (within-subject), we need to do a second level analysis (within-subject repeated measures -runs of the same task-) for the SS task, because it has two runs. This step was carried out to replicate (in part) the following from the thesis “For the two tasks that had more than one run (SS and ER), data were combined across the two runs using a fixed effects model...”


STEP 11: Run a 2nd level analysis to combine the two runs of the SS task. 
Open Feat and select Higher-level analysis.

- In the Data tab: Set the number of inputs to 48 (24 participants x 2 runs). 
To input the 48 first level analysis directories from runs 1 and 2 of the SS task, Click 'Select FEAT directories'. To speed up the process instead of having to manually input the 48 directories we can use the 'Paste' option. 
First, in the terminal window type cd /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/1/ 
Then type the next command line: 
ls -d1 "$PWD"/*/*ss_r1.feat ; ls -d1 "$PWD"/*/*ss_r2.feat

to show a list of each of the 48 *.feat directories in a separate line in the Terminal window. 
Then copy and paste the 48 directories to the Paste Window and press 'Ok'.
Once all the data is inputted press 'Ok' in the 'Select input data' window. 
Choose an output directory /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/2/lev2all_ss

- In the Stats tab: select 'Fixed effects' as Cohen described in her thesis
Click Full model setup
On the EVs tab set the number of main EVs to 24 (24 participants in the SS task). 
Label each EV with the number of each participant (sub001, sub002....sub014, sub016...sub029).
Going down the columns, put a '1' in any row of the EV column for which the participant has a matching scan (an input file corresponding to that specific participant). There are 48 input files in total and there should be 48 ones in the design matrix overall, the rest are zeros. 
E.g. EV1 -sub001- column has a '1' for Input 1 and for Input 25 ; EV24 -sub029- has a '1' for Input 24 and for Input 48, etc. 

On the Contrasts & F-tests tab, set the number of contrasts to 24 (means of the 24 subjects).
Name each contrast as the subjects (sub001, sub002...sub029).
Going down the columns, put a '1' in the row matching participants with their corresponding EVs (e.g. EV1 has a 1 in the C1 row -sub001- ; EV9 has a 1 in the C9 row -sub010- ; EV24 has a 1 in the C24 row -sub029- ; etc.)

Press 'Done', check the second level design and close the Model window. 

For the rest of the parameters accept defaults. 

Press Go

Output directory for the Second level analysis: /2/lev2all_ss.gfeat            

Note: A design.fsf file for the second level analysis is available in the replication folder. It can be loaded into the Feat window and can then be run /home/people/xxxxxx/replication/design_lev2all_ss.fsf


EXP 7
Two third level analyses (between-subjects; mean group effects) were carried out, one for the BART task and another for the SS task. This was in order to obtain the activation maps for the main effects of each task (cashing out – inflating the balloon in the BART task; successful stop – successful go in the SS task) as presented by Jessica Cohen in the Results section of Chapter 4 of her PhD thesis. The third level analysis was set up from the FEAT window and will be explained bellow. 


STEP 12 Obtain the demeaned values for number of pumps (BART) and Stop-Signal Reaction Time (SSRT; SS task), which will be included as a second regressor in the third level analysis design matrix, in order to replicate (in part) the following from the thesis “...The model for each task included a regressor modeling mean activity and demeaned regressors for SSTR (SS), number of pumps (BART), k (TD), and amount of reported regulation (ER)...”

To obtain the demeaned number of pumps:
- Open the sub0XX/func/sub-XX_task-balloonanalogrisktask_events.tsv files (have details of all events during the runs) for each subject.
- Filter the 'button_pressed' column to show only the option 'b', which corresponds to inflating the balloon. 
- Count how many times the participant inflated the balloon and store it in an excel file. 
- Once you have done this for every participant, you should have 24 rows with total number of pumps per participant. 
- Calculate the average number of pumps between all participants 
- Subtract this average (173.916667) from the total number of pumps of each participant and put the values in a new 'Demeaned NoP' column. 
- To check they are correct, you can add all of them and you need to obtain zero. 

An excel file is available at home/people/xxxxxx/replication/demeaned_NoP.xlsx


The process to obtain the demeaned SSRT is slightly more complicated.
- Open the .tsv files for run 1 and run 2 of SS task of each subject. 
- Filter the 'trial_type' column to show only the STOP responses and count them (always 32 STOP trials).
- Filter the 'trial_outcome' column to show only unsuccessful stop responses and count them. 
- Calculate the ratio of unsuccessful stop responses (unsuccessful stop / total stop)
- Remove the filter in 'trial_outcome' to show all types of stop responses and calculate the mean of the Stop Signal Delay (SSD) for every stop response.  
- Calculate the proportion of failed inhibition (ratio unsuccess / total of stop responses)
- Calculate the quantile Reaction Time (qRT) multiplying the calculated proportion of failed inhibition (ratio unsuccess) and the total number of successful go responses.
- Subtract the average SSD from the median RT that corresponds to the quatile RT and obtain the SSRT. 
- Average the SSRT corresponding to the two runs of the SS task. Obtain SSRT per subject. 
- Calculate the mean of all the SSRTs.
- This value was subtracted from each subject's SSRT. 
  
An excel file is available at home/people/xxxxxx/replication/demeaned_SSRT.xlsx



STEP 13 Run the third level analysis for the BART task   
Open Feat and select Higher-level analysis.

- In the Data tab: 
Set the number of inputs to 24 (24 participant data sets we want to combine).
 
To input the 24 first level analysis directories, Click 'Select FEAT directories'. Again, to speed up the process instead of having to input the 24 directories manually we can use the 'Paste' option. 
In the terminal window type cd /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/1/bart
Then type the next command line: 
ls -d1 "$PWD"/*.feat 
to list each of the 24 sub0XX_bart.feat directories in a separate line in the Terminal window. 
Then copy and paste the paths from the Terminal window to the Paste Window and press 'Ok'.
Once all the data is inputted press 'Ok' in the 'Select input data' window. 

Choose an output directory /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3/bart

- In the stats tab:
Choose 'Mixed effects: FLAME 1' in order to replicate (in part) the following from the thesis “For the two tasks that had more than one run (SS and ER), data were combined across the two runs using a fixed effects model, and then modeled using a mixed effects at the group level with FSL's FLAME model (Stage 1 only)...”

Tick the 'Use automatic outlier de-weighting box to replicate Cohen's analysis “...Outlier deweighting was performed using a mixture modeling approach (Woolrich, 2008).”

Click Full model setup and set the number of main EVs to 2. EV1 is 'bart_effect' and EV2 can be named as 'demeaned_NoP'. 
Press the 'Paste' button. Then Clear. 
Open the home/people/xxxxxx/replication/demeaned_NoP.xlxs file and copy the two indicated columns in your model. EV1 is fill with ones and EV2 is each subject's demeaned number of pumps. 

In the contrasts tab, set two contrasts: C1 Group mean (1 - 0) and C2 is group demeaned activity (0 - 1). 
Press Done

- In the Post-stats tab low the Z threshold to 2.3 in order to replicate the following from the thesis “Results were thresholded at a whole-brain level using cluster-based Gaussian random field theory, with a cluster-forming threshold of z > 2.3 and a whole brain corrected cluster significance level of p < .05 unless otherwise noted in the text.”

For the rest of the parameters accept defaults.
Press Go

Output directory for the Third level analysis of BART: /3/bart.gfeat           

Note: A design.fsf file for the third level analysis of the BART task is available in the replication folder. It can be loaded into the Feat window and can then be run /home/people/xxxxxx/replication/design_lev3_bart.fsf
    


STEP 14 Run the third level analysis for the SS task. 
Open Feat 
- In the Data tab: 
Set the number of inputs to 24 (24 participant data sets we want to combine) and selec the option 'Inputs are 3D cope images from FEAT directories'. 
 
To input the 24 second level analysis cope images, Click 'Select cope images'. Again, to speed up the process instead of inputting the 24 cope images manually we can use the 'Paste' option. 
In the Terminal window type cd /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/2/lev2all_ss.gfeat/cope1.feat/stats
Then type the next command line:
ls -1 "$PWD"/cope*.nii.gz
to list each of the 24 cope images in a separate line in the Terminal window. 
Then copy and paste the paths from the Terminal window to the Paste Window and press 'Ok'.
Once all the data is inputted press 'Ok' in the 'Select input data' window. 

Choose an output directory /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3/ss

- In the stats tab:
Choose 'Mixed effects: FLAME 1' in order to replicate (in part) the following from the thesis “For the two tasks that had more than one run (SS and ER), data were combined across the two runs using a fixed effects model, and then modeled using a mixed effects at the group level with FSL's FLAME model (Stage 1 only)...”

Tick the 'Use automatic outlier de-weighting box to replicate Cohen's analysis “...Outlier deweighting was performed using a mixture modeling approach (Woolrich, 2008).”

Click Full model setup and set the number of main EVs to 2. EV1 is 'ss_effect' and EV2 can be named as 'demeaned_SSRT'. 
Press the 'Paste' button. Then Clear. 
Open the home/people/xxxxxx/replication/demeaned_SSRT.xlxs file and copy the two indicated columns in your model. EV1 is fill with ones and EV2 is each subject's demeaned SSRT. 

In the contrasts tab, set two contrasts: C1 Group mean (1 - 0) and C2 is group demeaned activity (0 - 1). 
Press Done and check your model.

- In the Post-stats tab low the Z threshold to 2.3 in order to replicate the following from the thesis “Results were thresholded at a whole-brain level using cluster-based Gaussian random field theory, with a cluster-forming threshold of z > 2.3 and a whole brain corrected cluster significance level of p < .05 unless otherwise noted in the text.”

For the rest of the parameters accept the defaults.
Press Go

Output directory for the third level analysis of SS task: /3/ss.gfeat           

Note: A design.fsf file for the third level analysis of the SS task is available in the replication folder. It can be loaded into the Feat window and can then be run to replicate the analysis /home/people/xxxxxx/replication/design_lev3_ss.fsf




## Replication files

* t-statistic map for main effect of SS task; Output: /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3/ss.gfeat/cope1.feat/stats/tstat1.nii.gz  

* thresholded z-statistic map for main effect of SS task; Output: /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3/ss.gfeat/cope1.feat/thresh_zstat1.nii.gz 

* t-statistic map for main effect of BART task; Output: /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3/bart.gfeat/cope1.feat/stats/tstat1.nii.gz

* thresholded z-statistic map for main effect of BART task; Output: /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3/bart.gfeat/cope1.feat/thresh_zstat1.nii.gz




## Voxels in common across SS and BART

Describe how you generated your image showing voxels in common across the main
effects of the SS and BART tasks.

Point to the location of the image.



To show voxels in common across the main effects of the SS and BART tasks fslmaths was used with the following commands (shell script available and at home/people/xxxxxx/replication/voxels_common.sh):  

# First, we need to change our current directory to the third level analysis directory with:
cd /home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3
# and create a new folder to store the resulting images with 
mkdir voxels_in_common

# Second, the threshholded z-statistic images of both tasks were added: 
fslmaths bart.gfeat/cope1.feat/thresh_zstat1 -add ss.gfeat/cope1.feat/thresh_zstat1 added_thresh


# Then, the threshholded z-stat image of BART was binary (1=activation; 0=no activation) subtracted from the resulting image of the previous step (added_thresh) using a threshold of 0.5 (i.e. 50% probability) 
fslmaths added_thresh -bin -sub bart.gfeat/cope1.feat/thresh_zstat1 -thr 0.5 binsub_bart

# After that, the threshholded z-stat image of SS task was also binary (1=activation; 0=no activation) subtracted from the added_thresh image using a threshold of 0.5 (i.e. 50% probability)
fslmaths added_thresh -bin -sub ss.gfeat/cope1.feat/thresh_zstat1 -thr 0.5 binsub_ss

# Then, this two resulting images are added, creating the voxels that are not in common between the two tasks main effects 
fslmaths binsub_bart -bin -add binsub_ss added_binsub_ss_bart

# Finally, the previous image (voxels not in common) is binary subtracted from the added_thresh image. As a result, we obtain a binary map of the voxels in common between the SS and the BART task.
fslmaths added_thresh -bin -sub added_binsub_ss_bart voxels_common_bart_ss


The images were moved into the voxels_in_common folder with the 'mv' command (see voxels_common.sh) to have them organised in a same folder. 


The location of the final image showing the voxels in common between the two tasks is:
home/people/xxxxxx/replication/assessment/ds000009_R2.0.3/3/voxels_in_common/voxels_common_bart_ss.nii.gz







