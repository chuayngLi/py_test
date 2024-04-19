import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("datasets/MNIST_data", one_hot=True)

# 输入层
x = tf.placeholder(tf.float32, [None, 784])

# 输出层
y = tf.placeholder(tf.float32, [None, 10])

# 构建模型
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
pred = tf.nn.softmax(tf.matmul(x, W) + b)

# 定义代价函数
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), axis=1))

# 定义优化器
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# 训练模型
epochs = 50
batch_size = 100
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs, y: batch_ys})
            avg_cost += c / total_batch
        print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print("Optimization Finished!")

    # 模型评估
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))