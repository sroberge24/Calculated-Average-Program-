print('Calculated Average Score from 3 Recent Tests')

#Get user inputs for three test scores
def get_average():
    score_1= float(input("Enter Test 1 Score"))
    score_2= float(input("Enter Test 2 Score"))
    score_3= float(input("Enter Test 3 Score"))
#Calculate the average with formula
    average = (score_1 + score_2 + score_3)/3
#Return the average to main
    return average

def check_average(average):
    if average > 95:
        print(f"Congrats! You did great! {average:.2f}")
    elif 85<= average <= 95:
        print(f"You did well!, But did not reach the top high. {average:.2f} ")
    elif 70 <= average <= 84:
        print(f"Good effort, but you could do better. {average:.2f} ")
    else:
        print(f"You need to study harder next time {average:.2f}")
#Main function
def main():
    average = get_average()
    check_average(average)
main()
