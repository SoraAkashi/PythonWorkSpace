DATA_FILENAME = 'test.csv'
with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    person_data = []
    title = f.readline()
    for line in f:
        line = line.strip()
        person_data.append(line.split(','))

for data in person_data:
    name, scores = data[0],data[1:]
    scores = [int(num) for num in scores]
    total = sum(scores)
    print(name, total)
