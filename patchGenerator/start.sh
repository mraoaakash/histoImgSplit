#! /bin/bash
#PBS -N Data_organization
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=10
#PBS -q cpu

module load compiler/anaconda3
source /storage/tnbc/NewDatasetHnE/histoimgsplit
python3 /home/aakash.rao_ug23/cloud/histoImgSplit/keygetter.py