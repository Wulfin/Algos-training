class Solution(object):
    """
    def maximumPopulation(self, logs):
        minYearsOfBirths = min([logs[i][0] for i in range(len(logs))])
        maxYearsOfDeaths = max([logs[i][1] for i in range(len(logs))])

        yearsPopulations = [[minYearsOfBirths, 0]]
        maxPopulation = 0

        for year in range(minYearsOfBirths, maxYearsOfDeaths):
            for personLife in logs:
                if year >= personLife[0] and year < personLife[1]:
                    found = False
                    for i in range(0, len(yearsPopulations)):
                        if yearsPopulations[i][0] == year:
                            found = True
                            yearsPopulations[i][1] += 1
                            if yearsPopulations[i][1] > maxPopulation:
                                maxPopulation = yearsPopulations[i][1]
                            break
                    if not found: yearsPopulations.append([year, 1])

        for element in yearsPopulations:
            if element[1] == maxPopulation:
                return element[0]
    """
    def maximumPopulation(self, logs: list[list[int]]):
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))

        dates.sort()

        population = max_population = max_year = 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year

        return max_year


if __name__ == '__main__':
    solution = Solution()
    logs = [[1950,1961],[1960,1971],[1970,1981]]
    result = solution.maximumPopulation(logs)
    print(result)
