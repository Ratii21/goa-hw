

def check_exam(arr1,arr2):
    score = 0
    
    for i in range(len(arr2)):
        if arr2[i] == "":
            score = score
        elif arr2[i] != arr1[i]:
            score -= 1
        elif arr2[i] == arr1[i]:
            score += 4
    if score < 0:
        return 0
    else:
        return score
    
    