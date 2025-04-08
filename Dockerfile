FROM ubuntu

# Install any tools or configure anything:
RUN apt update

# Add exec-suid to the image (important for Python challenges to be able to read the flag):
ADD --chown=0:0 --chmod=6755 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid