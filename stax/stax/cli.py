import pywbu.console as csl
from pywbu.runtime import *

@main(handle_key_interrupt=True)
def main(argv: list[str]) -> int:
    
    while True:
        print(argv)

    return EXIT_SUCCESS

if __name__ == '__main__':
    main()
