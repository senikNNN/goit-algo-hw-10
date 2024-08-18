import pulp

# Створення задачі лінійного програмування
problem = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Змінні для кількості вироблених одиниць лимонаду та фруктового соку
x1 = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')

# Обмеження на ресурси
problem += 2 * x1 + 1 * x2 <= 100, "Water_Constraint"
problem += 1 * x1 <= 50, "Sugar_Constraint"
problem += 1 * x1 <= 30, "Lemon_Juice_Constraint"
problem += 2 * x2 <= 40, "Fruit_Puree_Constraint"

# Функція цілі (максимізація загальної кількості вироблених продуктів)
problem += x1 + x2, "Total_Production"

# Розв'язання задачі
problem.solve()

# Отримання результатів
lemonade_qty = x1.varValue
fruit_juice_qty = x2.varValue
total_production = pulp.value(problem.objective)

lemonade_qty, fruit_juice_qty, total_production
