# FNIR UI
# Beer Lambert Law
# Author: Anna Lu
# Last Modified: 11-2-2016 by Anna Lu

# 	Background:
#  transmittance of material sample is related to its optical depth (tau) and
#  to its absorbance A

from math import exp
from math import pow
from scipy import constants

# initialize variables
phi_t = 0 # radiant flux transmitted
phi_i = 1 # radiant flux received
tau = 0 # optical depth
A = 0 # 

# output variables
T_1 = phi_t / phi_i # (T)ransmittance
T_2 = exp(-tau) # (T)ransmittance = e^(-tau)
T_3 = pow(10, -A) # (T)ransmittance = 10^(-A)


# TODO: Identify as known or to be calculated
# The following are attributes of the attenuating species i in the material
# sample 

N = 0 # attenuating species in the material sample

omega_i = 0 # attenuation cross section
n_i = 0 # number density
epsilon_i = 0 # molar attenuation coeffeicient
c_i = 0 # amount concentration
l = 0 # path length of the beam of light


# N_A is Avogadro's constant 

# episilon_i = N_A / ln(10) * omega_i

# c_i = n_i/N_A









