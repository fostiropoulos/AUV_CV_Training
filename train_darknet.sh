#export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
./darknet/darknet detector train data/obj.data yolov3_tiny.cfg yolov3-tiny.conv.15
