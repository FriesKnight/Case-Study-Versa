import json

def prime_collision():
    result = []
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            result.append("BIGBANG")
        elif num % 3 == 0:
            result.append("BIG")
        elif num % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(num))
    return result

def main():
    array = prime_collision()

    with open('output.json', 'w') as file:
        json.dump(array, file)

if __name__=="__main__":
    main()