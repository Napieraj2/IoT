import numpy as np
import matplotlib.pyplot as plt

# Data
SNR = np.array([-15, -12, -9, -6, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])

BER_BPSK = np.array([0.429, 0.401, 0.361, 0.308, 0.239, 0.214, 0.185,
                     0.158, 0.131, 0.103, 0.079, 0.0565, 0.0378, 0.0228])

BER_QPSK_original = np.array([0.859, 0.802, 0.722, 0.615, 0.478, 0.425,
                              0.373, 0.316, 0.262, 0.206, 0.156, 0.113,
                              0.0758, 0.0458])

BER_QPSK_gray = np.array([0.46, 0.441, 0.411, 0.367, 0.302, 0.274,
                          0.244, 0.213, 0.179, 0.146, 0.111, 0.0814,
                          0.055, 0.0333])

# Plot
plt.figure()
plt.semilogy(SNR, BER_BPSK, 'o-', label='BPSK')
plt.semilogy(SNR, BER_QPSK_original, 's-', label='QPSK (Original)')
plt.semilogy(SNR, BER_QPSK_gray, '^-', label='QPSK (Gray)')

plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.title('BER vs SNR')
plt.grid(True, which='both')
plt.legend()
plt.tight_layout()
plt.show()