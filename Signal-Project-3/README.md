# Signal Project 1

## Section A: IPython Console from Spyder showing Name and NRP
      print ("Name: Hanin Ainussyamsi Prabowo")
      print ("NRP: 5009211036")
![Bagian-A](https://github.com/haninsyamsi036/Signal-Course/assets/144574915/7e3c4f69-3363-4eb3-85aa-c58df792d8d6)

## Section B: Savitzky-Golay Filter
      # -*- coding: utf-8 -*-
      """
      Created on Thu Sep 14 09:53:14 2023
      
      @author: user
      """

      import matplotlib.pyplot as plt
      import numpy as np
      mu, sigma = 0, 500
      x = np.arange(1, 100, 0.1)  # x axis
      z = np.random.normal(mu, sigma, len(x))  # noise
      y = x ** 2 + z # data
      #plt.plot(x, y, linewidth=2, linestyle="-", c="b")  # it include some noise

      from scipy.signal import savgol_filter
      w = savgol_filter(y, 101, 2)
      #plt.plot(x, w, 'b')  # high frequency noise removed

      #plot all
      fig, ax = plt.subplots(1,2)
      ax[0].plot(x, y, linewidth=2, linestyle="-", c="b")
      ax[1].plot(x, w, 'b')
![Bagian-B](https://github.com/haninsyamsi036/Signal-Course/assets/144574915/d4a0d593-53f0-4cbc-91f1-b73bcd2f318c)


## Section C: Last Commit Logs
![Bagian-C](https://github.com/haninsyamsi036/Signal-Course/assets/144574915/d0c1f0ac-39f3-485f-a554-57f02bfe410f)
