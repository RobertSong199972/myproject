#### 初稿

#### 单特征（只按照累计确诊人数分析，数据来源截止到3.31）

###### 1、logistic回归拟合疫情曲线

生物中学的增长模型，类似S曲线的拟合，阅读文章：
https://www.jianshu.com/p/4c90f8f7c1c1
https://blog.csdn.net/Zengmeng1998/article/details/104208284
https://blog.csdn.net/z_ccsdn/article/details/104134358?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
代码为logistic.py拟合结果如下图（横坐标代表1月20号开始累增）：

![image-20200511221956915](images/1.png)

##### 2、简单的神经网络拟合

构建一个简单的神经网络来拟合并预测未来疫情结果，代码为dpAsy.py
https://blog.csdn.net/weixin_44000193/article/details/104091767#comments_12149374
拟合效果如下：

![image-20200511222051196](images/2.png)

## 多特征（累计七个特征）
和单特征类似，增加特征拟合提高可信度
https://blog.csdn.net/weixin_44000193/article/details/104091767#comments_12149374
![image-20200511222819455](images/3.png)

##### 1、7个特征构建简单的神经网络拟合新冠曲线，参见manyFeatures.py

![image-20200511222840659](images/4.png)

##### 2、xgboost中选用7个特征拟合的新冠曲线，参见xgboost.py

![image-20200511223007798](images/5.png)
