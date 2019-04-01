#!/bin/bash

# script to start jupyter notebooks on the Heidelberg computer CIP-Pool.

# The Heidelberg CIP-Pool offers a large amount of terminals connected
# to a limited amount of servers. If different users on a single server
# run jupyter notebook simultaneously, it may happen that the sessions
# influence each other. To avoid this, we need to make sure that each
# user starts his jupyter notebook with a different port that the notebook
# listens to:

# change the following line if you want to use another broswer than
# firefox
BROWSER=/usr/local/bin/firefox

# The following line is specific to Heidelberg to acticate Anaconda
# Python 3.7
source /data/anaconda3/anaconda.sh

# and start the notebook:
jupyter notebook --port=$((`id -u` % 55535 + 10000)) --browser=${BROWSER}
