


temdegtuud = input("ta text oruulna uu!")
urt=0
for temdegt in temdegtuud:
    urt = urt +1
    print(f'{temdegtuud} urt:{urt}')



toli={
    'Father':'Аав',
    'Аав':'Father',
    'Mother':'Ээж',
    'Ээж':'Mother'
} 
orch = input('ta haih ugee oruulna uuu!')
hevleh=''
for key,val in toli.items():
    if key == orch:
        hevleh=f'{key} --- {val}'

    if hevleh != '':
        print(hevleh)
    else:
        print(f'{orch} ug oldsngue')

