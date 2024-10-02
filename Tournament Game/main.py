
def get_team_number():
    while True:
        team_number = int(input("Enter the number of teams in the tournament: "))
        if team_number >= 2:
            break
        print("The minimum number of teams is 2, try again.")
    return team_number

def validate_team(team):
    if len(team) >= 2:
        return True
    print("Team names must have at least 2 characters, try again.")
    return False


def get_team_members(team_number):
    team_members = []
    n = 0   
    while n<team_number:
        team = input(f"Enter the name for team #{n+1}: ")
        if not validate_team(team):
            continue
        team_members.append(team)
        n+=1
    return team_members



def get_number_of_games(team_members):
    while True:
        number_of_games = int(input("Enter the number of games played by each team: "))
        if number_of_games < len(team_members) - 1:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            continue
        else:
            break
    return number_of_games


def get_team_wins(team_number, number_of_games, team_members):
    teams = {}
    n = 0
    while n < team_number:
        win = int(input(f"Enter the number of wins Team {team_members[n]} had: "))
        if win < 0:
            print("The minimum number of wins is 0, try again.")
            continue
        elif win > number_of_games:
            print("Wins can't be more than number of games played")
            continue
        else:
            team_name = team_members[n]
            teams[team_name] = win
            n+=1
    return teams

team_number = get_team_number()
team_members = get_team_members(team_number)
number_of_games = get_number_of_games(team_members)
teams = get_team_wins(team_number, number_of_games, team_members)

      
        
print("Generating the games to be played in the first round of the tournament...")        
sorted_new_dict = dict(sorted(teams.items(), key=lambda x: x[1], reverse=True))

while len(sorted_new_dict) > 0:
    first = list(sorted_new_dict.keys())[0]
    last = list(sorted_new_dict.keys())[len(sorted_new_dict)-1]
    print(f"Home: {first} VS Away: {last}")
    sorted_new_dict.pop(first)
    sorted_new_dict.pop(last)


    
    

        
        

            
            
        

                
        

