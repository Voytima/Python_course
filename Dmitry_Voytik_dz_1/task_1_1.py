# Lesson_1_task_ 1

duration = int(input('Enter seconds: '))

if 0 <= duration < 60:
    print(duration, 'second(s)')
elif 60 <= duration < 3600:
    print(duration // 60, 'minute(s) and ',
          duration % 60, 'second(s)')
elif 3600 <= duration < 86400:
    print(duration // 3600, 'hour(s) ',
          duration % 3600 // 60, 'minute(s) and ',
          duration % 60, 'second(s)')
else:
    print(duration // 86400, 'day(s)',
          duration % 86400 // 3600,'hour(s) ',
          duration % 3600 // 60, 'minute(s) and ',
          duration % 60, 'second(s)')