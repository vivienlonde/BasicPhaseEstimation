import qsharp

qsharp.init(project_root = '../BasicPhaseEstimation')

n_shots = 10
phi = 0.
oracle_power = 1

result = qsharp.eval("PhaseEstimation.Run({}, {}, {})".format(n_shots, phi, oracle_power))

print(result)