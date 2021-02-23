import random
#print(random.randint(1,10))
target_string = "methinks it is like a weasel"

def generate_string():
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    gen_string = ""
    #Append a random letter from alphabets to generated_string
    while len(gen_string) < 28:
        j = random.randint(0,len(alphabets) - 1)
        #print(j)
        #print(alphabets[j])
        gen_string += alphabets[j]
    return gen_string

#print(generate_string())


def score_string(generated_string, target_string):
    score = 0
    #best_generated_string = ""
    for k in range(len(target_string)):
        if target_string[k] == generated_string[k]:
            score += 1
            best_generated_string += generated_string[k]
    score_percent = score / len(target_string) * 100
    #return round(score_percent),score_percent,score
    return round(score_percent), best_generated_string, target_string

#print(score_string(generate_string(),target_string))


def go_monkey(target_string):
    generated_string = ""
    best_generated_string = ""
    score = 0
    tries = 0
    while score < 100:
        generated_string = generate_string()
        score = score_string(generated_string,target_string)
        tries += 1
        if score > 0:
            best_generated_string = generated_string
            print(best_generated_string)
        elif tries == 1000:
            print(score)
    return print(generated_string, tries)

#go_monkey(target_string)


        