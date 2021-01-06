import sys
from modules.Converter import Converter

def main():
    if len(sys.argv) is not 3:
        print("Incorrect number of arguments. Usage: \n $>python3 MC.py <input_file.txt> <output_file.txt>")
        return 1
    try:
        conv = Converter()
        with open(sys.argv[1], "r") as file:
            lineas = file.readlines()
        for linea in lineas:
            conv.parse_line(linea)

        with open(sys.argv[2], "w+") as file:
            file.writelines(conv.output)
        
        return 0
    except Exception as e:
        print(e)
        print(f"Error: Can't open '{sys.argv[1]}', try moving it to the same folder where MC.py is")
        return 2



if __name__ == '__main__':
    main()
