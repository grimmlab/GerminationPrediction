FROM nvcr.io/nvidia/tensorflow:19.09-py3

# install build utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get -y upgrade

RUN useradd -ms /bin/bash GerminationPrediction
USER GerminationPrediction
WORKDIR /home/GerminationPrediction

#RUN apt-get install -y protobuf-compiler python-pil python-lxml python-tk && \
#    pip install Cython && \
#    pip install contextlib2 && \
#    pip install jupyter && \
#    pip install matplotlib && \
#    pip install pycocotools && \
#    pip install opencv-python && \
#    pip install tensorflow && \
#    pip install Pillow && \
#    pip install requests

#COPY --chown=GerminationPrediction . /home/GerminationPrediction/

# Compile protobuf configs
#RUN (cd /home/GerminationPrediction/models/research/ && protoc object_detection/protos/*.proto --python_out=.)
#WORKDIR /home/GerminationPrediction/models/research/

#COPY bashrc /etc/bash.bashrc
#RUN chmod a+rwx /etc/bash.bashrc


#RUN pip3 install Cython jupyter matplotlib pillow lxml pandas contextlib2 cmake numpy==1.17.5
RUN pip3 install tensorflow-gpu==1.14.0
RUN mkdir -p cocoapi
WORKDIR cocoapi
RUN git clone https://github.com/cocodataset/cocoapi.git
WORKDIR /cocoapi/PythonAPI
RUN make
RUN cp -r pycocotools /tools/models/research/
WORKDIR /tools/models/research/
#RUN ls
RUN protoc object_detection/protos/*.proto --python_out=.
RUN pwd
RUN export PYTHONPATH=$PYTHONPATH:/tools/models/research:tools/models/research/slim


#TODO: run tensorboard (-p 6006:6006)


ENV TF_CPP_MIN_LOG_LEVEL 3