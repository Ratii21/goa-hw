def solution(text, ending):
    
    
    for i in range(len(text)-1,-1,-1):
        for b in range(len(ending)-1,-1,-1):
            if text[i] == ending[b]:
                return True
            elif text[i] != ending[b]:
                return False

