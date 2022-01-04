#Programa para determinar una palabra es palindromo o no
#Depurador: $ mypy primo.py --check-untyped-defs
def is_palindrome(word: str) -> bool:
    word = word.replace(" ","").lower()
    return word == word[::-1]

def run():
    print(is_palindrome(500))

if __name__ == '__main__':
    run()