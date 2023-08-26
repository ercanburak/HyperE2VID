import torch
from torch import nn

from .unet import UNetRecurrent


class E2VIDRecurrent(nn.Module):
    """
    Recurrent, UNet-like architecture where each encoder is followed by a ConvLSTM or ConvGRU.
    """

    def __init__(self, unet_kwargs):
        super().__init__()
        self.num_bins = unet_kwargs['num_bins']  # legacy
        self.num_encoders = unet_kwargs['num_encoders']  # legacy
        self.unetrecurrent = UNetRecurrent(unet_kwargs)
        self.prev_recs = None

    def reset_states(self):
        self.unetrecurrent.states = [None] * self.unetrecurrent.num_encoders
        self.prev_recs = None

    def forward(self, event_tensor):
        """
        :param event_tensor: N x num_bins x H x W
        :return: output dict with image taking values in [0,1], and
                 displacement within event_tensor.
        """
        if self.prev_recs is None:
            self.prev_recs = torch.zeros(event_tensor.shape[0], 1, event_tensor.shape[2], event_tensor.shape[3],
                                         device=event_tensor.device)
        output_dict = self.unetrecurrent.forward(event_tensor, self.prev_recs)
        self.prev_recs = output_dict['image'].detach()
        return output_dict
