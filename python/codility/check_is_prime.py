# https://jobs.swmansion.com/v/i/t/h54p9gdpshve/d9h3ur6wkkrp

# keep it "global" or "store in cloud" in case of usage with high performance
# in case of usage extreme numbers make prime iterator static and check only higher numbers
prime_list = []


def check_is_prime_num(num):
    if num == 1:    ret = 0         # meanning: 1 IS NOT A PRIME
    else:           ret = num       # meanning: PRIME

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                ret = 0             # meanning: NOT A PRIME
                # print("esc")
                break
    return ret


def algorithm_job_interview_test(set_a, set_b):
    ret_list = []

    for num in set_a:
        num_count_in_b = set_b.count(num)

        #########################
        # check if num is a prime
        #########################
        if num_count_in_b not in prime_list:           # not a prime OR not computed yet
            is_prime = check_is_prime_num(num_count_in_b)
            if not is_prime:                           # computed that is not a prime
                ret_list.append(num)
            else:
                prime_list.append(is_prime)

    return ret_list


##############################################
# TEST UNIT
##############################################

A = [2,3,9,2,5,1,3,7,10]
B = [2,1,3,4,3,10,6,6,1,7,10,10,10]
C = [2,9,2,5,7,10]
C_test = algorithm_job_interview_test(A, B)

print ("primes = ", prime_list)
print ("OBSERVED C = ", C_test)
print ("EXPECTED C = ", C)

if C == C_test:     print("TEST PASS")
else:               print("TEST FAIL")
