import torch
import numpy as np

x = torch.rand(3, requires_grad=True)
print(x)

y = x + 3


# https://www.youtube.com/watch?v=c36lUUr864M
# timing 28:50