"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='QPSK Decoder',
            in_sig=[np.complex64],
            out_sig=[np.uint8]
        )

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        I = (np.real(x) >= 0).astype(np.uint8)
        Q = (np.imag(x) >= 0).astype(np.uint8)

        # quad code: BL=0, BR=1, TL=2, TR=3
        quad = (Q << 1) | I

        # map quad -> QPSK_MAP index: BL->0, BR->1, TL->2, TR->3
        lut = np.array([0, 1, 2, 3], dtype=np.uint8)
        y[:] = lut[quad]

        return len(output_items[0])
