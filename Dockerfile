# Docker file for DSCI522_Group_301
# Authors: Fanli Zhou, Haoyu Su, Kexin Zhao
# Feb, 2020

# Use continuumio/anaconda3 as base image
FROM continuumio/anaconda3 

# Install base R
RUN apt-get update && \
    apt-get install r-base r-base-dev -y && \
    apt-get install libcurl4-openssl-dev -y && \
    apt-get install libssl-dev -y


# Install R Packages
RUN Rscript -e "install.packages('testthat')" 
RUN Rscript -e "install.packages('docopt')"
RUN Rscript -e "install.packages('knitr')"
RUN Rscript -e "install.packages('dplyr')"
RUN Rscript -e "install.packages('readr')"
RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('cowplot')"
RUN Rscript -e "install.packages('ggridges')"


# install python packages   
RUN conda install requests 
RUN conda install docopt
RUN conda install numpy 
RUN conda install pandas 
RUN conda install scikit-learn
RUN conda install matplotlib
RUN conda install altair -y 

# Install Chromium
RUN apt-get update && \
    apt install -y chromium && \
    apt-get install -y libnss3 && \
    apt-get install unzip

# Install Chromedriver
RUN wget -q "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/bin/ && \
    rm /tmp/chromedriver.zip && chown root:root /usr/bin/chromedriver && chmod +x /usr/bin/chromedriver


# Put Anaconda Python in PATH
ENV PATH="/opt/conda/bin:${PATH}"

CMD ["/bin/bash"]
