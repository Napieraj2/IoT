"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):

    def __init__(self, window_size=100000):
        gr.sync_block.__init__(
            self,
            name='BER for QPSK',
            in_sig=[np.byte, np.byte],
            out_sig=[np.float32]
        )

        self.window_size = int(window_size)
        self.window = np.zeros(self.window_size, dtype=np.float32)
        self.win_ptr = 0


    def work(self, input_items, output_items):

        a = input_items[0].astype(np.uint8)
        b = input_items[1].astype(np.uint8)

        # sync_block guarantees same input lengths
        n = len(a)

        # XOR to find bit mismatches
        err = (a ^ b) & 0x03

        # Count bit errors (0,1,2)
        biterrors = ((err & 0x01) + ((err & 0x02) >> 1)).astype(np.float32)

        # Update cyclic window
        for k in range(n):
            self.window[self.win_ptr] = biterrors[k]
            self.win_ptr = (self.win_ptr + 1) % self.window_size

        # True BER per bit (2 bits per QPSK symbol)
        BER = np.sum(self.window) / (2*self.window_size)

        # Must output exactly n samples
        output_items[0][:] = BER

        return len(output_items[0])
