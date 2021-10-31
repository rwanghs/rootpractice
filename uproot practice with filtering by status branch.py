#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install uproot awkward


# In[3]:


import pandas 
import uproot
import awkward
import matplotlib.pyplot as plt
import numpy as np


# In[7]:


file = uproot.open('trkana_signal.root')
file.keys()
tree = file['TrkAna;1']['trkana;1']
branch = np.array(tree['dem.'])
t = branch['status']
t2= branch['mom'] #values of momentum


# In[25]:


zipped_t = zip(t,t2)
sorted_t= sorted(zipped_t) #sorts status and dem together in 2d list. Column 1 = status, Column 2 = dem


x = np.array(sorted_t) #turns sorted values into an array
print(x)

vals = x[x[:,0] > 0] #select rows where only positive values of status is returned

momentum_vals = vals[:,1] #values to be plotted
print(np.mean(momentum_vals))


# In[29]:


file_bkg= uproot.open("trkana_signalAndBkg.root")
tree_bkg = file_bkg['TrkAna']['trkana;1']
branches2 = tree_bkg.arrays()['dem.']
tbkg= branches2['status']
tbkg2 = branches2['mom']

zipped_bkg = zip(tbkg,tbkg2)
sorted_bkg= sorted(zipped_bkg)
x_bkg = np.array(sorted_bkg)
vals_bkg = x_bkg[x_bkg[:,0] > 0]
momentum_vals_bkg = vals_bkg[:,1]

print(np.mean(momentum_vals_bkg))

plt.hist(momentum_vals, bins= 20, label = "without background", alpha =.5)
plt.hist(momentum_vals_bkg, bins= 20, label = "with background", alpha = .5)


# In[100]:


#UEM

branch_mu = np.array(tree['dmm.'])
t_mu=branch_mu['status']
t_mu2=branch_mu['mom']

zipped_mu = zip(t_mu,t_mu2)
sorted_mu= sorted(zipped_mu)
x_mu = np.array(sorted_mu)
vals_mu = x_mu[x_mu[:,0] > 0]

momentum_vals_mu = vals_mu[:,1]

#UEM BKG
branch_mu2 = np.array(tree_bkg['dmm.'])
t_mu_bkg=branch_mu2['status']
t_mu2_bkg=branch_mu2['mom']
zipped_mu_bkg = zip(t_mu_bkg,t_mu2_bkg)
sorted_mu_bkg= sorted(zipped_mu_bkg)
x_mu_bkg = np.array(sorted_mu_bkg)
vals_mu_bkg = x_mu_bkg[x_mu_bkg[:,0] > 0]
momentum_vals_mu_bkg = vals_mu_bkg[:,1]
fig, axs = plt.subplots(2)

axs[0].hist(momentum_vals, bins= 20, label = "no background ", alpha =.5)
axs[1].hist(momentum_vals_mu, bins = 20, label = 'no background', alpha = .5)
axs[0].set_title("e- momentum fit")

axs[0].hist(momentum_vals_bkg, bins= 20, label = "with background ", alpha = .5)
axs[1].hist(momentum_vals_mu_bkg, bins = 20, label = 'with background', alpha = .5)
axs[1].set_title("mu- momentum fit")

axs[0].legend()
axs[1].legend()
fig.tight_layout()

print("\n mean e- fit momentum(without background):", np.mean(momentum_vals))
print("Standard deviation e- momentum fit (without background):", np.std(momentum_vals) )

print(" \n mean e- fit momentum (with background):", np.mean(momentum_vals_bkg))
print("Standard deviation e- fit momentum (with background):", np.std(momentum_vals_bkg))

print(" \n mean mu- fit momentum (with background):", np.mean(momentum_vals_mu))
print("Standard deviation mu- fit momentum (with background):", np.std(momentum_vals_mu))

print(" \n mean mu- fit momentum(without background):", np.mean(momentum_vals_mu_bkg))
print("Standard deviation mu- momentum fit (without background):", np.std(momentum_vals_mu_bkg) )


# In[ ]:




