FROM nickm543/pc-base

USER root

RUN apt-get update && \
    apt-get install -y \
        gcc \
        python3-full \
        python3-tqdm && \
    rm -rf /var/lib/apt/lists/*

