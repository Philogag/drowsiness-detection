# **睡意检测**

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/jackaduma/CycleGAN-VC2)


This code is a **PyTorch** implementation for paper: [CycleGAN-VC2: Improved CycleGAN-based Non-parallel Voice Conversion](https://arxiv.org/abs/1904.04631]), a nice work on **Voice-Conversion/Voice Cloning**.


一种计算机视觉系统，该系统可以自动检测实时视频流中的驾驶员睡意状况，然后在驾驶员感到困倦时发出警报

**睡意检测**，通过检测眼皮对眼球的遮挡程度，判定是否困倦/有睡意/打瞌睡😂

，通过检测眼皮对眼球的遮挡程度，判定是否困倦/有睡意/打瞌睡😂

这项技术将对行业有所帮助，并且理想情况下可以减少与疲劳相关的事故。

------

## **使用OpenCV进行睡意检测**

### [**Project Page**](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/cyclegan-vc2/index.html)


To advance the research on non-parallel VC, we propose CycleGAN-VC2, which is an improved version of CycleGAN-VC incorporating three new techniques: an improved objective (two-step adversarial losses), improved generator (2-1-2D CNN), and improved discriminator (Patch GAN).


![network](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/cyclegan-vc2/images/network.png "network")

------

**This repository contains:** 

1. [model code](model_tf.py) which implemented the paper.
2. [audio preprocessing script](preprocess_training.py) you can use to create cache for [training data](data).
3. [training scripts](train.py) to train the model.
4. [Examples of Voice Conversion](converted_sound/) - converted result after training.

------

## **Table of Contents**

- [**睡意检测**](#睡意检测)
  - [**使用OpenCV进行睡意检测**](#使用opencv进行睡意检测)
    - [**Project Page**](#project-page)
  - [**Table of Contents**](#table-of-contents)
  - [**Requirement**](#requirement)
  - [**Usage**](#usage)
    - [**preprocess**](#preprocess)
    - [**train**](#train)
  - [**Pretrained**](#pretrained)
  - [**Demo**](#demo)
  - [**Reference**](#reference)
  - [**TodoList**](#todolist)
  - [**License**](#license)
  
------



## **Requirement** 

```bash
pip install -r requirements.txt
```
## **Usage**

### **preprocess**

```python
python preprocess_training.py
```
is short for

```python
python preprocess_training.py --train_A_dir ./data/S0913/ --train_B_dir ./data/gaoxiaosong/ --cache_folder ./cache/
```


### **train** 
```python
python train.py
```

is short for

```python
python train.py --logf0s_normalization ./cache/logf0s_normalization.npz --mcep_normalization ./cache/mcep_normalization.npz --coded_sps_A_norm ./cache/coded_sps_A_norm.pickle --coded_sps_B_norm ./cache/coded_sps_B_norm.pickle --model_checkpoint ./model_checkpoint/ --resume_training_at ./model_checkpoint/_CycleGAN_CheckPoint --validation_A_dir ./data/S0913/ --output_A_dir ./converted_sound/S0913 --validation_B_dir ./data/gaoxiaosong/ --output_B_dir ./converted_sound/gaoxiaosong/
```

------

## **Pretrained**

a pretrained model which converted between S0913 and GaoXiaoSong

download from [Google Drive](https://drive.google.com/file/d/1iamizL98NWIPw4pw0nF-7b6eoBJrxEfj/view?usp=sharing) <735MB>

------

## **Demo**

Samples:


[S0913(./data/S0913/BAC009S0913W0351.wav)](https://drive.google.com/file/d/14zU1mI8QtoBwb8cHkNdZiPmXI6Mj6pVW/view?usp=sharing)

[GaoXiaoSong(./data/gaoxiaosong/gaoxiaosong_1.wav)](https://drive.google.com/file/d/1s0ip6JwnWmYoWFcEQBwVIIdHJSqPThR3/view?usp=sharing)



[Converted from S0913 to GaoXiaoSong (./converted_sound/S0913/BAC009S0913W0351.wav)](https://drive.google.com/file/d/1S4vSNGM-T0RTo_aclxRgIPkUJ7NEqmjU/view?usp=sharing)

------

## **Reference**
1. **CycleGAN-VC2: Improved CycleGAN-based Non-parallel Voice Conversion**. [Paper](https://arxiv.org/abs/1904.04631), [Project](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/cyclegan-vc2/index.html)
2. Parallel-Data-Free Voice Conversion Using Cycle-Consistent Adversarial Networks. [Paper](https://arxiv.org/abs/1711.11293), [Project](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/cyclegan-vc/)
3. Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks. [Paper](https://arxiv.org/abs/1703.10593), [Project](https://junyanz.github.io/CycleGAN/), [Code](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
4. Image-to-Image Translation with Conditional Adversarial Nets. [Paper](https://arxiv.org/abs/1611.07004), [Project](https://phillipi.github.io/pix2pix/), [Code](https://github.com/phillipi/pix2pix)

------

## **TodoList**

- [x] Dataset
  - [ ] VC
  - [x] Chinese Male Speakers (S0913 from [AISHELL-Speech](https://openslr.org/33/) & [GaoXiaoSong: a Chinese star](https://en.wikipedia.org/wiki/Gao_Xiaosong))
- [x] Usage
  - [x] Training
  - [x] Example 
- [ ] Demo

------

## **License**

[MIT](LICENSE) © Kun