# Kursi - Plastic Recycling Object Identifier

## Overview
Kursi is a project to develop an object identifier module that classifies plastic objects into three categories: black, transparent, and colorful. The system assigns each object to the correct conveyor belt for efficient recycling:
- Black → Conveyor Belt A
- Transparent → Conveyor Belt B
- Colorful → Conveyor Belt C

The classification is based on analyzing image brightness and color saturation using OpenCV in Python.

## Dataset
- The dataset contains 10–20 images per category.
- Images are organized into folders: `black/`, `transparent/`, and `colorful/`.

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

## Installation
Install the required packages using pip:

```bash
pip install opencv-python numpy
