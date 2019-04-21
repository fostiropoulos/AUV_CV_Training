#export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64

./darknet detector test data/obj.data yolov3-tiny_pill.cfg backup/yolov3-tiny_pill_last.weights -ext_output $1
