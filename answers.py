basic_answers = {'привет':'Привет', 'как дела?':'Нормально','увидимся':'Пока'}
def get_answer(question, answers = basic_answers):
	
	question = question.lower()
	print(answers[question])



#get_answer('ПРИВЕТ')
#get_answer('КаК ДеЛа?')