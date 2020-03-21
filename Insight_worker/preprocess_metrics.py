
time_series = {'closed-issues-count':['closed-issues-count','date'],
               'code-changes':['commit_count','date'],
               'code-changes-lines':['date','added','removed'],
               'issues-active':['date','issues'],
               'issues-closed':['date','issues'],
               'new-contributors':['date','new_contributors'],
               'reviews':['date','pull_requests']}

id_value = {'issue-backlog':['issue_id','duration','created_at'],
           'issue-participants':['issue_id','created_at','participants'],
           'review-duration':['"pull_request_id','created_at','duration'],
           'contributors':['user_id','commits','issues','commit_comments',
                           'issue_comments','pull_requests','pull_request_comments','total']}

text = {'message':['msg_id','cntrb_id','msg_text']} #currently there is no metrics avialable for text.


df_time_series = pd.DataFrame(index=index)
for endpoint in self.time_series.keys():
            
    url = base_url + endpoint
    logging.info("Hitting endpoint: " + url + "\n")
    try:
        data = requests.get(url=url).json()
    except:
        data = json.loads(json.dumps(requests.get(url=url).text))

    metric_df = pd.DataFrame.from_records(data)
    
    df_time_series = pd.DataFrame(pd.merged(df_time_series,metric_df, how='outer', on='date'))
    
    df_time_series.index = pd.to_datetime(df_time_series['date'], utc=True).dt.date
    
    
df_id = pd.DataFrame(index=index)
for endpoint in self.time_series.keys():
            
    url = base_url + endpoint
    logging.info("Hitting endpoint: " + url + "\n")
    try:
        data = requests.get(url=url).json()
    except:
        data = json.loads(json.dumps(requests.get(url=url).text))

    metric_df = pd.DataFrame.from_records(data)
    
    df_id = pd.DataFrame(pd.merged(df_time_series,metric_df, how='outer', on='issue_id'))
    
   
df_msg = pd.DataFrame(index=index)
for endpoint in self.time_series.keys():
            
    url = base_url + endpoint
    logging.info("Hitting endpoint: " + url + "\n")
    try:
        data = requests.get(url=url).json()
    except:
        data = json.loads(json.dumps(requests.get(url=url).text))

    metric_df = pd.DataFrame.from_records(data)
    
    df_msg = pd.DataFrame(pd.merged(df_time_series,metric_df, how='outer', on='msg_id'))
