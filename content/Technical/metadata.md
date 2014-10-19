Title: Metadata - done
Date: 2014-10-19
Tags: Progress, converter, metadata
Category: Technical
Slug: metadata-handled
Author: Rishi Baijal
Summary: AMPDs data set converter's metadata has been handled

As of writing this, the metadata for the AMPds data set is still incomplete. However, in order to test my converter, I replaced some of the appliance types in the building1.yaml file with random types (in most cases, I have used the type unknown). Obviously, those values are inaccurate and once the complete metadata for the dataset has been released, I will update my forked repository to reflect the changes in the metadata.

Regardless of that, the converter successfully manages to convert the yaml files to the hdf5 format. I have used the convert_yaml_to_hdf5() function in order to accomplish this, and the parameters that this finction accepts are:

1. The path of the directory containing the metadata files.
2. The path of the actual hdf5 file where the data needs to be stored.

Initially, I faced quite a few weird errors. The issue was as follows:- In the building1.yaml file, some of the appliances were described using comma-separated appliance types, while some appliances had a blank appliance type. Nilmtk cannot understand comma-separated appliance types or blank appliance types (at least not as far as I know). So, in order to fix that, wherever I found a blank appliance type, I labelled it as 'unknown', which is a standard way of naming devices that nilmtk does not recognize. Wherever I found a comma-separated list of appliance types, I replaced them with a single appliance type, removing the list. For some of the appliances, I have simply assigned my own appliance types. With that done, I was able to pass those files to the function without any problems.
