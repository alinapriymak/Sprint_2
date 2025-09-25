class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def football_wins(self):
        return f"Футбольных побед: {self.victories}"
    
    def football_draws(self):
        return f"Футбольных ничьих: {self.draws}"
    
    def football_losses(self):
        return f"Футбольных поражений: {self.losses}"
    
    def football_total_points(self):
        points = 3 * self.victories + self.draws
        return f"Общее количество очков: {points}"

class Hockey(Results):
    def hockey_wins(self):
        return f"Хоккейных побед: {self.victories}"
    
    def hockey_draws(self):
        return f"Хоккейных ничьих: {self.draws}"
    
    def hockey_losses(self):
        return f"Хоккейных поражений: {self.losses}"
    
    def hockey_total_points(self):
        points = 2 * self.victories + self.draws
        return f"Общее количество очков: {points}"
    

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

# Вызов всех методов для обоих подклассов в цикле
for team in (football_team, hockey_team):
        if isinstance(team, Football):
            print(football_team.football_wins())
            print(football_team.football_draws())
            print(football_team.football_losses())
            print(football_team.football_total_points())
        else:
            print(hockey_team.hockey_wins())
            print(hockey_team.hockey_draws())
            print(hockey_team.hockey_losses())
            print(hockey_team.hockey_total_points())
        
    