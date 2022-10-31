#! /bin/bash
#PBS -N Data_organization
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=50
#PBS -q cpu

module load compiler/anaconda3
source /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgsplit/env/bin/activate
python3 /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgret/imgRet.py