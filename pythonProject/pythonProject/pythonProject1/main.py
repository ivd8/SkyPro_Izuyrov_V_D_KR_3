def count_successful(a, b=50):
    score = 0

    for i in a:
        if i > a:
            score += 1


    return score


# не изменяйте код дальше, это проверка

values = '20 30 40 50'
score = input()

print(count_successful(values, int(score)) if score.isdigit() else count_successful(values))