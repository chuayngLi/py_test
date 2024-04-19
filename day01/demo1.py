import gym
import collections
import tqdm
import tensorflow as tf
import numpy as np
import statistics
from keras.layers import Dense
from keras import losses
from typing import Tuple, List


# 智能体
class Angen(tf.keras.Model):

    def __init__(self, num_action, num_hidden_unity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mod = None
        self.path = './mod/demo1'
        self.common = Dense(num_hidden_unity, activation='relu')
        self.acor = Dense(num_action)
        self.critic = Dense(1)
        # self.mod:tf.keras.Model = tf.keras.models.load_model(self.path)

    def call(self, inputs: tf.Tensor, **kwargs) -> Tuple[tf.Tensor, tf.Tensor]:
        # print(type(inputs), inputs)
        x = self.common(inputs)
        return self.acor(x), self.critic(x)

    def saveModel(self):
        self.save_weights(self.path)

    def load(self):
        self.mod: tf.keras.Model.weights = self.load_weights(self.path)

    def getActi(self, stat: tf.Tensor):
        stat = tf.convert_to_tensor(stat)
        print(type(stat), stat)
        return self.mod(stat)


# dqn训练体

# @tf.function
class DQN():

    # 主运行
    @tf.function
    def train_step(self,
                   init_state: tf.Tensor,
                   model: tf.keras.Model,
                   optimeizer: tf.keras.optimizers.Optimizer,
                   gamma: float,
                   max_steps_per_episode: int
                   ) -> tf.Tensor:

        with tf.GradientTape() as tape:
            # 收集数据
            action_probs, values, rawards = self.run_episode(init_state, model, max_steps_per_episode)

            # 预期收益
            returns = self.get_expected_return(rawards, gamma)
            # 转换成tensorflow可使用的张量
            action_probs, values, returns = [
                tf.expand_dims(x, 1) for x in [action_probs, values, returns]
            ]

            loss = self.compute_loss(action_probs, values, returns)

        gards = tape.gradient(loss, model.trainable_variables)
        optimezer.apply_gradients(zip(gards, model.trainable_variables))
        ease_reward = tf.math.reduce_sum(rawards)
        return ease_reward

    # 计算损失值
    def compute_loss(self, action_probs: tf.Tensor, values: tf.Tensor, returns: tf.Tensor) -> tf.Tensor:
        advtag = returns - values
        action_log_probs = tf.math.log(action_probs)
        actorloss = -tf.math.reduce_sum(action_log_probs * advtag)
        critic_loss = huber_loss(values, returns)
        return actorloss + critic_loss

    #   计算预期收益
    def get_expected_return(self, rewards: tf.Tensor, gamma: float, stand: bool = True) -> tf.Tensor:
        n = tf.shape(rewards)[0]
        returns = tf.TensorArray(dtype=tf.float32, size=n)
        rewards = tf.cast(rewards[::-1], dtype=tf.float32)
        dis_sum = tf.constant(0.0)
        dis_sum_shap = dis_sum.shape

        for i in tf.range(n):
            reward = rewards[i]
            dis_sum = reward + gamma * dis_sum
            dis_sum.set_shape(dis_sum_shap)
            returns = returns.write(i, dis_sum)
        returns = returns.stack()[::-1]
        if stand:
            returns = ((returns - tf.math.reduce_mean(returns)) / (tf.math.reduce_std(returns) + eps))
        return returns

    # 运行收集数据
    def run_episode(self, init_stat: tf.Tensor, model: tf.keras.Model, max_setps: int) -> Tuple[
        tf.Tensor, tf.Tensor, tf.Tensor]:
        action_probs = tf.TensorArray(dtype=tf.float32, size=0, dynamic_size=True)
        values = tf.TensorArray(dtype=tf.float32, size=0, dynamic_size=True)
        rawards = tf.TensorArray(dtype=tf.int32, size=0, dynamic_size=True)
        init_state_shape = init_stat.shape
        state = init_stat
        for t in tf.range(max_setps):
            state = tf.expand_dims(state, 0)
            action_log_t, value = model(state)
            action = tf.random.categorical(action_log_t, 1)[0, 0]
            # action = tf.argmax(action_log_t, axis=0)[0]
            action_probs_t = tf.nn.softmax(action_log_t)

            values = values.write(t, tf.squeeze(value))
            action_probs = action_probs.write(t, action_probs_t[0, action])

            state, reward, done = self.tf_env_step(action)

            state.set_shape(init_state_shape)

            rawards = rawards.write(t, reward)
            b = tf.cast(done, tf.bool)
            print('状态', b)
            if b:
                break
        return action_probs.stack(), values.stack(), rawards.stack()

    # 动作给到游戏
    def tf_env_step(self, action: tf.Tensor) -> List[tf.Tensor]:
        return tf.numpy_function(self.env_step, [action], [tf.float32, tf.int32, tf.int32])

    # 运行游戏环境
    def env_step(self, action: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        state, reward, done, _ = env.step(action)
        env.render()
        return (
            state.astype(np.float32),
            np.array(reward, np.int32),
            np.array(done, np.int32)
        )

    @tf.function
    def toNumpy(self, data: tf.Tensor):
        return data.numpy()


env = gym.make("CartPole-v1")  # render_mode="human"
env.reset()

# 损失函数
huber_loss = losses.Huber(reduction=tf.keras.losses.Reduction.SUM)
# 优化器
optimezer = tf.keras.optimizers.Adam(learning_rate=0.01)

# 智能体参数
num_actions = env.action_space.n
num_hidden_utils = 128
model = Angen(num_actions, num_hidden_utils)
dqn = DQN()

eps = np.finfo(np.float32).eps.item()
min_episodes_criterion = 10000
max_episodes = 10000
max_steps_per_episode = 1000

reward_threshold = 195
running_reward = 0

# 未来奖励的折扣系数
gamma = 0.99
episodes_reward: collections.deque = collections.deque(maxlen=min_episodes_criterion)

# model.load()
state = env.reset()
with tqdm.tgrange(min_episodes_criterion) as t:
    for i in t:
        # state = tf.expand_dims(state, 0)
        # action_log, val = model(state)
        # # print(val.numpy()[0,0])
        # action = tf.argmax(action_log, axis=1)[0]
        # # action = tf.random.categorical(action_log, 1)[0, 0]
        # action = action.numpy()
        #
        # state, reward, done, _ = env.step(action)
        # env.render()
        # if done:
        #     break
        # #
        init_state = env.reset()
        init_state = tf.constant(init_state, dtype=tf.float32)
        epi_reward = dqn.train_step(init_state, model, optimezer, gamma, max_steps_per_episode)
        epi_reward = int(epi_reward)
        episodes_reward.append(epi_reward)
        running_reward = statistics.mean(episodes_reward)
        env.step(env.action_space.sample())

        t.set_description(f'Episode {i}')

        t.set_postfix(
            episode_reward=epi_reward, running_reward=running_reward)
        model.saveModel()
        if running_reward > reward_threshold and i >= min_episodes_criterion:

            print('训练完成')
            break
        print("\r{}".format(t), end='')
env.close()
