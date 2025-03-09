function getGrade (s1, s2, s3) {
    let grade = (s1 + s2 + s3)/3
    return grade >= 90 && grade <=100 ? "A" :
           grade >= 80 && grade < 90 ? "B" :
           grade >= 70 && grade < 80 ? "C" :
           grade >= 60 && grade < 70 ? "D" :
           grade >= 0 && grade < 60 ? "F" :
           "errrror"
  }