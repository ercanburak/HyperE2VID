#!/bin/bash
for filename in $PWD/configs/config2d/*config2d.txt; do
 	echo "Processing $filename"
	rosrun esim_ros esim_node --v=1 --vmodule=data_provider_from_folder=10 --flagfile=$filename
done