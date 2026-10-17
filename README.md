# EEG Motor Imagery Classification with Mamba SSM

Bachelor's capstone project, Robotics Engineering, Nazarbayev University (2024–2025).
Author: **Rakhat Ospanov** · Supervisor: Prof. Berdakh Abibullaev

I tested whether a **Mamba state-space model** can replace the Transformer encoder in a compact EEG classifier for brain–computer interfaces. Mamba scales linearly with sequence length, which matters for long EEG windows and for running on small hardware.

## Result

| Task | Data | Model | Params | Test accuracy |
|---|---|---|---|---|
| Left vs right fist motor imagery (binary) | PhysioNet EEGMMIDB, subjects 1–79, 64 channels | CNN → Mamba → MLP | 293K | **70.9%** |

The data is split 81 / 9 / 10 (train / val / test) in recording order, without shuffling. Because epochs are ordered by subject, the test set comes mostly from the last ~8 subjects, who were not seen in training. This is closer to a cross-subject result than a within-subject one.

## Model

```
EEG (64 ch × 497 samples)
  → Conv1d(64→64, k=11) → BatchNorm → ReLU → Dropout   # spatial/temporal filtering
  → Conv1d(64→128, k=11) → BatchNorm
  → Mamba(d_model=128, d_state=64, d_conv=4, expand=2) # sequence modelling over time
  → mean over time
  → MLP(128→32→1)                                      # left / right
```

Training: Adam, lr 5e-4 with step decay (×0.1 at 25/50/75%), batch size 10, 100 epochs, PyTorch Lightning.

## Data

[EEG Motor Movement/Imagery Dataset](https://physionet.org/content/eegmmidb/1.0.0/) (Schalk et al., 2004). I use runs 4, 8 and 12 (imagined left/right fist), window 1.0–4.1 s after cue, 160 Hz. After dropping 178 bad epochs, 3,377 trials remain.

## Repository layout

```
notebooks/
  eeg_mi_cnn_mamba_mlp.ipynb   # main experiment (the 70.9% result)
experiments/
  ctnet_mamba/                 # CTNet with its Transformer blocks swapped for Mamba (exploratory)
requirements.txt
```

## Running it

`mamba-ssm` needs **Linux and an NVIDIA GPU** (it compiles CUDA kernels). I ran everything on Google Colab.

```bash
pip install -r requirements.txt
```

Then download EEGMMIDB and set `base_data_path` in the *Dataset* section of the notebook.

I also tried to build `mamba-ssm` natively on Windows (Python 3.10, custom wheels for `causal-conv1d` and Triton) and could not get a stable build. Linux was the practical path.

## Credits

- The data pipeline and training wrapper in the main notebook are adapted from [reshalfahsi/eeg-motor-imagery-classification](https://github.com/reshalfahsi/eeg-motor-imagery-classification) (CNN + Transformer + MLP). My change is the Mamba block in place of the Transformer, plus the multi-subject setup.
- `experiments/ctnet_mamba/` builds on **CTNet** by Wei Zhao et al. (convolutional Transformer for motor imagery EEG); `utils.py` comes from that project.
- Mamba: [state-spaces/mamba](https://github.com/state-spaces/mamba) (Gu & Dao, 2023), installed from PyPI.
