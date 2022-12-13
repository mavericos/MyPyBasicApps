import torch
import torchvision
from torch.utils.data import Dataset
import numpy as np

class WineDataset(Dataset):

    def __init__(self, transform=None):
        xy = np.loadtxt('wine.csv', delimiter=",", dtype=np.float32, skiprows=1)
        self.x = torch.from_numpy(xy[:, 1:])

        # node that we do not convert to tensor here
        self.x = xy[:, 1:]
        self.x = xy[:, [0]]

        self.transofom = transform

    def __getitem__(self, index):
        sample = self.x[index], self.y[index]

        if self.transofrm:
            sample = self.transofom(sample)

        return sample

    def __len__(self):
        return self.n_samples

    class ToTensor:
        def __call__(self, sample):
            inputs, targets = sample
            return torch.from_numpy(inputs), torch.from_numpy(targets)

    dataset = WineDataset(tranform=ToTensor)

    # https://www.youtube.com/watch?v=c36lUUr864M   2:19:20