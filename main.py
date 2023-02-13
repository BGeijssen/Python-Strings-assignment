# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1
scored_player_1 = 'Ruud Gullit '
scored_player_2 = 'Marco van Basten '
goal_0 = 32
goal_1 = 54

scorers = scored_player_1 + str(goal_0) + ', ' + scored_player_2 + str(goal_1);
print(scorers)

player_goal_1 = scored_player_1 + 'scored in the ' + str(goal_0) + 'nd minute';
player_goal_2 = scored_player_2 + 'scored in the ' + str(goal_1) + 'th minute';
report = player_goal_1 + '\n' + player_goal_2;
print(report)

#Part 2
player = 'Hans van Breukelen'

first_name = player[0:player.find(' ')];
print(first_name);

last_name = player[player.find(' ')+1:];
last_name_len = len(last_name);
print(last_name);
print(last_name_len);

name_short = player[:1] + '. ' + last_name;
print(name_short);

first_name_len = len(first_name);
chant = ' '.join([(first_name + '!')] * first_name_len);
print(chant);

last_character = chant[len(chant)-1:];
#print(last_character);
good_chant = bool(last_character != ' ');
print(good_chant);

