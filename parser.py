import argparse
import sys


def parser():
    parser_m = argparse.ArgumentParser(prog="help",
                                       description="Processing the input files.",
                                       epilog="Process datas",
                                       usage="union -h")

    # subparse = parser.add_subparsers()
    parser_m.add_argument('-l_name1', '--list_filename_1',
                          help="Enter the Filename 1")
    parser_m.add_argument('-l_name2', '--list_filename_2',
                          help="Enter the Filename 2")
    parser_m.add_argument('-r_name', '--result_filename',
                          help="Enter the Filename result")
    group = parser_m.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
    group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
    args = parser_m.parse_args()

    if len(vars(args)) > 0:
        args.func(vars(args))
    else:
        print('For help about this command, try -h option\nUsage : union -h')


if __name__ == '__main__':
    try:
        parser()
        sys.exit(0)
    except Exception as e1:
        print('COMMAND FAILURE: {0}'.format(str(e1)))
        import traceback
        traceback.print_exc()
        sys.exit(1)
