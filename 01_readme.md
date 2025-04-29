In 01.py an analysis of the speed of sorting in conducted for three sorting algorithms.

The algorithms in question are merge sort, insertion sort and Tim sort (the default sorting algorithm used in Python).

From running the analysis using the timit functionality it is evident that there is a varying performance in the runs and that it is not always guaranteed that one algorithm will always come out in top.

The factors that play a role in the efficiency of the sorting algorithm that were possible to analyze in this exercise was the size of the dataset being sorted. 

An overall finding was that for a relatively medium sized dataset of 10,000 elements we saw that the insertion sort algorithm outperformed the others, with Timsort coming in second.
merge_sort:        10.88123512500897 seconds,
insertion_sort:    9.955382250016555 seconds,
timsort:           10.050602875067852 seconds,

In a small dataset of 100 we saw Tim sort marginally outperform the other algorithms with Merge Sort once again being the slower algorithm of the group.
merge_sort:        0.19867499999236315 seconds,
insertion_sort:    0.18750149989500642 seconds,
timsort:           0.1869331250200048 seconds,

Finally on a large dataset of 100,000 elemets we saw an overall similar performance of the 10,000 unit set with insertion sort outperforming the other algorithms. However, Tim sort in this case was the one with the slowest relative speed.
merge_sort:        97.23317245801445 seconds,
insertion_sort:    96.48777291597798 seconds,
timsort:           97.77354299998842 seconds, 

As a result of these tests it is evident that the innovations in sorting algoritms do have an impact on the efficiency of the execution of the algorithms and that given an ensamble sorting algorithm that has elements of both merge sort and insertinon sort is oftern the best strategy as it will be optimal in most cases.