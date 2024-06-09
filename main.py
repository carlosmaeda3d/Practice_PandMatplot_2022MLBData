import pandas as pd
import matplotlib.pyplot as plt

rawPlayerBattingData = pd.read_csv('2022 MLB Player Stats - Batting.csv')
rawPlayerPitchingData = pd.read_csv('2022 MLB Player Stats - Pitching.csv')

# print('Player Batting')
# print(rawPlayerBattingData.keys())
# print('Player Pitching')
# print(rawPlayerPitchingData.keys())

#---- Removed totals lists from the raw
playerBattingData = rawPlayerBattingData.drop(rawPlayerBattingData[rawPlayerBattingData['Tm'] == 'TOT'].index)
playerPitchingData = rawPlayerPitchingData.drop(rawPlayerPitchingData[rawPlayerPitchingData['Tm'] == 'TOT'].index)

#---- Remove * and # from names
playerBattingData['Name'] = playerBattingData['Name'].str.replace('[*#]', '', regex=True)

#---- Total specific stats for team based info
# sumTeamBattingData = playerBattingData.groupby('Tm')[['R', 'H', 'HR']].sum()

#---- Totals and averages specific stats for team based info
teamBattingData = playerBattingData.groupby('Tm').agg({'H': ['sum', 'mean', 'max'], 'R': ['sum', 'mean', 'max'], 'HR': ['sum', 'mean', 'max']}).reset_index()

#---- Rename columns
newBatDataHeads = ['Tm', 'Sum_H', 'Mean_H', 'Highest_H','Sum_R', 'Mean_R', 'Highest_R', 'Sum_HR', 'Mean_HR', 'Highest_HR']
teamBattingData.columns = newBatDataHeads

#---- Creating scatter plot for total HR for teams
plt.figure(figsize=(17, 6))

plt.scatter(teamBattingData['Tm'], teamBattingData['Sum_HR'])

plt.xlabel('Teams')
plt.ylabel('Sum of HRs')
plt.title('Team Total HRs')

plt.show()

#---- Create histogram of total HR

plt.hist(teamBattingData['Sum_HR'], bins=5)

plt.show()

