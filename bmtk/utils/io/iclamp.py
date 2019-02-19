import os
import sys
import csv

import pandas as pd
import numpy as np

def IClampInput(object):
    def __init__(self, gids, amplitude, delay, duration):
        self.df = pd.DataFrame(data={'gids':gids, 'amplitude':amplitude, 'delay':delay, 'duration':duration}, index=gids)
        self.stim_dict = {}
        # self.gids = gids
        # self.amplitude = dict(zip(gids, amplitude))
        # self.delay = dict(zip(gids, delay))
        # self.duration = dict(zip(gids, duration))

    @classmethod
    def from_csv(cls, input_file):
        return pd.read_csv(input_file, index_col='gid', sep=' ')

    def amplitude(self, gid):
        return self.df.amplitude.iat(gid)

    def delay(self, gid):
        return self.df.delay.iat(gid)

    def duration(self, gid):
        return self.df.duration.iat(gid)

    def gids(self):
        return self.df.index.values
    
    def to_csv(self, file_path):
        df.to_csv(file_path, sep=' ')

    def attach_current(self, cell):
        self.stim_dict
        for gid in gids:
            stim = h.IClamp(cell.hobj.soma[0](0.5))
            stim.delay = self.delay(gid)
            stim.dur = self.duration(gid)
            stim.amp = self.amplitude(gid)
            stim_dict[gid] = stim
        return self.stim_dict