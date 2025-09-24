#decimal nums representing percentage of max light for that direction
season_db = {
  "Winter": { 
      "Morning":   {"East":0.75,"South":0.40,"West":0.05,"North":0.20},   #08:00–11:00
      "Midday":    {"East":0.20,"South":0.50,"West":0.20,"North":0.20},   #11:00–13:00
      "Afternoon": {"East":0.05,"South":0.40,"West":0.80,"North":0.20},   #13:00–16:00
      "Evening":   {"East":0.03,"South":0.20,"West":0.40,"North":0.10}    #16:00–17:30
  },
  "Spring": { 
      "Morning":   {"East":1.00,"South":0.70,"West":0.10,"North":0.30},   #07:00–11:00
      "Midday":    {"East":0.40,"South":0.90,"West":0.40,"North":0.30},   #11:00–14:00
      "Afternoon": {"East":0.10,"South":0.70,"West":1.00,"North":0.30},   #14:00–17:30
      "Evening":   {"East":0.05,"South":0.40,"West":0.70,"North":0.20}    #17:30–20:00
  },
  "Summer": { 
      "Morning":   {"East":1.00,"South":0.80,"West":0.10,"North":0.30},   #06:00–11:00
      "Midday":    {"East":0.30,"South":1.00,"West":0.50,"North":0.30},   #11:00–14:00
      "Afternoon": {"East":0.10,"South":0.80,"West":1.00,"North":0.30},   #14:00–18:00
      "Evening":   {"East":0.05,"South":0.50,"West":0.80,"North":0.20}    #18:00–21:00
  },
  "Fall": { 
      "Morning":   {"East":1.00,"South":0.60,"West":0.10,"North":0.25},   #07:30–11:00
      "Midday":    {"East":0.30,"South":0.70,"West":0.30,"North":0.25},   #11:00–14:00
      "Afternoon": {"East":0.10,"South":0.60,"West":0.90,"North":0.25},   #14:00–17:00
      "Evening":   {"East":0.05,"South":0.30,"West":0.60,"North":0.20}    #17:00–19:30
  }
}

#print (season_db["Winter"]["Morning"]["East"])
def season_from_month(m: int) -> str: #grab season from month
    if m in (12, 1, 2):
        return "Winter"
    elif m in (3, 4, 5):
        return "Spring"
    elif m in (6, 7, 8):
        return "Summer"
    elif m in (9, 10, 11):
        return "Fall"

def time_of_day(season: str, h: int) -> str: #grab time of day from hour and season
    if season == "Winter":  #sunrise ~8, sunset ~5
        if 8 <= h < 11:  return "Morning"
        if 11 <= h < 13: return "Midday"
        if 13 <= h < 16: return "Afternoon"
        if 16 <= h < 18: return "Evening"

    if season == "Spring":  #sunrise ~7, sunset ~8
        if 7 <= h < 11:  return "Morning"
        if 11 <= h < 14: return "Midday"
        if 14 <= h < 17: return "Afternoon"
        if 17 <= h < 20: return "Evening"

    if season == "Summer":  #sunrise ~6, sunset ~9
        if 6 <= h < 11:  return "Morning"
        if 11 <= h < 14: return "Midday"
        if 14 <= h < 18: return "Afternoon"
        if 18 <= h < 21: return "Evening"

    if season == "Fall":  #sunrise ~7:30, sunset ~7
        if 7 <= h < 11:  return "Morning"
        if 11 <= h < 14: return "Night"
        if 14 <= h < 17: return "Afternoon"
        if 17 <= h < 20: return "Evening"

    return "Night"  # outside daylight
