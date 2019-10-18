import matplotlib.pyplot as plt
import sys
import argparse
import matplotlib
matplotlib.use('Agg')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A script to draw scatter plot from STDIN.',
        prog='scatter')

    parser.add_argument('--out_file', type=str,
                        help='Name of the output file', required=True)
    parser.add_argument('--x_label', type=str,
                        help='Label of X-axis', required=True)
    parser.add_argument('--y_label', type=str,
                        help='Label of y-axis', required=True)

    args = parser.parse_args()

    out_file = args.out_file
    x_label = args.x_label
    y_label = args.y_label

    X = []
    Y = []
    i = 0
    for l in sys.stdin:
        A = l.rstrip().split()
        if len(A) == 2:
            X.append(float(A[0]))
            Y.append(float(A[1]))
        elif len(A) == 1:
            X.append(float(i))
            Y.append(float(A[0]))
            i += 1

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.savefig(out_file, bbox_inches='tight')
