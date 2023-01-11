# # list1 = [2,23,4,9,5]

# # print(sum(sorted(list1)[:4]),sum(sorted(list1,reverse=True)[:4]))

# # string = 'ketan'
# # print(string.__contains__('k'))

# # s = "03:01:00AM"

# def timeConversion(s):

#     if s.__contains__("PM") & s.__contains__("12"):
#         return s[:8]
#     elif s.__contains__("PM"):    
#         op =str(int(s.split(':')[0])+12) +':'+s.split(':')[1]+':'+s.split(':')[2][:2]
#         return op

#     if s.__contains__("AM") & s.__contains__("12"):
#         op = str(int(s.split(':')[0])-12)+'0'+':'+s.split(':')[1]+':'+s.split(':')[2][:2]
#         return op

#     elif s.__contains__("AM"):

#         if int(s.split(':')[0]) < 10:
#             op = '0'+str(int(s.split(':')[0]))+':'+s.split(':')[1]+':'+s.split(':')[2][:2]
#         else:
#             op = str(int(s.split(':')[0]))+':'+s.split(':')[1]+':'+s.split(':')[2][:2]
#         return op

# s = "12:45:54PM"
# result = timeConversion(s)
# print(result)
print(abs(2-100))