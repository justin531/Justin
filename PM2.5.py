import time
while True:
    def sendmail(message):
        import smtplib
        from email.mime.text import MIMEText

        # 寄件者，收件者
        from_addr = '810234@stu.nknush.kh.edu.tw'
        to_addr = '810234@stu.nknush.kh.edu.tw'


        smtpssl=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtpssl.login(from_addr, "xxxxxxxxx")

        msg = '復興站PM2.5='+ message
        mime=MIMEText(msg, "plain", "utf-8")
        mime["Subject"]="今日PM25資料"
        # 顯示的名稱
        mime["From"]="PM2.5監視器"
        mime["To"]= to_addr

        smtpssl.sendmail(from_addr, to_addr, mime.as_string())
        smtpssl.quit()



    import requests, json
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get('https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json', verify=False)
    sites = response.json()
    for site in sites:
        if site['Site'] == '復興':
            print('現在 復興站 PM2.5='+site['PM25'])
            sendmail(site['PM25'])
            break
    time.sleep(43200)




