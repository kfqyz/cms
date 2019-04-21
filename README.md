# CMS
Content management system based on Flask.
The project is under development.

基于Flask的内容管理系统.
项目正在开发之中……

安装前设置环境变量：
1.新建.env文件：
    
    SECRET_KEY = 'hello'
    CMS_ADMIN='admin@qq.com'#管理员邮箱
    MAIL_SERVER='smtp.sina.com'
    MAIL_USERNAME='xxx@sina.com'
    MAIL_PASSWORD='xxxxxx'
    MAIL_USE_SSL=True
    MAIL_PORT=465


1.用户名、邮箱、手机均可登录
2.后台管理使用Flask-admin 访问：http://localhost:5000/admin
3.提示，错误反馈中文化
4.增加了文章分类，文章标签
5.增加评论及对评论的回复

