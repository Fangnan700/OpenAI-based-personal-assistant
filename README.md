# 基于OpenAI实现的个人助理

最近OpenAI所开发的ChatGPT非常火，于是我也去体验了一下。

在玩过之余，就想着能不能把它移植到系统环境，成为一个日常的个人助理，帮助我解决学习、开发或者摸鱼时的种种需求。

于是，看过官方文档之后，发现官方提供了GPT模型的API，那还等什么，开始coding......

项目已开源：[git@github.com:Fangnan700/OpenAI-based-personal-assistant.git]()



## 0x00 注册OpenAI帐号

这步是最基础的，网址如下：

```http
https://openai.com/api/
```

（需要科学上网，具体的注册方法网上一大把，这里不再赘述）

![image-20221216234912593](https://yvling-typora-image-1257337367.cos.ap-nanjing.myqcloud.com/typora/image-20221216234912593.png)



## 0x01 获取API密钥

注册成功后，进入个人帐号管理页面：

![image-20221216235054152](https://yvling-typora-image-1257337367.cos.ap-nanjing.myqcloud.com/typora/image-20221216235054152.png)

选择左侧的 “API keys”，点击 “Create new secret key”，获取API密钥，记得要保存好，页面关闭后将无法再查看。



## 0x02 使用方法

这里可以在虚拟环境中运行，也可以在实体环境中运行，由于我使用的是Linux系统，所以这里我选择配置在虚拟环境中，通过shell脚本运行程序。

这里主要是Linux下的操作步骤，Windows下另寻教程

**一、安装python环境**

```shell
sudo apt install python
```

**二、安装pip**

```shell
sudo apt installl pip
```

**三、安装openai依赖包**

```shell
sudo pip install openai
```

**四、克隆项目**

```shell
git clone git@github.com:Fangnan700/OpenAI-based-personal-assistant.git
```

**五、运行**

```shell
./chat.sh
```

![image-20221217000909083](https://yvling-typora-image-1257337367.cos.ap-nanjing.myqcloud.com/typora/image-20221217000909083.png)



