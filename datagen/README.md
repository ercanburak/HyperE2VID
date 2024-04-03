## Generating Training Dataset

* The training set is generated using the ESIM event simulator. Therefore, the first step is to install ESIM as described in [here](https://github.com/uzh-rpg/rpg_esim/wiki/Installation). You must have ESIM sourced (command `ssim`, if you followed the install instructions). 

* We use the [Multi Objects 2D](https://github.com/uzh-rpg/rpg_esim/wiki/Multi-Objects-2D-renderer) rendering engine of the ESIM to create the flying chairs style sequences of training data. The dataset contains 280 sequences, 10 s in length. These sequences will be created by ESIM with the config and scene files given in [datagen/configs](datagen/configs). These config and scene files are the ones shared by the authors of ECCV 2020 paper "Reducing the Sim-to-Real Gap for Event Cameras" (except for the absolute filepaths), and they generate the same training dataset used in the paper.

* The training set uses COCO images. Specifically, some images from the ``unlabeled2017`` split is used, so we should [download this split](http://images.cocodataset.org/zips/unlabeled2017.zip). These images are used for background and foreground objects of the dataset. We also use some additional custom foreground objects, which should be downloaded from [here](https://drive.google.com/drive/folders/1F6fNgZFmMvGkw6sAwDFE7j8Q7EH3TMve?usp=sharing). The exact images that will be used by ESIM can be seen in ``autoscene.txt`` files under ``datagen/configs/``.

* ESIM requires the background images given in scene files to be jpg images, and foreground images to be 4 channel (BGRA) png images. Since some of our foreground images are from COCO dataset and in jpg format, we should convert those images to png. For this we have the script ``datagen/convert_required_jpg_to_png.py``.  This script converts only the required COCO images to png. The required images are read from the ``datagen/cocopng.txt`` file (whose lines are those taken from all the 281 scene file that will be used). Folder paths for jpg and png images should also be set in ``jpg_path`` and ``png_path`` variables in ``datagen/convert_required_jpg_to_png.py``.

* After preparing all the images (COCO jpg, custom foreground png, and COCO png), we should fix their exact paths in all the ``autoscene.txt`` files under [datagen/configs](datagen/configs).

* We should also fix the paths in config files under [datagen/configs/config2d](datagen/configs/config2d). The paths to be fixed are the scene files and bag files that will be generated.

* After installing and sourcing ESIM, preparing all the images and fixing all the paths, and starting a rosmaster node at a separate tab with the command ``roscore``, we are ready to run the ``datagen/generate_ecnn_data.sh`` script. 

```
./generate_ecnn_data.sh
```

This script processes config files under ``datagen/config`` one by one and generates a rosbag file for each one of them. This will take a long time (from several hours to one day). After finished, there should be 280 rosbag files, which are at least a few hundred megabytes each. 
