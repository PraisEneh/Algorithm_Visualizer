# TODO: Write a function that returns conditional entropy: H(Y|X)
# INPUT:   * List of instances, with label in last column
#          * Feature index integer that indicates which feature to calculate I.G. for
#          * List of values feature can take on (comes from attribs file) 
#          * value for first class (first possible value for label)
#          * value for second class (second possible value for label)
# RETURN:  Return single float value for conditional entropy.
import math


def get_inst_from_file(filename):
    all_instances = []
    fin = open(filename, "r")
    fin.readline()

    for line in fin:
        all_instances.append(line.strip().split(","))

    fin.close()

    return all_instances


def get_entropy(instances, class0, class1):
    count = 0
    count2 = 0
    for i in instances:
        if i[5] == class0:
            count += 1
        else:
            count2 += 1
    pr = count / len(instances)
    pr2 = count2 / len(instances)
    ent = -(pr * math.log2(pr)) - (pr2 * math.log2(pr2))
    return ent


def get_cond_entropy(instances, feat_index, feat_vals, class0, class1):
    num_inst = len(instances)
    total_entropy = 0.0
    adult_counter = 0
    adults = []
    adult0 = 0
    adult1 = 0
    child_counter = 0
    kids = []
    child0 = 0
    child1 = 0
    # HINT: Iterate over all feat_vals (i.e., all values the current feature--feat_index--can take on).
    for i in instances:
        if i[feat_index] == feat_vals[0]:
            #             print('adult')
            adult_counter += 1
            if i[5] == class0:
                adult0 += 1
            else:
                adult1 += 1
            adults.append(i)
        else:
            #             print('child')
            child_counter += 1
            if i[5] == class0:
                child0 += 1
            else:
                child1 += 1
            kids.append(i)
    print(adult_counter, ", ", adult0, ", ", adult1, ", ", child_counter, ", ", child0, ", ", child1)
    adult_prob = adult_counter / len(instances)
    dead_adult_prob = adult0 / adult_counter
    alive_adult_prob = adult1 / adult_counter
    child_prob = child_counter / len(instances)
    dead_child_prob = child0 / child_counter
    alive_child_prob = child1 / child_counter
    H = -(dead_adult_prob * math.log2(dead_adult_prob)) + (alive_adult_prob * math.log2(alive_adult_prob)) + \
        (dead_child_prob * math.log2(dead_child_prob)) + (alive_child_prob * math.log2(alive_child_prob))
    a_ent = get_entropy(adults, '0', '1')
    k_ent = get_entropy(kids, '0', '1')
    cond_ent = k_ent + a_ent
    print('Adult Entropy: ', a_ent)
    print('Child Entropy: ', k_ent)
    print('Conditional Entropy: ', cond_ent)
    print('H ', H)
    #     print(H)
    #     print(H2)
    total_entropy = H
    print('cond ', total_entropy)
    return total_entropy


titanic_instances = get_inst_from_file("titanic_new.csv")

ent = get_entropy(titanic_instances, '0', '1')
print('All Entropy ', ent)

this_e = get_cond_entropy(titanic_instances, 2, ['A', 'C'], '0', '1')
print('This e:', this_e)


def check(i):
    if i == sorted(i):
        return True
    else:
        return False

lst = [1, 2, 3, 5, 4]

print('sorted? ', check(lst))
