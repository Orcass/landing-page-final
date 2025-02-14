from django.shortcuts import render
from django.http import JsonResponse
import requests

def index_view(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.php')

def github_contributions(request):
    username = "Orcass"  # Ganti dengan username GitHub kamu
    token = "your_personal_access_token"  # Tambahkan token jika diperlukan

    # Endpoint API GitHub
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Authorization": f"token {token}"} if token else {}

    # Request data dari GitHub
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Data dalam format JSON
        contributions = []

        # Proses data untuk ditampilkan
        for event in data:
            contributions.append({
                "type": event["type"],
                "repo": event["repo"]["name"],
                "created_at": event["created_at"],
            })

        return JsonResponse({"status": "success", "contributions": contributions})
    else:
        return JsonResponse({"status": "error", "message": response.text}, status=response.status_code)
