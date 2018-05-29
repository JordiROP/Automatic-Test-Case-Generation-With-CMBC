# Automatic Test Case Generation With CMBC
Program for helping in the automation of the process of generating input test cases for the code coverage analysis of a set of functions. Tries to find test cases for all the assert( 0 ) points of the function funcnameinside ccode source code, and using k for the unwind parameter. Also, for each case, tries to find a set of input values for the parameters of the function with name funcname located inside source file ccode, and that the set of input values make the function to reach the “assert( 0 )” point of the function with cbmc identifier propname.

## Built With
[Python](https://www.python.org/) - Primary and unique Language.


## Authors
* **Jordi Ricard Onrubia Palacios** - *Programming* - [JordiROP](https://github.com/JordiROP)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
