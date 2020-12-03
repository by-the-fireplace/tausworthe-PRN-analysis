"""
- Statistical tests on the generator to see whether it gives
  PRN’s that are approximately i.i.d. Uniform(0,1).

- Plot adjacent PRN’s (Ui, Ui+1), i = 1, 2, . . ., on the unit
  square to see if there are any patterns.

- Generate a few Nor(0,1) deviates using Unif(0,1)’s from the
  Tausworthe generator
"""

from scipy import stats
from utils import *

__author__ = "James Wang"
__email__ = "jq.wang1214@gmail.com"


def ks(a: np.array, name: str="uniform") -> Tuple[float]:
	"""
	Perform Kolmogorov-Smirnov test for goodness of fit on a given numpy array

	Performs a test of the distribution F(x) of an observed random variable 
	against a given distribution G(x). Under the null hypothesis, the two 
	distributions are identical, F(x)=G(x).
	"""
	ks_value, p_value = stats.kstest(a, name)
	return ks_value, p_value

def main() -> None:
	SIZE = 100

	print(f"1. Generating {SIZE} PRNs using TG ...", file=sys.stderr, end=" ")
	tg = TG(length=100)
    tg.seed(r=5, q=17, chunk_len=19)
    a = tg.random()
    print("done!", file=sys.stderr)

    print(f"2. Generating a histogram ...", file=sys.stderr, end=" ")
    visualize_dist(a)
    print("done!", file=sys.stderr)

    print(f"3. Plotting the pattern ...", file=sys.stderr, end=" ")
    visualize_pattern(a)
    print("done!", file=sys.stderr)














