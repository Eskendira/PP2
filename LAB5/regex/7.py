"""Write a python program to convert snake 
case string to camel case string."""

import re
snake = "snake_case_asdfg"
capital = snake.upper()
camel = ""
i = 0
while(i != len(snake)):
    if(snake[i] == '_'):
        camel = camel + capital[i+1]
        i = i + 2
    else:
        camel = camel + snake[i]
        i = i + 1
print(camel)