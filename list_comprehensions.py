def run():
   # squares = []
    #for i  in range(1, 101):
     #   if i % 3 != 0:
      #      squares.append(i**2)

   # squares = [i**2 for i in range (1, 101) if  i %3 != 0]
   # print(squares)

    reto = [i for i in range (36, 100000) if i %36 == 0]
    print(reto)
    

if __name__ == "__main__":
    run()