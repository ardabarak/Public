import requests
from bs4 import BeautifulSoup

def fetchText(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_text = [span.get_text(strip=True) for span in soup.find_all('span')]
    return [t for t in raw_text if t]

def parseCoords(lines):
    coords = []
    i = 0
    while i < len(lines):
        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])
            coords.append((x, y, char))
            i += 3
        except (ValueError, IndexError):
            i += 1

    return coords

def rendGrid(coords):
    if not coords:
        print("No chars")
        return

    max_x = max(c[0] for c in coords)
    max_y = max(c[1] for c in coords)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in coords:
        grid[y][x] = char

    for row in grid:
        print(''.join(row))

def processMsg(url):
    print(f"decrypt result: \n")
    lines = fetchText(url)
    coords = parseCoords(lines)
    rendGrid(coords)

processMsg("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
