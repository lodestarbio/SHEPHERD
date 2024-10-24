FROM python:3.12.7-bullseye AS base

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Versions
ARG MINIFORGE_VERSION="24.7.1-2"
ENV MINIFORGE_VERSION=${MINIFORGE_VERSION}

# Install OS-level dependencies
RUN apt-get update && apt-get install -y \
    wget git \
    && rm -rf /var/lib/apt/lists/*

# Make /opt directory for eveything
RUN mkdir -p /opt
WORKDIR /opt

FROM base AS conda
# Install Miniforge3 (mamba and conda)
RUN curl -L -O "https://github.com/conda-forge/miniforge/releases/download/${MINIFORGE_VERSION}/Miniforge3-${MINIFORGE_VERSION}-$(uname)-$(uname -m).sh" && \
    bash Miniforge3-${MINIFORGE_VERSION}-$(uname)-$(uname -m).sh -b -p /opt/miniforge3
COPY environment.yml /opt/environment.yml
RUN /opt/miniforge3/bin/conda env create -f /opt/environment.yml && \
    /opt/miniforge3/bin/conda init && \
    echo "conda activate shepherd" >> ~/.bashrc
COPY install_pyg.sh /opt/install_pyg.sh
RUN bash /opt/install_pyg.sh

# if you want to build it in, but easier to mount it
# ADD . /opt/app
# WORKDIR /opt/app