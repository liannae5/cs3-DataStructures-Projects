'''
CS 2302
Lab 7
StudyGuide.py

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 05/08/2022
'''
def getBestGuide_type1(chapters, maxTime):
  n = len(chapters) #number of chapters
  selection = [0] * n #holds the which chapters will be studied. (1 will be inserted for chapters to study)
  time_total = 0 #total time for study guide
  grade_total = 0 #total grade for chapters studied
  grades= [0]*(maxTime+1) #will hold grade combinations
  times = [0]*(maxTime+1) #will hold corresponding time combinations
  final_times = [0] #will hold times of chapters to be studied

  if maxTime == 0: #returns zeroes if there is no time left
    return selection, time_total, grade_total

  for i in range(n): #repeats for each chapter
    if chapters[i][0] > maxTime:
      continue
    for time in range(maxTime,0,-1): #repeats for each hour starting from maxtime
      if chapters[i][0] <= time: #if chapter's time less than/equal to currrent time in loop
        if(grades[time-chapters[i][0]]+chapters[i][1]) > grades[time]: #if there's a better point value than current at index time
          grades[time] = grades[time-chapters[i][0]]+chapters[i][1] #add the point value at current time index
          times[time] = times[time-chapters[i][0]]+chapters[i][0] #insert corresponding time of point value to time index it time arr
        if time == maxTime and grades[time] > grade_total: #to add to selection array
          if grade_total == 0: #takes out initial time of zero
            final_times.pop(0)
          grade_total = grades[time] #uses grade_total to temporarily hold highest grade so far
          final_times.append(chapters[i][1]) #keeps track of times of chapters to read
          selection[i] = 1

  sum_check = sum(final_times) #sums up the final times for time check
  #the following if statement is used to check a bug where the first element's time
  if sum_check > maxTime:
    selection[0] = 0

  time_total = times[maxTime] #updates time_total with study time
  grade_total = grades[maxTime] #updates grade_total with max grade
  return selection, time_total, grade_total #returns study guide, time, and grade


def getBestGuide_type2(chapters, maxTime):
  n = len(chapters) #number of chapters
  selection = [0] * n #stores study guide
  time_total = 0 #stores time takes to study
  grade_total = 0 #stores grade study guide provides
  ratios = [0]*n #holds points-to-time ratios
  remaining_time = maxTime #holds remaining time

  for i in range(n):
    ratios[i] = (chapters[i][1]/chapters[i][0],chapters[i][1],chapters[i][0],i) #stores in tuple((points-time ratio,points,time,chapter_num)
  sRatios = sorted(ratios,reverse=True) #sorts chapters by points-to-time ratio

  for chapter in sRatios: #iterates through each chapter
    if(chapter[1] <= remaining_time): #if a whole chapter can be studied
      selection[chapter[3]] = 1 #put one in its corresponding chapter index in selection
      grade_total += chapter[1] #add its weight(points) to grade_total
      time_total += chapter[2] #add its time to time_total
      remaining_time -= chapter[2] #subtract its time from remaining time

    elif remaining_time > 0: #if there's not enough time to study an entire chapter
      fraction_studied = remaining_time/chapter[2] #find the fraction of the chapter you can study with remaining time
      selection[chapter[3]] = fraction_studied #insert the fraction studied in its corresponding chapter index in selection
      grade_total += (fraction_studied*chapter[1]) #add the amount of points that the fraction studied will contribute to grade_total
      time_total += remaining_time #adds remaining time to time_total
      break #exits out of the loop since there is no remaining time

  return selection, time_total, grade_total

def generate_example_study():
  study = [(17, 20),(28, 40),(23, 30),(33, 50)]
  max_time = 50
  return study, max_time