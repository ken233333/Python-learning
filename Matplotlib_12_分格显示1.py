import matplotlib.pyplot as plt

plt.figure()
# 两行两列
# plt.subplot(2, 2, 1)
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(2, 2, 2)
# plt.plot([0, 1], [0, 2])
#
# plt.subplot(2, 2, 3)
# plt.plot([0, 2], [0, 2])
#
# plt.subplot(2, 2, 4)
# plt.plot([0, 5], [0, 5])

# 两行一列
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 2], [0, 2])

plt.subplot(2, 3, 6)
plt.plot([0, 5], [0, 5])


plt.show()

