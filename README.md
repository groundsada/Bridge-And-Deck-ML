# The Bridge-And-Deck Machine Learning Team at DPI

## Team Members

- Mohammad Firas Sada (msada@hawk.iit.edu)
- Arjun Aggarwal (arjuna4@illinois.edu)
- Lauren-Charlise Walls (lwalls4@uic.edu)

## Python Data Generators

### Data Generator 1: Mimicking the Experimental Setup

We have developed a Python 3 script that generates a CSV file that mimics the data produced by the experimental setup. Each row in the CSV file represents an instance of a sensor report, and each column contains a random value within some column-specific bounds. Initially, we use a uniform distribution for each column with specified bounds. If the data is timestamped, the timestamps progress logically between rows. Additionally, we can optionally inject noise into the non-time values. The program generates a small random noise delta value from a Gaussian distribution that is added to the data. This data generator can be used for testing and validation purposes.

### Data Generator 2: Synthesizing Multiple CSV Files

We have also developed a Python 3 script that generates multiple CSV files that synthesize the values produced by the experimental setup. Each row in the CSV file represents an instance of a sensor report, and each column contains a random value within some column-specific bounds. Initially, we use a uniform distribution for each column with specified bounds. If the data is timestamped, the timestamps progress logically between rows. Additionally, we can optionally inject noise into the non-time values. The program generates a small random noise delta value from a Gaussian distribution that is added to the data.

#### Synthesizer Iteration 1

This script takes an input file and the average timestamp step as input. It starts right after the last timestamp in the last file and ensures incremental timestamps in all of the synthesized files with no duplicates. It also takes a parameter as the bounds of the injected noise. This script is the first iteration of the synthesizer and can be used to generate synthetic data for training machine learning models. 

## License

All source code included is licensed under the [GNU General Public License.](/LICENSE)
