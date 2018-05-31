import os
import sys

"""
As before the output allways follows the same pattern, as we are only
interested in the input variables values so, we can just read for the line with
INPUT and take the following value.
"""


def get_vars():
    f = open("tmp_vars.txt", 'r')
    for line in f:
        if "INPUT" in line:
            ln = line.split(" ")
            print "{0} = {1}".format(ln[3][0], ln[4])


"""
The information shown by the cbmc always follows the same patter, the
properties can be found after the text "** Results:". With this what we do
is check if we read that line, after that line the properties follow the
pattern [function_name.property.#] information about the property: SUCCES or
FAILURE.

To get the property name, we read the line in search of a "]" and split it
getting the first part and removing the "[", for the property info we know
that the info ends with a ":", so we take the part after the "]" and before
the semicolon, and for the state of the property we just take the part after
the semicolon.

Once we have the property name we can execute the command to check the input
values for the property.
"""


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


"""
General function, this executes the cbmc with the parameters passed by
argument and saves it in a temporal file that will be processed by
get_properties method. At the end of the execution the file will be deleted.
"""


def general_properties(ccode, funcname, k):
    cmd = "cbmc {0} --function {1} --unwind {2}".format(ccode, funcname, k)
    os.system(cmd + " > tmp.txt")
    get_properties(ccode, funcname, k)
    os.system("rm tmp.txt")


"""
Basic function, this executes the cbmc with the parameters passed by argument
and an aditional parameter "--trace" so we can check the inputs. The result
is stored in another temporal file that will be used to check the inputs. The
file will be deleted at the end of the execution.
"""


def particular_property(ccode, funcname, propname, k):
    cmd = "cbmc {0} --function {1} --property {2} --unwind {3} --trace".\
        format(ccode, funcname, propname, k)
    os.system(cmd + " > tmp_vars.txt")
    get_vars()
    os.system("rm tmp_vars.txt")


"""
The program takes as input 3 arguments, the code to test, the name of the
functon to test inside the code and the number of unwinds.
"""


if __name__ == "__main__":
    if len(sys.argv) == 4:
        general_properties(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print "python automatic_test_generation <code> <function_name> \
                <unwind>"
