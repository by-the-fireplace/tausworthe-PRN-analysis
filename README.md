# Implementation of the Tausworthe pseudo-random number generator

An introduction to Tausworthe PRN generator:

https://homes.luddy.indiana.edu/kapadia/project2/node9.html


First setup conda virtual environment:

```
cd tausworthe-PRN-analysis
conda env create -f environment.yml
conda activate tausworthe
```

To repeat the analysis, changing the value of `SIZE` in `analysis.py` and run `python analysis.py`. 

Figures will be saved in `./figs` and statistical reports will be saved in `./kstests`

