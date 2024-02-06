def user_info1(**kwargs):
	print(f"类型是{type(kwargs)},内容是：{kwargs}")
user_info1(name = "小明",age = 15,gender = "male")
