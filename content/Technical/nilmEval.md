Title: The nilm-eval project
Date: 2014-11-13
Tags: nilm-eval, nilmtk, comparison
Category: Technical
Slug: nilm-eval
Author: Rishi Baijal
Summary: The nilm-eval project analysis

This is the first in a series of posts that I am going to write about the nilm-eval project, which is one of the more recent attempts at building a Non-Intrusive Load Monitoring System. Nilm-eval has been written in Matlab with the primary aim of making it easy to evaluate the performance of Non Intrusive Load Monitoring algorithms. 

The Backstory
==========

The energy needs of the world are increasing at an exponential rate as a result of an increase in population and the growing demands of that population. This could have adverse repurcussions on the environment in general. In order to regulate our energy usage, we need to first monitor the usage of individual appliances and correlate that with the overall energy consumption. One of the ways to do this would be to monitor the energy output of every single electrical appliance that we use, and that is not possible for a number of reasons. The solution to this is the advent of Non-Intrusive Load Monitoring algorithms. These algorithms analyse the aggregate energy consumption of a house and through that data, they can figure out which appliances are running and what is the electricity consumption of those appliances.

The problem
==========

The problem arises when you need to analyse the performance and behaviour of the algorithms that you are using in your NILM system. Analysis of NILM algorithms involves:

1. Different underlying assumptions
2. Tailored parameter settings
3. Lack of comprehensive data sets.

As a result of this, evaluation of NILM algorithms is cumbersome. NILM-Eval is a framework designed to alleviate such problems.

NILM-Eval - The Basic Approach
==============================

The NILM-Eval framework uses the ECO dataset to assess the performance of NILM algorithms, because that is the most comprehensive dataset available. They have evaluated the performance of supervised, unsupervised and semi-supervised algorithms. The algorithms that have been used are:

1. Parson's algorithm
2. Baranski's algorithm
3. Weiss' algorithm
4. Kolter's algorithm

I will now describe some of the basic characteristics of each of these algorithms:

Parson's algorithm
------------------

1. It relies on Hidden Markov Models (HMMs) and the Viterbi algorithm inorder to disaggregate the electricity consumption of a household.
2. It determines the most likely sequences of states 
3. It uses a semi-supervised learning process in order to determine the transition probabilities and the power demand of each appliance.
4. It evaluates 

Baranski's algorithm
-------------------

Weiss' algorithm
----------------

Kolter's algorithm
------------------
