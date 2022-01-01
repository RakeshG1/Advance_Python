#!/bin/sh

# Conda Version
conda -V 

# List Existing Conda Environments in System
conda info --envs

# Create Conda Environment
conda create --name Conda_Environment_1 python=3.8.5 -y

# Activate Conda Environment
conda activate Conda_Environment_1

# Install Python Packages
pip install -r requirements.txt

# Deactivate Conda Environment
conda deactivate