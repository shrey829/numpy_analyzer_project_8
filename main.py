
print("numpy analyzer")
print("please choose your choices")
print("1.create a numpy array")
print("2.perform mathematical function")
print("3.combine or split array")
print("4.search,sort,filter array")
print("5.compute aggreates and statistics")
print("6.exit")
while True:
    a=int(input("enter your choice"))
    match a:
        case 1:
            import array
            re,res=array.main()
            print(re,res)
        case 2:
            import mathematicaloperations
            re,res=mathematicaloperations.main()
            print(re,res)
        case 3:
            import combinesplit
            re=combinesplit.main()
            print(re)
        case 4:
            import filtersearchsort
            re=filtersearchsort.main()
            print(re)
        case 5:
            import aggregationfunction
            re=aggregationfunction.main()
            print(re)
        case 6:
            exit()
        case _:
            print("invalid choice")
if __name__=="__main__":
    main()