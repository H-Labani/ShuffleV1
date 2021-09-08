import random, math;

n = 100  # the total number of items to be shuffled
r = 2  # the number of rounds
l = int(math.sqrt(n)) # the batch length
# a list of sequential integers from 0 to n. Used as a seed for formatting the data
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


if __name__ == '__main__':

    # Create a data list divided into batches of size l
    data = create_batches(sorted_array);

    # Generate permutations for the rounds
    permutations = generate_permutations();

    # Shuffle the data
    permuted_data = apply_permutation(data, permutations);

    # Display the data before and after the shuffle
    print(f'Data before permutation:{sorted_array}')
    print(f'Data after  permutation:{permuted_data}')
