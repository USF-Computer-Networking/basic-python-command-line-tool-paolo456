
import os
import argparse




def read(args):
    # get the file name/path
    file_name = args.read[0]

    '''
    # validate the file name/path
    validate_file(file_name)
    '''
    # read and print the file content
    with open(file_name, 'r') as f:
        print(f.read(20))

def add(args):
    i = args.sum[0] + args.sum[1]
    print(i)
def sub(args):
    i = args.sub[0] - args.sub[1]
    print(i)
def div(args):
    i = args.div[0] / args.div[1]
    print(i)
def mult(args):
    i = args.mult[0] * args.mult[1]
    print(i)
def hello(args):
    print(args.hello[0])
def bye(args):
    print(args.bye[0])
def thanks(args):
    print("thanks for using my program!")

def main():
    parser = argparse.ArgumentParser(description = "Welcome!")
    
    parser.add_argument("--read", type = str, nargs = 1, metavar = "file_name",
                        default = None, help = "reads file inputted")
    parser.add_argument("--sum", type = int, nargs = 2, metavar = "i",
                    default = None, help = "adds two nums together",)
    parser.add_argument("--div", type = int, nargs = 2, metavar = "i",
                    default = None, help = "divides two nums together",)
    parser.add_argument("--mult", type = int, nargs = 2, metavar = "i",
                    default = None, help = "multiplies two nums together",)
    parser.add_argument("--hello", type = str, nargs = 1, metavar = "i",
                    default = None, help = "prints user input",)
    parser.add_argument("--sub", type = int, nargs = 2, metavar = "i",
                    default = None, help = "subtracts two nums together",)
    parser.add_argument("--bye", type = str, nargs = 1, metavar = "i",
                    default = None, help = "prints user input",)
    parser.add_argument("--thanks", type = str, nargs = 1, metavar = "i",
                    default = None, help = "displays greeting",)

    args = parser.parse_args()

    if(args.read) != None:
        read(args)
    if(args.sum) != None:
        add(args)
    if(args.sub) != None:
        sub(args)
    if(args.mult) != None:
        mult(args)
    if(args.div) != None:
        div(args)
    if(args.hello) != None:
        hello(args)
    if(args.bye) != None:
        bye(args)
    if(args.thanks) != None:
        thanks(args)

if __name__ == "__main__":
    main()