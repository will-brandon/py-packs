import pywbu.console as csl
from pywbu.runtime import *

@main
def main(argv: list[str]) -> int:
    
    while True:
        csl.log(argv)

    return EXIT_SUCCESS

if __name__ == '__main__':
    main()
