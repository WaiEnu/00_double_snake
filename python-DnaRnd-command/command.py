import generate

maximum = input('塩基数を指定:')
sequence = generate.sequence(maximum)
generate.out_seq(sequence)

locate = input('変異導入箇所を指定:')
if int(locate)>int(maximum) or int(locate)==0:
    print('1～'+maximum+'までの数値を入力してください')
else:
    base = input('導入塩基を指定[1:A ,2:G ,3:C ,4:T]:')
    if int(base)>4 or int(base)==0:
        print('1～4までの数値を入力してください')
    else:
        mutation_sequence = generate.mutate(sequence,base,locate,maximum)
        generate.out_seq(mutation_sequence)
