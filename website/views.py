from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})
def add(request):
	from random import randint

	num1 = randint(0,10)
	num2 = randint(0,10)
	# check if the user has entered answer in page
	if request.method == "POST":
		# answer variable catches user input
		answer = request.POST['answer']

		old_num1 = request.POST['old_num1']
		old_num2 = request.POST['old_num2']

		
		#error handling for no form entry !		
		if not answer:
			my_answer = "Enter a number"
			color = "danger"

			return render(request, 'divide.html', {
				'answer':answer,
				'my_answer': my_answer,
				'num1':num1,
				'num2':num2,
				'color':color
				})
		
		correct_answer = int(old_num1) + int(old_num2)
		if correct_answer == int(answer):
			my_answer = "correct " + old_num1 + " + " + old_num2 + " = " + answer
			color = 'success'
		else:
			my_answer = "incorrect " + old_num1 + " + " + old_num2 + " does not equal " + answer + " it is " + str(correct_answer)
			color = 'danger'


		#return answer to the page using dictionary
		return render(request, 'add.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num1':num1,
			'num2':num2,
			'color':color
			})
	return render(request, 'add.html', {
		'num1':num1,
		'num2':num2, 
		})

def subtract(request):
	from random import randint

	num1 = randint(0,10)
	num2 = randint(0,10)
	# check if the user has entered answer in page
	if request.method == "POST":
		# answer variable catches user input
		answer = request.POST['answer']

		old_num1 = request.POST['old_num1']
		old_num2 = request.POST['old_num2']

		
		#error handling for no form entry		
		if not answer:
			my_answer = "Enter a number"
			color = "danger"

			return render(request, 'divide.html', {
				'answer':answer,
				'my_answer': my_answer,
				'num1':num1,
				'num2':num2,
				'color':color
				})
		
		correct_answer = int(old_num1) - int(old_num2)
		if correct_answer == int(answer):
			my_answer = "correct " + old_num1 + " - " + old_num2 + " = " + answer
			color = 'success'
		else:
			my_answer = "incorrect " + old_num1 + " - " + old_num2 + " does not equal " + answer + " it is " + str(correct_answer)
			color = 'danger'


		#return answer to the page using dictionary
		return render(request, 'subtract.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num1':num1,
			'num2':num2,
			'color':color
			})
	return render(request, 'subtract.html', {
		'num1':num1,
		'num2':num2, 
		})

def multiply(request):
	from random import randint

	num1 = randint(0,10)
	num2 = randint(0,10)
	# check if the user has entered answer in page
	if request.method == "POST":
		# answer variable catches user input
		answer = request.POST['answer']

		old_num1 = request.POST['old_num1']
		old_num2 = request.POST['old_num2']

		
		#error handling for no form entry		
		if not answer:
			my_answer = "Enter a number"
			color = "danger"

			return render(request, 'divide.html', {
				'answer':answer,
				'my_answer': my_answer,
				'num1':num1,
				'num2':num2,
				'color':color
				})

		
		correct_answer = int(old_num1) * int(old_num2)
		if correct_answer == int(answer):
			my_answer = "correct " + old_num1 + " x " + old_num2 + " = " + answer
			color = 'success'
		else:
			my_answer = "incorrect " + old_num1 + " x " + old_num2 + " does not equal " + answer + " it is " + str(correct_answer)
			color = 'danger'


		#return answer to the page using dictionary
		return render(request, 'multiply.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num1':num1,
			'num2':num2,
			'color':color
			})
	return render(request, 'multiply.html', {
		'num1':num1,
		'num2':num2, 
		})


def divide(request):
	from random import randint

	num1 = randint(0,10)
	num2 = randint(1,10)
	# check if the user has entered answer in page
	if request.method == "POST":
		# answer variable catches user input
		answer = request.POST['answer']

		old_num1 = request.POST['old_num1']
		old_num2 = request.POST['old_num2']
		
		
		#error handling for no form entry		
		if not answer:
			my_answer = "Enter a number"
			color = "danger"

			return render(request, 'divide.html', {
				'answer':answer,
				'my_answer': my_answer,
				'num1':num1,
				'num2':num2,
				'color':color
				})



		correct_answer = int(old_num1) / int(old_num2)
		if correct_answer == float(answer):
			my_answer = "correct " + old_num1 + " / " + old_num2 + " = " + answer
			color = 'success'
		else:
			my_answer = "incorrect " + old_num1 + " / " + old_num2 + " does not equal " + answer + " it is " + str(correct_answer)
			color = 'danger'


		#return answer to the page using dictionary
		return render(request, 'divide.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num1':num1,
			'num2':num2,
			'color':color
			})
	return render(request, 'divide.html', {
		'num1':num1,
		'num2':num2, 
		})

