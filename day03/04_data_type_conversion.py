

# eval() 是一个内置函数，用于执行字符串形式的Python表达式，并返回计算结果。
# eval() 会执行任意代码，如果输入来自不可信的来源（如用户输入），可能会引发安全问题：
"""
如：
    user_input = input("请输入命令：")
    eval(user_input)   # 如果用户输入 `__import__('os').system('rm -rf /')`，可能删除文件

更加安全的替代方式为：
    ast.literal_eval() # 但仅支持字面量，如数字、列表、字典等
 """

ans = eval(input("请你输入要计算的算式（比如2 + 2）:"))
print(ans, type(ans))

# 数据类型转换
"""                                                                        
int(x):                                                                    
    可以把整数字符串，或小数转换成整数，会直接舍弃小数部分 # round(x)函数可以四舍五入                         

float(x):                                                                  
    将 x 转换为浮点数，字符串可以是 "3.14" 或 "42"（自动补 .0）                                

str(x)                                                                     
    将任意对象 x 转换为可读的字符串形式。
    
bool(x)                                                   
    非空非零为True，否则False
    
complex(real, imag)                                                        
    生成实部为 real、虚部为 imag 的复数。                                               
    如：                                                                     
       # c = complex(2, 3)     # 输出 (2+3j)                                 
       # print(c.real)         # 实部 2.0                                    
       # print(c.imag)         # 虚部 3.0                                    

repr(x)                                                                    
    返回对象的官方字符串表示（通常可用于 eval() 重建对象）                                     
    与 str() 的区别：                                                           
       # str("Hello") → Hello                                              
       # repr("Hello") → 'Hello'（带引号，符合Python语法）                           

eval(str) 如上解释                                                             

tuple(s)                                                                   
    将序列 s 转为元组	 # tuple([1, 2]) → (1, 2)                                  

list(s)                                                                    
    将序列 s 转为列表	 # list((1, 2)) → [1, 2]                                   

chr(x)                                                                     
    整数转Unicode字符	 # chr(65) → 'A'                                       

ord(x)                                                                     
    字符转ASCII码	 # ord('A') → 65                                       

hex(x)                                                                     
    整数转十六进制字符串 # hex(255) → '0xff'                                         

oct(x)                                                                     
    整数转八进制字符串	 # oct(8) → '0o10'                                         

bin(x)                                                                     
    整数转二进制字符串	 # bin(5) → '0b101'                                        

"""

