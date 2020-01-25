import argparse
parser =  argparse.ArgumentParser()
parser.add_argument("-a", "--all", help="show all leagues available", action="store_true")
parser.add_argument("-b", "--bll", help="test", action="store_true")
args = parser.parse_args()

if args.all:
    print("NHL")
    print("NBA")
    print("NCAAB: PAC-12, Mountain West, Big Sky, West Coast Conference")

if args.bll:
    print("here")




