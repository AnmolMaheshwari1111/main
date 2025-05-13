import tensorflow as tf
import tensorflow_probability as tfp

# Define the data
data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the graphical model
model = tfp.distributions.JointDistribution(
    tfp.distributions.Normal(loc=0, scale=1),
    tfp.distributions.Normal(loc=0, scale=1),
    tfp.distributions.Normal(loc=0, scale=1)
)

# Estimate the graph structure
graph = tfp.graphical_model.estimate_graph(model, data)

# Print the estimated graph
print(graph)