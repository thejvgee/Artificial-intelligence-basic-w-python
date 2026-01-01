s='django'

#garalt:d
print(s[0])

#garalt:0
print(s[-1])

#garalt:djan
print(s[0:4])

#garalt:jan
print(s[1:4])

#garalt:go
print(s[4:])

#garalt:django reverse
print(s[::-1])

l=[3,7,[1,4,'hello']]
# hello-g goodbye bolgo
print(l)
l[2][2] = 'goodbye'
print(l)

d1={'simple_key':'hello'}
print(d1['simple_key'])

d2={'k1':
    {'k2':'hello'}}
print(d2['k1']['k2'])

d3={'k1':
    [
        {
            'nest_key':
            ['this is deep',
            ['hello']]
            }
    ]
    }
print(d3['k1'][0]['nest_key'][1])


#daraah jagsaaltig utgiin dawhtsalgui jagsaalt bolgo
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

print(mylist)
print(set(mylist))


age = 4
name = "Sammy"
#daraah formataar hewle

print("Hello my dog's name is {} and he is {} years old".format(name,age))

print(f"Hello my dog's name is {name} and he is {age} years old")