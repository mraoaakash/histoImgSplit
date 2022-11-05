#! /bin/bash
#PBS -N Data_organization
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=10
#PBS -q cpu

module load compiler/anaconda3
source /storage/tnbc/dev-phase-001/histoimgsplit/bin/activate
python3 /home/aakash.rao_ug23/cloud/histoImgSplit/patchGenerator/keys.py
python3 /home/aakash.rao_ug23/cloud/histoImgSplit/patchGenerator/splitter.py