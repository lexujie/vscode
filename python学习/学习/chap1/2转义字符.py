#转义字符：反斜杠+想要实现的转义功能首字母
#换行\n 回车\r 水平制表符\t 退格\b

print('hello\nworld')
print('hello\tworld') #\t 4个单元格，hell,o   ,worl,d
print('helloooo\tworld')
print('hello\rworld')#world将hello覆盖了
print('hello\bworld')

print('http:\\\\www.baidu.com')
print('曰：\'善哉\'')

#原字符：不希望转义字符起作用，在字符串之前加上r或R
#注：最后一个字符不能是反斜杠
print(r'hello\nworld')
#print(r'hello\nworld\')
print(r'hello\nworld\\')