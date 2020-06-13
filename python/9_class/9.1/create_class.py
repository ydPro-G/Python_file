# 9.1 创建和使用类
# 使用类几乎可以模拟任何东西
# 类表示的不是特定的，而是普遍的

# 9.1.1 创建dog类
# 每个Dog类都将存储名字和实例，我们赋予每条小狗蹲下sit()和打滚roll_over()的能力

class Dog(): # 定义了一个名为Dog的类 ， 在Python中首字母大写的名称值的是类，类定义中的括号是空的， 因为从空白创建这个类
    """
    模拟小狗的简单尝试
    """

    def __init__(self,name,age): # 方法_init_ ，类中的函数称为方法，关于函数的一切都适用于方法 ， 唯一重要的差别是调用方法的方式，
                                 
                                 # _init_()是一个特殊的方法，根据Dog类创建新实例时，Python都会自动运行它，
                                 
                                 # 开头和末尾各有两个下划线，避免python默认方法与普通方法发生名称冲突
                                 
                                 # 方法_init_定义成包含三个形参，self,name,age,   self就是调用实例.方法时的实例自己，它是一个 指向 实例本身 的  引用
                                
                                 # 形参self必不可少，并位于其他形参前面，python调用_init_()方法创建Dog实例时，自动传入实参self
                                 # 每个与类相关联的方法调用都自动传递实参self，它是一个 指向 实例本身 的  引用，让实例能够访问类中的属性和方法
                                 # 创建实例时，python将调用类的方法_init_(),然后通过实参向类传递名字和年龄，self自动传递，so，每当我们根据类创建实例时，都只需给最后两个形参(name,age)提供值

        
        # 属性
        """初始化属性name和age"""
        self.name = name # 两个变量前缀都有self，self为前缀的变量都可  供类中所有 方法 使用，通过 类的任何实例来访问这些变量
        self.age = age # 获取存储在形参age中的值，存储到变量age中，变量被关联到当前创建的实例中，像这样可  通过  实例访问的变量被称为属性
                        # 实参的值被储存到形参中，形参中的值被存储到变量中，变量通过self可以被类中方法使用，        这些变量也被关联到当前创建的实例中
        
        # 方法
    def sit(self): # Dog类定义了方法sit(),这些方法不需要额外的信息，它们只需要形参self，让实例能够访问这些方法
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

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

print("My dog name is " + my_dog.name.title() + ".") # 访问实例的属性，可使用句点表示法——例：my_dog.name
print("My dog age is " + str(my_dog.age) + ".") # Python先找到实例my_dog，再查找与这个实例相关联的属性name  在Dog类中引用这个属性时，使用的时self.name






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