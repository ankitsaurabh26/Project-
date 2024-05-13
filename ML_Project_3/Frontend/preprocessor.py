import re
import pandas as pd

def preprocess(data):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s-\s|\sAM|\sPM)\s+- "

    message = re.split(pattern,data)[1:]

    dates = re.findall(pattern,data)

    df = pd.DataFrame({'user_message':message, 'message_date':dates})

    x=[]
    for i in df['message_date']:
        x.append(i.split(",")[0]+", "+pd.to_datetime(i.split(",")[1].replace("-",'').strip(),format='%I:%M %p').strftime('%H:%M:%S'))
    df['message_date']=pd.DataFrame(x)

    final=[]
    for i in df.message_date:
        final.append(pd.to_datetime(i))
    df['message_date']=pd.DataFrame(final)
    df.rename(columns={'message_date':'date'},inplace=True)

    users=[]
    messages = []   
    for message in df.user_message:
        entry = re.split(r"([\w\W]+?):\s",message.strip())
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append("Group_Notification")
            messages.append(entry[0])
    df['user']=users
    df['message']=messages
    df.drop(columns=['user_message'],inplace=True)

    df['year']=df['date'].dt.year
    df['month']=df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['hour']=df['date'].dt.hour
    df['minute']=df['date'].dt.minute
    df['month_num']=df['date'].dt.month 
    df['day_name']=df['date'].dt.day_name()

    period = []
    for hour in df[['day_name','hour']]['hour']:
        if hour==23:
            period.append(str(hour)+"-"+str('00'))
        elif hour==0:
            period.append(str('00')+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    
    df['period']=period

    return df