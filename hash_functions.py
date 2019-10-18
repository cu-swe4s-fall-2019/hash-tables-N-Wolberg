import sys

def h_ascii_sum(key, N):
    '''
    Uses a string(key) and sums the ascii representation and returns the hash
    value according to the appropriate reducer(N - typically tablesize)
    '''

    if type(key) != str:
        raise TypeError('First Argument Must Be A String')
        return None
    if type(N) != int:
        raise TypeError('Second Argument Must Be An Interger')
        return None

    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_polynomial_rolling(key, N, p=53, m=2**64):
    '''
    Uses a string(key) and sums a scaled ascii representation and returns the hash
    value according to the appropriate reducer(N - typically tablesize)
    p - a prime number roughly equal to the number of characters in the input alphabet
    m - should be a large number, since the probability of two random strings colliding is
      about 1/m. Sometimes m=2^64 is chosen
    '''
    if type(key) != str:
        raise TypeError('First Argument Must Be A String')
        return None
    if type(N) != int:
        raise TypeError('Second Argument Must Be An Interger')
        return None
    if type(p) != int:
        raise TypeError('Third Argument Must Be An Interger - default:53')
        return None
    if type(m) != int:
        raise TypeError('Fourth Argument Must Be An Interger - default:2^64')
        return None

    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N 

def h_python(key, N):
    return hash(key) % N

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
             description='Implementation of hash functions',
             prog='hash_functions')

    parser.add_argument('--input_file', type=str,
                        help='Name of the input file', required=True)
    parser.add_argument('--hash_method', type=str,
                        help='ascii, rolling, python', required=True)

    args = parser.parse_args()


    if (os.path.exists(args.input_file)):
        for l in open(sys.argv[1]):
            if args.hash_method == 'ascii':
                print(h_ascii_sum(l, 1000))
                sys.exit(1)
            elif args.hash_method == 'rolling':
                print(h_polynomial_rolling(l, 1000))
                sys.exit(1)
            elif args.hash_method == 'python':
                print(h_python(l, 1000))
                sys.exit(1)
            else:
                print('Invalid Hash Method')
                sys.exit(1)
