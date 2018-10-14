"项目配置文件"
#coding:utf-8
import os
import logging


#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #获取当前路径的文件夹名(获取当前文件的路径)
data_path = os.path.join(prj_path,'data')
testcase_path = os.path.join(prj_path,'testcase')

report_file = os.path.join(prj_path,'report','report.html')
log_file = os.path.join(prj_path,'log','log.txt')

#日志配置
logging.basicConfig(level=logging.INFO, #log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式
#数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'

#邮件配置
smtp_sever = 'smtp.qq.com'  #smtp服务器地址
smtp_user = '625397195@qq.com'
smtp_password = 'iwanttofly234@#$'

subject = '接口测试邮件'   #邮件主题
sender = smtp_user   #邮件发件人
receiver = '625397195@qq.com'  #邮件收件人

is_send_email = False  #是否发送邮件的开关


if __name__ == "__main__":      #当前文件调试
    print(prj_path)
    print(data_path)
    print(testcase_path)