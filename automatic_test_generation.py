import os
import sys


def get_properties(ccode, funcname, k):
    results = False
    f = open("tmp.txt", 'r')
    for line in f:
        if results:
            if line == "\n":
                results = False
            else:
                splited = line.split("]")
                property_name = splited[0].lstrip("[")
                splited = splited[1].split(":")
                property = splited[0].lstrip(" ")
                result = splited[1].strip(" \n")
                print "Property Name: {0}\nProperty: {1}\nVerification: {2}".\
                    format(property_name, property, result)
                particular_property(ccode, funcname, property_name, k)
                print "\n+++++++++++++++++++++++++++++++++++++++++++++++++\n"
        if "** Results:" in line:
            results = True


def general_properties(ccode, funcname, k):
    cmd = "cbmc {0} --function {1} --unwind {2}".format(ccode, funcname, k)
    os.system(cmd + " > tmp.txt")
    get_properties(ccode, funcname, k)
    os.system("rm tmp.txt")


def particular_property(ccode, funcname, propname, k):
    cmd = "cbmc {0} --function {1} --property {2} --unwind {3} --trace".\
        format(ccode, funcname, propname, k)
    os.system(cmd + " > tmp_vars.txt")
    get_vars()
    os.system("rm tmp_vars.txt")


def get_vars():
    f = open("tmp_vars.txt", 'r')
    for line in f:
        if "INPUT" in line:
            ln = line.split(" ")
            print "{0} = {1}".format(ln[3][0], ln[4])


if __name__ == "__main__":
    if len(sys.argv) == 4:
        general_properties(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print "python automatic_test_generation <code> <function_name> \
                <unwind>"
