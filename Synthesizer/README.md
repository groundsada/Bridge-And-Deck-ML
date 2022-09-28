# Python Data Generator

#### Python 3 script to generate multiple CSV files that synthsize and multiple the values that were produced by the experimental setup.

1. Each row is an instance of a sensor report and  each column contains a random value within some column specific bounds (each column has a probability distribution associated with it from which a sample is drawn).
2. Initially just use a uniform distribution for each column with some specified bounds.
3. If the data is timestamped, the timesteps progress in a logical way, stepping accordingly between rows.
4. We can optionally inject noise into the non-time values. The program generates some small random noise delta value from a Gaussian distribution that gets added to the data.

#### Synthesizer Iteration 1

1. Takes in an input file
2. Takes the avergae timestamp step
3. Starts right after the last timestamp in the last file
4. It ensures incremental timestamps in all of the synthesized file with no duplicates
5. It takes a parameter as the bounds of the injected noise.

#### Running the program

Sample:

`python Synthesizer_iter1.py input.txt 5 -0.5,0.5`

where "input.txt" is the input file name, "5" is the number of synthesized output files. and "-0.5,0.5" are the gaussian bounds for the noise.

#### Synthesizer Iteration 2

Has the same functionality as the first iteration. Only difference is that the 1st iteration injects noise on the same data as the original column values.
The 2nd iteration generates new uniform distribution data from the bounds taken from the input file.

#### Running the program

Sample:

`python Synthesizer_iter2.py input.txt 5 -0.5,0.5`

where "input.txt" is the input file name, "5" is the number of synthesized output files. and "-0.5,0.5" are the gaussian bounds for the noise.

#### Notes:

> * The program handles incorrect parameter count/format.
> * The program outputs the data in new output csv file (incrementing numbers)

