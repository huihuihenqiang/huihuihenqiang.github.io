# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:41:39 2023
三维拟合裂缝聚类
@author: songshaopeng
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.cluster import KMeans


#做聚类
def kmeans_clustering(data):
    '''
    输入平面法向量的球坐标，进行kmeans聚类

    Parameters
    ----------
    data : TYPE 
        DESCRIPTION.

    Returns
    -------
    labels_pred : TYPE
        DESCRIPTION.

    '''
    # 转换为NumPy数组
    data_np = np.array(data)

    # 提取特征
    features = data_np

    # 执行KMeans聚类
    kmeans = KMeans(n_clusters=4)  # 根据需要设置聚类的数量
    kmeans.fit(features)
    #结果
    labels_pred = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # 绘制聚类结果
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制数据点
    scatter = ax.scatter(features[:, 0], features[:, 1], features[:, 2],
                         c=labels_pred, cmap='viridis', s=50, alpha=0.7)

    # 绘制聚类中心
    ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2],
               c='red', marker='x', s=100, label='Centroids')

    ax.set_xlabel('azimuth_angle')
    ax.set_ylabel('polar_angle')
    ax.set_zlabel('z0')
    ax.set_title('KMeans Clustering(delete special point)')

    # 设置坐标轴范围
    #ax.set_xlim([features[:, 0].min(), features[:, 0].max()])
    ax.set_xlim([features[:, 0].min(), np.sort(features[:, 0])[-2]])
    ax.set_ylim([features[:, 1].min(), features[:, 1].max()])
    ax.set_zlim([features[:, 2].min(), features[:, 2].max()])

    # 添加颜色条
    fig.colorbar(scatter)

    plt.legend()
    plt.savefig('KMeans Clustering(delete special point).png', dpi=400)
    plt.show()

    return labels_pred


def CalculatePolarcoordinates(coefficient):
    '''
    根据拟合平面求出单位法向量，进而求出球坐标。

    Parameters
    ----------
    coefficient : TYPE list
        DESCRIPTION. 拟合平面的系数

    Returns
    -------
    ploar_coordinates : TYPE list
        DESCRIPTION. 球坐标：方位角，极角，向量起点z值

    '''
    #先转化为单位法向量
    unit_normal_vector = []
    for coe in coefficient:
        a = -coe[0]/(math.sqrt(coe[0]**2+coe[1]**2+1))
        b = -coe[1]/(math.sqrt(coe[0]**2+coe[1]**2+1))
        c = 1/(math.sqrt(coe[0]**2+coe[1]**2+1))
        d = coe[2]
        unit_normal_vector.append([a, b, c, d])
    #再转化为极坐标
    ploar_coordinates = []
    for vector in unit_normal_vector:
        azimuth = math.atan(vector[1]/vector[0])
        polar_angle = math.acos(vector[2])
        z0 = vector[3]
        ploar_coordinates.append([azimuth, polar_angle, z0])
    return ploar_coordinates


def Calculate(x, y, z):
    '''
    根据x,y,z坐标计算出平面的方程

    Parameters
    ----------
    x : TYPE np
        DESCRIPTION. x坐标
    y : TYPE np
        DESCRIPTION. y坐标
    z : TYPE np
        DESCRIPTION. z坐标

    Returns
    -------
    list
        DESCRIPTION. z = a * x + b * y + c 返回了[a,b,c]

    '''
    N = len(x)
    # ------------------------构建系数矩阵-----------------------------
    A = np.array([[sum(x ** 2), sum(x * y), sum(x)],
                  [sum(x * y), sum(y ** 2), sum(y)],
                  [sum(x), sum(y), N]])

    B = np.array([[sum(x * z), sum(y * z), sum(z)]])

    # 求解
    X = np.linalg.solve(A, B.T)
    print('平面拟合结果为：z = %.3f * x + %.3f * y + %.3f' % (X[0], X[1], X[2]))
    #return [X[0], X[1], X[2]]

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")
    ax1.scatter(x, y, z, c='r', marker='o')
    x_p = np.linspace(-80, 80, 80)
    y_p = np.linspace(-80, 80, 80)
    x_p, y_p = np.meshgrid(x_p, y_p)
    z_p = X[0] * x_p + X[1] * y_p + X[2]
    ax1.plot_wireframe(x_p, y_p, z_p, rstride=10, cstride=10)
    plt.show()

    return [list(X[0])[0], list(X[1])[0], list(X[2])[0]]

#主函数
if __name__ == "__main__":
    #读入数据
    df = pd.read_excel('三维拟合用程序1108generation_data.xls',
                       sheet_name='Sheet1', header=None)
    #将dtaframe转化成列表
    data_list = df.values.tolist()
    lists = {}
    for i in range(1, 19):
        lists[f"list_{i}"] = []
        for j in data_list:
            if j[3] == float(i):
                lists[f"list_{i}"].append(j)

    
    coefficient = []
    for i in range(1, 19):

        x = np.array(lists[f'list_{i}'])[:, 0]
        y = np.array(lists[f'list_{i}'])[:, 1]
        z = np.array(lists[f'list_{i}'])[:, 2]
        abc = Calculate(x, y, z)
        coefficient.append(abc)
    #得到极坐标
    ploar_coordinates = CalculatePolarcoordinates(coefficient)

    #对极坐标进行聚类
    cluster_labels = kmeans_clustering(ploar_coordinates)

    print("聚类结果:", cluster_labels)
