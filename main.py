import matplotlib.pyplot as plt
import torch
import pandas as pd
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("device: ", device)