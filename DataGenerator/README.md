# Python Data Generator

#### Python 3 script to generate a CSV file that mimics that produced by the experimental setup.

1. Each row is an instance of a sensor report and  each column contains a random value within some column specific bounds (each column has a probability distribution associated with it from which a sample is drawn).
2. Initially just use a uniform distribution for each column with some specified bounds.
3. If the data is timestamped, the timesteps progress in a logical way, stepping accordingly between rows.
4. We can optionally inject noise into the non-time values. The program generates some small random noise delta value from a Gaussian distribution that gets added to the data.

#### The script should just be command line driven for now with parameters for:

1. Starting timestamp
2. Timestamp step size
3. Number of rows to generate
4. Uniform distribution bounds for each column
5. Noise values to add for each column

#### Running the program

Sample:

`python DataGenerator.py  41794.3866064352 0.0000000463041942566633 20 -1,6`

`python DataGenerator.py  41794.3866064352 0.0000000463041942566633 20 -1,6 0.01,0.02`

#### Notes:

> * The program can handle 4/5 parameters.
> * The program handles incorrect parameter count/format.
> * The program outputs the data in a new output csv file (incrementing numbers)

