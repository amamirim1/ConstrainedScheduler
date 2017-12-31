from ConstrainedScheduler import Scheduler;

test_path = "C:\\Users\\amina\\Desktop\\Convoy-Data\\Small\\"
problem = Scheduler.GetProblem(test_path)
solution = Scheduler.SolveProblem(problem)
print(solution)

