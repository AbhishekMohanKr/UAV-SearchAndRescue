<h1 align="center">UAV-SearchAndRescue</h1>

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/AbhishekMohanKr/UAV-SearchAndRescue?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/AbhishekMohanKr/UAV-SearchAndRescue)
![GitHub issues](https://img.shields.io/github/issues-raw/AbhishekMohanKr/UAV-SearchAndRescue)
![GitHub pull requests](https://img.shields.io/github/issues-pr/AbhishekMohanKr/UAV-SearchAndRescue)
![GitHub](https://img.shields.io/github/license/AbhishekMohanKr/UAV-SearchAndRescue)
![Github](https://img.shields.io/github/contributors/AbhishekMohanKr/UAV-SearchAndRescue)
<a href="https://twitter.com/AbhishekMohanKr">
    <img alt="Twitter: AbhishekMohanKr" src="https://img.shields.io/twitter/follow/AbhishekMohanKr.svg?style=social" target="_blank" />



## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Functions](#functions)
- [Usage](#usage)
- [Authors](#authors)
- [License](#license)

## About

It is an computer vision AI based project to process images taken by UAS (unmanned aerial system) for SAR(Search and Rescue).

As we are priotising the houses in burnt area and green area.
<p align="center">
  <img src="https://github.com/AbhishekMohanKr/UAV-SearchAndRescue/blob/main/source%20code/1.png">

## Getting Started

By installing python and some python libraries.You need basic knowledge of python, opencv, numpy.

### Prerequisites

This project need opencv and numpy 
- [OpenCV](https://www.opencv.org)
- [Numpy](https://www.numpy.org)

### Installing

install opencv by coping command in cli
```sh
    pip install opencv
```

install numpy
```sh
    pip install numpy
```

## Functions

Explanation of several functions used in the program.

### 1. change_color()
This function is used to change the color of area for better user understanding.
It takes four attributes image, lower HSV value of color, upper HSV value of color.

<img src="https://github.com/AbhishekMohanKr/UAV-SearchAndRescue/blob/main/source%20code/1.png" width="300" height="300"> <img src="https://github.com/AbhishekMohanKr/UAV-SearchAndRescue/blob/main/source%20code/Changed%20Images/image1.png" width="300" height="300">


### 2. crop()
This function is used to crop the area with specific background color.
It takes four attributes image, lower HSV value of color, upper HSV value of color.
<img src="https://github.com/AbhishekMohanKr/UAV-SearchAndRescue/blob/main/source%20code/1.png" width="300" height="300"><img src="https://github.com/AbhishekMohanKr/UAV-SearchAndRescue/blob/main/source%20code/cropped1.png" width="300" height="300">

### 3. count()
This function is used to count no of triangles of specific color on specific background.
It takes four attributes image, lower HSV value of color, upper HSV value of color.

## Usage
Use for satellite imaging processing in natural calimities.

## Authors

  - **Abhishek Mohan**

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this project.

## License

This project is licensed under the [GPL-3.0](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

