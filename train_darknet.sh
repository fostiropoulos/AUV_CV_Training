#export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
./darknet/darknet detector train data/obj.data cfg/yolov3_tiny.cfg cfg/yolov3-tiny.conv.15
