'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.
'''

# def runnerup():
#
#     user_input = (input("Enter the scores:"))
#     scores = user_input.split()
#
#     scores = sorted(scores, reverse=True)
#
#     print("The runner up is: ", scores[1])
#
# runnerup()

def runnerup():

    scores = [2, 3, 6, 5, 6]

    max_score = max(scores)

    for ele in scores:
        if ele == max_score:
            scores.remove(ele)
        print(scores)

    runnerup = sorted(scores)

    print(runnerup[-1])


runnerup()