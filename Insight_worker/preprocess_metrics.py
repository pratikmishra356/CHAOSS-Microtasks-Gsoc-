
time_series = {'closed-issues-count':['closed-issues-count','date'],
               'code-changes':['commit_count','date'],
               'code-changes-lines':['date','added','removed'],
               'issues-active':['date','issues'],
               'issues-closed':['date','issues'],
               'new-contributors':['date','new_contributors'],
               'reviews':['date','pull_requests']}

Id_value = {'issue-backlog':['issue_id','duration','created_at'],
           'issue-participants':['issue_id','created_at','participants'],
           'review-duration':['"pull_request_id','created_at','duration'],
           'contributors':['user_id','commits','issues','commit_comments',
                           'issue_comments','pull_requests','pull_request_comments','total']}

text = {'message':['msg_id','cntrb_id','msg_text']} #currently there is no metrics avialable for text.
