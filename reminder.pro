; reminder, context = 'test1', subject = 'test2'
pro reminder, subject = subject, context = context, channel = channel
commandline = 'python slack_reminder.py'
if keyword_Set(subject) then commandline += ' -s ' + subject
if keyword_Set(context) then commandline += ' -c ' + context
if keyword_Set(channel) then commandline += ' -cl ' + channel
spawn, commandline
return
end
