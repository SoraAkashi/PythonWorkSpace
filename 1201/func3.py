def do_anything(*args): 
    '''引数の個数によって何かする。intとstrで動作'''  
    print(f'受け取った値:{args}')

    if len(args) == 0:
        print('やることが無いので暇です')
    elif len(args) == 1:
        args1 = args
        if type(args1) !=int and type(args1)!=str:
            print('難しくて無理です')
        else:
            print(args1 * 2)
    elif len(args) == 2:
        args1,args2=args
        if type(args1)==type(args2)!=int and type(args1)==type(args2) !=str:
            print('無茶言わないで！')
        elif type(args1)!=type(args2):
            print('できません')
        else:
            print(args1 + args2)
    else:
        print('無理です...')
    



# main 
do_anything() 
do_anything(10) 
do_anything('asdfg') 
do_anything([1,2,3]) 
do_anything(10,20)
do_anything(10,'abc') 
do_anything('x','yz') 
do_anything([1,2,3],[4,5,6]) 
do_anything(1,2,3)