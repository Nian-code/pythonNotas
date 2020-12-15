def primo(num):
    contador = 1
    num_list = [2,3,5,7]

    for n in num_list:
        if num == n:
            continue
        if num % n == 0:
            contador +=1

    if num == 1 or contador > 1:
        return False
    else:
        return True

    
if __name__ == "__main__":
    for i in range(101):
        if primo(i):
            print("El número {} es primo".format(i))
   
   