

FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest
RUN pip3 install pytest-testdox mock && npm i breathecode-cli@1.1.81 -g
