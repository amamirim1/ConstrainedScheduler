import pandas as pd;

def ReadCsvFiles(base_path):
    demand = pd.read_csv(base_path + "Demand.csv", index_col = 0)
    supply = pd.read_csv(base_path + "Supply.csv", index_col = 0)
    distances = pd.read_csv(base_path + "Distances.csv", index_col = 0)
    speeds = pd.read_csv(base_path + "Speeds.csv", index_col = 0)
    return [demand, supply, distances, speeds]
