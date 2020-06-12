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
                                 
                                 # 开头和末尾各有两个下划线，避免python默认方法于普通方法发生名称冲突
                                 
                                 # 方法_init_定义成包含三个形参，self,name,age
                                
                                 # 形参self必不可少，并未与其他形参前面，python调用_init_()方法创建Dog实例时，自动传入实参self
                                 # 每个于类相关联的方法调用都自动传递实参self，它是一个 指向 实例本身 的  引用，让实例能够访问类中的属性和方法
                                 # 创建Dog实例时，python将调用Dog类的方法_init_(),然后通过实参向Dog()传递名字和年龄，self自动传递，so，每当我们根据Dog类创建实例时，都只需给最后两个形参(name,age)提供值

        
        """初始化属性name和age"""
        self.name = name # 两个变量前缀都有self，已self为前缀的变量都可供类中所有方法使用，通过类的任何实例来访问这些变量
        self.age = age # 获取存储在形参age中的值，将其存储到变量age中，该变量被关联到当前创建的实例，像这样可通过实例访问的变量被称为属性

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")