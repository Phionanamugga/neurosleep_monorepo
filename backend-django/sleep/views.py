from django.http import JsonResponse
# Simple mock endpoints similar to your front-end data model

def last_night(request):
    return JsonResponse({
        "durationMin": 420,
        "efficiency": 92,
        "latency": 12,
        "rem": 1.5,
        "deep": 1.2,
        "hrv": 62,
        "rhr": 54,
        "score": 86
    })

def nights(request):
    # Return a week of synthetic 'durationMin' + 'score'
    data = []
    for i in range(7):
        data.append({
            "date": i,  # client can map this as needed
            "durationMin": 380 + (i * 5),
            "score": 70 + (i % 4) * 5
        })
    return JsonResponse({"nights": data})

def journal(request):
    # For demo purposes, return static entries
    return JsonResponse({
        "entries": [
            {"text": "Felt energized; no caffeine after 2pm.", "ts": 1710000000000},
            {"text": "Late workout, sleep slightly delayed.", "ts": 1710086400000}
        ]
    })