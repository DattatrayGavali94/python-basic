is_friend = True
user = True

if is_friend and user:
    print('best friend forver')



# Logical Operator

# Grater than
print(4<5)

# Less than
print(4>5)

# equal == 
print(4 == 4)
print('a'=='a')
print('a'=='A')
print('a'=='x')

print(5<2<3<4)
print('=================')
print(1 >= 2)

print('===========')

is_magician = False
is_expert = True

# check if magician AND experts: "you are a master magician"
# check if magician but not expert: "at least you're getting there"
# if you're not a magician: "You need magic powers"
if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("You need magic powers")