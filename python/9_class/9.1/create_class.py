# 9.1 创建和使用类
# 类表示的不是特定的，而是普遍的

# 9.1.1 创建dog类
# 每个Dog类都将存储名字和实例，我们赋予每条小狗蹲下sit()和打滚roll_over()的能力

class Dog(): # 定义了一个名为Dog的类 ， 在Python中首字母大写的名称值的是类，类定义中的括号是空的， 因为从空白创建这个类
    """
    模拟小狗的简单尝试
    """

    def __init__(self,name,age): # 类中的函数称为方法，关于函数的一切都适用于方法 ， 唯一重要的差别是调用方法的方式，
                                 

                                 # 两个下划线开头的函数是声明该属性为私有，不能在类的外部被使用或访问

                                 # __init__函数（方法）支持带参数类的初始化，也可为声明该类的属性（类中的变量）
                                                                 
                                 # 方法_init_定义成包含三个形参，self,name,age__init__函数（方法）的第一个参数必须为self，后续参数为自己定义
                                
                                 # self，它是一个 指向 实例本身 的  引用
                                 
                                 # 在类中定义方法去设定该类的属性，这样过于繁琐，而用__init__（）这个特殊的方法就可以方便地自己对类的属性进行定义，__init__()方法又被称为构造器（constructor）

                                 # 定义类的时候，若是添加__init__方法，那么在创建类的实例的时候，实例会自动调用这个方法，一般用来对实例的属性进行初始化。
        
        # 属性
        """初始化属性name和age"""
        self.name = name # 属性 = 形参 属性也可以被实例使用
        self.age = age # 可以获取输入的值也可以自定义值，两者的不同就是，属性设置默认值后就可以不用有形参了，形参的作用在于获取实参
                        

        # 方法
    def sit(self): # Dog类定义了方法sit(),这些方法不需要额外的信息，它们只需要形参self，让实例能够访问这些方法
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.") # 使用属性

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!" + "age is " + str(self.age))










# 9.1.2 根据类创建实例
# 可将类视为创建实例的说明，Dog类是一系列说明，让Python知道如何创建表示特定小狗的实例。
print("\n9.1.2")

# my_dog是实例，调用的类是Dog

my_dog = Dog('xiaobai',6) # 使用的是Dog类，使用实参调用Dog类中的方法_init_()
                          # 方法_init_()创建一个表示特定小狗的实例，使用提供的值来设置属性name和age
                          # 方法_init_()并未显式地包含return语句，但python自动返回一个表示这条小狗的实例
                          # 将这个实例实例存储在变量my_dog中
                          # 首字母大写的名称指的是类，小写的名称指的是根据类创建的实例

print("My dog name is " + my_dog.name.title() + ".") # 访问实例的属性，可使用句点表示法——例：实例.属性
print("My dog age is " + str(my_dog.age) + ".") # Python先找到实例my_dog，再查找与这个实例相关联的属性 在Dog类中引用这个属性时，使用的时self.name






# 9.1.2.2 调用方法
# 根据类创建实例后，用句号表示法来调用类中定义的任何方法
print("\n9.1.2.2")
my_dogs = Dog('xiaohuang',7)

my_dogs.sit()                      # | 调用方法可指定实例的名称和要调用的方法，用句点分隔
my_dogs.roll_over()                # | def sit(self): 定义方法
                                   # | print(self.name.title() + " is now sitting.")  方法所运行的代码
                                   # | 遇到代码my_dogs.sit()时,Python在类Dog中查找方法sit()并运行其代码





# 9.1.2.3 创建多个实例
# 可按需求根据 类 创建 任意数量 的 实例
print("\n9.1.2.3")

i_dog = Dog('xiaohong',8) # 属性
your_dog = Dog('xiaolv',9)

print("My dog name is " + i_dog.name.title() + ".") 
print("My dog age is " + str(i_dog.age) + ".") 
i_dog.sit() # 方法

print("\nYour dog name is " + your_dog.name.title() + ".")
print("Your dog age is " + str(your_dog.age) + ".")
your_dog.sit() # 方法