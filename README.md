# rasa_qq
基于rasa的qq机器人
qq框架采用cqhttp
###### 由于使用了mitieNLP，需要下载total_word_feature_extractor_zh.dat 中文训练模型 并放入data文件夹中

# 安装依赖
`pip3 install -r requirements.txt`

# rasa
推荐使用conda管理python环境
#### 训练数据
`rasa train`
#### 测试nlu模型
`rasa shell nlu`
#### 启动微服务
`rasa run actions`
#### 启动服务器
`rasa run`

# qq
在cqhttp/config.yml中修改qq号与密码
#### 启动cqhttp
运行go-cqhttp.bat
#### 启动qq机器人
运行bot.py脚本
