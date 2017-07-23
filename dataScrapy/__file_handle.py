import os, time
import datetime
import decimal

def getDay(index):
    today = datetime.date.today()
    intervalDay = datetime.timedelta(days=index)
    dayTime = today - intervalDay
    return dayTime

def getNum(num):
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP
    b = decimal.Decimal(str(num), decimal.getcontext())
    return b.__round__(2)

# result = ''

pre_css='<style>@import "https://fonts.googleapis.com/css?family=Montserrat:300,400,700";.body{margin-left:55px}.rwd-table{margin:1em 0;min-width:300px}.rwd-table tr{border-top:1px solid #ddd;border-bottom:1px solid #ddd}.rwd-table th{display:none}.rwd-table td{display:block}.rwd-table td:first-child{padding-top:.5em}.rwd-table td:last-child{padding-bottom:.5em}.rwd-table td:before{content:attr(data-th) ": ";font-weight:bold;width:6.5em;display:inline-block}@media(min-width:480px){.rwd-table td:before{display:none}}.rwd-table th,.rwd-table td{text-align:left}@media(min-width:480px){.rwd-table th,.rwd-table td{display:table-cell;padding:.25em .5em}.rwd-table th:first-child,.rwd-table td:first-child{padding-left:0}.rwd-table th:last-child,.rwd-table td:last-child{padding-right:0}}body{padding:0 2em;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;color:#444;background:#eee}h1{font-weight:normal;letter-spacing:-1px;color:#34495e}.rwd-table{background:#34495e;color:#fff;border-radius:.4em;overflow:hidden}.rwd-table tr{border-color:#46637f}.rwd-table th,.rwd-table td{margin:.5em 1em}@media(min-width:480px){.rwd-table th,.rwd-table td{padding:1em!important}}.rwd-table th,.rwd-table td:before{color:#dd5}h3{margin-left:35px}.wrapper{overflow:hidden;padding:10px}</style>'
pre_html = '<h3>&nbsp;&nbsp;&nbsp;这是最近一周酒标识别服务统计表</h3><div class="wrapper"><h3>Snapwine酒标识别服务统计：</h3><div class="section">	<table class="rwd-table">		<tr>		<th>日期</th>		<th>日请求量</th>		<th>成功匹配量</th>		<th>匹配成功率</th>		<th>平均耗时&nbsp;(ms)</th>		<th>最大耗时&nbsp;(ms)</th>		</tr>'
pre_html_DrWine ='<h3>Drwine酒标识别服务统计：</h3><div class="section">	<table class="rwd-table">		<tr>		<th>日期</th>		<th>日请求量</th>		<th>成功匹配量</th>		<th>匹配成功率</th>		<th>平均耗时&nbsp;(ms)</th>		<th>最大耗时&nbsp;(ms)</th>		</tr>'
# mid_html = '<tr>		<td data-th="Movie Title">'+ str(getDay(index))+ '</td>		<td data-th="Genre">' + count +'</td>		<td data-th="Year">' + usefulCount+ '</td>		<td data-th="Gross">'+ rate + '</td>		<td data-th="Gross">' + max_time +'</td>		<td data-th="Gross">'+ avg_time+ '</td>		</tr>'
end_html = '</table></div>'


# 合并HTML代码将html数据保存在变量中或返回html数据
def save_html(count, usefulCount, rate, max_time,  avg_time, index, api_id):
    result = ''
    # api_id为18即snapWine表在上,index为0时加上表头，为6时加上表尾
    if api_id == 18 and index == 0:
        result += pre_css
        result += pre_html
    if api_id == 26 and index == 0:
        result +=pre_html_DrWine
    result += '<tr>		<td data-th="Movie Title">'+ str(getDay(index))+ '</td>		<td data-th="Genre">' + str(count) +'</td>		<td data-th="Year">' + str(usefulCount)+ '</td>		<td data-th="Gross">'+ str(getNum(rate*100)) + '&nbsp;%</td>		<td data-th="Gross">' + str(avg_time) +'</td>		<td data-th="Gross">'+ str(max_time) + '</td>		</tr>'
    if index == 6:
        result += end_html
    return result

# 将数据写入文件
def write_file(count, usefulCount, rate, max_time,  avg_time, index, api_id):
    dir_name = "/home/echelon/yunshitu/红酒识别脚本/data/"
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    with open(time.strftime(dir_name + "%Y年%m月%d日%H时" + '.html', time.localtime()), 'a') as f:
        # api_id为18即snapWine表在上
        if api_id == 18 and index == 0:
            f.write(pre_css)
            f.write(pre_html)
        if api_id == 26 and index == 0:
            f.write(pre_html_DrWine)
        f.write('<tr>		<td data-th="Movie Title">'+ str(getDay(index))+ '</td>		<td data-th="Genre">' + str(count) +'</td>		<td data-th="Year">' + str(usefulCount)+ '</td>		<td data-th="Gross">'+ str(getNum(rate*100)) + '&nbsp;%</td>		<td data-th="Gross">' + str(avg_time) +'</td>		<td data-th="Gross">'+ str(max_time) + '</td>		</tr>')
        if index == 6:
            f.write(end_html)
















    # count_file.write('日处理数据量： '+ str(count) +'次\r\n')
    # count_file.write('成功匹配量：  ' + str(usefulCount) + '次\r\n')
    # count_file.write('处理成功率： '+ str(getNum(rate*100)) +'%\r\n')
    #
    # count_file.write('单次处理最大耗时：  '+  str(max_time) +'毫秒\r\n')
    #
    # count_file.write('当天处理平均单次耗时：  '+ str(avg_time) +'毫秒\r\n\r\n\r\n\r\n\r\n\r\n')

