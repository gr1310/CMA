import numpy as np

# A = np.array([
#     [0.45520947, 0.82390391, -0.32588869, -0.08810930],
#     [0.56494298, -0.42892699, -0.10690409, -0.69672992],
#     [0.56078923, -0.34046789, -0.26817218, 0.70546491],
#     [0.39892256, 0.14589588, 0.90025094, 0.09551665]
# ])
# print(np.diag(np.diag(A)))
# print(np.eye(2))
# off_diag_sum = np.sum(np.abs(A - np.diag(np.diag(A))))

# print("Off-diagonal sum:", off_diag_sum)

num_nodes=5
page_rank_scores = np.ones(num_nodes) / num_nodes
print(page_rank_scores)