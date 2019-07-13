import data1
import data2
import data3

def get_teams_for_person(person, people):
  teams = []

  for p in people:
    if not p.is_team:
      continue

    additional_teams = get_teams_for_person(person, p.members)
    for at in additional_teams:
      if at not in teams:
        teams.append(at)

    if (len(additional_teams) > 0) or (person in p.members):
      teams.append(p)

  return teams


def build_member_list(person, visited_people, members):
  if person in visited_people:
    return
  
  visited_people.append(person)
  if not person.is_team:
    members.append(person)
    return
  
  for member in person.members:
    build_member_list(member, visited_people, members)  


def get_members(team):
  members = []
  build_member_list(team, [], members)
  return members

def exercise1(person, people):
  return get_teams_for_person(person, people)

def main():
    print("Task 1:")
    print([t.displayname for t in exercise1(data1.alice, data1.people)])

    print("Task 2:")
    print([t.displayname for t in exercise1(data2.alice, data2.people)])

    print("Task 3:")
    print(sorted(p.displayname for p in get_members(data2.c_team)))

    print("Task 3.5:")
    print(sorted(p.displayname for p in get_members(data3.c_team)))

if __name__ == "__main__":
  main()