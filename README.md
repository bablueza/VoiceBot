# VoiceBot
## Install miniconda
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
conda update --all --yes
conda create -n grpc python=3.6.13
conda activate grpc
```
## Install jupyterlab
```
conda install -c conda-forge jupyterlab
jupyter-lab password
jupyter-lab --port 7777 --allow-root --no-browser --ip=0.0.0.0
```
#Reference
- https://grpc.io/docs/languages/
- https://github.com/grpc/grpc/tree/master/examples
- https://developers.google.com/protocol-buffers/docs/proto3
