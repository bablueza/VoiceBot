# VoiceBot
## Install miniconda
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
conda update --all --yes
conda create -n nemo_blue python=3.6.13
conda activate nemo
```
## Install jupyterlab
```
conda install -c conda-forge jupyterlab
jupyter-lab password
jupyter-lab --port 7777 --allow-root --no-browser --ip=0.0.0.0
```
