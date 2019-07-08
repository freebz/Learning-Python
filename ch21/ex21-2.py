# 3.3에서 새로운 타이머 함수들

if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.pref_counter   # 또는 process_time
else:
    tiemr = time.clock if sys.platform[:3] == 'win' else time.time


try:
    timer = time.pref_counter   # 또는 process_time
except AttributeError:
    timer = time.clock if sys.platform[:3] == 'win' time.time
