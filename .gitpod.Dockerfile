FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.4.2 pytest-testdox mock
RUN npm i learnpack@0.1.14 -g && learnpack plugins:install learnpack-python@0.0.35
