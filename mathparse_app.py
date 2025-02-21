import sys
sys.path.append('libs/mathparse')

from mathparse import mathparse

def main():
    expression = '10 + 5 * 2'
    result = mathparse.parse(expression)
    print(f"'{expression}' ifadesinin sonucu: {result}")

if __name__ == "__main__":
    main()
