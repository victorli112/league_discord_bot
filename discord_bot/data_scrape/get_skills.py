"""
INPUT: the soup object containing all information about champion skills
OUTPUT: a list of the recommended order of skills
DESCRIPTION: get the recommended skills of the champion
"""
def get_skills(blocks) -> list[str]:
    possible_skills = ['q','w','e','r']
    skills = [""] * 18

    # first find each row
    skill_num = 0
    for i in blocks.find_all('div', {'class' : ['skill-order']}):

        # find all 'level-ups' in the row
        for j in i.find_all('div', {'class': ['skill-up']}):
            level = int(j.find('div').text) - 1
            skills[level] = possible_skills[skill_num]
        skill_num += 1
    return skills


