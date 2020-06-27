#!/usr/bin/env python


import os
import glob

	#CREATES ALL THE design.fsf FILES FOR THE 24 PARTICIPANTS IN THE BART TASK

datadir = '/home/people/lxb998/replication/assessment/ds000009_R2.0.3'

fsf_files = "%s/fsf_files"%(datadir)

subdirs = glob.glob("%s/sub0[0-2][0-9]/func"%(datadir)) #glob.glob is used to simplify the process. Instead of creating a for loop to go throug each subdirectory the glob module of python automatically looks for all the pathnames you need and you can store them in a variable (in this case 'subdirs').

for dir in list(subdirs):
  splitdir = dir.split('/')
  splitdir_sub = splitdir[7]
  subnum = splitdir_sub[-3:]
  print(subnum)
  fmrivols = os.popen('fslnvols %s/*balloonanalogrisktask_bold.nii.gz'%(dir)).read().rstrip()
  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
  with open("/home/people/lxb998/replication/template_bart.fsf") as infile:
    with open("%s/bart/design_bart_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
      for line in infile:
        for src, target in replacements.items():
          line = line.replace(src, target)
        outfile.write(line)



	#CREATES ALL THE design.fsf FILES FOR RUN 1 OF THE SS TASK


#SUBJECTS WITH FOUR EVs (not missing the goincorrect.txt)
have_goincorrect = '01', '02', '03', '04', '06', '07', 12, 13, 14, 17, 18, 20, 21, 23, 24, 25, 26, 28, 29

for dir in have_goincorrect:
	  subnum = '0%s'%(dir)
	  print(subnum)
	  fmrivols = os.popen('fslnvols /home/people/lxb998/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run001_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/lxb998/replication/template_ss_r1.fsf") as infile:
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
	  fmrivols = os.popen('fslnvols /home/people/lxb998/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run001_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/lxb998/replication/template_ss_miss_r1.fsf") as infile:
	    with open("%s/ss_r1/design_ss_r1_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
	      for line in infile:
		for src, target in replacements.items():
		  line = line.replace(src, target)
		outfile.write(line)


	#CREATE ALL THE design.fsf FILES FOR RUN 2 OF THE SS TASK


#SUBJECTS WITH FOUR EVs (NOT missing the goincorrect.txt)
have_goincorrect = '01', '02', '03', '04', 12, 13, 14, 17, 18, 20, 21, 23, 24, 25, 26, 29

for dir in have_goincorrect:
	  subnum = '0%s'%(dir)
	  print(subnum)
	  fmrivols = os.popen('fslnvols /home/people/lxb998/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run002_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/lxb998/replication/template_ss_r2.fsf") as infile:
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
	  fmrivols = os.popen('fslnvols /home/people/lxb998/replication/assessment/ds000009_R2.0.3/sub0%s/func/*stopsignal_run002_bold.nii.gz'%(dir)).read().rstrip()
	  replacements = {'SUBNUM':subnum, 'NTPTS':fmrivols} 
	  with open("/home/people/lxb998/replication/template_ss_miss_r2.fsf") as infile:
	    with open("%s/ss_r2/design_ss_r2_sub%s.fsf"%(fsf_files,subnum), 'w') as outfile:		
	      for line in infile:
		for src, target in replacements.items():
		  line = line.replace(src, target)
		outfile.write(line)
