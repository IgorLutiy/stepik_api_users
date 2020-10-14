import requests
import json

def pars_json(id):
        jx = json.loads(requests.get('https://stepik.org/api/users/' + id).text)
        print('\n')
        print('%-24s%-20s' % ('full_name: ', jx['users'][0]['full_name']))
        print('%-24s%-20s' % ('knowledge: ', jx['users'][0]['knowledge']))
        print('%-24s%-20s' % ('knowledge_rank: ', jx['users'][0]['knowledge_rank']))
        print('%-24s%-20s' % ('reputation: ', jx['users'][0]['reputation']))
        print('%-24s%-20s' % ('reputation_rank: ', jx['users'][0]['reputation_rank']))
        print('%-24s%-20s' % ('join_date: ', jx['users'][0]['join_date']))
        print('%-24s%-20s' % ('solved_steps_count: ', jx['users'][0]['solved_steps_count']))
        print('%-24s%-20s' % ('created_courses_count: ', jx['users'][0]['created_courses_count']))
        print('%-24s%-20s' % ('created_lessons_count: ', jx['users'][0]['created_lessons_count']))
        print('%-24s%-20s' % ('followers_count: ', jx['users'][0]['followers_count']), '\n')

while True:
        id = input('Введите id пользователя: ')
        if id == '':
                break
        pars_json(id)

