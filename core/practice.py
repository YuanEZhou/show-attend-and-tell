import tensorflow as tf
import numpy as np
tf.set_random_seed(1234)
# x=np.array([[[1,1,1,1],[2,2,2,2],[3,3,3,3]],
#             [[4,4,4,4],[5,5,5,5],[6,6,6,6]]],dtype=np.float32)#2*3*4
# context=np.array([[9,9,9,9],
#                   [8,8,8,8]],dtype=np.float32)#2*4
# c=tf.constant([[0,0,0,0,0],
#             [0,0,0,0,0]],dtype=tf.float32)
# h=tf.constant([[1,1,1,1,1],
#             [1,1,1,1,1]],dtype=tf.float32)
# lstm_cell = tf.contrib.rnn.BasicLSTMCell(num_units=5)
# _, (c, h) = lstm_cell(inputs=tf.concat([x[:,1,:], context],1), state=[c, h])

# with tf.Session() as sess:
    # sess.run(tf.global_variables_initializer())
    # print tf.get_variable_scope().trainable_variables()
    # c ,h=sess.run([c,h])
    # print h

#####################################################
# with tf.variable_scope('scope1'):
#     a=tf.get_variable('a',[1])
#     tf.get_variable_scope().reuse_variables()
#     a2 = tf.get_variable('a', [1])
#     assert  a==a2
# tf.get_variable_scope().reuse_variables()
# with tf.variable_scope('scope1'):
#     a3 = tf.get_variable('a', [1])

# with tf.variable_scope('scope2'):
#     b=tf.get_variable('b',[2])
# a=tf.Variable(1,trainable=False,name='a',collections=[tf.contrib.framework.model_variable])
# b=tf.Variable(2,trainable=True,name='b')
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print tf.GraphKeys.GLOBAL_VARIABLES
#     print tf.global_variables()
#     print tf.GraphKeys.TRAINABLE_VARIABLES
#     print tf.trainable_variables()
#     print tf.get_collection(tf.GraphKeys.MODEL_VARIABLES)
#
# dummy_input=tf.random_normal([3])
# dummy_input=tf.Print(dummy_input,data=[dummy_input],message='dummy inputs have been created:')
# q=tf.FIFOQueue(capacity=3,dtypes=tf.float32)
# enqueue_op=q.enqueue_many(dummy_input)
# date=q.dequeue()
# date=tf.Print(date,data=[q.size()],message='items are left in q:')
# fg=date+1
# with tf.Session() as sess:
#     sess.run(enqueue_op)
#     sess.run(fg)
#     sess.run(fg)
#     sess.run(fg)
#     sess.run(fg)
#     print 'here!'
with tf.variable_scope('scope1'):
    a=tf.get_variable('a',[1])
with tf.variable_scope('scope1',reuse=True):
    b = tf.get_variable('a',[1])
assert a==b
# a_t=tf.transpose(a)
# with tf.variable_scope('scope2'):
#     b=tf.Variable([[1,2]],name='b')
#     c=a_t+b

# with tf.variable_scope('scope2'):
#     b=tf.Variable([2],name='b')
#     with tf.variable_scope('scope1'):
#         c=tf.Variable([1],name='a')
#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print a
    print b