Title: NILM-Eval evaluation methodology
Date: 2014-11-15
Tags: nilm-eval, nilmtk, comparison, evaluation
Category: Technical
Slug: nilm-eval, evaluation
Author: Rishi Baijal
Summary: The nilm-eval project evaluation methodology

We saw the difficulties presented in the previous post. I will now go over some of the features offered by NILM-Eval that help in alleviating difficulties like the ones mentioned.In order to achieve this end, NILM-Eval offers the foillowing features:

1. It enables the evaluation of NILM algorithms on different datasets, households, granularities, time periods and specific algorithm parameters.
2. It allows the user to repeat the experiments performed by others with little effort, evaluate algorithms on a new data-set and fine tune the parameters in order to optimize the performance of an algorithm in a particular setting.

Metrics Evaluated
-----------------

NILM-Eval evalulates the following metrics in order to evaluate the performance of an algorithm:

1. Root mean square error
2. Precision
3. Recall
4. F1 score.

Dataset used
------------

As I have stated earlier, the ECO dataset has been used in testing the NILM-Eval framework for the following reasons:

1. It contains data collected over 8 months. Only the AMPds and the UK-Dale dataset cover a comparably long time-span.
2. The aggregate electricity consumption available with the ECO dataset is very detailed because it contains measurements of real and reactive power.
3. The data can be colected at a freqwuency of 1 Hz.
4. ECO is the only dataset that contains occupancy information about the households.

Comparison between NILMTK and NILM-Eval
----------------------------------------

The similarity between these two frameworks is the fact that they both are used to monitor the electricity consumption of a particular household in a way that does not feel meddlesome. While the focus of NILMTK seems to be on compatibility and ease of usage (there is even an issue open on github that says that NILMTK installation is difficult for the average user and it), NILM-Eval focuses more on the algorithms that are to be used in order to accomplish this task. The birth of NILM-Eval was due to the lack of a framework that was good enough to provide a yardstick to measure the performance of algorithms that are concerned with non-intrusive load monitoring. As opposed to this, NILMTK is a framework that provides rich metadata support and has converters for the various datasets that are out there. On the other hand, NILM-Eval has mostly been tested on the ECO dataset. 

Both frameworks could possibly learn from each other. NLMTK could take inspiration from NILM-Eval and use a more algorithmic approach (although doing that in python would be dangerously tedious), while NILM-Eval could increase its metadata support in order to support a greater amount of compatibility.
