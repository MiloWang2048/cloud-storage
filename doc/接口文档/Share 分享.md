# 前后端接口设计说明书

## Share 分享

### 创建分享链接

* Request
  * Url: `/api/share/109[目录id]/30[天数，不填为无限]/`
  * Method: POST

* Response
  * Status Code: 200 OK

    ```json
    {
        "url": "xbabasdasd",
        "pwd": "1234",
        "expiration": "2019-11-30T15:34:42.257461+08:00",
    }
    ```

### 保存别人的分享到个人仓库

* Request
  * Url: `/api/share-to-me/xbabasdasd[分享url]/233[个人仓库id，不填为根目录]/`
  * Method: POST

* Response
  * Status Code: 200 OK
