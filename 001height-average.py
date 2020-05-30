heights = {'taro':168,'jiro':171,'takashi':165}

total=0
for i in heights.values():
    total +=i

average = total/ len(heights)

print('平均身長は{0}cmです。'.format(average))
