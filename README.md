# HyperE2VID: Improving Event-Based Video Reconstruction via Hypernetworks

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://ercanburak-evreal.hf.space/)
[![arxiv.org](http://img.shields.io/badge/cs.CV-arXiv%3A2305.06382-B31B1B.svg)](https://arxiv.org/abs/2305.06382/)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/hypere2vid-improving-event-based-video/video-reconstruction-on-event-camera-dataset)](https://paperswithcode.com/sota/video-reconstruction-on-event-camera-dataset?p=hypere2vid-improving-event-based-video)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/hypere2vid-improving-event-based-video/video-reconstruction-on-mvsec)](https://paperswithcode.com/sota/video-reconstruction-on-mvsec?p=hypere2vid-improving-event-based-video)

This is the official repository of our IEEE TIP paper **[HyperE2VID: Improving Event-Based Video Reconstruction via Hypernetworks](https://ieeexplore.ieee.org/document/10462903)** by [Burak Ercan](https://ercanburak.github.io/), [Onur Eker](https://github.com/ekeronur/), [Canberk Sağlam](https://github.com/CanberkSaglam/), [Aykut Erdem](https://aykuterdem.github.io/), and [Erkut Erdem](https://web.cs.hacettepe.edu.tr/~erkut/).

<div align="center">
  <a href="https://www.youtube.com/watch?v=BWEV56-E0mE"><img src="media/video_thumbnail.png" alt="HyperE2VID: Improving Event-Based Video Reconstruction via Hypernetworks" width="600"></a>
</div

In this work we present **HyperE2VID, a dynamic neural network architecture for event-based video reconstruction**. Our approach extends existing static architectures by using **hypernetworks** and **dynamic convolutions** to generate **per-pixel adaptive filters** guided by a **context fusion** module that combines information from event voxel grids and previously reconstructed intensity images. We show that this dynamic architecture can generate **higher-quality videos** than previous state-of-the-art, **while also reducing memory consumption and inference time**.

![Overview of our proposed HyperE2VID architecture](media/detailed.png "Overview of our proposed HyperE2VID architecture")

- Our HyperE2VID paper has been accepted by [IEEE Transactions on Image Processing](https://ieeexplore.ieee.org/document/10462903).
- For more details please see our [paper](https://arxiv.org/abs/2305.06382). 
- For qualitative results please see our [project website](https://ercanburak.github.io/HyperE2VID.html).
- For more results and experimental analyses of HyperE2VID, please see the [interactive result analysis tool of EVREAL](https://ercanburak-evreal.hf.space/).
- Model codes are published under the [model folder in this repository](model).
- The pretrained model of HyperE2VID can be found [here](https://drive.google.com/drive/folders/1UuGnKwSz5C9di-cVH1QzSFjgTRNqpYep).
- For evaluation and analysis of HyperE2VID model, please use the codes in [EVREAL repository](https://github.com/ercanburak/EVREAL).
- Instructions to generate training data can be found in the [datagen folder](datagen).
- Training codes will be published soon.

## Citations

If you use code in this repo in an academic context, please cite the following:

```
@article{ercan2024hypere2vid,
title={{HyperE2VID}: Improving Event-Based Video Reconstruction via Hypernetworks},
author={Ercan, Burak and Eker, Onur and Saglam, Canberk and Erdem, Aykut and Erdem, Erkut},
journal={IEEE Transactions on Image Processing},
year={2024},
volume={33},
pages={1826--1837},
doi={10.1109/TIP.2024.3372460},
publisher={IEEE}}
```

## Acknowledgements

- This work was supported in part by KUIS AI Center Research Award, TUBITAK-1001 Program Award No. 121E454, and BAGEP 2021 Award of the Science Academy to A. Erdem.
- This code borrows from or is inspired by the following open-source repositories:
  - https://github.com/uzh-rpg/rpg_e2vid
  - https://github.com/TimoStoff/event_cnn_minimal
  - https://github.com/ZeWang95/ACDA
