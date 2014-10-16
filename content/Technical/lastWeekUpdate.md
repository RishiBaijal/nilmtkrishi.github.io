Title: Last Week's update
Date: 2014-10-16
Tags: Progress
Category: Technical
Slug: working-so-far
Author: Rishi Baijal
Summary: AMPDs data set converter

So this week's assignment involved writing an hdf5 converter for the AMPDs dataset. Specifically, I was supposed to read all the .csv files in the dataset, store the data as a dataframe and load that dataframe into an hdf5 file. It is done for the most part. Basically, what I had to do was define a function that took as input the path to the actual dataset, the path to the metadata of the set, a key generation scheme and the path to a single h5 file which would finally contain all the accumulated information from the entire dataset.

Initial failure using h5py
--------------------------

When I was given this assignment, I immediately googled for ways to convert csv files to h5 files, since the AMPds dataset consists entirely of csv files. I successfully installed h5py and wrote some hacky code which read all the files contained in that directory and used the h5 library to push all that data into the same file. Everything seemed to work once I put my laptop away. However, a few days later, when I tried to run the code, it would not run. Strange, seeing how it should have worked given how it was working a few days ago. Immediately my spirits dropped.

It turns out that the h5py module was unable to detect a file which should have been in the library itself. I tried to fix this manually, but to no avail. I upgraded it the library to the latest version, but I still got the same error. After wasting about two or three days on h5py, I decided to give up and try something else instead.

Using HDFStore
--------------

An excellent library is already available if you want to work with hdf files (and here I was wasting time on h5py). After re-writing the entire code using HDFStore, I finally got it to work, at least for some time. As of now, the code seems to be working perfectly. It manages to retrieve the csv data from the files and successfully stores that data in an h5 file specified by the user. This should have been done quite a while back, but better late than never. I have not handled the metadata yet and according to my mentor, that is going to be harder to deal with than the csv files themselves. However, the author of this dataset has recently released some files himself. I hope that will save me some time. Unfortunately, that set is still incomplete. Let's see how it goes.
