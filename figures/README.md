# Figures Folder

This folder stores figures and plots exported from Jupyter notebooks.

---

## Usage

When running the notebooks, save any generated plots here using:

```python
import matplotlib.pyplot as plt
plt.savefig('../figures/your_figure_name.png', dpi=150, bbox_inches='tight')
```

---

## Expected Contents

As the project progresses, this folder may include:
- CSI amplitude time-series plots (normal vs. fall-like)
- Smoothed/filtered signal comparison plots
- Feature distribution plots
- Confusion matrix heatmaps

---

> All figures in this repository are generated from **synthetic, simulated data** and are for research and demonstration purposes only.
