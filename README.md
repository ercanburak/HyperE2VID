# HyperE2VID: Improving Event-Based Video Reconstruction via Hypernetworks

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://ercanburak-evreal.hf.space/)
[![arxiv.org](http://img.shields.io/badge/cs.CV-arXiv%3A2207.02696-B31B1B.svg)](https://arxiv.org/abs/2305.06382/)

This is the official repository of our paper titled **[HyperE2VID: Improving Event-Based Video Reconstruction via Hypernetworks](https://arxiv.org/abs/2305.06382)** by [Burak Ercan](https://ercanburak.github.io/), [Onur Eker](https://github.com/ekeronur/), [Canberk Sağlam](https://github.com/CanberkSaglam/), [Aykut Erdem](https://aykuterdem.github.io/), and [Erkut Erdem](https://web.cs.hacettepe.edu.tr/~erkut/).

<div align="center">
  <a href="https://www.youtube.com/watch?v=BWEV56-E0mE"><img src="media/video_thumbnail.png" alt="HyperE2VID: Improving Event-Based Video Reconstruction via Hypernetworks" width="600"></a>
</div

In this work we present **HyperE2VID, a dynamic neural network architecture for event-based video reconstruction**. Our approach extends existing static architectures by using **hypernetworks** and **dynamic convolutions** to generate **per-pixel adaptive filters** guided by a **context fusion** module that combines information from event voxel grids and previously reconstructed intensity images. We show that this dynamic architecture can generate **higher-quality videos** than previous state-of-the-art, **while also reducing memory consumption and inference time**.

![Overview of our proposed HyperE2VID architecture](media/detailed.png "Overview of our proposed HyperE2VID architecture")

For more details please see our [paper](https://arxiv.org/abs/2305.06382). 

For qualitative results please see our [project website](https://ercanburak.github.io/HyperE2VID.html).

For more results and experimental analyses of HyperE2VID, please see the [interactive result analysis tool of EVREAL](https://ercanburak-evreal.hf.space/).

Codes will be published soon.

## Citations

If you use code in this repo in an academic context, please cite the following:

```
@article{ercan2023hypere2vid,
title={{HyperE2VID}}: Improving Event-Based Video Reconstruction via Hypernetworks},
author={Ercan, Burak and Eker, Onur and Saglam, Canberk and Erdem, Aykut and Erdem, Erkut},
journal={arXiv preprint arXiv:2305.06382},
year={2023}
```

## Acknowledgements

This work was supported in part by KUIS AI Center Research Award, TUBITAK-1001 Program Award No. 121E454, and BAGEP 2021 Award of the Science Academy to A. Erdem.

