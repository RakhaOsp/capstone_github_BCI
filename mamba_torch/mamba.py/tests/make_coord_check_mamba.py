import torch
from torch.utils.data import Dataset, DataLoader

import sys
sys.path.append('..')
from mambapy.mamba import MambaConfig
from mambapy.lm import LM

from coord_check import get_coord_data, plot_coord_data

use_mup = True
lr = 2e-3

batch_size = 64
batch_len = 256
max_value = 100

widths = [64, 128, 256, 512, 1024]
n_layers = 8

class RandomDataset(Dataset):
    def __len__(self):
        return 9999999

    def __getitem__(self, idx):
        data = torch.randint(low=0, high=max_value, size=(batch_size, batch_len))
        x = data[:, :-1].int()
        y = data[:, 1:].long()
        return x, y

def lazy_model(width):
    config = MambaConfig(d_model=width, n_layers=n_layers, mup=use_mup, mup_base_width=widths[0], use_cuda=True)
    return lambda: LM(config, vocab_size=max_value).to("cuda")

models = {width: lazy_model(width) for width in widths}

dataset = RandomDataset()
loader = DataLoader(dataset, batch_size=None, shuffle=True)
iter_ = iter(loader)

optcls = lambda model: model.configure_optimizers(0.1, lr, (0.9, 0.95), "cuda")

df = get_coord_data(models, iter_, optcls, nsteps=10)

if use_mup:
    name = "mamba_mup.png"
else:
    name = "mamba.png"

plot_coord_data(df, legend="auto", save_to=name)
