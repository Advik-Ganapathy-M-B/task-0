import numpy as np
hours_studied=np.array([5.9,3.6,6.5,5.4,1.2])
attendance=np.array([100,85,73,73,74])
prev_scores=np.array([52,74,49,78,77])
fin_scores=np.array([90,47,88,50,35])
print("Hours studied:",hours_studied)
print("Attendance: ",attendance)
print("Previous scores: ",prev_scores)
print("Final scores: ",fin_scores)
print("Hours studied array shape and datatype:",np.shape(hours_studied)," ",hours_studied.dtype)
print("Attendance array shape and datatype:",np.shape(attendance)," ",attendance.dtype)
print("Previous Scores array shape and datatype:",np.shape(prev_scores)," ",prev_scores.dtype)
print("Final Scores array shape and datatype:",np.shape(fin_scores)," ",fin_scores.dtype)
print("Mean final score: ",np.mean(fin_scores)) #mean final score
print("Maximum of final score: ",np.max(fin_scores))
print("Minimum of final score: ",np.min(fin_scores))
print("Standard deviation of final score: ",np.std(fin_scores))
fin_scores=fin_scores+5
print("Updated final scores after adding 5: ",fin_scores)
above75=fin_scores>=75
print("Boolean array for scores over 75",above75)
print("Boolean indexing to print scores over 75",fin_scores[above75])
