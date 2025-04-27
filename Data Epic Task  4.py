import random
import time

def get_scores(student_dict):
    for student in student_dict:
        name = student["name"]
        for score in student["scores"]:
            yield name, score

def avg_score(scores):
    if not scores:
        return 0
    if len(scores) == 1:
        return scores[0]
    else:
        return (scores[0] + avg_score(scores[1:])) / len(scores)

def log_and_retry(n):
    def wrapper_function(func):
        def inner(*args, **kwargs):
            for attempt in range(1, n + 1):
                print(f"Calling {func.__name__}... try {attempt}")
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Error:", e)
                    time.sleep(1)  
            print(f"{func.__name__} failed after {n} tries.")
        return inner
    return wrapper_function

@log_and_retry(3)
def generate_report(student_dict):
    if random.random() < 0.3: 
        raise Exception("Oops! Something went wrong.")
    avg = avg_score(student_dict["scores"])
    print(f"{student_dict['name']}'s average score is {avg:.2f}")

student_dict = [
    {"name": "Bukky", "scores": [70, 80, 80]},
    {"name": "Lisa", "scores": [89, 61, 70]},
    {"name": "Lynn", "scores": [65, 80, 75]}
]

# Print scores using generator
for name, score in get_scores(student_dict):
    print(f"name: {name}\nscore: {score}")

# Print average scores
for student in student_dict:
    name = student["name"]
    scores = student["scores"]
    average = avg_score(scores)    
    print(f"{name}'s average score is {average:.2f}")


# Call the decorated generate_report function
for student in student_dict:
    generate_report(student)