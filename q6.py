from matplotlib import pylab as plt
import pandas as pd
datafile=pd.read_csv("data/processed_student_performance.csv")
plt.figure()
plt.bar(datafile['Student'],datafile['Final_Score'])
plt.xlabel("Student Name")
plt.ylabel("Final Score")
plt.xticks(rotation=90,fontsize=12) 
#note: the graph fontsize is set such that the names are visible without overlapping in FULL SCREEN mode
plt.tight_layout()
plt.title("Names vs Score")
plt.savefig('plots/final_scores.png')
plt.show()

plt.figure()
plt.scatter(datafile["Hours_Studied"],datafile["Final_Score"],s=100,edgecolors="black",c="g",alpha=0.6)
plt.xlabel('Hours Studied')
plt.ylabel('Final Score')
plt.title("Hours Studied vs Final Score")
plt.tight_layout()
plt.savefig("plots/study_vs_score.png")
plt.show()

plt.figure()
bins=[10,20,30,40,50,60,70,80,90,100]
median_score=datafile["Final_Score"].median()
plt.hist(datafile["Final_Score"],bins=bins,edgecolor="black")
plt.axvline(median_score,color="Red",label="Median Final Score")
plt.xlabel('Final Score')
plt.ylabel('Number of Students')
plt.title("Distribution of Final Scores")
plt.legend()
plt.tight_layout()
plt.savefig("plots/score_distribution.png")
plt.show()

plt.figure()
improved=(datafile["Improvement"]>0).sum()
not_improved=(datafile["Improvement"]<=0).sum()
colours=['royalblue','indianred']
plt.pie([improved,not_improved],labels=["Improved","Not Improved"],autopct="%1.1f%%",colors=colours,explode=[0.5,0],shadow=True)
plt.title("Improved vs Not Improved")
plt.legend()
plt.tight_layout()
plt.savefig("plots/custom_plot.png")
plt.show()


