# JsQndxx

通过 Github Actions 自动完成 **江苏省** 青年大学习

## 2023-03-08 更新 已适配新版大学习

## 使用方法

### Fork 项目

点击右上角 `Fork` 到自己的账号下

### 获取 Cookie

[手机抓包教程](https://blog.csdn.net/nikeylee/article/details/125363582)

按照 [青年大学习抓包教程](https://yuzaii.github.io/archives/c59a0c1a.html)（[备份](https://web.archive.org/web/20230306140515/https://yuzaii.github.io/archives/c59a0c1a.html)） 获取自己的 `laravel_session`

### 添加 Cookie 至 Secrets

回到项目页面，依次点击 Settings --> Secrets and variables --> Actions --> New repository secret

建立名为 `LARAVEL_SESSION` 的 secret，值为先前获取的 `laravel_session`，最后点击 Add secret

### 启动 Github Actions

> Actions 默认为关闭状态，Fork 之后需要**手动执行**一次，若成功运行其才会激活。
> 此外，你需要**每 60 天**手动执行一次，不然会被 GitHub 暂停。

返回项目主页面，点击上方的 `Actions`，再点击左侧的 `Auto JsQndxx`，再点击 `Run workflow`

至此，部署完毕。

### 查看结果

当你完成上述流程，可以在 `Actions` 页面点击 `Auto JsQndxx` --> `build` --> `Run script`查看结果。

- 若程序发生异常，请**先手动学习**最新一期青年大学习，再**重新获取** `laravel_session`



## 感谢
https://github.com/BeiyanYunyi/AntiFacistIndoctrination

~~https://github.com/yuzaii/JsQndxx_Python~~