# Docker file for the breast cancer recurrence predictor project
# 
# Feb., 2020

# Use continuumio/anaconda3 as base image
FROM continuumio/anaconda3 

# Install base R
RUN apt-get update && \
    apt-get install r-base r-base-dev -y


# Install Python packages
RUN conda install -y -c anaconda docopt==0.6.2 


# Upgrade scikit-learn to 0.22.1
RUN pip install -U scikit-learn


# Install R packages
RUN conda install -y -c r r-tidyverse==1.2.1 && \
    conda install -y -c conda-forge r-docopt==0.6.1 && \
    conda install -c conda-forge r-ggridges  && \
    conda install -y -c conda-forge r-cowplot


# Put Anaconda Python in PATH
ENV PATH="/opt/conda/bin:${PATH}"


CMD ["/bin/bash"]
