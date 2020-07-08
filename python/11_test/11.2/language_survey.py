from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question) # 向类传递变量




# 显示问题并存储答案
my_survey.show_question() # 调用方法，显示问题
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response) # 实例调用类方法，添加变量获取的信息；在while循环里获取所有数据


# 显示调查结果

print("\nThank you!")
my_survey.show_results() # 实例.方法()