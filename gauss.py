# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-09-17 16:51:18
# Last Modified time: 2020-09-17 20:11:31


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


class Gaussian():
	"""
	Creates a 1D gaussian given mean and variance

	'mu' is the mean
	'sigma' is the variance

	"""
	def __init__(self,mu,sigma,size,test):
		self.mu=mu
		self.sigma=sigma
		self.size=size
		self.test=test
		self.mesh()
		
	def mean(self):
		return self.mu

	def variance(self):
		return self.sigma

	def mesh(self):
		self.x = np.linspace(int(self.size[0])+self.mu, int(self.size[1])+self.mu, num=100)
		self.z = 1./(np.sqrt(2.*np.pi)*self.sigma)*np.exp(-np.power((self.x - self.mu)/self.sigma, 2.)/2)
		self.y=np.ones(len(self.x))*self.test
		

	def plot(self):
		plt.figure(1)
		plt.plot(self.x,self.z)

	def plot3d(self):
		fig=plt.figure(1)
		ax = fig.gca(projection='3d')
		xs=self.x
		ys=self.y
		zs=self.z
		
		ax.set_xlabel='x'
		ax.set_ylabel='y'
		ax.set_zlabel='z'
		plt.plot(xs, ys, zs)
		plt.pause(0.1)


if __name__=="__main__":
	
	sigma1=5
	size=np.array([-10,10])

	p1,p2=4,6
	lin=np.linspace(p1,p2,10)

	gauss_arr=[]

	for i in lin:
		gauss_arr.append(Gaussian(i,sigma1,size,i))

	for i in range(len(gauss_arr)):
		gauss_arr[i].plot3d()

	ze=np.ones(len(lin)).reshape(-1,1)
	lin=lin.reshape(-1,1)
	out=np.concatenate((lin,ze),axis=1)
	
	# plt.scatter(out[1],out[0],out[2])

	plt.show()
