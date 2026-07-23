# Enhancing YOLO-based SAR Ship Detection with Attention Mechanisms

Official implementation accompanying the paper:

> **Enhancing YOLO-Based SAR Ship Detection with Attention Mechanisms**  
> Ranyeri do Lago Rocha, Felipe A. P. de Figueiredo  
> *Remote Sensing*, 2025.

---

# Overview

Synthetic Aperture Radar (SAR) imagery plays a fundamental role in maritime surveillance due to its ability to acquire images regardless of weather conditions or daylight. However, detecting ships in SAR images remains challenging because of:

- small vessel dimensions;
- speckle noise;
- complex coastal environments;
- cluttered backgrounds;
- large scale variation.

This repository investigates how modern attention mechanisms can improve recent YOLO architectures for SAR object detection.

Three attention modules were evaluated:

- CBAM
- Bi-Level Routing Attention (BRA)
- Swin Transformer

using the latest YOLO architectures:

- YOLOv10
- YOLOv11
- YOLOv12

The work evaluates both **adding** and **replacing** attention layers inside the backbone and neck of the networks to identify the best architecture for SAR imagery.

---

# Main Contributions

- First systematic evaluation of attention mechanisms on YOLOv11 and YOLOv12 for SAR object detection.
- Comprehensive ablation study evaluating different insertion and replacement positions.
- Cross-dataset validation.
- Evaluation on four SAR datasets.
- Improved detection of small ships.
- Reduced computational complexity while improving accuracy.

---

# Attention Mechanisms

The following attention modules were investigated.

## CBAM

Convolutional Block Attention Module using sequential

- Channel Attention
- Spatial Attention

to improve feature representation while suppressing irrelevant SAR background.

---

## BRA

Bi-Level Routing Attention introduces sparse dynamic attention capable of preserving global and local contextual information while reducing unnecessary computation.

---

## Swin Transformer

Window-based self-attention using shifted windows for hierarchical feature extraction and long-range dependency modeling.

---

# Evaluated Architectures

Baseline models:

- YOLOv10n
- YOLOv11n
- YOLOv12n

Modified models include combinations of:

- Attention addition
- Attention replacement
- Multiple insertion positions
- Small-object detection head (TODL)

---

# Datasets

Experiments were performed using four public SAR datasets.

| Dataset | Purpose |
|----------|----------|
| SSD | SAR Ship Detection |
| SSDD | SAR Ship Detection Dataset |
| SADD | SAR Aircraft Detection Dataset |
| MSAR | Multi-Class SAR Dataset |

These datasets contain different object scales, cluttered environments and challenging maritime scenarios.

---

# Experimental Strategy

The experiments were divided into three phases.

## 1. Baseline Evaluation

Performance comparison among:

- YOLOv10
- YOLOv11
- YOLOv12

---

## 2. Attention Addition

Evaluation of adding CBAM, BRA and Swin modules at multiple locations inside the architecture.

---

## 3. Attention Replacement

Replacement of native YOLO attention blocks with:

- CBAM
- BRA
- Swin

This strategy produced the best overall results.

---

# Best Configuration

The best model obtained in this work was:

**YOLOv12n + CBAM replacing Layer 4**

Main results:

- mAP@0.5: **98.0%** (SSD)
- mAP@0.5: **98.6%** (SSDD)
- Lower computational cost
- Better small-object detection
- Real-time inference

---

# Repository Organization

```
.
├── 
├── README.md
```

---

# Paper

If this repository contributes to your research, please cite:

```bibtex
@article{Rocha2025AttentionSAR,
  author  = {Ranyeri do Lago Rocha and Felipe A. P. de Figueiredo},
  title   = {Enhancing YOLO-Based SAR Ship Detection with Attention Mechanisms},
  journal = {Remote Sensing},
  year    = {2025},
  volume  = {17},
  number  = {3170},
  doi     = {10.3390/rs17183170}
}
```

---

# License

This repository is released for academic and research purposes.

Please cite the associated publication when using this work.
