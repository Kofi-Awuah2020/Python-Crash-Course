import greetings
from greetings import greet_users
from greetings import greet_users as sup
import greetings as hi
from greetings import *

names = ['Sifu', 'Shinock', 'IP Man', 'Donny Yen', 'Jet Li']
greetings.greet_users(names)
greet_users(names)
sup(names)
hi.greet_users(names)
greet_users(names)