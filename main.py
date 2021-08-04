import random, math;
from collections import Counter;
import matplotlib.pyplot as plt
import numpy as np

n = 100
r = 2
l = int(math.sqrt(n))
max_possible_outcomes = l ** r
sorted_array = list(range(0, n));


# generate a data set consisting of sequential integer starting from 0 to n.
# The elements of data is divided into batches each of size l
def create_batches(data):
    divided_data  = [data[x:x+l] for x in range(0, n, l)]
    return divided_data;


# Generate r number of permutations
def generate_permutations():
    generated_permutations = [];
    for i in range(r):
        generated_permutations.append(random.sample(sorted_array, len(sorted_array)));
    return generated_permutations;


# Given the data set and the rounds' permutations, apply the permutations to the data
def apply_permutation(data, permutations):
    permuted_data = [None] * n # The output of applying the permutation to the whole data (output of the round)
    for i in range(r): # iterate through rounds
        for j in range(int(n/l)): # iterate through batches
            batch = data[j]
            for k in range(l): # iterate through items in the batch
                # Save in the kth item of the batch in its position after the permutation.
                permuted_data[permutations[i][(j*l)+k]] = batch[k]
    return permuted_data;


# Find the possible positions of a target position after the permutation
def get_outcomes(target, permutation):
    outcomes = []
    for i in range(l):
        outcomes.append(permutation[math.floor(target / l) * l + i]);
    return outcomes;

    # Finding the start index of the target's batch: start index = floor(index / l) * l


if __name__ == '__main__':
    # Create a data list divided into batches of size l
    data = create_batches(sorted_array);
    # Generate permutations for the rounds
    permutations = generate_permutations();

    permuted_data = apply_permutation(data, permutations);
    print(f'Data before permutation:{sorted_array}')
    print(f'Data after  permutation:{permuted_data}')
    #target = 0;
    # Apply the permutation for each round
    # for i in range(r):
    #     data = permute_data(data,permutations[i])
    #     print(f'P{i}:{permutations[i]}')
    #     print(f'D{i}:{data}')

    # First permutation of item in target
    # outcomes = get_outcomes(target, permutations[0])
    #
    # for i in range(r - 1):
    #     inp = outcomes;
    #     outcomes = [];
    #     for j in inp:
    #         outcomes.extend(get_outcomes(j, permutations[i + 1]));
    # # print(outcomes);

    # Find the probability that the target item ends up in each position of the data set.
    # a dictionary of the outcomes where keys are the positions and the
    # values are the number of times this position occured in the set of possible outcomes
    # doutcomes = Counter(outcomes);
    #
    # # A list of the doutcome keys
    # dkeys = list(doutcomes);
    #
    # # A dictionary containing all the possible positions and the probability of the target item landing on them at the end of the shuffle
    # dprobability = dict.fromkeys(range(n))
    #
    # # Generate the probability for the target to land on each position.
    # for x in range(len(dkeys)):
    #     dprobability[dkeys[x]] = round(doutcomes[dkeys[x]] / max_possible_outcomes, 2);
    # # print(dprobability);

    ############################## Copied from a website
    #
    # # An "interface" to matplotlib.axes.Axes.hist() method
    # plt.style.use('seaborn-white')
    #
    # plt.bar(dprobability.keys(), dprobability.values(), 1.0, color ='g')
    # plt.show()

    #####################################################################