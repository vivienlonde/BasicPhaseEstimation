import qsharp
# from PhaseEstimation import run

qsharp.init(project_root = '../PhaseEstimation')

n_shots = 10
phi = 0.
oracle_power = 1

result = qsharp.eval("PhaseEstimation.Run({}, {}, {})".format(n_shots, phi, oracle_power))

print(result)