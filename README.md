Optimal experimental design on adaptive observation experiments

## Motivation

This repository shows the story of the adaptive observation experiments by 40-variable Lorenz-96 model: 
$$\frac{dx_i}{dt}=(x_{i+1}-x_{i-2})x_{i-1} - x_i + F,$$ 
where $F$ is the forcing and the variable $x_i$ is taken to be periodic: $x_{i+n} = x_{i}$.
In this study, we set $n=40$ and $F=8$.  The
nodes numbered from 1 to 20 lie over the ocean, and those from 21 to 40 lie over
the land (Fig. 1).

<p align="center" width="100%">
<img src="./Figure/Lorenz96_40D.png" width="40%">
</p>
<p align="center" width="100%">
<em>Figure 1. An illustration on the 40-variable Lorenz-96 model </em>
</p>

All land sites receive observations very 6 hours; while there are no routine observations all over the ocean. 

**The objective of this study is to find one supplementary oceanic site which receives observation every 6 hour to provide the best forecast skills over the globe.** 

## Background

To reproduce the experiments by Lorenz and Emanuel (1998), I set the experiments totally based on the paper. 
The time step is 0.05 unit, equals to 6 h.
The total experiments last for 360 + 7200 + 40 time steps. 
L = 360 (i.e., 90 days) represents the transient behaivour. 
N = 7200 (i.e., 5 years) uses as the reference data (nature run or true state). 
M = 40 (i.e., 10 days) is the forecast range which will be verified. 


## Literature review

## Experimental settings

## Results and discussions

## Summary
