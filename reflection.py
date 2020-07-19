#!usr/bin/python

import sys
import time

def ask_user(f, msg):
	f.write("\n\n"+msg)
	print(msg)
	lines = []
	while True:
		line = raw_input()
		if line:
			lines.append(line)
		else:
			break
	text = '\n'.join(lines)
	f.write("\n"+text)
	print("_____________________________________________________________\n")
	f.write("_____________________________________________________________\n")

def main():

	if len(sys.argv) == 2:
		if sys.argv[1] == "help":
			help_msg = (
			"\n	You will be asked a series of questions pertaining to your life. \
			\n	There are 38 questions in total. \
			\n	Enter your answer into the terminal when prompted. \
			\n	Double space to move to the next question. \
			\n	Your answers will be saved in a text file in the current directory \
		in case you ever want to go back to it. \
			\n\n	Let's start.\n"
			)

			print(help_msg)
			time.sleep(20)

	date_tag = time.strftime("%Y-%m-%d")
	f = open("reflection "+date_tag+".txt", "w")
	f.write("--- Reflection Logs ---")
	print("")

	ask_user(f, "What are your future goals? \n")
	ask_user(f, "What are the consequences of attaining or failing them? \n")
	ask_user(f, "What's the reality? \n")

	ask_user(f, "What is really important to you? \n")
	ask_user(f, "What do you want? \n")

	ask_user(f, "What are your 3 most important values in life? \n")
	ask_user(f, "What are the 3 things in life that important to you? \n")
	ask_user(f, "What are your 3 best qualities as a person? \n")

	ask_user(f, "What 3 personal accomplishments in your life that are you most proud of? \n")
	ask_user(f, "What 3 skills/abilities are you the best at? \n")
	ask_user(f, "What are the 3 things you do that account for most of the contributions you make? \n")

	ask_user(f, "What have been your 3 biggest successes in your work? \n")
	ask_user(f, "What are the 3 best jobs/parts of jobs that you've ever had? \n")
	ask_user(f, "What 3 activities give you the greatest satisfaction? \n")

	ask_user(f, "If you were forced to take an extended period of time off from work and you had the money to do anything you wanted, how you would you spend the time? \n")
	ask_user(f, "Where would you go and what would you do? \n")

	ask_user(f, "What are the 3 worst experiences in your life? \n")
	ask_user(f, "What are the 3 biggest mistakes you've made in your life? \n")
	ask_user(f, "What did you learn from them? \n")

	ask_user(f, "What are the 3 most important lessons you've learned in your life? \n")
	ask_user(f, "What are your 3 biggest worries or concerns? \n")

	ask_user(f, "Who are 3 people (living or dead) that you most admire? \n")
	ask_user(f, "Who are the 3 or more people that you care about the most? \n")
	ask_user(f, "What qualities in other people do you most admire? \n")
	ask_user(f, "What 3 words would you like people to describe you as to other people when you aren't present? \n")

	print("\n\n--- Questions for reflection ---\n")
	f.write("--- Questions for reflection ---\n\n")
	print("_____________________________________________________________\n")
	f.write("_____________________________________________________________\n")

	ask_user(f, "What have been the happiest moments of your life? \n")
	ask_user(f, "What do you most enjoy doing in your spare time? \n")
	ask_user(f, "What advice would you give your child or close friend in order to be successful? \n")

	ask_user(f, "What is your best talent or skill? \n")
	ask_user(f, "What are you really excellent at doing? \n")
	ask_user(f, "What 1 quality would you like to develop in yourself? \n")

	ask_user(f, "What is the most important business lesson that you have ever learned? \n")
	ask_user(f, "What is the most important personal lesson that you have ever learned? \n")

	print("Project your life in 5 years and everything is ideal in that time.\n")
	f.write("Project your life in 5 years and everything is ideal in that time.\n\n")

	ask_user(f, "What would it look like? \n")
	ask_user(f, "What would you be doing? \n")
	ask_user(f, "What would you no longer be doing? \n")
	ask_user(f, "What would you have for yourself and your family? \n")

	ask_user(f, "If your life were perfect in every way, how would it be different from today? \n")

	f.close()

if __name__ == "__main__":
	main()
