import Problem as problemModule
import DataReader as dataReader
import ProblemState as stateModule

def GetProblem(data_path):
    data = dataReader.ReadCsvFiles(data_path)
    problem = problemModule.Problem(data)
    return problem

def SolveProblem(problem):
    print(problem.Distances)
    # Create ProblemState at Time 0
    zero_state = stateModule.ProblemState(0)
    return ""
