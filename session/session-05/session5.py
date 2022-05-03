
# #리스트
# #리스트 초기화
# my_team = ['선영', '영권', '민규','진우','하린','상민','수은','주현']

# #리스트 접근
# a = my_team[3]

# #리스트 값 지정
# my_team[0] = '지원'
# print(my_team[0])

# #리스트 메소드
# my_team[0] = '선영'
# my_team.append('승아')
# my_team.append('교현')
# my_team.append('나예')
# print(my_team)

# 딕셔너리
    # 딕셔너리 초기화
from this import d


my_team_dic = {
    '대장' : '선영',
    '짱' : '영권',
    '졸개1' : '민규',
    '졸개2' : '진우',
    '졸개3' : '하린',
    '졸개4' : '주현',
    '졸개5' : '상민',
    '졸개6' : '수은'
}

    #딕셔너리 값 지정
my_team_dic['짱'] = '승아'
    #딕셔너리 접근
a = my_team_dic['대장'] 
# print(a)
my_team_dic['초신성'] = '교현'
    #딕셔너리 메소드
dic_val = my_team_dic.values()
# print(dic_val)
dic_keys = my_team_dic.keys()
# print(dic_keys)
dic_items = my_team_dic.items()
# print(dic_items)
 
 # for, if
# my_team_list = ['선영', '영권', '민규','진우','하린','상민','수은','주현']
# blank_list= []

# for i in my_team_list:
#     blank_list.append(i)
#     print(blank_list)

# new_data = []
# num_list = list(range(1,10+1))
# for n in num_list:
#     if n%2 == 0:
#         new_data.append(n)
# print(new_data)


# str = '영권 선영 민규 하린 상민 수은 주현 진우'
# if '민규' in str:
#     print("exist")
# else:
#     print("don't exist")

