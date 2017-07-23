# -*- coding: utf-8 -*-
# import mysql.connector
import os, time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dataScrapy.dayCount import *







def open_file():
    file_path = '/home/echelon/yunshitu/红酒识别脚本/data/2017年07月19日23时.html'
    with open(file_path, 'r') as f:
        htmlcode = f.read()
        return htmlcode

# htmlCode = open_file()
# htmlcode = '<html><style>@import "https://fonts.googleapis.com/css?family=Montserrat:300,400,700";.rwd-table{margin:1em 0;min-width:300px}.rwd-table tr{border-top:1px solid #ddd;border-bottom:1px solid #ddd}.rwd-table th{display:none}.rwd-table td{display:block}.rwd-table td:first-child{padding-top:.5em}.rwd-table td:last-child{padding-bottom:.5em}.rwd-table td:before{content:attr(data-th) ": ";font-weight:bold;width:6.5em;display:inline-block}@media(min-width:480px){.rwd-table td:before{display:none}}.rwd-table th,.rwd-table td{text-align:left}@media(min-width:480px){.rwd-table th,.rwd-table td{display:table-cell;padding:.25em .5em}.rwd-table th:first-child,.rwd-table td:first-child{padding-left:0}.rwd-table th:last-child,.rwd-table td:last-child{padding-right:0}}body{padding:0 2em;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;color:#444;background:#eee}h1{font-weight:normal;letter-spacing:-1px;color:#34495e}.rwd-table{background:#34495e;color:#fff;border-radius:.4em;overflow:hidden}.rwd-table tr{border-color:#46637f}.rwd-table th,.rwd-table td{margin:.5em 1em}@media(min-width:480px){.rwd-table th,.rwd-table td{padding:1em!important}}.rwd-table th,.rwd-table td:before{color:#dd5}h3{margin-left:35px}.wrapper{overflow:hidden;padding:10px}</style><h1>识别数据表</h1><h3>上边：snapWine&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下边：Drwine</h3><div class="wrapper">	<div class="left">	<table class="rwd-table">		<tr>		<th>日期</th>		<th>日请求量</th>		<th>成功匹配量</th>		<th>匹配成功率</th>		<th>平均耗时</th>		<th>最大耗时</th>		</tr>		<tr>		<td data-th="Movie Title">Star Wars</td>		<td data-th="Genre">Adventure, Sci-fi</td>		<td data-th="Year">1977</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">Howard The Duck</td>		<td data-th="Genre">"Comedy"</td>		<td data-th="Year">1986</td>		<td data-th="Gross">$16,295,774</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>	</table></div><div class="right">	<table class="rwd-table">		<tr>		<th>日期</th>		<th>日请求量</th>		<th>成功匹配量</th>		<th>匹配成功率</th>		<th>平均耗时</th>		<th>最大耗时</th>		</tr>		<tr>		<td data-th="Movie Title">Star Wars</td>		<td data-th="Genre">Adventure, Sci-fi</td>		<td data-th="Year">1977</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">Howard The Duck</td>		<td data-th="Genre">"Comedy"</td>		<td data-th="Year">1986</td>		<td data-th="Gross">$16,295,774</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td><td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>		<tr>		<td data-th="Movie Title">American Graffiti</td>		<td data-th="Genre">Comedy, Drama</td>		<td data-th="Year">1973</td>		<td data-th="Gross">$115,000,000</td>		<td data-th="Gross">$460,935,665</td>		<td data-th="Gross">$460,935,665</td>		</tr>	</table></div></div></html>'


result_html = ''

result_html += save_final_html(18)
result_html += save_final_html(26)
htmlCode = result_html

# me == my email address
# you == recipient's email address
send_list = {
    # "me": "wangzitian@yunshitu.cn",
    # "屈姐": "quchunya@pai9.com.cn",
    # "小林哥": "niuxiaolin@yunshitu.cn",
    # "袁总": "yuangd@yunshitu.cn",
    "Echelon": "2954632969@qq.com",
    # "Jason": "2954632969@qq.com",
    # 'alle': "2954632969@qq.com",
}





me = "wangzitian@yunshitu.cn"
me1 = "2954632969@qq.com"
paijiu = "quchunya@pai9.com.cn"
xiaolinge = "niuxiaolin@yunshitu.cn"
yuanzong = "yuangd@yunshitu.com"

# Create message container - the correct MIME type is multipart/alternative.


key = send_list.keys()
value = send_list.values()

# a1 = key[0]

for key, value in send_list.items():
    pre_html = ''
    html = ''
    pre_html = '<h1>' + key + '，您好：</h1>'

    # Create the body of the message (a plain-text and an HTML version).
    text = "因设备原因无法正常显示该邮件内容，请更换设备查看！"
    html = pre_html + htmlCode

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html', 'utf-8')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "酒标识别服务数据表"
    msg['From'] = me
    msg['To'] = me1
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    mail = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)

    mail.ehlo()

    # mail.starttls()
    mail.set_debuglevel(1)

    mail.login('wangzitian@yunshitu.cn', 'Wang100111')
    mail.sendmail(me, value, msg.as_string())
    mail.quit()
    # time.sleep(10)

