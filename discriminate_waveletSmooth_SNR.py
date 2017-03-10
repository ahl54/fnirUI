
# coding: utf-8

# In[63]:

get_ipython().magic('matplotlib inline')
#Discriminate wavelet reduction of motion noise
#Authored by: Connor Johnson
#Last modified: 3/10/2017 by Anna

# file processing
import os, ast
# signal processing
import pywt
import numpy as np
import math
# visualization
import matplotlib.pyplot as plt

# Depreciated to avoid fortran dependency
#from statsmodels.robust import mad

def mad(data, axis=None):
    # median absolute deviation
    return np.median(np.absolute(data - np.median(data,axis)), axis)

def waveletSmooth(signal, wavelet, level=1):
    # returns y a rectified and smoothed signal
    
    # multilevel wavelet decomposition generates coefficients
    coeff = pywt.wavedec(signal, wavelet, mode="per") #by default last axis is used
    # calc a threshold to exclude outliers beyond one median absolute deviation of gaussian
    sigma = mad(coeff[-level])
    signal_len = len(signal)
    threshold = sigma * np.sqrt(2*np.log(signal_len))
    # Note: alternative distance metrics can be used to vary the threshold
    coeff[1:] =(pywt.threshold(i , value=threshold, mode="soft") for i in coeff[1:])
    #reconstruct signal
    y = pywt.waverec(coeff, wavelet, mode="per")
    return y
    
def rms(data):
    # returns the root mean squared amplitude of the data
    baseline = np.median(data)
    return np.sqrt(((data - baseline)**2).mean())
    
def signal_to_noise(signal, noise):
    # returns the signal to noise ratio
    # assumption: Equal impedance

    Asignal = rms(signal)
    Anoise = rms(noise)
    
    if Anoise == 0:
        SNRdb = float('nan')
    else:
        SNRdb = 10*math.log10((Asignal/Anoise)**2)
    return SNRdb
    
    
raw_signal_path = """raw_signal/"""

for filename in os.listdir(raw_signal_path):
        signal = []
        if (not filename.endswith('.ipynb_checkpoints')):
            
            # fetch signal from file
            with open(raw_signal_path + filename) as fin:
                signal = ast.literal_eval(fin.read())
                
                # format list of tuples (time, amplitude) as numpy array
                dt=np.dtype('float,float')
                signal = np.array(signal, dtype=dt)
                                
                raw = [amplitude[1] for amplitude in signal]

            fin.close()
            
            # Eight part gaussian wavelet decomposition on amplitudes
            # f(t) = y(t) + e(t), where y(t) is the signal and e(t) is the noise
            wavelet_type = 'db2' # Daubechies wavelet mapping
            # smoothing level maxes out at 7
            filt = waveletSmooth(raw, wavelet_type, level=7)
            SNRdb = signal_to_noise(raw, filt)
           
            # visualize
            p1, = plt.plot(raw, color="b", alpha=0.5, label='raw_signal')
            p2, = plt.plot(filt, color="b", label='filtered')
            SNR_report = ('SNRdB: ', '%.3f'%(SNRdb))
            plt.legend([p1, p2], ['raw_signal', 'filtered'], loc=0, title=SNR_report)
            plt.title('Raw & Filtered Signal Overlay ' + filename )
            plt.xlabel('Time (ms)')
            plt.ylabel('Amplitude (mV)')
            plt.grid()
            plt.show()


# In[ ]:



