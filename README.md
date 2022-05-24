# JsQndxx

通过 Github Actions 自动完成 **江苏省** 青年大学习



## 使用方法

### Fork 项目

点击右上角 `Fork` 到自己的账号下

### 获取 Cookie

按照 [青年大学习抓包教程](https://yuzai.xyz/archives/c59a0c1a.html) 获取自己的 `laravel_session`

### 添加 Cookie 至 Secrets

回到项目页面，依次点击 Settings --> Secrets --> Actions --> New repository secret

建立名为 `LARAVEL_SESSION` 的 secret，值为先前获取的 `laravel_session`，最后点击 Add secret

### 启动Github Actions

> Actions 默认为关闭状态，Fork 之后需要手动执行一次，若成功运行其才会激活。

返回项目主页面，点击上方的 `Actions`，再点击左侧的`Auto JsQndxx`，再点击`Run workflow`

至此，部署完毕。

### 查看结果

当你完成上述流程，可以在 `Actions` 页面点击 `Mihoyo sign in` --> `build` --> `run sign`查看结果。

- 若程序发生异常，请**先手动学习**最新一期青年大学习，再**重新获取** `laravel_session`



## 感谢

https://github.com/yuzaii/JsQndxx_Python

