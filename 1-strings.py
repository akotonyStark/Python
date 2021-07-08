course = 'Python for "beginners"'
text = '''
hi John Doe,
You're receiving this email
because you signed up with us
'''

print(text)
print(course[-2])
print(course[0:3])
print(course[:5])
print(course[0:])

name = 'Jennifer'
print(name[1:-1])

firstName = 'John'
lastName = 'Smith'

message = firstName + ' [' + lastName + '] is a coder'
print(message)

formattedMessage = f'{firstName} [{lastName}] is a coder'
print(formattedMessage)

print(len(formattedMessage))

print(course.upper(), course.lower(), course.title())

# returns the index of the item being searched for
print(course.find('b'))

# returns boolean if item exists
print('python' in course)

print(course.replace('Python', 'Java'))
